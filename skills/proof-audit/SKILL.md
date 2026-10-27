---
name: proof-audit
description: "Audit a mathematical proof for gaps, invalid assumptions and counterexamples."
---

# proof-audit

## Inputs and scope

Theorem, complete proposed proof and allowed premises.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Parse the exact target and compare it with the statement actually established.

2. Trace dependencies and inspect critical quantifier changes, limit exchanges, circular reasoning and missing edge cases.

3. Seek small counterexamples or failed lemma hypotheses, and separate a repairable gap from a false theorem.

4. Report verified portions and obligations without rewriting the theorem unnoticed.

## Deliverable and verification

Proof audit, localized gaps/counterexamples and repair requirements.

A missing proof cannot be certified. Compilation of a different statement is not evidence for the target.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Audit a proof that exchanges a limit and an expectation without justification.
