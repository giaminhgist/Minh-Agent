---
name: parallel-task-execution
description: "Split independent work across authorized agents and integrate their results."
---

# parallel-task-execution

## Inputs and scope

Independent task candidates, shared resources, ownership and available delegation tools.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. First check whether delegation is permitted by the current host and instructions. Partition by non-overlapping writes or isolated workspaces, with explicit input/output contracts.

2. Give each worker sufficient raw context and acceptance criteria, without requiring them to infer shared state. Keep dependent tasks sequential.

3. Inspect outputs, resolve conflicts deliberately, and run integration checks. Attribute unverified worker claims as claims until checked.

## Deliverable and verification

Ownership map, worker deliverables and verified integrated result.

If delegation is unavailable or unauthorized, execute sequentially and disclose that parallel execution was not used.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Investigate three independent failing modules with isolated write ownership.
