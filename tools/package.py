"""Create a portable plugin ZIP with a content checksum manifest."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXCLUDE={'.git','.validation-deps','__pycache__','dist','.venv','PACKAGE_CHECKSUMS.json'}


def package(output):
    output=Path(output).absolute()
    if output.exists():
        raise ValueError('Archive exists; choose a new path')
    files=[]
    for path in sorted(ROOT.rglob('*')):
        if any(part in EXCLUDE for part in path.relative_to(ROOT).parts):
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink not packaged: {path}')
        if path.is_file() and path.resolve()!=output.resolve():
            files.append(path)
    hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
    output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path,path.relative_to(ROOT).as_posix())
        archive.writestr('PACKAGE_CHECKSUMS.json',json.dumps(hashes,indent=2))
    return {'path':str(output),'files':len(files),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('output',type=Path)
    try:
        print(json.dumps(package(p.parse_args().output),indent=2))
    except (ValueError,OSError) as exc:
        p.exit(1,f'{exc}\n')
