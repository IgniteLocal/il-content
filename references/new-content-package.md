# Workflow 1 — New Content Package

Use this for a new site build or a full redesign, where you're producing content for the whole taxonomy from scratch. This is the heaviest workflow. It ends with a package the editor can humanize, the developer can build, and the SEO can QA before R1/R2.

## The end-to-end sequence

1. **Ingest the intake + interview** (from Google Drive)
2. **Build the Voice Profile** (capture once, reuse on every page)
3. **Keyword + SERP research** (live data required: the client's Keyword Data sheet from the CRM, see `keyword-data.md`)
4. **Content gap analysis** → confirm the taxonomy
5. **Content Blueprint** for every page (keyphrase + intent + question bank + schema)
6. **Draft content for every page** in the taxonomy
7. **Blog topic list** (15–20 ideas) for client review
8. **Self-QA** the whole package, then hand off

Do them in order. Each step feeds the next, and skipping real research is how packages end up generic.

Artifact audiences (label each in the package): the **Voice Profile summary, gap analysis, taxonomy, Blueprint, and blog topic list are client-facing** (the WPC presents them for approval); the **page drafts, schema plan, internal links, and QA notes are internal** (editor/dev/SEO).

---

## Step 1 — Ingest the intake and interview

Find and read the client's **intake form and discovery interview** in Google Drive (search the client name; they're usually in the client's folder). Extract and note:
- Services offered (and how the client describes them)
- Service area (primary city + surrounding towns)
- Target customers and their pain points
- Differentiators, guarantees, warranties
- Credentials: licenses, certifications, years in business, memberships, awards
- Real proof: review counts/ratings, notable projects, team bios
- Brand voice cues and anything the client explicitly wants said or avoided
- Existing URL, if a redesign

If the intake or interview is missing or thin, ask for it before proceeding. Everything downstream is only as grounded as this step. Capture unanswered but needed facts as a running `⚑ VERIFY:` list.

## Step 2 — Build the Voice Profile

Before writing anything, capture the client's voice once so every page and blog sounds like one business. Pull from the intake, their best existing copy, and their Google/Yelp reviews (their customers' actual words). Full method and worked example in `references/voice-profile.md`. Store it at the top of the package; the WPC can confirm it with the client, and every draft references it.

## Step 3 — Keyword + SERP research (live data required)

Real data is a required input, not a nice-to-have. Models reason on top of it; they do not invent it.

- Read the client's **Keyword Data sheet** (`keyword-data.md`; run **Pull Keyword Data** in the CRM if it doesn't exist): **keyword volume + difficulty** from Local Keywords and Keyword Ideas.
- Take **People-Also-Ask** questions from its People Also Ask tab for each service — these become the question bank in the Blueprint and are the biggest driver of AI citations.
- Analyze the **SERP + top 3 competitors** (SERP Top 10, Local Pack and AI Overview tabs): who ranks, what they cover, where the gaps are, which queries trigger AI Overviews and who gets cited.
- Pull **market facts** (pricing ranges, timelines, permits, codes) from live results and flag `⚑ VERIFY` against the client's real numbers.
- Establish the **local geography set** (primary city + real surrounding towns).

If a data source isn't wired in yet for a step, say so and mark those figures directional. Never fabricate a volume or a price. Full method in `content-blueprint.md` §3 and `seo-geo-aeo.md`.

## Step 4 — Content gap analysis → confirm taxonomy

Compare what the client offers and what competitors rank for against what the site currently has (or, for a new build, against a strong template for the vertical). Identify:
- **Missing service pages** the client should have at launch (services they offer but wouldn't have a page for).
- **Missing supporting pages** (location pages, key FAQ page, financing, warranties).
- **Over/under-consolidation** (services that should be split into their own pages, or thin ones to combine).

Output a short gap analysis and a **recommended taxonomy**, then confirm it before building the Content Blueprint. Details and format in `content-gap-analysis.md`.

## Step 5 — Content Blueprint

Build the full Content Blueprint for the confirmed taxonomy: one primary keyphrase, search intent, secondary keyphrases, a real question bank (from People-Also-Ask), and the schema plan per page. This is the map every page draft follows, and the WPC's client-review artifact. Meta title/description are drafted per page at build time. Full method and output format in `content-blueprint.md`.

## Step 6 — Draft content for every page

Work through the taxonomy page by page. For each page:
- Load the **Voice Profile** and pull the page's **Blueprint row** (primary keyphrase, intent, secondaries, question bank, schema).
- Choose the right **page recipe** (home, about, service, location, FAQ, contact) from `page-recipes.md`.
- Apply the always-on quality bar (`writing-guidelines.md`), answer-first + GEO structure (`seo-geo-aeo.md`), and conversion structure (`conversion.md`).
- Turn the question bank into **answer-first, question-style H2s**, and put the best 3–5 into an on-page FAQ block with FAQPage schema.
- Lead the page with its **metadata block**, then the formatted body with labeled headings.
- Recommend the **schema type** and **internal links**.
- Add any `⚑ VERIFY:` notes.

Deliver as clean formatted text (not HTML, not a design comp). Keep pages in taxonomy order so the package reads as a coherent site.

**Per-page output template:**
```
=== [PAGE NAME] ===
URL: /[slug]
Primary Keyphrase: [phrase]
Meta Title: [...] (NN chars)
Meta Description: [...] (NNN chars)
Secondary Keyphrases: [...]
Recommended Schema: [type]
Suggested Internal Links: [page → page]

# [H1 with primary keyphrase]
[Above-the-fold: what / who / where / why / CTA]

## [Question-style H2]
[Answer-first section...]

## [Question-style H2]
[...]

## [Closing section + primary CTA]

⚑ VERIFY: [anything unconfirmed — stat, credential, guarantee]
```

## Step 7 — Blog topic list (15–20 ideas)

Produce a client-facing list of **15–20 blog topic ideas** for ongoing content, organized as content clusters supporting the service (pillar) pages. This is what the client reviews and approves to feed monthly blog production. Format and cluster logic in `content-gap-analysis.md`.

## Step 8 — Self-QA and hand off

Run the whole package through `scripts/content_qa.py` (or the manual rubric in `qa-rubric.md`):
- Every page has a complete metadata block within length limits.
- Primary keyphrase placed correctly, no cannibalization across pages.
- No banned phrases, no em dashes.
- Answer-first sections and question H2s present.
- Real E-E-A-T signals used; all unverified claims flagged, not invented.
- Every transactional page has a clear CTA; intent matches page type.
- Consolidate all `⚑ VERIFY:` notes into one list at the top for the editor/account manager.

Then hand off with a one-line summary of what's included and what still needs client-verified facts.

**For Astro-stack clients:** once copy is approved, emit it as **content-as-code** (markdown + YAML frontmatter) in the `src/content/` shape `il-website-build` ingests, with every `⚑ VERIFY:` converted to a structured `needsVerification` frontmatter item. Supply `locations/cities.json` with unique per-city blurbs. Full contract in `references/handoff.md` and `references/location-content.md`. Run `content_qa.py` on the emitted files too — it reads the frontmatter.

## Handoff note to include

Start the package with a short header the editor and developer can act on:
```
CONTENT PACKAGE: [Client] — [# pages] pages + Blueprint + gap analysis + [# ] blog topics
STATUS: First draft for editor humanization → dev build → SEO QA → R1/R2
NEEDS VERIFICATION: [consolidated ⚑ VERIFY list]
```
