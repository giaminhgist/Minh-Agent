# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: meta-apply

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/meta-apply/SKILL.md)

Capability: Áp corpus patch sau lựa chọn/review và kiểm tra

Preservation condition / known gap: V1 chủ động bỏ tự apply; khôi phục apply có yêu cầu, test và rollback.

## R: meta-optimize

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/meta-optimize/SKILL.md)

Capability: Dùng run logs đề xuất cải tiến corpus

Preservation condition / known gap: Audit v1 chưa thay hết optimization/apply cycle.

## S: writing-skills

Source: [pinned manifest](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/writing-skills/SKILL.md)

Capability: Author Skill, trigger discovery, baseline/with-skill behavior tests

Preservation condition / known gap: Không để audit-only v1 làm mất authoring; reuse skill-creator có sẵn.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
