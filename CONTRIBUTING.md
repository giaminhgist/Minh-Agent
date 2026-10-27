# Contributing

Keep each Skill focused on a distinct user task. Before merging modes, preserve its trigger, inputs, decisions, outputs, dependencies and failure behavior in the source contract map.

Edit SKILL.md and conditional references together. Update catalog.json descriptions and tests/acceptance-cases.json when behavior changes. New executable helpers need real fixture tests including failure handling; instruction-only changes need realistic acceptance cases, not phrase-matching tests.

Run `python tools/validate.py` and `python -m unittest discover -s tests -v`. For Claude Code also run `claude plugin validate .` and a local plugin load when that CLI is available. For Codex test installation in a temporary project first. Record host/version and actual execution rather than asserting compatibility from a manifest.

Do not commit credentials, private papers, installed copies, generated test output or the user's chat backups. Source imports require pinned attribution and a compatible license. Increment plugin and catalog versions together for releases.
