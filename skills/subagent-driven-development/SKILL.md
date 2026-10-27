---
name: subagent-driven-development
description: "Deliver a plan through isolated implementer and reviewer contexts when delegation is authorized."
---

# subagent-driven-development

## Inputs and scope

Task plan, repository state, specification and available agent mechanisms.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Give one implementer a bounded task and raw context, with ownership boundaries.

2. Review the result against the specification before assessing maintainability. Use separate review context when available and permitted; return concrete issues for correction.

3. Verify fixes and integrate completed tasks, then review the assembled change against the overall plan.

## Deliverable and verification

Per-task implementation and review records plus integration evidence.

Do not treat different prompts as statistical independence. If agents are unavailable, use a disclosed inline implementation/review cycle.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Implement a parser task and review both its spec compliance and error handling.
