# Catalog and benchmarks

CATALOG.md is the readable task index; catalog.json supplies exact names and profiles to the installer. The default Claude plugin exposes all 69 Skills. Codex users can install all, a catalog group or selected names without changing the source tree.

The ponytail-help capability is represented by the catalog, README and per-skill usage. Its off/mode/band/update features are not an implemented persistent UI here. The ponytail-gain capability is represented by transparent benchmark reporting, not by copying published gains into this repository's claims.

No token savings, speedup or reviewer reliability score has been measured for this collection. To compare against a baseline, keep the same task artifacts, tool permissions, model/runtime, stopping criteria and scoring rubric. Record failures, cost and latency as observed. Use held-out cases and multiple runs where variability matters; do not substitute prompt length for measured efficiency.

tests/acceptance-cases.json defines a request, required artifacts and failure boundary for each Skill. All cases start NOT_RUN. A result needs the actual output and a reviewed scoring record before its status can change. tests/test_repository.py covers executable helpers and packaging, not all these model-behavior cases.

awesome-harness-engineering contributes harness/evaluation ideas and an external resource index. This repository does not claim to include or audit every linked product. The pinned index remains available through docs/source-map.json.
