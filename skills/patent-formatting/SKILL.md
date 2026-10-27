---
name: patent-formatting
description: "Format a patent package for a specified jurisdiction and output template."
---

# patent-formatting

## Inputs and scope

Draft package, target CN/US/EP or other jurisdiction, current requirements and format.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Retrieve or use supplied current official formatting requirements for the actual filing route.

2. Map sections, numbering, drawings and forms to those requirements without altering technical scope silently.

3. Generate editable documents using available document tools and render-check pagination, figures and references.

4. List unresolved administrative requirements separately from formatting success.

## Deliverable and verification

Formatted draft package, compliance checklist and rendering evidence.

Do not call the package filing-ready solely because it matches a template; missing legal or administrative inputs remain open.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Format a supplied patent draft into DOCX using a provided jurisdiction template.
