---
name: experiment-implementation
description: "Translate an experiment plan into executable code and a verified smoke-run handoff."
---

# experiment-implementation

## Inputs and scope

Approved experiment design, codebase, data paths and target environment.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Connect each planned claim/metric to code, configuration and output artifacts. Implement the smallest complete baseline before variants.

2. Validate shapes, split boundaries, metrics and deterministic seed handling with a small fixture.

3. Run an affordable smoke test within authorization and capture revision, environment, command and output location.

4. Prepare deployment/run instructions for the actual target; do not confuse local smoke success with remote readiness.

## Deliverable and verification

Experiment code, configs, smoke evidence and runner handoff.

Missing data or remote tooling yields a blocked deployment step, not fabricated initial results.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Implement a baseline and ablation configuration with a tiny synthetic smoke test.
