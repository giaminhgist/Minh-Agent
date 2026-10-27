---
name: paper-figures
description: "Create reproducible scientific plots and tables from real data."
---

# paper-figures

## Inputs and scope

Raw data, column meanings/units, intended claim, plot style and publication dimensions.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Validate rows, units, missingness, aggregation and uncertainty definitions before plotting.

2. Choose an encoding suited to the comparison; preserve denominators and avoid misleading axes. Use the bundled SVG helper for simple numeric line/bar/scatter plots or a suitable scientific plotting library for advanced plots.

3. Keep generation code and input identity alongside editable/vector outputs. Label panels, units and uncertainty; write a caption supported by the plotted data.

4. Render and inspect legibility at final size; ensure the figure and manuscript use the same numbers.

## Deliverable and verification

Data provenance, reproducible generation command/code, SVG/PDF as available, preview and caption.

Never use generated imagery as scientific measurements. Unsupported plot types require another renderer rather than silently changing the analysis.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

For the bundled executable adapter, read [local helper usage and limits](references/local-helper.md) before running it. Resolve scripts relative to this Skill directory, not the user's project.

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Create a multi-seed accuracy plot with a caption and reproducible source.
