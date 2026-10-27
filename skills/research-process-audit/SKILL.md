---
name: research-process-audit
description: "Audit a research workflow's decisions, gates and evidence lineage."
---

# research-process-audit

## Inputs and scope

Project logs, artifact versions, stage requirements and audit scope.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Reconstruct the sequence of decisions and artifact changes from available records.

2. Check whether stage acceptance criteria were met and whether downstream conclusions used the correct versions.

3. Identify undocumented deviations, missing reviews and unresolved obligations; distinguish absent records from proven misconduct.

4. Produce a concise process summary with recoverable next actions.

## Deliverable and verification

Process timeline, gate/evidence matrix, deviations and remediation plan.

Do not infer a complete history from chat summaries alone or certify an unaudited stage.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Audit whether a paper pipeline used the final dataset and completed its required reviews.
