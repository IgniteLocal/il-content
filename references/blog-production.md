# Workflow 2 — Blog Production

Use this for monthly blog output: 1–4 blogs drawn from the client's approved blog topic list, drafted for the editor to review/rewrite/post, then human SEO QA. Blogs are the engine of topical authority and AI citation — they answer the real questions customers ask, and they funnel readers to the service (pillar) pages.

## Inputs

- The client's **Voice Profile** (reuse the one built at package kickoff — see `references/voice-profile.md`). Do not re-derive voice per blog; consistency across months is the point.
- The client's **approved blog topic list** (from the new package or a later planning round). Each topic ideally carries: title, primary keyphrase, supporting keywords, rationale, the pillar/service page it supports, and internal-link targets. Format in `content-gap-analysis.md`.
- The client's **URL** and enough business context to write with authority (pull from intake/site if needed).
- Which **topics** to write this month, and how many (1–4).

If there's no approved topic list yet, generate one first (see `content-gap-analysis.md`) and flag that it needs client review before writing at volume. If the client wants a one-off blog without a list, proceed but still slot it into a cluster mentally so it supports a service page.

## Blog structure

A blog is **informational intent**. Teach genuinely; earn the click to a service page. Never write a disguised sales page — that loses the informational ranking and the reader's trust.

Target ~800–1,200 words unless the topic warrants more or less (cover the topic completely, then stop; don't pad to a number).

Apply `writing-guidelines.md`, `seo-geo-aeo.md`, and the light-touch blog CTA rule in `conversion.md` §7.

**Per-blog output template:**
```
=== BLOG: [Title] ===
URL: /[slug]
Primary Keyphrase: [phrase]
Secondary/Supporting Keyphrases: [...]
Meta Title: [...] (NN chars)
Meta Description: [...] (NNN chars)
Recommended Schema: Article (or HowTo if step-based) + FAQPage if an FAQ block is included
Supports (pillar): [service page it links up to]
Suggested Internal Links: [this blog → pillar page], [→ related blog/page]

# [H1 — often a question or clear promise, contains primary keyphrase]

[Intro: name the reader's question/problem in their words, promise the answer. Answer-first — give the core answer briefly up top, then deliver the detail below. No "in today's world" openers.]

## [Question-style H2]
[Answer-first section. Lead with the self-contained answer, then explain. Use lists/tables/steps where genuinely enumerable — these get cited by AI.]

## [Question-style H2]
[...]

## [Optional FAQ block: 3–5 real questions with direct answers — high AEO value, back with FAQPage schema]

## [Close: brief takeaway + one relevant, low-pressure CTA to the pillar service page]

⚑ VERIFY: [any unconfirmed claim/stat]
```

## GEO/AEO priorities for blogs

Blogs are your best AI-citation surface. Prioritize:
- **Question-shaped H2s** matching real queries.
- **Answer-first blocks** that stand alone when quoted.
- **Definitions, steps, comparisons, price ranges** — extractable formats.
- **An FAQ block** with FAQPage schema where the topic supports it.
- **Freshness** — current-year references and an update date where relevant.
- **Internal links up to the pillar page** so the cluster relationship is explicit.

## Conversion in blogs (light touch)

- One primary CTA at the end, linking to the relevant service page. Optionally one contextual link mid-article where it's genuinely helpful.
- Micro-proof is fine ("licensed since 2004"); a hard sell is not.
- The reader came to learn. Respect that, and the click to the service page is earned rather than forced.

## Batch handling (multiple blogs)

When drafting 2–4 in a month:
- **Vary angle and CTA wording** so the set doesn't read as templated.
- **Cross-link** related blogs to each other and to the shared pillar page.
- Keep each blog's primary keyphrase distinct (no cannibalization within the batch or against existing posts).
- Deliver each blog as its own complete block (metadata + body), in a single document, with a short batch header listing the titles and the pillar pages they support.

## QA before handoff

Run `scripts/content_qa.py` on each blog and confirm: metadata within limits, keyphrase placement clean, no banned phrases or em dashes, answer-first + question H2s present, internal link to pillar included, intent stayed informational, all unverified claims flagged. Then hand to the editor.
