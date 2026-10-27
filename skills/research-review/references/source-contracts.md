# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: auto-review-loop-llm

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/auto-review-loop-llm/SKILL.md)

Capability: Review nhiều vòng qua API OpenAI-compatible

Preservation condition / known gap: Giữ generic reviewer adapter; không giả định giống Codex về assurance.

## R: auto-review-loop-minimax

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/auto-review-loop-minimax/SKILL.md)

Capability: Review nhiều vòng qua MiniMax MCP/API

Preservation condition / known gap: Giữ MiniMax adapter; state/retry phải tương thích contract chung.

## R: auto-review-loop

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/auto-review-loop/SKILL.md)

Capability: Review–revise nghiên cứu, phản hồi và stop gates

Preservation condition / known gap: Giữ bounded iteration và verdict scope; không tự coi score tăng là đúng.

## R: kill-argument

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/kill-argument/SKILL.md)

Capability: Adversarial attack→defense→unresolved issue adjudication

Preservation condition / known gap: V1 nhắc phản luận nhưng thiếu hai lượt độc lập và verdict contract.

## R: research-review

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/research-review/SKILL.md)

Capability: Critical review idea/method/results/manuscript

Preservation condition / known gap: Giữ standalone review cùng rubric/anchors.

## A: academic-paper-reviewer

Source: [pinned manifest](https://github.com/Imbad0202/academic-research-skills/blob/1ec249df98728682dfbbdfb940a658338bfd6f80/academic-paper-reviewer/SKILL.md)

Capability: 6 mode: full/quick/methodology/re-review/guided/calibration

Preservation condition / known gap: Không gọi review thường là đã có calibration/guided/re-review contracts.
## Additional ARS modes

- deep-research / review: Review văn bản được cung cấp, không chạy research mới mặc định.
- academic-paper-reviewer / full / quick / methodology-focus: Giữ rubric và scope; multi-seat panel là mode optional, không default bắt buộc.
- academic-paper-reviewer / re-review: Kiểm actual revisions theo frozen criteria; không chỉ hỏi reviewer chấm lại.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
