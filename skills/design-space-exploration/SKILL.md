---
name: design-space-exploration
description: "Explore configurations against explicit objectives and compute constraints."
---

# design-space-exploration

## Inputs and scope

Search space, objective direction, constraints, evaluator and budget.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Validate the evaluator and baseline before searching. Separate tunable dimensions from fixed experimental assumptions.

2. Select a search strategy appropriate to space size; record each attempted configuration and measured objectives.

3. Track feasible candidates and Pareto tradeoffs rather than hiding conflicting objectives behind an unexplained score.

4. Stop on budget, convergence or invalid evaluator; reproduce promising candidates before declaring improvement.

## Deliverable and verification

Trial ledger, feasible/Pareto set, reproducibility evidence and stopping reason.

Failed or timed-out evaluations are not favorable scores. Keep validation/test data out of tuning.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Explore latency versus accuracy under a fixed memory ceiling.
