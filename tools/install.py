"""Install selected skills into a Codex/OpenCode discovery directory. Dry-run by default."""
import argparse
import hashlib
import json
import re
import shutil
import stat
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest_tree(path, ignore_generated=False):
    if path.is_symlink():
        raise ValueError(f"Symlink root refused: {path}")
    result = {}
    for item in sorted(path.rglob('*')):
        if ignore_generated and ('__pycache__' in item.relative_to(path).parts or item.suffix == '.pyc'):
            continue
        if item.is_symlink():
            raise ValueError(f"Symlink refused: {item}")
        if item.is_file():
            result[item.relative_to(path).as_posix()] = hashlib.sha256(item.read_bytes()).hexdigest()
    return result


def inside(path, parent):
    resolved = path.resolve()
    if not resolved.is_relative_to(parent.resolve()) or resolved == parent.resolve():
        raise ValueError(f"Path escapes destination: {path}")
    return resolved


def install(destination, names, apply=False, remove=False):
    dest = Path(destination).expanduser().absolute()
    if dest.is_symlink():
        raise ValueError('Destination must not be a symlink')
    catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    known = {x['name'] for x in catalog['skills']}
    plans = []
    # Preflight the entire selection before any writes.
    for name in sorted(set(names)):
        if name not in known or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            raise ValueError(f'Unknown skill: {name}')
        source = ROOT / 'skills' / name
        target = dest / name
        inside(target, dest)
        if target.is_symlink():
            raise ValueError(f'Symlink target refused: {target}')
        receipt = dest / '.minh-agent-receipts' / (name + '.json')
        inside(receipt, dest)
        if receipt.is_symlink():
            raise ValueError('Symlink receipt refused')
        expected = digest_tree(source, ignore_generated=True)
        if remove:
            if not receipt.is_file() or not target.is_dir():
                raise ValueError(f'No owned installation: {name}')
            record = json.loads(receipt.read_text(encoding='utf-8'))
            if record.get('name') != name or record.get('destination') != str(target.resolve()):
                raise ValueError(f'Receipt identity mismatch: {name}')
            if digest_tree(target) != record['files']:
                raise ValueError(f'Locally modified installation; preserve it manually: {name}')
            action = 'remove'
        elif target.exists():
            if not target.is_dir() or digest_tree(target) != expected:
                raise ValueError(f'Existing different skill will not be overwritten: {name}')
            action = 'unchanged'
        else:
            action = 'install'
        plans.append((name, source, target, receipt, expected, action))
    if apply:
        dest.mkdir(parents=True, exist_ok=True)
        for name, source, target, receipt, expected, action in plans:
            if action == 'install':
                # Same-filesystem staging; copy never overwrites an existing target.
                stage = Path(tempfile.mkdtemp(prefix='.minh-stage-', dir=dest))
                try:
                    shutil.copytree(source, stage / name, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
                    # OneDrive can mark source directories read-only; copies must be maintainable.
                    for copied in [stage / name, *(stage / name).rglob('*')]:
                        copied.chmod(copied.stat().st_mode | stat.S_IWUSR)
                    if digest_tree(stage / name) != expected:
                        raise ValueError('Staged content checksum mismatch')
                    if target.exists():
                        raise ValueError(f'Target appeared during install: {target}')
                    (stage / name).rename(target)
                    receipt.parent.mkdir(exist_ok=True)
                    receipt.write_text(json.dumps({'name': name, 'destination': str(target.resolve()), 'files': expected}, indent=2), encoding='utf-8')
                finally:
                    # stage is freshly created within the explicitly checked destination.
                    inside(stage, dest)
                    shutil.rmtree(stage)
            elif action == 'remove':
                inside(target, dest)
                # Delete only files verified against our receipt, then empty directories.
                for item in sorted(target.rglob('*'), key=lambda p: len(p.parts), reverse=True):
                    inside(item, target)
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        item.rmdir()
                target.rmdir()
                receipt.unlink()
    return [{'name': n, 'action': a, 'destination': str(t), 'applied': apply} for n, s, t, r, e, a in plans]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', choices=['codex', 'opencode'], default='codex')
    parser.add_argument('--scope', choices=['project', 'user'], default='project')
    parser.add_argument('--project', type=Path, default=Path.cwd())
    parser.add_argument('--destination', type=Path, help='Explicit discovery directory, useful for test installations')
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument('--skills', nargs='+')
    selection.add_argument('--profile', default='all', help='all or an exact catalog group name')
    parser.add_argument('--apply', action='store_true', help='Perform the printed actions; default is dry-run')
    parser.add_argument('--remove', action='store_true', help='Remove only unmodified installations owned by receipts')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
    if args.skills:
        names = args.skills
    elif args.profile == 'all':
        names = [x['name'] for x in catalog['skills']]
    else:
        if args.profile not in catalog['groups']:
            parser.error('Unknown profile; use an exact group from catalog.json')
        names = catalog['groups'][args.profile]
    base = Path.home() if args.scope == 'user' else args.project
    if args.host == 'codex':
        default = base / '.agents' / 'skills'
    elif args.scope == 'user':
        default = base / '.config' / 'opencode' / 'skills'
    else:
        default = base / '.opencode' / 'skills'
    try:
        print(json.dumps(install(args.destination or default, names, args.apply, args.remove), indent=2))
    except (ValueError, OSError) as exc:
        parser.exit(1, f'{exc}\n')


if __name__ == '__main__':
    main()
