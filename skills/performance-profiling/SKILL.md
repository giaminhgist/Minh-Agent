---
name: performance-profiling
description: "Find measured runtime or memory bottlenecks and verify optimization effects."
---

# performance-profiling

## Inputs and scope

Representative workload, environment, baseline and performance objective.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Measure wall time, throughput or peak memory with a stable workload and note warmup/caching effects.

2. Use profiling tools available for the actual runtime; attribute costs to code paths or resources instead of guessing from source size.

3. Change one bottleneck at a time and compare under matched conditions, including correctness checks.

4. Report distribution or repeated-run variation where meaningful and distinguish microbenchmarks from end-to-end effects.

## Deliverable and verification

Profile, bottleneck explanation, benchmark comparison and correctness evidence.

Do not claim a speedup from unmatched machines or inputs; unavailable profiler data limits attribution.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Explain a training pipeline slowdown before changing the model.
