# Catalog — 69 Skills

All entries are implemented as task guidance. Behavioral evaluations remain NOT_RUN unless separately documented; source mapping is not full backend parity. See [coverage](docs/COVERAGE.md) and [validation](docs/VALIDATION.md).

## Coding & delivery

| Skill | When to use |
|---|---|
| [scoped-planning](skills/scoped-planning/SKILL.md) | Turn an ambiguous change or research task into a design and executable plan before implementation. |
| [lean-implementation](skills/lean-implementation/SKILL.md) | Implement a scoped software change with a working vertical slice and explicit tradeoffs. |
| [root-cause-debugging](skills/root-cause-debugging/SKILL.md) | Investigate a reproducible failure, flaky test or compatibility problem before applying a fix. |
| [test-driven-development](skills/test-driven-development/SKILL.md) | Use a red-green-refactor loop for a requested behavior change or regression fix. |
| [evidence-verification](skills/evidence-verification/SKILL.md) | Check whether completion claims are supported by fresh, relevant evidence. |
| [code-review](skills/code-review/SKILL.md) | Review a diff or repository, prepare a review request, or evaluate incoming review feedback. |
| [plan-execution](skills/plan-execution/SKILL.md) | Execute an existing multi-step plan inline with progress and evidence per task. |
| [parallel-task-execution](skills/parallel-task-execution/SKILL.md) | Split independent work across authorized agents and integrate their results. |
| [subagent-driven-development](skills/subagent-driven-development/SKILL.md) | Deliver a plan through isolated implementer and reviewer contexts when delegation is authorized. |
| [workspace-lifecycle](skills/workspace-lifecycle/SKILL.md) | Create or reuse isolated workspaces and finish development branches without losing work. |
| [agent-session-diagnostics](skills/agent-session-diagnostics/SKILL.md) | Analyze agent session logs for repeated work, wasted calls and workflow failures. |
| [technical-debt-ledger](skills/technical-debt-ledger/SKILL.md) | Inventory intentional shortcuts and define measurable conditions for retiring them. |

## Skill engineering

| Skill | When to use |
|---|---|
| [skill-authoring-and-evaluation](skills/skill-authoring-and-evaluation/SKILL.md) | Create, revise or evaluate a reusable Skill, including proposed improvements from run logs. |

## Discovery & proposals

| Skill | When to use |
|---|---|
| [literature-review](skills/literature-review/SKILL.md) | Search and synthesize literature, compare prior work or assess a specific novelty claim. |
| [paper-reading](skills/paper-reading/SKILL.md) | Read one or a small set of papers and explain methods, evidence and limitations. |
| [idea-generation](skills/idea-generation/SKILL.md) | Generate and rank research ideas with novelty and feasibility checks. |
| [idea-discovery](skills/idea-discovery/SKILL.md) | Run an end-to-end discovery workflow from literature gaps to a refined research proposal. |
| [research-proposal](skills/research-proposal/SKILL.md) | Write or refine a technical research proposal with testable contributions and an experiment plan. |
| [grant-proposal](skills/grant-proposal/SKILL.md) | Draft or revise a funding proposal against a specific call and agency requirements. |

## Experiments & compute

| Skill | When to use |
|---|---|
| [experiment-design](skills/experiment-design/SKILL.md) | Design experiments, baselines and ablations that can support or falsify research claims. |
| [experiment-implementation](skills/experiment-implementation/SKILL.md) | Translate an experiment plan into executable code and a verified smoke-run handoff. |
| [experiment-runner](skills/experiment-runner/SKILL.md) | Launch or inspect a scoped research experiment and collect reproducible results. |
| [experiment-queue](skills/experiment-queue/SKILL.md) | Schedule batches of seeds/configurations with bounded concurrency and safe resume. |
| [compute-management](skills/compute-management/SKILL.md) | Inspect and provision authorized compute resources with explicit cost and ownership tracking. |
| [design-space-exploration](skills/design-space-exploration/SKILL.md) | Explore configurations against explicit objectives and compute constraints. |
| [performance-profiling](skills/performance-profiling/SKILL.md) | Find measured runtime or memory bottlenecks and verify optimization effects. |
| [research-evidence-audit](skills/research-evidence-audit/SKILL.md) | Analyze experiment results or audit manuscript claims against raw research evidence. |

## Paper writing & review

| Skill | When to use |
|---|---|
| [manuscript-writing](skills/manuscript-writing/SKILL.md) | Draft a research paper, outline, abstract or section from traceable evidence. |
| [paper-revision](skills/paper-revision/SKILL.md) | Revise a manuscript against a review or improvement objective while controlling claim regressions. |
| [paper-pipeline](skills/paper-pipeline/SKILL.md) | Coordinate evidence, outline, writing, figures, review and build into a paper deliverable. |
| [paper-build-and-format](skills/paper-build-and-format/SKILL.md) | Compile, format or convert a paper and inspect the rendered document. |
| [citation-verification](skills/citation-verification/SKILL.md) | Verify bibliographic metadata, reference existence and support for cited claims. |
| [research-review](skills/research-review/SKILL.md) | Review research quality or a revised manuscript with explicit scope and evidence. |
| [rebuttal-and-response](skills/rebuttal-and-response/SKILL.md) | Prepare point-by-point reviewer responses and audit their consistency with revisions. |
| [venue-transfer](skills/venue-transfer/SKILL.md) | Adapt a paper to a new venue while tracking scope and submission constraints. |
| [integrity-forensics](skills/integrity-forensics/SKILL.md) | Perform scoped research-integrity triage or prepare a supported external forensic run. |

## Figures & communication

| Skill | When to use |
|---|---|
| [paper-figures](skills/paper-figures/SKILL.md) | Create reproducible scientific plots and tables from real data. |
| [technical-diagrams](skills/technical-diagrams/SKILL.md) | Create editable architecture, workflow or relationship diagrams using structured vector sources. |
| [scientific-illustration](skills/scientific-illustration/SKILL.md) | Create conceptual scientific illustrations with an available image-generation tool. |
| [research-talk](skills/research-talk/SKILL.md) | Build, polish or coordinate a research presentation with speaker support. |
| [research-poster](skills/research-poster/SKILL.md) | Create an academic HTML/CSS poster with real assets and a print-size layout. |

## Theory & proofs

| Skill | When to use |
|---|---|
| [formula-derivation](skills/formula-derivation/SKILL.md) | Derive a mathematical expression with explicit assumptions and notation. |
| [proof-writing](skills/proof-writing/SKILL.md) | Construct a mathematical proof for a fixed statement and assumptions. |
| [proof-audit](skills/proof-audit/SKILL.md) | Audit a mathematical proof for gaps, invalid assumptions and counterexamples. |
| [formal-proof](skills/formal-proof/SKILL.md) | Develop or continue a Lean proof and verify the exact theorem and axiom dependencies. |
| [proof-project](skills/proof-project/SKILL.md) | Manage a multi-stage proof effort with durable theorem and obligation state. |

## Patents

| Skill | When to use |
|---|---|
| [patent-prior-art](skills/patent-prior-art/SKILL.md) | Search and organize patent and non-patent prior art for an invention. |
| [invention-design](skills/invention-design/SKILL.md) | Structure an invention disclosure and explore technically grounded variants. |
| [patent-claims](skills/patent-claims/SKILL.md) | Draft patent claim candidates and map their support to a disclosure. |
| [patent-specification](skills/patent-specification/SKILL.md) | Draft a patent specification, embodiments and drawing descriptions from supported material. |
| [patent-review](skills/patent-review/SKILL.md) | Review a patent draft for internal consistency, support and technical clarity. |
| [patent-formatting](skills/patent-formatting/SKILL.md) | Format a patent package for a specified jurisdiction and output template. |
| [patent-workflow](skills/patent-workflow/SKILL.md) | Coordinate prior-art search, invention structuring, claims, specification and review. |

## Knowledge & utilities

| Skill | When to use |
|---|---|
| [research-memory](skills/research-memory/SKILL.md) | Maintain a research knowledge base with traceable sources and resumable context. |
| [research-workflow](skills/research-workflow/SKILL.md) | Coordinate a research project across discovery, experiments, writing and review with durable state. |
| [overleaf-sync](skills/overleaf-sync/SKILL.md) | Set up or reconcile synchronization between a local LaTeX project and Overleaf. |
| [report-rendering](skills/report-rendering/SKILL.md) | Render a structured report as readable HTML or another requested document format. |
| [technical-tutorial](skills/technical-tutorial/SKILL.md) | Create a technical tutorial with explanations, derivations, runnable examples and assessment questions. |
| [pixel-art](skills/pixel-art/SKILL.md) | Create or edit pixel-art assets with a deliberate palette and native pixel grid. |

## ARS specialist extensions

| Skill | When to use |
|---|---|
| [systematic-screening](skills/systematic-screening/SKILL.md) | Screen records for a systematic review with explicit eligibility and adjudication. |
| [systematic-review](skills/systematic-review/SKILL.md) | Conduct a protocol-based literature review with reproducible search, screening and synthesis. |
| [research-coaching](skills/research-coaching/SKILL.md) | Guide a researcher through question formation, reading or writing without taking over their decisions. |
| [research-fact-check](skills/research-fact-check/SKILL.md) | Verify factual research statements against accessible primary evidence. |
| [publication-disclosure](skills/publication-disclosure/SKILL.md) | Draft accurate publication disclosures for AI assistance, contributions and research practices. |
| [reviewer-calibration](skills/reviewer-calibration/SKILL.md) | Calibrate a review rubric against labeled examples and report limits of agreement. |
| [committee-response](skills/committee-response/SKILL.md) | Prepare responses to a thesis committee or research oversight group with traceable revisions. |
| [research-process-audit](skills/research-process-audit/SKILL.md) | Audit a research workflow's decisions, gates and evidence lineage. |
| [literature-monitoring](skills/literature-monitoring/SKILL.md) | Design or run an authorized literature watch and produce a deduplicated digest. |
| [ethics-and-preregistration](skills/ethics-and-preregistration/SKILL.md) | Prepare research ethics and preregistration materials tied to a concrete study. |
