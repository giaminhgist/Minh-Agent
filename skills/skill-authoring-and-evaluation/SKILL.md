---
name: skill-authoring-and-evaluation
description: "Create, revise or evaluate a reusable Skill, including proposed improvements from run logs."
---

# skill-authoring-and-evaluation

## Inputs and scope

Target task, host format, existing Skill and representative requests.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Use an available skill-creator workflow where present. Define precise activation boundaries, required outputs and neighboring tasks that should not trigger the Skill.

2. Keep essential decisions in SKILL.md and load conditional references by mode. Add scripts only for repeated deterministic operations.

3. Compare observable outcomes on realistic baseline and with-skill tasks when an evaluation runner is available. Include a boundary and failure case.

4. For optimize/apply mode, prepare a source patch with evidence, apply within authorized scope, validate and retain a reversible diff.

## Deliverable and verification

Skill bundle, source attribution, evaluation cases/results and change rationale.

Structural validation alone does not establish behavioral quality. Do not self-modify a whole corpus from one anecdote.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Create a CSV chart Skill and test valid input, missing data and an unrelated image request.
