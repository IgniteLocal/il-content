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
- The client's **Keyword Data sheet** (live SERP + People-Also-Ask + keyword volume/difficulty from DataForSEO, pulled from the CRM; `keyword-data.md`). See §3 — this is required, not optional.

## 3. Research method (real data required)

Real market data is a required input. Models reason on top of it; they do not invent it.

- **Keyword volume + difficulty:** from the Keyword Data sheet (Local Keywords, Keyword Ideas). Prefer local, commercial-intent phrases with realistic difficulty over high-volume head terms a local business can't win ("collision repair Bellevue," not "auto repair").
- **People-Also-Ask + related searches:** pull the real questions for each service. These become the question bank (§5) and are the single biggest driver of AI citations.
- **SERP + competitor analysis:** who ranks for each target, what they cover, where the gaps are, and which queries trigger an AI Overview and who gets cited.
- **Market facts** (pricing ranges, timelines, permits, codes): pull from live results and flag `⚑ VERIFY` against the client's real numbers.

When a step's data isn't available yet, say so and mark the affected figures directional — don't fabricate a volume or a price.

## 4. Choosing the primary keyphrase per page

- **One primary keyphrase per page**, matched to that page's intent. No two pages compete for the same phrase (cannibalization).
- **Home:** broadest core service + primary city. **Service pages:** specific service (+ city). **Location pages:** service + location. **About:** trust/entity phrase. **Blog landing:** informational phrase. **Contact:** action phrase.
- The **slug is the whole primary keyphrase, slugified**, geo included (see §6). Write keyphrases without filler ("roof repair Auburn WA", not "roof repair in Auburn WA") so the slug stays clean.

## 5. Building the question bank (the AEO engine)

For each page, list the real questions a customer asks about that service, sourced from People-Also-Ask and related searches. These do double duty:
- They become the page's **answer-first, question-style H2s**.
- The best 3–5 become an on-page **FAQ block** with FAQPage schema — the most reliable AI-citation surface on the site.

Phrase them the way people actually search ("How much does a fence cost in North Shelby County?" not "Pricing"). Favor cost, how-to-choose, how-it-works, timeline, permit/code, and comparison questions.

## 6. Meta title, description, and slug rules

**Meta title:** `[Power word] [service] in|serving|near [location] | [Brand]`, ≤ 60 characters, title-case. Annotate the count.
- Start with a power word that is **true for the client**: Trusted, Expert, Professional, Reliable, Dependable, Experienced, Licensed, Local, Skilled, Affordable, Fast, Free (estimate/contact pages), Emergency, Family-Owned. Never Best, #1, Top-Rated, Certified or Award-Winning without proof. Vary it across sibling pages.
- Join the service and the place with **in** (home city, cities they work in), **serving** (counties, regions, out-of-town cities) or **near**. Every keyphrase word must appear in the title; the exact string doesn't need to.
- Keyphrases with no place (blog, FAQ) still lead with a power word. If the keyphrase already has a connector ("roofing tips for Michigan homeowners"), keep it.
- Shorten the brand when space is tight (`| Double R` vs `| Double R Roofing`).
- Examples: `Trusted Roofing Company in Sterling Heights, MI | Double R` (58) · `Expert Roofer Serving Rochester Hills, MI | Double R Roofing` (60) · `Free Roofing Estimate in Sterling Heights | Contact Double R` (60).
- The H1 stays the natural keyphrase phrase without the power word ("Roofing Company in Sterling Heights, MI").

**Meta description:** ~150–160 characters, benefit + service area + light CTA, primary keyphrase natural. Annotate the count.

**URL slug:** the **full primary keyphrase, slugified**: lowercase, hyphen-separated, `&` → `and`, geo included. "residential roofing Sterling Heights" → `/residential-roofing-sterling-heights`; city hub "roofing company Troy MI" → `roofing-company-troy-mi`. No dates, underscores, spaces, special characters, or the `|` pipe. Home is `/`.
- **Exception, utility pages:** About, Contact, FAQ, Blog, Thank-You, Gallery keep conventional slugs (`/about`, `/contact`, `/faq`, `/blog`). Their keyphrases make long, unstable URLs.
- `content_qa.py` fails a slug that isn't the slugified keyphrase, and a meta title without the power word, the connector, or a keyphrase word. `il-website-build`'s `site_qa.mjs` enforces the same at build time.

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
