# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: paper-slides

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/paper-slides/SKILL.md)

Capability: Paper→Beamer/PPTX, speaker notes và script

Preservation condition / known gap: Mode build; output editable và hình render phải được kiểm tra.

## R: paper-talk

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/paper-talk/SKILL.md)

Capability: Talk pipeline: outline→deck→polish→assurance/export

Preservation condition / known gap: Mode end-to-end giữ timing, claims, citation, anonymity.

## R: slides-polish

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/slides-polish/SKILL.md)

Capability: Per-page layout/render review, PPTX/Beamer sửa có mục tiêu

Preservation condition / known gap: Mode polish cho deck có sẵn; không ép rebuild.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
