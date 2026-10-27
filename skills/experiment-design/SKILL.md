---
name: experiment-design
description: "Design experiments, baselines and ablations that can support or falsify research claims."
---

# experiment-design

## Inputs and scope

Claims, datasets, metrics, available code, compute budget and constraints.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Map each claim to an observable comparison and specify data splits before looking at final outcomes.

2. Select meaningful baselines, ablations, seed counts and uncertainty reporting; prevent leakage and unequal budgets.

3. Define execution order, expected artifacts, failure criteria, negative-result handling and resource ceilings.

4. Identify the cheapest pilot that could invalidate the approach before an expensive run.

## Deliverable and verification

Experiment roadmap, claim/control/metric matrix, run manifest and analysis plan.

Do not choose metrics after seeing favorable results without disclosing exploration; unresolved data access blocks dependent runs.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Design ablations separating a model's architecture change from its training budget.
