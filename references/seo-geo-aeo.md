# SEO + GEO/AEO — Ranking and Getting Cited

Classic SEO gets you ranked in Google's blue links. **GEO/AIO/AEO** (Generative Engine Optimization / AI Optimization / Answer Engine Optimization) gets you *quoted* by Google AI Overviews, ChatGPT, Perplexity, Gemini, and Copilot. Both matter, and the same content can win both if you structure it right. This file is the layer the old prompts were missing.

## Table of contents
1. The mental model
2. Search intent by page type
3. Classic SEO checklist
4. GEO/AEO: how to get cited by AI
5. Entities and topical authority
6. E-E-A-T for local service businesses
7. Structured data (schema) — what to use where
8. Local SEO specifics

---

## 1. The mental model

Google ranks pages. AI answer engines **extract and synthesize answers**, then sometimes cite the source. To win the second, your content has to contain **clean, self-contained, factual, quotable units** an AI can lift with confidence: a direct answer to a real question, a definition, a step list, a price range, a comparison, a stat with a source.

The good news: content built this way (answer-first, well-structured, genuinely helpful, provably trustworthy) is also exactly what Google's helpful-content systems reward. You are not writing two versions. You are writing one disciplined version.

## Real data is a required input

Do not invent search data. Ground the work in real sources, and let the model reason on top:
- **Keyword volume + difficulty:** the client's Keyword Data sheet (DataForSEO via the CRM; `keyword-data.md`). Prefer local, commercial-intent phrases with realistic difficulty.
- **People-Also-Ask + related searches:** pull the real questions per service. These become the answer-first H2s and the FAQ block, and they are the single biggest driver of AI citations.
- **SERP + competitor analysis:** who ranks, what they cover, which queries trigger an AI Overview and who gets cited.
- **Market facts** (pricing, timelines, permits, codes): from live results, flagged `⚑ VERIFY` against the client's real numbers.

If a source isn't wired in yet for a given step, say so and mark those figures directional rather than fabricating them.

## 2. Search intent by page type

Match the page's job to the searcher's intent. Getting this wrong is the most common ranking failure.

| Page type | Dominant intent | What that means for the copy |
|---|---|---|
| Home | Transactional / navigational | Who you are, what you do, where, why you, act now. Broadest primary keyphrase. |
| Service page | Transactional | Solve-my-problem + hire-someone. Lead to the CTA. |
| Location page | Transactional (local) | Same service, localized proof and geography. |
| About | Trust / navigational | Story, credentials, team, proof. Convert on trust. |
| FAQ | Informational (high AEO value) | Direct answers to real questions. Prime schema + AI-citation target. |
| Blog | Informational | Teach first. Earn the click to a service page. Never a disguised sales page. |
| Contact | Transactional | Remove friction. Every way to reach them + service area. |

## 3. Classic SEO checklist

For every page:
- **One primary keyphrase**, chosen for intent + realistic difficulty (see `content-blueprint.md`). Present in H1, first ~100 words, meta title, URL slug, and body.
- **Secondary/variant keyphrases** woven naturally; they capture long-tail and signal topical depth.
- **Unique, compelling meta title** ≤ 60 characters, primary keyphrase near the front, plus a differentiator or locale.
- **Meta description** ~150–160 characters, written to earn the click (benefit + locale + CTA). Not a ranking factor directly, but drives CTR, which matters.
- **Clean URL slug**: lowercase, hyphenated, keyphrase-based, no stop-word clutter, no dates. (Full rules in `content-blueprint.md`.)
- **Descriptive H2/H3** using real query language.
- **Internal links** to related service pages and relevant blogs, with descriptive anchor text (not "click here").
- **Image alt text** describing the image with natural keyphrase use.
- **Scannable structure** and adequate depth for the topic (don't pad to a word count; cover the topic completely, then stop).

## 4. GEO/AEO: how to get cited by AI

Add these on top of classic SEO. These are the practices that get you into AI Overviews and chatbot answers.

- **Answer-first blocks.** Open each section with a 1–3 sentence, self-contained answer to the question the H2 implies. Self-contained means it makes sense quoted alone, without the surrounding paragraph. This is the single highest-leverage AEO tactic.
- **Question-shaped H2s** that match real queries ("What does a roof inspection cost in Huntsville?" not "Roof Inspections"). Mirror the way people ask.
- **Extractable formats.** Definitions, numbered steps, comparison tables, pros/cons, price ranges, "X vs Y." AI engines lift these readily.
- **Concrete, checkable facts.** Numbers, ranges, timeframes, specifics. "Most installs take 4–6 hours" is quotable; "installs are quick" is not.
- **Stand-alone sentences.** Favor sentences that carry their full meaning without the previous sentence for context. Pronoun-heavy, "as mentioned above" prose is hard to extract.
- **A crisp definition early.** If the topic has a definable core ("What is soft washing?"), define it in one clean sentence near the top. Definitions get cited constantly.
- **Freshness signals** where relevant (update dates, current-year references) — AI engines favor current information.
- **FAQ sections** with real questions and direct answers, backed by FAQPage schema (section 7). This is the most reliable AI-citation surface on a local business site.

Quick test: could an AI quote one sentence from this section, out of context, and be correct and helpful? If not, tighten it.

## 5. Entities and topical authority

AI models reason about **entities** (the business, its services, its locations, its people) and the relationships between them. Help them:

- **Name things explicitly and consistently.** Use the real business name, exact service names, and specific city/neighborhood names. Avoid vague "we" and "the area" where a name would clarify.
- **Build topical authority through clusters.** A pillar page (the service) supported by blogs that answer common customer questions about that service tells both Google and AI that this business is a genuine authority, not a thin brochure. See `content-gap-analysis.md` for cluster planning.
- **Connect the cluster with internal links** so the relationships are explicit.

## 6. E-E-A-T for local service businesses

Experience, Expertise, Authoritativeness, Trust. For local service businesses, weave in the signals they actually have:
- **Experience:** years in business, jobs completed, "family-owned since 1998," real project examples.
- **Expertise:** licenses, certifications, manufacturer training, specializations, credentials of named team members.
- **Authoritativeness:** memberships (BBB, trade associations), awards, press, manufacturer authorizations.
- **Trust:** license/insurance numbers, warranties and guarantees, transparent process, review counts and ratings, service-area clarity, real contact info.

These do triple duty: they help ranking, they get cited by AI ("a licensed, BBB-accredited shop"), and they convert. Always request or `⚑ VERIFY:` — never invent.

## 7. Structured data (schema) — what to use where

Recommend the right JSON-LD for the developer to implement. Ready templates are in `assets/schema-templates.json`.

| Page type | Schema to recommend |
|---|---|
| Home + Contact | `LocalBusiness` (or the specific subtype, e.g. `Plumber`, `AutoRepair`, `MedicalBusiness`) with NAP, hours, geo, `sameAs` socials, `areaServed` |
| Service page | `Service` (with `provider` → the LocalBusiness, `areaServed`, `serviceType`) |
| FAQ section | `FAQPage` (each Q/A as `Question` → `acceptedAnswer`) — highest AEO value |
| Blog / article | `Article` or `BlogPosting` (headline, author, datePublished, dateModified) |
| How-to content | `HowTo` (steps) |
| All pages | `BreadcrumbList` for navigation context |
| Reviews | `AggregateRating` / `Review` — **only with real, verifiable data** |

In your deliverable, note the recommended schema type at the top of the metadata block so the developer implements it. Do not hand-author invalid schema; point them to the template.

## 8. Local SEO specifics

- **NAP consistency:** Name, Address, Phone identical to the Google Business Profile everywhere it appears.
- **Service-area geography:** name the primary city plus the real surrounding towns/neighborhoods the client serves. This is how you rank in nearby towns without keyword-stuffing "near me."
- **Location pages** for genuinely distinct service areas — but only with unique, localized content, never doorway-page duplicates.
- **"Near me" intent** is captured by strong local relevance (city names, local landmarks, service-area language, GBP alignment), not by literally repeating "near me."
- **Local proof:** neighborhood references, local project examples, local review mentions.
