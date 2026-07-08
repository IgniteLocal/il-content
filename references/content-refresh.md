# Workflow 3 — Content Refresh / Rewrite

Use this when existing page(s) are flagged for underperformance (low performance-score reads on the regular monitoring cadence) and need to be digested and rewritten to current best practices. A refresh follows the same research and production discipline as new content — it is not a light edit. The goal is to bring an older page up to today's SEO + GEO/AEO + conversion standard without losing what already works.

## Inputs

- The client's **Voice Profile** on file (reuse it — see `references/voice-profile.md`), so the refreshed page matches the rest of the site.
- The **URL(s)** to refresh and, if available, **why** they were flagged (ranking drop, low conversions, thin content, outdated info, losing to a competitor, not appearing in AI answers).
- The page's **current primary keyphrase / Blueprint row**, if one exists.
- The **top 3 competitors** currently outranking the page for the target keyphrase.

## The refresh sequence

1. **Digest the current page.** Read what's there. Identify what it targets, its intent, its structure, and what's working (keep it) vs. what's weak (fix it). Note existing internal links, real proof/E-E-A-T signals, and any client-specific facts you must preserve.
2. **Diagnose against competitors.** Compare the page to the top 3 ranking pages for the keyphrase. Where are the content gaps, the intent mismatches, the missing subtopics, the weaker structure? What are they doing that gets them ranked/cited that this page isn't?
3. **Reconfirm or upgrade the keyphrase.** Is the primary keyphrase still the right intent + difficulty? If a better-matched or more winnable phrase exists, propose it (and note the change so redirects/links can be handled). Refresh secondary keyphrases and metadata.
4. **Rebuild the outline to match intent.** Structure the rewrite around what the searcher actually wants, with question-style H2s and answer-first sections. Add the subtopics competitors cover that this page misses.
5. **Rewrite to current standard.** Apply `writing-guidelines.md`, `seo-geo-aeo.md`, and `conversion.md` in full. Preserve real, verified facts from the original (credentials, guarantees, service area, review data). Upgrade weak, generic, or dated copy. Strip AI tells and em dashes if the old copy has them.
6. **Add what was missing.** Answer-first blocks, an FAQ section with FAQPage schema where it fits, recommended schema, internal links up to/related pages, updated freshness signals.
7. **Self-QA and hand off.**

## What to preserve vs. change

**Preserve:** verified client facts, real proof and E-E-A-T signals, working internal links, a keyphrase that's still right, anything genuinely well-written. Don't rewrite for the sake of rewriting.

**Change:** generic/AI-sounding copy, buried answers (make them answer-first), vague labels (make H2s question-style), missing schema, thin sections competitors beat, dated info, weak or missing CTAs, intent mismatches, banned phrases, em dashes.

## Output template

```
=== REFRESH: [Page Name] ===
URL: /[slug]   [note if slug should change → include redirect flag]
Primary Keyphrase: [phrase]   [note if changed from previous]
Secondary Keyphrases: [...]
Meta Title: [...] (NN chars)
Meta Description: [...] (NNN chars)
Recommended Schema: [type(s)]
Suggested Internal Links: [...]

WHAT CHANGED (for the SEO/editor):
- [e.g., Reworked H2s to question format for AEO]
- [e.g., Added FAQ block + FAQPage schema]
- [e.g., Rewrote thin "process" section competitors were beating us on]
- [e.g., Primary keyphrase upgraded from X to Y — needs redirect if slug changes]

# [H1]
[Rewritten body, answer-first, conversion-structured...]

⚑ VERIFY: [any unconfirmed claim; anything from the old page you couldn't confirm]
```

The **"WHAT CHANGED" block is required** on refreshes — it lets the human SEO review the diff quickly and decide on redirects, and it documents the reasoning for R1/R2.

## QA before handoff

Same gate as the other workflows (`qa-rubric.md` / `scripts/content_qa.py`), plus: confirm no verified fact from the original was lost, and confirm any keyphrase/slug change is flagged for redirect handling.
