# Attribution and reuse boundaries

The instructions were composed for this project from the approved source audit, with changed names, task boundaries, host selection, authorization handling, explicit failure states and output contracts. They are not a verbatim merge of the source repositories. The Python helpers in this repository were authored for this project; no upstream script is vendored.

| Source | Pinned revision | Copyright / declared license |
|---|---|---|
| [superpowers](https://github.com/obra/superpowers) | `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` | Jesse Vincent, 2025; [MIT notice](licenses/S-LICENSE.txt) |
| [ARIS](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep) | `18bceb3c71c638bef58096274e1c9a6d323dbc0a` | wanshuiyin, 2026; [root MIT notice](licenses/R-LICENSE.txt) |
| [ponytail](https://github.com/DietrichGebert/ponytail) | `09c434ab73ca43761c5d8b0c5d341926c2fba710` | DietrichGebert, 2026; [MIT notice](licenses/P-LICENSE.txt) |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | `1ec249df98728682dfbbdfb940a658338bfd6f80` | Cheng-I Wu, 2026; [CC BY-NC 4.0 notice](licenses/A-LICENSE.txt) |
| [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) | `8534467b139471788c376339165acd8d2483caf9` | Audited as CC0 resource index; links do not relicense external works |

## Scope of adaptation

Per-skill pinned source links and mode notes are in `skills/*/references/source-contracts.md`; the full 113-entrypoint map and 28 ARS mode groups are in `docs/source-map.json`. ARS-derived notes and specialist guidance retain their noncommercial boundary. Core research tasks that also map to ARS are not claimed MIT-clean merely because another reference is MIT.

ARIS writing/figure acknowledgments include multiple upstream sources, including ARS. Component-level clearance remains unresolved; no promise of commercial redistribution rights is made. The root MIT notice is retained, not used to override another source's terms. ARIS proof-orchestrator and poster have separate notices in the upstream audit; neither implementation is vendored here. Full Anti-Autoresearch, Paperbanana, FigureSpec and provider implementations remain external.

For redistributed individual Skills, retain the per-skill `references/license-notices.txt` created in this distribution. It includes the source notices and this private-distribution boundary. Do not remove attribution when packaging a selected profile.
