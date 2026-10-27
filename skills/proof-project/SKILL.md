---
name: proof-project
description: "Manage a multi-stage proof effort with durable theorem and obligation state."
---

# proof-project

## Inputs and scope

Project goal, theorem graph, existing proof artifacts and verification tools.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Inventory target statements, lemmas and their dependencies; classify each as conjectured, sketched, proved, audited or formalized.

2. Work on ready obligations and retain evidence for every state change.

3. Audit the assembled argument and formalize selected components when tools are available; invalidate dependents when assumptions change.

4. Save a handoff with exact versions, unresolved obligations and the next executable step.

## Deliverable and verification

Proof dependency graph, artifact ledger, audit state and resume instructions.

State is not proof: no task advances to verified solely because a prior agent said complete.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Resume a proof project after a key lemma's assumptions changed.
