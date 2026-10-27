# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## S: requesting-code-review

Source: [pinned manifest](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/requesting-code-review/SKILL.md)

Capability: Chuẩn bị base/head/spec, dispatch reviewer và follow-up

Preservation condition / known gap: Thêm request-review mode, khác tự review diff.

## S: receiving-code-review

Source: [pinned manifest](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/receiving-code-review/SKILL.md)

Capability: Hiểu/xác minh/phản biện/triển khai feedback và reply workflow

Preservation condition / known gap: Giữ feedback mode; gửi comment chỉ khi được yêu cầu.

## P: ponytail-review

Source: [pinned manifest](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/skills/ponytail-review/SKILL.md)

Capability: Review diff và connected code, lỗi tác động thực

Preservation condition / known gap: Giữ mode diff và finding input→bad effect.

## P: ponytail-audit

Source: [pinned manifest](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/skills/ponytail-audit/SKILL.md)

Capability: Audit toàn repo: bugs/security/load/tests/perf/bloat

Preservation condition / known gap: Giữ mode repo-audit, không áp mặc định vào mọi PR.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
