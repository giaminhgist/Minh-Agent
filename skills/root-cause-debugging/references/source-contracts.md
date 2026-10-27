# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: web-debug-search

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/web-debug-search/SKILL.md)

Capability: GitHub/Q&A/community/docs search, version compatibility

Preservation condition / known gap: Mode external discovery; không tự xác nhận workaround hoặc biến thành citation paper.

## S: systematic-debugging

Source: [pinned manifest](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/systematic-debugging/SKILL.md)

Capability: Root cause, hypothesis testing, trace/polluter/condition-based waiting

Preservation condition / known gap: Giữ supporting techniques, không chỉ khẩu hiệu tìm nguyên nhân.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
