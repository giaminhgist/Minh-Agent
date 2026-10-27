# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: paper-plan

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/paper-plan/SKILL.md)

Capability: Outline/story/claims-evidence/figure plan

Preservation condition / known gap: Giữ outline-only mode và writing handoff.

## R: paper-write

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/paper-write/SKILL.md)

Capability: Draft LaTeX theo section, citations, style và reverse outline

Preservation condition / known gap: Giữ standalone section draft; provenance writing sources cần audit.

## R: writing-systems-papers

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/writing-systems-papers/SKILL.md)

Capability: Systems-paper paragraph blueprint, design/eval structure

Preservation condition / known gap: Domain profile riêng; không ép template ML chung.

## A: academic-paper

Source: [pinned manifest](https://github.com/Imbad0202/academic-research-skills/blob/1ec249df98728682dfbbdfb940a658338bfd6f80/academic-paper/SKILL.md)

Capability: 11 mode: draft/outline/revision/abstract/lit-review/format/citation/plan/coach/disclosure/rebuttal-audit

Preservation condition / known gap: V1 thiếu bilingual/format/disclosure/committee; map thêm theo mode.
## Additional ARS modes

- academic-paper / full / outline-only / abstract-only: Bổ sung abstract song ngữ, keywords, outline evidence map và output-format selection.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
