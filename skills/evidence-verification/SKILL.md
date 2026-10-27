---
name: evidence-verification
description: "Check whether completion claims are supported by fresh, relevant evidence."
---

# evidence-verification

## Inputs and scope

Claims, exact artifact revision, commands, logs and acceptance criteria.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Associate each claim with an observable check and the inputs that determine its validity.

2. Run the required checks or inspect existing results only when their revision and environment still match. Distinguish static inspection, fixture tests and live integration tests.

3. Report PASS, FAIL, NOT_RUN or UNSUPPORTED separately, with scope and evidence location. Recheck only the checks invalidated by subsequent changes.

## Deliverable and verification

Claim-to-evidence table with revision, result and limitations.

A reviewer statement or successful file generation is not runtime evidence; downgrade unsupported claims.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Verify whether a generated plugin can honestly be called installed and tested.
