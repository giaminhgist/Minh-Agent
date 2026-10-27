# Maintaining Minh-Agent Skills

The user approved all 69 catalog entries and three integration/documentation groups on 2026-10-27. Keep Claude Code plugin packaging and Codex installation supported from one skills/ source tree.

- SKILL.md is the authoritative instruction; catalog.json indexes it. Update both when changing names or trigger descriptions.
- Preserve source-to-mode coverage in docs/source-map.json and each Skill's references/source-contracts.md. A missing backend is not a reason to silently remove a capability.
- Keep workflows provider-neutral; select tools that actually exist in the active host. No automatic hooks, account configuration or external sends are installed by this package.
- Read LICENSE and THIRD_PARTY_NOTICES.md before importing upstream text or code. Do not apply a blanket MIT label to ARS-related guidance.
- Use Python standard library for repository tooling. Run `python tools/validate.py` and `python -m unittest discover -s tests -v` after relevant changes. Do not treat these checks as behavioral evaluation of all 69 Skills.
- Record real test evidence in docs/VALIDATION.md; unsupported and unrun integrations stay explicit. Never replace NOT_RUN with PASS from structural validation.
- Keep generated test artifacts in a temporary directory. Preserve session-backups outside this repository.
