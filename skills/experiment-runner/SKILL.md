---
name: experiment-runner
description: "Launch or inspect a scoped research experiment and collect reproducible results."
---

# experiment-runner

## Inputs and scope

Run command/config, dataset identity, environment, output location and compute authorization.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Record revision, config/seed, environment and input identities before launch. Confirm an existing run is not already active.

2. Launch through the available host or selected provider and retain its real process/job identifier.

3. Inspect status, logs, resource use and metrics; use a host scheduler only if recurring monitoring is requested.

4. On completion collect exit status, artifacts and missing results, then reconcile metrics with the plan.

## Deliverable and verification

Run record, logs, metrics, status and artifact references.

A lost connection is UNKNOWN rather than failed; inspect the backend before retrying. Stop or cancel only the identified authorized run.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Run one smoke configuration and report its actual metric file and exit status.
