---
name: workspace-lifecycle
description: "Create or reuse isolated workspaces and finish development branches without losing work."
---

# workspace-lifecycle

## Inputs and scope

Repository status, intended base, worktree ownership and requested finish action.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Inspect existing worktrees and uncommitted changes. Prefer an appropriate existing workspace; create isolation only when justified by the task and supported by host tooling.

2. Establish dependencies and a baseline before edits. Record the actual checkout path and revision for later evidence.

3. At completion verify the change, then follow the authorized merge, PR, retain or discard choice. Preserve recoverable work before cleanup and confirm ownership of the target.

## Deliverable and verification

Workspace identity, baseline, delivery/retention decision and cleanup evidence.

Do not infer discard from inactivity or a failed test; do not remove a shared or unrelated checkout.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Prepare an isolated fix and keep the branch ready for review.
