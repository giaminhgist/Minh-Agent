---
name: paper-build-and-format
description: "Compile, format or convert a paper and inspect the rendered document."
---

# paper-build-and-format

## Inputs and scope

Main source, supporting assets, bibliography, target format and venue/template.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Identify the real main document and build method; preserve project-relative assets and bibliography.

2. For LaTeX use the available compiler with required passes and bibliography tools, capturing logs. For DOCX/other formats use appropriate document tooling and retain editable sources.

3. Resolve errors within a bounded repair loop and inspect rendered pages for clipping, figure placement, references, page limits and missing glyphs.

4. Report the exact engine/template and any remaining warnings that affect output.

## Deliverable and verification

Build command/log, editable sources, rendered artifact and layout findings.

Opening an editor is not compilation evidence. If no compiler/converter exists, provide source and NOT_RUN status rather than claiming a PDF.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Compile a multi-file LaTeX paper and identify unresolved citations.
