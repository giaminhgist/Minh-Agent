---
name: proof-writing
description: "Construct a mathematical proof for a fixed statement and assumptions."
---

# proof-writing

## Inputs and scope

Exact theorem, definitions, admissible assumptions and known lemmas.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Restate quantifiers and dependencies precisely; test edge cases before choosing a proof strategy.

2. Decompose into lemmas and write the argument so each inference has stated premises.

3. Check existence, boundary cases and whether imported lemmas meet their hypotheses.

4. Return the proof with a dependency list and remaining obligations, if any.

## Deliverable and verification

Theorem, proof, lemma dependencies and unresolved gaps.

Do not weaken a theorem silently or label a proof sketch complete.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Prove a convergence statement under explicitly stated boundedness assumptions.
