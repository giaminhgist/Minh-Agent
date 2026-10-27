---
name: report-rendering
description: "Render a structured report as readable HTML or another requested document format."
---

# report-rendering

## Inputs and scope

Report content, audience, assets, links and output format.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Preserve evidence anchors and tables while structuring the report for reading.

2. Produce portable HTML with escaped content and local assets, or use available document tooling for the requested format.

3. Inspect overflow, table width, broken links and accessibility labels in the rendered output.

4. Keep editable source and report any unavailable export step.

## Deliverable and verification

Report source, rendered artifact and readability checks.

Do not substitute an HTML file for a requested PDF without disclosing the missing conversion.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Render an experiment audit as a self-contained HTML report.
