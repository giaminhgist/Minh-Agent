"""Read-only scanner for explicit shortcut:/ponytail: debt markers."""
import argparse
import json
import re
from pathlib import Path

SKIP = {'.git','node_modules','.venv','venv','__pycache__','dist','build','.agents','.claude'}
PATTERN = re.compile(r'\b(?:shortcut|ponytail):\s*(.*)', re.IGNORECASE)


def scan(root):
    root = Path(root).resolve()
    results=[]
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if any(part in SKIP for part in rel.parts) or path.is_symlink() or not path.is_file():
            continue
        if path.stat().st_size > 2_000_000:
            continue
        try:
            content=path.read_text(encoding='utf-8')
        except (UnicodeError,OSError):
            continue
        if '\x00' in content:
            continue
        for line,text in enumerate(content.splitlines(),1):
            match=PATTERN.search(text)
            if match:
                results.append({'path':rel.as_posix(),'line':line,'text':match.group(0),'status':'UNTRIAGED'})
    return results


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('root',type=Path)
    print(json.dumps(scan(p.parse_args().root),indent=2,ensure_ascii=False))
