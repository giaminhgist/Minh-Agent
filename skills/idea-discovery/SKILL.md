---
name: idea-discovery
description: "Run an end-to-end discovery workflow from literature gaps to a refined research proposal."
---

# idea-discovery

## Inputs and scope

Topic, existing ideas, constraints and desired stopping point.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Establish a literature map and generate candidates; independently examine closest prior work before selecting a direction.

2. Stress-test feasibility and possible negative outcomes. For robotics specify embodiment, observations/actions, simulator, benchmark, hardware availability and transfer risk.

3. Refine promising candidates into a mechanism, contribution claims and a minimal pilot. Execute a pilot only within available authorized resources.

4. Deliver the chosen proposal and experiment handoff, preserving why other candidates were rejected.

## Deliverable and verification

Survey, ranked candidates, novelty comparison, refined proposal and pilot evidence or NOT_RUN.

A novelty check alone is not discovery. Stop at the user's requested stage and retain unresolved viability questions.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Discover a robotics research direction with simulator-only resources.
