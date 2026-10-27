# Host integration

One skills/ tree is authoritative. Claude Code discovers it through the plugin's default layout; Codex/OpenCode receive identical self-contained folders through tools/install.py. Skill instructions do not assume a fixed tool name, model, account or API key.

| Capability | Claude Code | Codex | OpenCode |
|---|---|---|---|
| Discovery | Plugin/marketplace manifest | Project/user .agents/skills installer | .opencode/skills or user config installer |
| File/shell execution | Available host tools | Available host tools | Available host tools |
| Independent agents | Only if host and active instructions authorize | Only if host and active instructions authorize | Capability probe required |
| Search/reviewer/image services | Use configured connectors/tools | Use configured connectors/tools | Use configured connectors/tools |
| Periodic jobs | Actual configured scheduler required | Actual configured scheduler required | Actual configured scheduler required |
| UI band/statusline/telemetry | Not implemented | Not implemented | Not implemented |

No hooks are installed. No mandatory global invocation ritual is added. Inline execution remains usable when delegation is unavailable, with the limitation disclosed. Ponytail lite/full/ultra/off are task-level choices described in lean-implementation; persistence, hooks and UI parity are not claimed.

Claude commands use the `minh-agent:` namespace; Codex installed Skills retain their kebab-case names. The local installer never overwrites a different existing skill. Selecting only a profile does not automatically install other task Skills: each workflow remains instruction-usable, but a missing specialized tool or companion must be disclosed at handoff.

Optional providers from the source audit include arXiv, OpenAlex, Exa, Firecrawl, Gemini, AlphaXiv, DeepXiv, Keenable, reviewer APIs, SSH/screen, cloud GPU providers and Overleaf. This package does not contain their credentials or SDK clients. On use, probe the actual connector and verify current vendor documentation. A generic web search is a fallback, not equivalence for citation graphs, filtered metadata or full-page extraction.

The host-specific runtime state is recorded in VALIDATION.md. Installation tests in a temporary directory establish file packaging, not successful discovery inside a running host.

Sources checked 2026-10-27: [Claude manifest](https://code.claude.com/docs/en/plugins-reference), [Claude marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [Codex discovery](https://learn.chatgpt.com/docs/build-skills), [OpenCode discovery](https://opencode.ai/docs/skills/).
