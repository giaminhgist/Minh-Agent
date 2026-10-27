# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## A: sr-screener

Source: [pinned manifest](https://github.com/Imbad0202/academic-research-skills/blob/1ec249df98728682dfbbdfb940a658338bfd6f80/sr-screener/SKILL.md)

Capability: 8 mode: protocol/quick/pilot/TA/FT/adjudicate/audit/report

Preservation condition / known gap: V1 chủ động loại; đưa lại vào full-coverage extension, license NC chưa port.
## Additional ARS modes

- sr-screener / protocol / quick / pilot: Protocol freeze, small triage, calibration against team labels.
- sr-screener / ta-screen / ft-screen: Resumable title/abstract và fulltext screening, page-anchored exclusions.
- sr-screener / adjudicate / audit: Conflict suggestions/exclusion audit; advisory vs final human decisions.
- sr-screener / report: XLSX, RIS groups, PRISMA counts, methods, corpus handoff.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
