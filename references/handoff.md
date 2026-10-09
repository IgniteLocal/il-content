# Handoff to il-website-build

`il-content` produces the words and the on-page SEO. `il-website-build` turns them into a live Astro + Cloudflare Pages site. This file is the contract between them. Get it right and a package drops into a build with zero rekeying; get it wrong and someone hand-copies copy into files at 11pm.

## Ownership boundary (who owns what)

| il-content owns | il-website-build owns |
|---|---|
| Copy, headings, reading level, voice | The build, routing, deployment |
| On-page keyphrase placement | Technical SEO (canonicals, sitemap, redirects) |
| Meta title + description **text** | Design tokens + **colors (from the client logo)** |
| URL slug **recommendation** | Final URLs + the dual-hub route structure |
| Schema **type** recommendation | Schema **implementation** (JSON-LD) |
| Internal-link **suggestions** | `client.json` tokens, GTM, CallRail, form handler |
| FAQ/question copy | The uniqueness-floor enforcement + `site_qa.mjs` gate |
| The `needsVerification` list | Performance, images, launch QA |

**il-content never** specifies colors, fonts, or design tokens (those come from the logo in `client.json`), never writes HTML, never hard-codes final URLs (recommend slugs; the build owns routing), and never invents client facts (trust signals are evidence-gated from intake — flag, don't fabricate).

## Two delivery formats, one source

- **Human-review Doc** (for the WPC/editor): the readable metadata block + prose we've been producing. Good for review and client approval.
- **Content-as-code** (for the build): the same content emitted as markdown files with YAML frontmatter, in the folder shape `il-website-build` ingests. This is what actually ships.

Produce the Doc for approval; emit content-as-code once copy is approved. The `content_qa.py` script validates **either** format (it reads the frontmatter too).

## The file shape il-website-build ingests

Approved copy lands in the client site's `src/content/`:

```
src/content/
├── pages/
│   ├── home.md
│   ├── about.md
│   └── contact.md
├── services/
│   └── {service-slug}.md         # one file per service (e.g. wood-privacy-fences.md)
├── locations/
│   └── cities.json               # the city list that feeds the location generator
└── reviews/ (optional)
```

Per-city/service pages under `/locations/{city-st}/{service}/` are **generated** by `il-website-build` from `cities.json` + the service files, subject to the uniqueness floor. `il-content` supplies the raw material for that (see `location-content.md`), not the generated pages themselves.

## Frontmatter contract (pages/*.md and services/*.md)

```yaml
---
title: "Trusted Wood Privacy Fences Serving North Shelby County"  # meta title, <=60 chars, power word + in|serving|near
description: "Custom wood privacy fence installation ..."  # meta description, ~150-160
slug: "/wood-privacy-fence-north-shelby-county"            # = primaryKeyphrase slugified
primaryKeyphrase: "wood privacy fence North Shelby County"
secondaryKeyphrases: ["cedar privacy fence Inverness", "6 foot privacy fence Hoover"]
service: "wood-privacy-fence-north-shelby-county"   # service pages only; matches the file slug
schema: "Service + FAQPage"          # recommended JSON-LD type(s); build implements
internalLinks: ["/residential-fence-installation", "/pool-fencing", "/contact"]
needsVerification:                   # machine-readable ⚑ VERIFY (see below)
  - "price ranges vs Masters' real pricing"
  - "wood species offered"
  - "warranty terms"
---

# Wood Privacy Fence Installation in North Shelby County

[body markdown: answer-first H2s, conversion structure, CTA — exactly as drafted]
```

Field notes:
- **title / description** map straight to what `site_qa.mjs` checks for presence and length. Keep title ≤60, description ~150–160.
- **slug** = the primary keyphrase slugified (utility pages keep `/about`, `/contact`, `/faq`, `/blog`). Home is `/`. The build serves it as `/services/{slug}/` (service) or `/locations/{slug}/` (city hub), and its `fkp` field = `primaryKeyphrase`; `site_qa.mjs` fails a mismatch.
- **schema** is the recommended type only. The build writes the JSON-LD from `assets/schema-templates.json` and `client.json` data.
- **internalLinks** are suggestions the build wires up.
- Keep frontmatter **keys in sync with il-website-build's content-collection schema** — that schema is the source of truth. If a key name differs there, match it here.

## cities.json contract (locations/)

The city list that drives the location generator. One object per served city:

```json
[
  { "city": "Inverness",  "state": "AL", "lat": 33.4187, "lng": -86.6836, "blurb": "…", "primary": true },
  { "city": "Greystone",  "state": "AL", "lat": 33.4290, "lng": -86.6620, "blurb": "…", "primary": true },
  { "city": "Hoover",     "state": "AL", "lat": 33.4054, "lng": -86.8114, "blurb": "…", "primary": true },
  { "city": "Chelsea",    "state": "AL", "lat": 33.3390, "lng": -86.6360, "blurb": "…", "primary": false }
]
```

- `primary: true` = a city included in blog geo-targeting and given a full page; `false` = supporting/served-area mention.
- `blurb` is a **unique** 1–2 sentence local description (real neighborhoods, landmarks, or context) — not a template. See `location-content.md` for the uniqueness floor.
- `lat`/`lng` feed LocalBusiness/`areaServed` schema; `⚑ VERIFY` or geocode from the real address.

## The `needsVerification` bridge (this is the important part)

Every `⚑ VERIFY:` note becomes a structured `needsVerification` array item in frontmatter. This is deliberate: `il-website-build`'s `site_qa.mjs` build gate **fails the build on unresolved TODO business facts**, so unverified claims cannot silently ship. The flow:

1. `il-content` flags an unconfirmed fact (a price, a guarantee, a review count) as `needsVerification`.
2. The WPC/editor confirms it with the client and either fills the real value or removes the claim.
3. Only when the list is cleared does `site_qa.mjs` pass and the site build.

So `il-content` must be honest and complete with this list. A missing flag = an invented fact that slips past the gate. A thorough list = the gate does its job.

## Two gates, different jobs

- **`content_qa.py`** (this skill): the **copy** gate — voice, banned phrases, em dashes, keyphrase placement, meta lengths, reading level. Runs before handoff.
- **`site_qa.mjs`** (il-website-build): the **build** gate — meta/schema presence, redirects, and unresolved `needsVerification`. Runs before deploy.

They don't overlap; run both. Copy passes `content_qa.py` here; the assembled site passes `site_qa.mjs` there.
