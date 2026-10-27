"""Render simple-diagram-v1 boxes and edges; not an implementation of upstream FigureSpec."""
import argparse
import html
import json
import math
from pathlib import Path


def render(spec):
    if spec.get('schema') != 'simple-diagram-v1':
        raise ValueError('Expected simple-diagram-v1; upstream FigureSpec requires its own renderer')
    width, height = spec.get('width',800), spec.get('height',400)
    if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) and 100 <= v <= 20000 for v in (width,height)):
        raise ValueError('Invalid canvas')
    nodes = {}
    for node in spec.get('nodes',[]):
        key = node.get('id')
        if not isinstance(key,str) or not key or key in nodes:
            raise ValueError('Node IDs must be nonempty and unique')
        coords = [node.get(k) for k in ('x','y','width','height')]
        if not all(isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(v) for v in coords):
            raise ValueError('Node geometry must be finite numbers')
        x,y,w,h = coords
        if x<0 or y<0 or w<=0 or h<=0 or x+w>width or y+h>height:
            raise ValueError('Node is outside canvas')
        if not isinstance(node.get('label'),str):
            raise ValueError('Node label must be a string')
        nodes[key] = node
    if not nodes:
        raise ValueError('No nodes')
    esc = lambda s: html.escape(str(s),quote=True)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">', f'<title>{esc(spec.get("title","Diagram"))}</title>', '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#39465d"/></marker></defs>', '<rect width="100%" height="100%" fill="white"/>']
    for edge in spec.get('edges',[]):
        if edge.get('source') not in nodes or edge.get('target') not in nodes:
            raise ValueError('Edge references an unknown node')
        if edge['source'] == edge['target']:
            raise ValueError('Self-loops are not supported by this renderer')
        a,b = nodes[edge['source']],nodes[edge['target']]
        ax,ay = a['x']+a['width']/2,a['y']+a['height']/2
        bx,by = b['x']+b['width']/2,b['y']+b['height']/2
        dx,dy = bx-ax,by-ay
        if dx == 0 and dy == 0:
            raise ValueError('Connected nodes have the same center')
        def border(n,cx,cy,vx,vy):
            t = min(n['width']/2/abs(vx) if vx else math.inf,n['height']/2/abs(vy) if vy else math.inf)
            return cx+vx*t,cy+vy*t
        x1,y1 = border(a,ax,ay,dx,dy)
        x2,y2 = border(b,bx,by,-dx,-dy)
        parts.append(f'<line x1="{x1:.3f}" y1="{y1:.3f}" x2="{x2:.3f}" y2="{y2:.3f}" stroke="#39465d" stroke-width="2" marker-end="url(#arrow)"/>')
        if edge.get('label'):
            parts.append(f'<text x="{(x1+x2)/2:.3f}" y="{(y1+y2)/2-8:.3f}" text-anchor="middle" font-family="Arial" font-size="13">{esc(edge["label"])}</text>')
    for n in nodes.values():
        parts.append(f'<rect x="{n["x"]}" y="{n["y"]}" width="{n["width"]}" height="{n["height"]}" rx="8" fill="#edf3ff" stroke="#245bba"/>')
        lines = n['label'].split('\n')
        if len(lines)*18 > n['height']-10 or any(len(line)*8 > n['width']-16 for line in lines):
            raise ValueError('Label may overflow; wrap text or enlarge its box')
        for i,line in enumerate(lines):
            parts.append(f'<text x="{n["x"]+n["width"]/2}" y="{n["y"]+n["height"]/2+(i-(len(lines)-1)/2)*18+5}" text-anchor="middle" font-family="Arial" font-size="14">{esc(line)}</text>')
    return '\n'.join(parts+['</svg>'])


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('spec',type=Path)
    p.add_argument('output',type=Path)
    a = p.parse_args()
    try:
        svg = render(json.loads(a.spec.read_text(encoding='utf-8')))
        a.output.parent.mkdir(parents=True,exist_ok=True)
        with a.output.open('x',encoding='utf-8') as out:
            out.write(svg)
    except (ValueError,OSError) as exc:
        p.exit(1,f'{exc}\n')
