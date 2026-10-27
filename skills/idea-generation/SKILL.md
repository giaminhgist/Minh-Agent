---
name: idea-generation
description: "Generate and rank research ideas with novelty and feasibility checks."
---

# idea-generation

## Inputs and scope

Research area, available assets, expertise, time/compute limits and prior work.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Derive candidate mechanisms from concrete gaps or conflicting findings rather than topic variations.

2. For each candidate state the problem, mechanism, closest work, testable improvement and cheapest falsifying experiment.

3. Rank using explicit novelty, impact, feasibility and evidence criteria. Preserve rejected candidates with reasons and distinguish speculation from pilot evidence.

## Deliverable and verification

Ranked idea cards, rejected alternatives, novelty risks and pilot plans.

If closest work is unknown, mark novelty unresolved rather than claiming originality; do not invent pilot results.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Propose feasible ideas for a two-week project with a single GPU.
