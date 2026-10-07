# il-content

The Ignite Local content engine. Produces and optimizes website + blog content for local-service-business clients so it **ranks in search, gets cited by AI answer engines, reflects the client honestly, and converts.** It is the single source of truth that replaced a sprawl of copy-paste prompt docs.

Pairs with **il-website-build** (which owns the Astro + Cloudflare Pages build, technical SEO, and deploy). This skill owns copy + on-page SEO; see `references/handoff.md` for the content-as-code contract between them.

## Workflows

- **New Content Package** — intake → Voice Profile → live keyword/SERP research → gap analysis → Content Blueprint → page drafts → 15–20 blog topics.
- **Blog Production** — monthly blogs from an approved topic list.
- **Content Refresh** — performance-triggered rewrites.

## Layout

```
il-content/
├── SKILL.md                     # router + core principles + the four goals
├── references/
│   ├── writing-guidelines.md    # voice, banned phrases, reading level, AIDA
│   ├── voice-profile.md         # capture client voice once, reuse everywhere
│   ├── seo-geo-aeo.md           # SEO + GEO/AEO + E-E-A-T + schema (real data required)
│   ├── conversion.md            # above-the-fold, CTAs, risk reversal
│   ├── content-blueprint.md     # per-page keyphrase + intent + question bank + schema
│   ├── new-content-package.md   # workflow 1
│   ├── blog-production.md        # workflow 2
│   ├── content-refresh.md        # workflow 3
│   ├── content-gap-analysis.md  # gaps + blog topic list
│   ├── page-recipes.md          # per-page structure recipes
│   ├── qa-rubric.md             # the human review gate
│   ├── handoff.md               # content-as-code contract to il-website-build
│   ├── location-content.md      # per-city material for the location generator
│   ├── keyword-data.md          # the CRM's Keyword Data sheet: tabs, FKP selection
│   └── automation-gas.md        # running it inside Google Apps Script
├── assets/
│   └── schema-templates.json    # JSON-LD templates
└── scripts/
    └── content_qa.py            # copy QA gate (validates prose OR frontmatter)
```

## QA

```bash
python scripts/content_qa.py path/to/page.md      # a drafted page (prose block or frontmatter)
python scripts/content_qa.py --stdin < page.md
```

Checks meta lengths, slug format, banned phrases, em dashes, keyphrase placement, and reading level. It is the **copy** gate; `il-website-build`'s `site_qa.mjs` is the **build** gate. Run both.

## Install into Claude

Package the folder as a `.skill` (zip) and install it:

```bash
zip -r il-content.skill il-content -x "*__pycache__*" "*.DS_Store"
```

## Versioning

The `.skill` is a build artifact — commit the **folder**, not the zip. Keep frontmatter keys in `handoff.md` in sync with il-website-build's content-collection schema.
