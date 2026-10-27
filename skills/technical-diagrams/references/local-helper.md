# simple-diagram-v1

This local schema is intentionally distinct from upstream FigureSpec. It supports finite positioned rectangular nodes and straight directed edges. Labels can contain newlines. It rejects unknown endpoints, duplicate IDs, out-of-bounds nodes, oversized labels and self-loops. It does not automatically route around overlapping nodes.

```json
{"schema":"simple-diagram-v1","width":720,"height":260,"title":"Method overview","nodes":[{"id":"input","x":40,"y":90,"width":160,"height":70,"label":"Input data"},{"id":"model","x":280,"y":90,"width":160,"height":70,"label":"Model"},{"id":"output","x":520,"y":90,"width":160,"height":70,"label":"Prediction"}],"edges":[{"source":"input","target":"model","label":"features"},{"source":"model","target":"output"}]}
```

```text
python <skill-directory>/scripts/render_svg.py diagram.json diagram.svg
```

Output must be a new file. Review semantic arrows and layout in an actual renderer. PDF export requires a separate available converter. Mermaid sequence/class/ER/Gantt diagrams use the host's Mermaid workflow, not this schema.
