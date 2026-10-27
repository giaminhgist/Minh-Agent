# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: monitor-experiment

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/monitor-experiment/SKILL.md)

Capability: Status/process/log/metric snapshots của run

Preservation condition / known gap: Giữ monitoring; polling định kỳ dùng host scheduler.

## R: run-experiment

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/run-experiment/SKILL.md)

Capability: Launch local/SSH/Vast/Modal, collect logs/artifacts

Preservation condition / known gap: Tách backend lifecycle khỏi execution; hiện chưa có backend test.

## R: training-check

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/training-check/SKILL.md)

Capability: NaN/divergence/idle GPU và health monitoring

Preservation condition / known gap: Stop policy phải được cho phép; state không đồng nhất quality.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
