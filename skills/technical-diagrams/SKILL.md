---
name: technical-diagrams
description: "Create editable architecture, workflow or relationship diagrams using structured vector sources."
---

# technical-diagrams

## Inputs and scope

Entities, relationships, labels, layout constraints and desired diagram type.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Choose Mermaid for supported structural/sequence/ER/Gantt types or a structured vector spec for exact positioned diagrams.

2. Validate node identifiers, edge endpoints, relationship semantics and reading order before rendering.

3. Use the bundled simple-diagram-v1 renderer for boxes/arrows, or an available full FigureSpec renderer for that upstream schema. These schemas are not interchangeable.

4. Keep source and SVG; export PDF when a real converter is available and inspect arrows, overlaps and label legibility.

## Deliverable and verification

Editable diagram source, SVG, optional PDF and semantic/layout checks.

Report renderer limitations; do not present the simple schema as complete upstream FigureSpec parity.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

For the bundled executable adapter, read [local helper usage and limits](references/local-helper.md) before running it. Resolve scripts relative to this Skill directory, not the user's project.

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Draw a model architecture with labeled tensors and editable arrows.
