# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: research-pipeline

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/research-pipeline/SKILL.md)

Capability: End-to-end idea→implementation→experiment→review→writing handoff

Preservation condition / known gap: State/resume v1 không thay thế phase-specific research orchestration.

## A: academic-pipeline

Source: [pinned manifest](https://github.com/Imbad0202/academic-research-skills/blob/1ec249df98728682dfbbdfb940a658338bfd6f80/academic-pipeline/SKILL.md)

Capability: 10 stage, integrity gates, resume/mid-entry, external reviews, process records

Preservation condition / known gap: State chung không thay Material Passport, branch/adjudication/collaboration semantics.
## Additional ARS modes

- academic-pipeline / 10 stages + mid-entry/external reviews: Giữ domain phases, integrity gates, review/revise/re-review/finalize; không thay bằng generic state machine.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
