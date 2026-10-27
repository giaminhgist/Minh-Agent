# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: qzcli

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/qzcli/SKILL.md)

Capability: Qizhi resource discovery, submit/stop/list/watch/batch jobs

Preservation condition / known gap: Qizhi adapter; có external CLI cần kiểm chứng, không chỉ GPU runner.

## R: serverless-modal

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/serverless-modal/SKILL.md)

Capability: GPU training/inference/batch/API service, volume/results/cost

Preservation condition / known gap: Modal adapter phải giữ cả inference/service, không chỉ training job.

## R: vast-gpu

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/vast-gpu/SKILL.md)

Capability: Provision/rent/setup/list/destroy GPU instances

Preservation condition / known gap: Vast adapter; destructive cleanup có resource identity, không blanket destroy.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
