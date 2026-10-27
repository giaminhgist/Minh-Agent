# Coverage: guidance, local execution and unresolved parity

Approved scope: 69 task Skills plus host-integration, notification-integration and catalog-and-benchmarks. All 69 entrypoints now have authored instructions; all 113 canonical source entrypoints have an explicit design destination in [source-map.json](source-map.json). The 28 additional ARS mode groups are retained there and in relevant source-contract references.

## What exists

- Task-specific activation, inputs, workflows, output contracts, failure handling and examples for all 69 Skills.
- Pinned source/mode notes attached to each task, including aliases and intentionally changed behavior.
- Claude Code plugin and local/Git-hostable marketplace manifests; one common Skill tree for the Codex/OpenCode installer.
- Four executable local adapters: numeric CSV→SVG with provenance, simple-diagram-v1→editable SVG, serial local queue with safe resume, and read-only debt scanner.
- Structural validation, executable fixture tests, package checksums, and 69 unrun behavioral acceptance cases.

## What is still partial or unavailable

| Area | Actual status |
|---|---|
| Full source equivalence | Not established; entrypoint mapping is complete, flag/mode/helper parity is not |
| ARIS 110 host/reviewer variants | Full diff remains outstanding; provider-neutral guidance is not a verified port |
| Search/reviewer providers | Selection/fallback contracts written; provider SDK/API clients not included or integration-tested |
| Experiments | Local serial queue tested; remote SSH/screen, wave scheduling, OOM retry, GPU/cloud allocation not implemented in this bundle |
| Paper figures | Basic numeric line/bar/scatter SVG helper; advanced statistics/multipanel/PDF rely on available external plotting tools |
| Diagrams | Local small schema plus Mermaid guidance; not the complete upstream FigureSpec schema/renderer |
| Illustrations/talks/posters | Authored workflows require actual image/document/render tools; no bundled image service or full poster layout engine |
| Integrity forensics | Deterministic triage guidance; full external Anti-Autoresearch engine absent; no CLEAN verdict from limited checks |
| ARS compatibility | Task/mode guidance exists; exact Material Passport/wire schemas, all rubrics and authority profiles not ported |
| Recurring literature monitoring | Workflow/configuration guidance; no background job unless a real scheduler is configured at user request |
| Overleaf | Sync workflow; no live account/bridge test |
| Host UI | Ponytail band/statusline/telemetry and cross-host hooks absent |
| License | Pinned attribution retained; unresolved component provenance prevents a blanket permissive redistribution claim |
| Model behavior | 69 acceptance cases specified, not independently executed; no production/reliability claim |

## Intentional changes

No source can grant automatic permission to push, send messages, spend on compute, discard work or proceed on a timeout. User authorization and active host rules govern those actions. These actions can still be performed when authorized with real supporting tools.

Paper-poster remains an alias in source mapping to the HTML poster workflow; the retired renderer is not restored. Generic plan execution, task delegation, subagent development, proof writing/auditing/formalization and research/grant proposals retain separate contracts where their evidence and outputs differ.

## Upgrading a coverage claim

For each source mode verify trigger routing, accepted inputs, important workflow steps, output schema/formats, dependencies, side effects and failure semantics. Execute a representative positive case and a meaningful failure case on the target host. Attach the artifacts and revision to the claim. Only then mark that mode covered at runtime; a passed metadata validator is insufficient.
