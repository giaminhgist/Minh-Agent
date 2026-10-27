---
name: compute-management
description: "Inspect and provision authorized compute resources with explicit cost and ownership tracking."
---

# compute-management

## Inputs and scope

Provider/account context, workload requirements, budget, storage and desired lifecycle action.

Use the user's requested language and deliverable format. This Skill supplies a workflow; it does not install services or grant access to accounts. Resolve tool availability in the current host before relying on an external backend.

## Workflow

1. Inspect available local/SSH/cloud resources and compare suitability with workload and transfer requirements.

2. Before a paid allocation, establish the authorized spend, duration and shutdown condition. Use provider tooling actually present and current documentation.

3. Record resource identifiers, region, environment and persistent storage. Separate job termination from deletion of data volumes.

4. At handoff report active resources and cleanup needs; stop/delete only resources in scope.

## Deliverable and verification

Resource plan, actual allocation records, cost assumptions and lifecycle status.

No credential or provider capability means NOT_RUN, not simulated provisioning; keep secrets out of artifacts.

Report what was actually inspected, executed and rendered. Preserve existing user work and authorization boundaries for external messages, publishing, paid compute and destructive cleanup.

## Mode details and sources

Read [source contracts](references/source-contracts.md) when selecting an upstream mode, provider adapter or checking feature parity. Those notes distinguish implemented guidance from upstream functionality still requiring tools or verification.

## Example

Prepare a bounded GPU run and list resources that remain billable afterwards.
