"""Serial local job queue with atomic state, exclusive lock and fail-closed crash resume.

Only execute a manifest whose argv entries have been reviewed and authorized.
No shell, remote backend, automatic retries or OOM configuration changes.
"""
import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import tempfile
from pathlib import Path


def atomic_json(path, value):
    fd,tmp = tempfile.mkstemp(prefix=path.name+'.',suffix='.tmp',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as stream:
            json.dump(value,stream,indent=2)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def validate_manifest(manifest):
    if manifest.get('schema') != 'local-queue-v1' or not isinstance(manifest.get('jobs'),list) or not manifest['jobs']:
        raise ValueError('Expected nonempty local-queue-v1 manifest')
    seen=set()
    for job in manifest['jobs']:
        if not isinstance(job,dict):
            raise ValueError('Job must be an object')
        ident=job.get('id','')
        if not isinstance(ident,str) or not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}',ident) or ident in seen:
            raise ValueError('Job IDs must be safe and unique')
        seen.add(ident)
        argv=job.get('argv')
        if not isinstance(argv,list) or not argv or not all(isinstance(x,str) and x and '\x00' not in x for x in argv):
            raise ValueError('argv must be a nonempty list of strings')
        if Path(argv[0]).suffix.lower() in {'.bat','.cmd'}:
            raise ValueError('Windows batch launchers are not accepted; use the executable directly')
        timeout=job.get('timeout_seconds',300)
        if not isinstance(job.get('cwd','.'),str) or not job.get('cwd','.') or '\x00' in job.get('cwd','.'):
            raise ValueError('cwd must be a nonempty path string')
        if isinstance(timeout,bool) or not isinstance(timeout,(int,float)) or not math.isfinite(timeout) or timeout<=0:
            raise ValueError('timeout_seconds must be positive and finite')


def run_queue(manifest_path,state_path,execute=False):
    manifest_path=Path(manifest_path).resolve()
    state_path=Path(state_path).absolute()
    if state_path.is_symlink():
        raise ValueError('Symlink state refused')
    if state_path.resolve()==manifest_path:
        raise ValueError('State must not overwrite manifest')
    raw=manifest_path.read_bytes()
    manifest=json.loads(raw)
    validate_manifest(manifest)
    digest=hashlib.sha256(raw).hexdigest()
    if not execute:
        return {'status':'DRY_RUN','jobs':[j['id'] for j in manifest['jobs']],'manifest_sha256':digest}
    state_path.parent.mkdir(parents=True,exist_ok=True)
    lock=state_path.with_suffix(state_path.suffix+'.lock')
    try:
        fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    except FileExistsError as exc:
        raise ValueError('Queue locked. Inspect the owner/process; do not delete a live lock.') from exc
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as stream:
            stream.write(json.dumps({'pid':os.getpid(),'manifest':str(manifest_path)}))
        if state_path.exists():
            state=json.loads(state_path.read_text(encoding='utf-8'))
            if state.get('manifest_sha256')!=digest:
                raise ValueError('Manifest changed; use a new state file or reconcile explicitly')
            if set(state.get('jobs',{}))!={j['id'] for j in manifest['jobs']}:
                raise ValueError('Queue state job IDs do not match manifest')
            allowed={'pending','running','succeeded','failed','unknown'}
            if any(j.get('status') not in allowed for j in state['jobs'].values()):
                raise ValueError('Invalid queue job state')
            if any(j['status'] in {'running','unknown'} for j in state['jobs'].values()):
                raise ValueError('Ambiguous prior launch; reconcile backend/process evidence before resuming')
        else:
            state={'schema':'local-queue-state-v1','manifest_sha256':digest,'jobs':{j['id']:{'status':'pending','attempts':0} for j in manifest['jobs']}}
            atomic_json(state_path,state)
        logs=state_path.parent/(state_path.stem+'-logs')
        if logs.is_symlink():
            raise ValueError('Symlink log directory refused')
        logs.mkdir(exist_ok=True)
        for job in manifest['jobs']:
            record=state['jobs'][job['id']]
            if record['status'] in {'succeeded','failed'}:
                continue
            cwd=(manifest_path.parent/job.get('cwd','.')).resolve()
            if not cwd.is_dir():
                raise ValueError(f'Working directory not found: {cwd}')
            record.update(status='running',attempts=record['attempts']+1)
            atomic_json(state_path,state)
            log=logs/(job['id']+f'-{record["attempts"]}.log')
            try:
                with log.open('xb') as output:
                    result=subprocess.run(job['argv'],cwd=cwd,stdout=output,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,timeout=job.get('timeout_seconds',300),shell=False)
                record.update(status='succeeded' if result.returncode==0 else 'failed',returncode=result.returncode,log=str(log))
            except subprocess.TimeoutExpired:
                # Direct process was killed/reaped by subprocess.run; grandchildren may still exist.
                record.update(status='unknown',reason='timeout; reconcile possible child processes before retry',log=str(log))
            except OSError as exc:
                record.update(status='failed',reason=str(exc),log=str(log))
            atomic_json(state_path,state)
            if record['status']=='unknown':
                break
        return state
    finally:
        lock.unlink()


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('manifest',type=Path)
    p.add_argument('state',type=Path)
    p.add_argument('--execute',action='store_true')
    a=p.parse_args()
    try:
        result=run_queue(a.manifest,a.state,a.execute)
        print(json.dumps(result,indent=2))
        if a.execute and any(j['status']!='succeeded' for j in result['jobs'].values()):
            raise SystemExit(2)
    except (ValueError,OSError) as exc:
        p.exit(1,f'{exc}\n')
