---
name: formula-derivation
description: "Derive a mathematical expression with explicit assumptions and notation."
---

# formula-derivation

## Inputs and scope

Target expression, definitions, domain restrictions and starting relations.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Normalize notation and list dimensions, domains and regularity assumptions.

2. Derive in checkable steps with the rule used at each nontrivial transition; distinguish equality, approximation and asymptotic statements.

3. Check limiting cases, dimensions and numerical examples where meaningful.

4. State the resulting formula with its domain of validity and unresolved steps.

## Deliverable and verification

Derivation, assumptions, sanity checks and limitations.

A plausible symbolic expression is not a proof; if a step cannot be justified, isolate it as an obligation.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Derive a loss gradient and check its dimensions and boundary cases.
