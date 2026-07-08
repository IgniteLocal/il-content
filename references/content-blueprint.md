# Content Blueprint

The Content Blueprint is the keyword-and-structure backbone of a content package. It replaces the old flat "FKP" (a bare keyphrase + metadata list) with a richer per-page map that also carries **search intent, a real question bank, and the schema plan** — everything a drafter needs to write the page, and everything the WPC needs to walk the client through the strategy. One artifact, two audiences.

## Table of contents
1. What the Blueprint is and where it fits
2. Inputs you need first
3. Research method (real data required)
4. Choosing the primary keyphrase per page
5. Building the question bank (the AEO engine)
6. Meta title, description, and slug rules
7. The output schema (with worked example)

---

## 1. What the Blueprint is and where it fits

For every page in the taxonomy, the Blueprint records:
- **Primary keyphrase** (one per page, no cannibalization)
- **Search intent** (transactional / informational / trust / navigational)
- **Secondary keyphrases** (variants, related services, "near me," localized forms)
- **Question bank** — the real questions people ask, which become the page's answer-first H2s and FAQ block
- **Recommended schema** type(s)
- **Internal links** up to the pillar and across the cluster

It's produced after intake + gap analysis and before drafting. It is **client-facing** (the WPC reviews the keyword→page map and topic strategy with the client) and **drafter-facing** (every page draft pulls its row).

## 2. Inputs you need first

- The client's **intake + discovery interview** (services, area, differentiators, credentials).
- The client's **URL** (if any) and **top 3 local competitors**.
- The **confirmed taxonomy** from the gap analysis.
- **Live SERP + People-Also-Ask data** and **keyword volume/difficulty** (DataForSEO / SE Ranking). See §3 — this is required, not optional.

## 3. Research method (real data required)

Real market data is a required input. Models reason on top of it; they do not invent it.

- **Keyword volume + difficulty:** pull from DataForSEO / SE Ranking. Prefer local, commercial-intent phrases with realistic difficulty over high-volume head terms a local business can't win ("collision repair Bellevue," not "auto repair").
- **People-Also-Ask + related searches:** pull the real questions for each service. These become the question bank (§5) and are the single biggest driver of AI citations.
- **SERP + competitor analysis:** who ranks for each target, what they cover, where the gaps are, and which queries trigger an AI Overview and who gets cited.
- **Market facts** (pricing ranges, timelines, permits, codes): pull from live results and flag `⚑ VERIFY` against the client's real numbers.

When a step's data isn't available yet, say so and mark the affected figures directional — don't fabricate a volume or a price.

## 4. Choosing the primary keyphrase per page

- **One primary keyphrase per page**, matched to that page's intent. No two pages compete for the same phrase (cannibalization).
- **Home:** broadest core service + primary city. **Service pages:** specific service (+ city). **Location pages:** service + location. **About:** trust/entity phrase. **Blog landing:** informational phrase. **Contact:** action phrase.
- Geo can live in the primary keyphrase, but keep the **slug** built on the keyphrase *head* (the service); trailing city/region is optional in the slug to keep it clean (see §6).

## 5. Building the question bank (the AEO engine)

For each page, list the real questions a customer asks about that service, sourced from People-Also-Ask and related searches. These do double duty:
- They become the page's **answer-first, question-style H2s**.
- The best 3–5 become an on-page **FAQ block** with FAQPage schema — the most reliable AI-citation surface on the site.

Phrase them the way people actually search ("How much does a fence cost in North Shelby County?" not "Pricing"). Favor cost, how-to-choose, how-it-works, timeline, permit/code, and comparison questions.

## 6. Meta title, description, and slug rules

**Meta title:** ≤ 60 characters, primary keyphrase near the front, then a differentiator or locale. Compelling, title-case. Annotate the count.

**Meta description:** ~150–160 characters, benefit + service area + light CTA, primary keyphrase natural. Annotate the count.

**URL slug:** lowercase, hyphen-separated, built on the keyphrase **head** (the service). Trailing geo optional. No dates, underscores, spaces, special characters, or the `|` pipe. Home is `/`. Keep it short and human-readable.

## 7. The output schema (with worked example)

Deliver the Blueprint as a table (fast for the WPC to review) plus a short geo note. Meta title/description are drafted per page at build time.

**Columns:** Page | Primary keyphrase | Intent | Question bank | Schema | Internal links

**Worked example (abridged — Masters Fence Co):**

| Page | Primary keyphrase | Intent | Question bank | Schema |
|---|---|---|---|---|
| Home | fence company North Shelby County | Transactional | Areas served? Fences built? Why us? | LocalBusiness (FenceContractor) + Breadcrumb |
| Residential Fence Installation *(pillar)* | residential fence installation North Shelby County | Transactional | Cost here? Best material? Remove old fence? How long? Permit? | Service + FAQPage + Breadcrumb |
| Pool Fencing | pool fence installation North Shelby County | Transactional + high AEO | AL/Shelby pool code? Height? Gate rules? Best material? Permit? | Service + FAQPage + Breadcrumb |
| FAQ | fence installation FAQ | Informational, high AEO | (client FAQs + permit + pool code + cost) | FAQPage + Breadcrumb |

Add a one-line **geo note**: primary cities woven into every page (e.g., 35242 Inverness/Greystone, Hoover, Chelsea) and secondary cities used as supporting mentions.

The Blueprint contains keyphrases + intent + questions + schema. The **blog topic list** and **gap analysis** are separate deliverables produced alongside it (see `content-gap-analysis.md`).
