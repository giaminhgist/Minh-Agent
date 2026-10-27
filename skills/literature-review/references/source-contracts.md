# Source contracts and mode boundaries

These are traceability notes from the approved 2026-10-26 audit, not executable upstream code. Load only the relevant source when exact behavior is required. Runtime parity is not established by this mapping.

## R: arxiv

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/arxiv/SKILL.md)

Capability: Search, metadata, tải PDF, quản lý bản đã tải

Preservation condition / known gap: Adapter arxiv riêng; download/version/rate limits là capability phải kiểm thử.

## R: comm-lit-review

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/comm-lit-review/SKILL.md)

Capability: Survey chuyên communication/networking; knowledge-base-first

Preservation condition / known gap: Domain profile riêng, venue/source routing và local library.

## R: exa-search

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/exa-search/SKILL.md)

Capability: Web search, find-similar, content extraction

Preservation condition / known gap: Adapter Exa giữ filters/content modes; search web dùng được ngoài literature.

## R: firecrawl-search

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/firecrawl-search/SKILL.md)

Capability: Search và scrape URL thành Markdown

Preservation condition / known gap: Adapter Firecrawl giữ domain/time/full-page modes.

## R: gemini-search

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/gemini-search/SKILL.md)

Capability: Discovery literature qua Gemini MCP/CLI

Preservation condition / known gap: Adapter Gemini; kiểm lại nguồn, không dùng lời model làm citation.

## R: keenable-search

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/keenable-search/SKILL.md)

Capability: Keyless web search/fetch, date/site filters

Preservation condition / known gap: Adapter Keenable; không bỏ khả năng provider-specific khi gộp.

## R: novelty-check

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/novelty-check/SKILL.md)

Capability: Closest prior work, novelty delta, khoảng trống evidence

Preservation condition / known gap: Giữ mode novelty có thể gọi độc lập; không bảo đảm absolute novelty.

## R: openalex

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/openalex/SKILL.md)

Capability: Metadata/citation graph, affiliations/funding, filters

Preservation condition / known gap: Adapter OpenAlex riêng; generic web search không thay thế các fields.

## R: research-lit

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/research-lit/SKILL.md)

Capability: Survey/related work/synthesis với multi-source search

Preservation condition / known gap: Giữ source selection, local libraries, metadata vs fulltext scope.

## R: semantic-scholar

Source: [pinned manifest](https://github.com/wanshuiyin/auto-claude-code-research-in-sleep/blob/18bceb3c71c638bef58096274e1c9a6d323dbc0a/skills/semantic-scholar/SKILL.md)

Capability: Search published work, citations, venue metadata, filters

Preservation condition / known gap: S2 adapter; metadata coverage khác arXiv.

## A: deep-research

Source: [pinned manifest](https://github.com/Imbad0202/academic-research-skills/blob/1ec249df98728682dfbbdfb940a658338bfd6f80/deep-research/SKILL.md)

Capability: 8 mode: full/quick/review/lit-review/three-way-scan/fact-check/socratic/systematic-review

Preservation condition / known gap: Không gộp cả 8 vào survey; xem bảng mode A chi tiết.
## Additional ARS modes

- deep-research / full / quick / lit-review / three-way-scan: Báo cáo dài/ngắn, annotated bibliography và WHY/HOW/WHAT comparison phải có mode riêng.
- academic-paper / lit-review: Giữ literature section/full survey boundary.

## Reuse and provenance

Instructions in this bundle are newly composed adaptations of the audited workflows; they are not verbatim upstream manifests. Modified naming, routing, authorization, failure reporting and host selection are intentional. Source scripts, exact wire schemas and provider clients are not implicitly included.

ARS-derived guidance retains the CC BY-NC 4.0 boundary (Cheng-I Wu, 2026); rewriting does not remove it. ARIS root MIT is not a component-level clearance; writing/figure acknowledgments and external dependencies need separate provenance review. See the plugin root LICENSE and THIRD_PARTY_NOTICES.md before redistribution. Per-skill installation also includes the applicable notices in this directory.
