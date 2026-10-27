---
name: lean-implementation
description: "Implement a scoped software change with a working vertical slice and explicit tradeoffs."
---

# lean-implementation

## Inputs and scope

Approved task, repository conventions, baseline behavior and requested mode.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Select lite for a small direct change, full for interface-affecting work, ultra for aggressive scope reduction within correctness requirements, or off to use repository defaults. Modes never disable security or correctness checks.

2. Build a minimal working path through the real interfaces, then add the remaining required behavior. Reuse established code before introducing abstractions.

3. Document assumptions and intentional limitations that affect users. Verify changed behavior and record actual commands/results; remove speculative scaffolding.

## Deliverable and verification

Working change, verification evidence and explicit deferred debt with upgrade conditions.

On a failed assumption, revise the design before layering workarounds; do not silently remove requested behavior to meet a simplicity target.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Add CSV export to an existing results table without replacing the UI.
