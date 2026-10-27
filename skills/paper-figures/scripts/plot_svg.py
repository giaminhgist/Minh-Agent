"""Render validated numeric CSV as deterministic line/bar/scatter SVG (standard library)."""
import argparse
import csv
import hashlib
import html
import json
import math
from pathlib import Path


def render(csv_path, output, x, y, kind='line', width=800, height=500, title='', x_label=None, y_label=None):
    if kind not in {'line', 'bar', 'scatter'} or width < 240 or height < 200:
        raise ValueError('Unsupported plot kind or canvas too small')
    data_path = Path(csv_path)
    output = Path(output)
    metadata_path = output.with_suffix('.provenance.json')
    if output.resolve() == data_path.resolve() or metadata_path.resolve() == data_path.resolve():
        raise ValueError('Output must not overwrite input data')
    if output.exists() or metadata_path.exists():
        raise ValueError('Output already exists; choose a new path')
    raw = data_path.read_bytes()
    reader = csv.DictReader(raw.decode('utf-8-sig').splitlines())
    if not reader.fieldnames or x not in reader.fieldnames or y not in reader.fieldnames:
        raise ValueError('Requested columns are missing')
    points = []
    for line, row in enumerate(reader, 2):
        try:
            pair = (float(row[x]), float(row[y]))
        except (ValueError, TypeError, KeyError) as exc:
            raise ValueError(f'Invalid numeric value on CSV line {line}') from exc
        if not all(math.isfinite(v) for v in pair):
            raise ValueError(f'Non-finite value on CSV line {line}')
        points.append(pair)
    if not points:
        raise ValueError('No data rows')
    if kind == 'line' and any(b[0] < a[0] for a, b in zip(points, points[1:])):
        raise ValueError('Line plot requires nondecreasing x; sort explicitly before rendering')
    if kind == 'bar' and len({p[0] for p in points}) != len(points):
        raise ValueError('Duplicate bar positions; aggregate explicitly first')
    xs, ys = zip(*points)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = (min(0, min(ys)), max(0, max(ys))) if kind == 'bar' else (min(ys), max(ys))
    if xmin == xmax:
        xmin, xmax = xmin - 0.5, xmax + 0.5
    if ymin == ymax:
        ymin, ymax = ymin - 0.5, ymax + 0.5
    xpad = (xmax - xmin) * 0.08
    xmin, xmax = xmin - xpad, xmax + xpad
    left, top, right, bottom = 90, 55, width - 30, height - 80
    sx = lambda v: left + (v - xmin) / (xmax - xmin) * (right - left)
    sy = lambda v: bottom - (v - ymin) / (ymax - ymin) * (bottom - top)
    esc = lambda s: html.escape(str(s), quote=True)
    elements = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">', f'<title>{esc(title or y + " versus " + x)}</title>', '<rect width="100%" height="100%" fill="white"/>', '<g font-family="Arial, sans-serif" font-size="13" fill="#172033">']
    elements.append(f'<text x="{width/2}" y="28" text-anchor="middle" font-size="19">{esc(title)}</text>')
    for i in range(6):
        xv = xmin + (xmax-xmin)*i/5
        yv = ymin + (ymax-ymin)*i/5
        elements += [f'<line x1="{left}" y1="{sy(yv):.3f}" x2="{right}" y2="{sy(yv):.3f}" stroke="#e3e7ee"/>', f'<text x="{left-12}" y="{sy(yv)+4:.3f}" text-anchor="end">{yv:.4g}</text>', f'<text x="{sx(xv):.3f}" y="{bottom+23}" text-anchor="middle">{xv:.4g}</text>']
    elements += [f'<path d="M {left} {top} V {bottom} H {right}" fill="none" stroke="#172033"/>', f'<text x="{(left+right)/2}" y="{height-20}" text-anchor="middle">{esc(x_label or x)}</text>', f'<text transform="translate(20 {(top+bottom)/2}) rotate(-90)" text-anchor="middle">{esc(y_label or y)}</text>']
    if kind == 'line':
        coords = ' '.join(f'{sx(a):.3f},{sy(b):.3f}' for a,b in points)
        elements.append(f'<polyline points="{coords}" fill="none" stroke="#245bba" stroke-width="2"/>')
    if kind in {'line', 'scatter'}:
        elements += [f'<circle cx="{sx(a):.3f}" cy="{sy(b):.3f}" r="3.5" fill="#245bba"/>' for a,b in points]
    else:
        sorted_x = sorted(xs)
        step = min((sx(b)-sx(a) for a,b in zip(sorted_x, sorted_x[1:])), default=40)
        bar_width = min(40, step * 0.7)
        for a,b in points:
            elements.append(f'<rect x="{sx(a)-bar_width/2:.3f}" y="{min(sy(b),sy(0)):.3f}" width="{bar_width:.3f}" height="{abs(sy(b)-sy(0)):.3f}" fill="#245bba"/>')
    elements.append('</g></svg>')
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('x', encoding='utf-8') as stream:
        stream.write('\n'.join(elements))
    provenance = {'schema':'plot-svg-v1','input':str(data_path),'sha256':hashlib.sha256(raw).hexdigest(),'rows':len(points),'x':x,'y':y,'kind':kind,'aggregation':'none','uncertainty':'not computed','output':str(output)}
    with metadata_path.open('x', encoding='utf-8') as stream:
        json.dump(provenance, stream, indent=2)
    return provenance


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv', type=Path)
    p.add_argument('output', type=Path)
    p.add_argument('--x', required=True)
    p.add_argument('--y', required=True)
    p.add_argument('--kind', choices=['line','bar','scatter'], default='line')
    p.add_argument('--title', default='')
    p.add_argument('--x-label')
    p.add_argument('--y-label')
    a = p.parse_args()
    try:
        print(json.dumps(render(a.csv,a.output,a.x,a.y,a.kind,title=a.title,x_label=a.x_label,y_label=a.y_label),indent=2))
    except (ValueError,OSError) as exc:
        p.exit(1,f'{exc}\n')
