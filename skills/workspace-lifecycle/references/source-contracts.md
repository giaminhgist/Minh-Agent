# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## S: using-git-worktrees

Source: [pinned manifest](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/using-git-worktrees/SKILL.md)

Capability: Phát hiện isolation, native/Git fallback, setup và baseline

Preservation condition / known gap: V1 loại entrypoint; khôi phục capability có trigger rõ và host ownership.

## S: finishing-a-development-branch

Source: [pinned manifest](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/finishing-a-development-branch/SKILL.md)

Capability: Verify→merge/PR/keep/discard choice→cleanup

Preservation condition / known gap: Native tools không tự thay toàn bộ decision workflow; preserve work.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
