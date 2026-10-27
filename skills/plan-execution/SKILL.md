---
name: plan-execution
description: "Execute an existing multi-step plan inline with progress and evidence per task."
---

# plan-execution

## Inputs and scope

Plan, dependencies, acceptance criteria and authorized actions.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Check the plan against the present workspace and note stale assumptions before editing.

2. Execute ready tasks in dependency order; keep each task pending, active, blocked or verified. Ask only when an unresolved decision blocks consequential work.

3. Validate milestones and integrate the final artifacts. Record deviations with reasons and perform a final comparison against the requested outcome.

## Deliverable and verification

Completed artifacts, task ledger, verification and handoff.

If a task is blocked, preserve progress and continue independent tasks. Do not mark a plan complete while required outputs are missing.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Execute an approved manuscript revision plan and track each reviewer issue.
