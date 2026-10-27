---
name: formal-proof
description: "Develop or continue a Lean proof and verify the exact theorem and axiom dependencies."
---

# formal-proof

## Inputs and scope

Lean project/version, target theorem, imports and partial proofs.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Inspect the project toolchain and reproduce its baseline before editing.

2. Match the formal theorem to the intended mathematical statement, including quantifiers and assumptions.

3. Prove incremental lemmas and compile with the real toolchain. Inspect placeholders and transitive axioms rather than only the final file.

4. Deliver source, build logs and the target/dependency audit.

## Deliverable and verification

Lean sources, actual compilation evidence, theorem comparison and axiom report.

No Lean installation means NOT_RUN. Do not replace the target with a trivial or stronger-assumption theorem to obtain a green build.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Complete a Lean lemma and show that no new axioms or sorry placeholders were introduced.
