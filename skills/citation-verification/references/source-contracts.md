# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: citation-audit

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/citation-audit/SKILL.md)

Capability: Citation có thật, đúng metadata và đúng context

Preservation condition / known gap: Ba loại kiểm tra riêng; source inaccessible ≠ false.

## R: citation-crosscheck

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/citation-crosscheck/SKILL.md)

Capability: Đối chiếu field bib–web và bảng side-by-side

Preservation condition / known gap: Thêm XLSX export và isolation contract; generic ledger v1 chưa đủ.
## Additional ARS modes

- academic-paper / citation-check: Locale-aware citation checks; không áp Latin-name sorting cho mọi ngôn ngữ.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
