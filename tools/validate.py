"""Offline structural validation; does not replace host or behavioral evaluation."""
import argparse
import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT=Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    root=Path(root).resolve()
    errors=[]
    catalog=json.loads((root/'catalog.json').read_text(encoding='utf-8'))
    names=[x['name'] for x in catalog['skills']]
    actual={p.parent.name for p in (root/'skills').glob('*/SKILL.md')}
    if len(names)!=69 or len(set(names))!=69 or actual!=set(names):
        errors.append('Catalog must match exactly the 69 approved Skill names')
    grouped=[name for group in catalog['groups'].values() for name in group]
    if sorted(grouped)!=sorted(names):
        errors.append('Profiles must partition the catalog exactly once')
    for record in catalog['skills']:
        path=root/record['path']/'SKILL.md'
        if not path.is_file():
            errors.append(f'Missing {path}')
            continue
        text=path.read_text(encoding='utf-8')
        # Authoring convention: a JSON-quoted description is also a valid YAML scalar.
        match=re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: (".*")\n---\n',text)
        if not match:
            errors.append(f'Invalid supported frontmatter: {path}')
            continue
        if match[1]!=record['name'] or json.loads(match[2])!=record['description']:
            errors.append(f'Catalog/frontmatter mismatch: {path}')
        if len(match[1])>64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',match[1]):
            errors.append(f'Invalid name: {path}')
        if not record['description'] or len(record['description'])>1024:
            errors.append(f'Invalid description: {path}')
        if '[TODO:' in text or 'YOUR_SKILL_NAME' in text:
            errors.append(f'Unfinished scaffold: {path}')
        if not (path.parent/'references'/'license-notices.txt').is_file():
            errors.append(f'Missing standalone license notices: {path}')
    mapping=json.loads((root/'docs/source-map.json').read_text(encoding='utf-8'))
    integrations={'host-integration','notification-integration','catalog-and-benchmarks'}
    if len(mapping['sourceMappings'])!=113:
        errors.append('Expected 113 canonical source mappings')
    for item in mapping['sourceMappings']:
        if item['target'] not in set(names)|integrations:
            errors.append(f'Unknown mapping target: {item}')
    for item in mapping['arsModes']:
        if item[2] not in set(names)|integrations:
            errors.append(f'Unknown ARS mode target: {item[2]}')
    for path in root.rglob('*.md'):
        if any(p in {'.validation-deps','dist'} for p in path.relative_to(root).parts):
            continue
        for target in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if re.match(r'^[a-zA-Z]+:',target) or target.startswith('#'):
                continue
            clean=unquote(target.split('#')[0].strip('<>'))
            if not (path.parent/clean).exists():
                errors.append(f'Broken local link in {path.relative_to(root)}: {target}')
    plugin=json.loads((root/'.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    market=json.loads((root/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    if plugin['name']!='minh-agent' or plugin['version']!=catalog['version']:
        errors.append('Plugin name/version mismatch')
    if not market.get('owner',{}).get('name') or market['name']!='minh-agent-marketplace':
        errors.append('Invalid marketplace ownership/name')
    for entry in market['plugins']:
        source=(root/entry['source']).resolve()
        if not source.is_relative_to(root) or not (source/'.claude-plugin/plugin.json').is_file():
            errors.append('Marketplace source escapes repository or lacks manifest')
        if entry['name']!=plugin['name'] or entry['version']!=catalog['version']:
            errors.append('Marketplace and plugin mismatch')
    for script in root.rglob('*.py'):
        if any(x in {'.validation-deps','dist'} for x in script.relative_to(root).parts):
            continue
        try:
            ast.parse(script.read_text(encoding='utf-8'))
        except SyntaxError as exc:
            errors.append(f'Python syntax: {script}: {exc}')
    return {'status':'FAIL' if errors else 'PASS','skills':len(names),'source_entrypoints':len(mapping['sourceMappings']),'errors':errors,'scope':'Offline structure and local references only; not live host or behavioral parity.'}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=ROOT)
    result=validate(p.parse_args().root)
    print(json.dumps(result,indent=2,ensure_ascii=False))
    raise SystemExit(bool(result['errors']))
