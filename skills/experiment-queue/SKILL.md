---
name: experiment-queue
description: "Schedule batches of seeds/configurations with bounded concurrency and safe resume."
---

# experiment-queue

## Inputs and scope

Job manifest, backend, concurrency/budget limits and retry policy.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Validate unique job identities, commands and output isolation. Use the bundled local serial runner only for trusted local manifests; remote SSH/screen or cloud execution needs an actual adapter.

2. Persist state before launch and retain backend identity. Do not relaunch an ambiguous running job after interruption until it has been reconciled.

3. Retry only classified transient failures within a declared attempt limit. An OOM retry must record changed resource/config settings rather than silently alter the experiment.

4. Collect per-job results and distinguish succeeded, failed, pending and unknown jobs.

## Deliverable and verification

Durable queue state, attempt history, logs and completion summary.

Local helper is serial, not SSH/screen or Modal/Vast parity. Never retry an unknown launch automatically.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

For the bundled executable adapter, read [local helper usage and limits](references/local-helper.md) before running it. Resolve scripts relative to this Skill directory, not the user's project.

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Run two local seeds, resume the queue and verify successful jobs are not launched twice.
