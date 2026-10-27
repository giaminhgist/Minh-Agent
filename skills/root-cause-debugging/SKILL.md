---
name: root-cause-debugging
description: "Investigate a reproducible failure, flaky test or compatibility problem before applying a fix."
---

# root-cause-debugging

## Inputs and scope

Observed versus expected behavior, reproducer, logs, versions and recent changes.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Reproduce the smallest failing case and capture the first meaningful divergence. Trace invalid state backward through callers or process boundaries.

2. Write a falsifiable cause hypothesis and change one variable at a time. For order-dependent tests, isolate the polluting predecessor; for races, wait on the observable condition with a deadline instead of increasing arbitrary sleeps.

3. Check official version-specific documentation and relevant issue discussions for external failures. Fix the cause, add a regression check where meaningful and rerun the original reproducer.

## Deliverable and verification

Root-cause chain, minimal correction, regression evidence and residual uncertainty.

If reproduction is unavailable, label hypotheses and request targeted evidence; do not present a guessed patch as a confirmed fix.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Diagnose a test that passes alone but fails after the integration suite.
