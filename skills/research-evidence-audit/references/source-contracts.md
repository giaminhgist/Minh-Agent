# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: analyze-results

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/analyze-results/SKILL.md)

Capability: Thống kê, aggregate, bảng so sánh và diễn giải kết quả

Preservation condition / known gap: Giữ mode results; không trộn với integrity verdict.

## R: experiment-audit

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/experiment-audit/SKILL.md)

Capability: Trace evaluation/GT/metric và tính toàn vẹn kết quả

Preservation condition / known gap: Mode integrity riêng; sự advisory của skill khác parent gate.

## R: paper-claim-audit

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/paper-claim-audit/SKILL.md)

Capability: So manuscript claims/numbers với raw results

Preservation condition / known gap: Mode manuscript giữ source anchors và missing evidence.

## R: result-to-claim

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/result-to-claim/SKILL.md)

Capability: Claim support status và route pivot/supplement/confirm

Preservation condition / known gap: Giữ decision routing chứ không chỉ tính bảng.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
