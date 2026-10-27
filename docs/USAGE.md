# Usage examples

Invoke the task directly in natural language or by Skill name. Claude plugin commands use `/minh-agent:<name>`; Codex uses `$<name>` for installed Skills. Read only the reference for the requested mode.

| Your task | Suggested entrypoint | Concrete result |
|---|---|---|
| Find feasible research directions | idea-discovery | Literature map, ranked candidates, novelty risks, proposal/pilot handoff |
| Generate candidates without a full pipeline | idea-generation | Ranked idea cards and rejected alternatives |
| Write a technical proposal | research-proposal | Method, testable contributions, risks, resources and evaluation plan |
| Apply for funding | grant-proposal | Draft tied to the actual call, aims, milestones and compliance gaps |
| Draft paper text | manuscript-writing | Outline/sections/abstract tied to supplied evidence |
| Prepare the whole paper package | paper-pipeline | Sources, figures, references, build and audit coverage |
| Plot results | paper-figures | Real-data plot, generation source, provenance and caption |
| Draw architecture | technical-diagrams | Editable diagram source and SVG, PDF if a converter is available |
| Illustrate a concept | scientific-illustration | Generated illustration with provenance and visual review |
| Debug an implementation | root-cause-debugging | Reproducer, cause, patch and regression evidence |
| Review a revision | research-review | Comparison between responses and actual manuscript changes |

## Research handoffs

Discovery can stop at an idea or continue to a proposal when requested. An experiment-design handoff contains claims, controls, metrics, splits and budgets. experiment-implementation turns that into code and smoke evidence; experiment-runner/queue require authorized execution resources. paper-pipeline consumes actual results, not imagined future results.

## Example prompts

```text
Use idea-discovery to identify three viable directions from my paper notes. I have one GPU and four weeks. Stop at a research proposal and pilot plan.

Use grant-proposal with this call and my actual CV. Mark missing facts instead of inventing team experience or preliminary results.

Use paper-figures on results.csv. Plot the measured values with units and preserve a reproducible command. Flag any missing uncertainty information.

Use research-evidence-audit to compare this manuscript table with the per-seed CSV. Report mismatches and denominator differences.
```

## Local executable examples

Synthetic fixtures are in examples/. They are for testing the tools, not scientific evidence. Use a fresh output path:

```sh
python skills/paper-figures/scripts/plot_svg.py examples/results.csv output/accuracy.svg --x seed --y accuracy --kind scatter --title "Synthetic fixture"
python skills/technical-diagrams/scripts/render_svg.py examples/diagram.json output/diagram.svg
python skills/technical-debt-ledger/scripts/scan_debt.py PATH_TO_REPOSITORY
```

For a queue, read the experiment-queue local-helper reference first. Its manifest contains executable commands; dry-run validates it but does not establish that commands are safe. For missing services, the Skill should state the limitation and produce useful local planning/output without pretending a remote job or delivery occurred.
