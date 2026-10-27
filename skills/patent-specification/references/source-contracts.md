# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: embodiment-description

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/embodiment-description/SKILL.md)

Capability: Mô tả cách thực hiện invention, variations, claim support

Preservation condition / known gap: Mode embodiments với numeral consistency; không bịa implementation.

## R: figure-description

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/figure-description/SKILL.md)

Capability: Mô tả patent drawings và reference numerals

Preservation condition / known gap: Mode drawings; không phải công cụ tạo paper figure.

## R: specification-writing

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/specification-writing/SKILL.md)

Capability: Patent specification với drawings/embodiments/support

Preservation condition / known gap: Dù catalog nguồn xếp paper-core, manifest thực là patent.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
