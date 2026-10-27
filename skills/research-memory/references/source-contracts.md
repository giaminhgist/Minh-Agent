# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: research-wiki

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/research-wiki/SKILL.md)

Capability: Knowledge graph papers/ideas/experiments/claims, query/lint/stats

Preservation condition / known gap: V1 Markdown+JSON chưa tương đương đầy đủ graph operations.

## R: wiki-enrich

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/wiki-enrich/SKILL.md)

Capability: Fill paper-note TODOs từ nguồn đọc, giữ notes đã có

Preservation condition / known gap: Thêm enrich/backfill; tạo scaffold không bằng ingest đủ nội dung.
## Additional ARS modes

- academic-pipeline / inquiry ledger / replay / cross-run adjudication: Cần branch/ownership/stale contracts; Markdown notes v1 chưa tương đương schema ARS.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
