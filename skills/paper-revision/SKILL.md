---
name: paper-revision
description: "Revise a manuscript against a review or improvement objective while controlling claim regressions."
---

# paper-revision

## Inputs and scope

Manuscript, comments, evidence, editable scope and build target.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Translate comments into concrete changes with an allowed-edit scope. Separate textual correction from requests for new evidence.

2. Apply focused edits and preserve terminology, cross-references and valid existing claims.

3. Compare changed assertions with raw evidence and ensure an improvement in one section does not contradict another.

4. Rebuild and inspect the affected pages when tools are available. Bound review/revise loops by issue resolution and evidence, not a model score.

## Deliverable and verification

Revised sources, issue/change/evidence ledger, rendered output when available and remaining issues.

If a comment requires new experiments, identify it rather than inventing results; report compile/render failures.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Address clarity comments without altering the reported experimental results.
