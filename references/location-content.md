# Location Content Package (feeds the il-website-build generator)

This **supersedes the single "location" recipe in `page-recipes.md` for the code stack.** Use `page-recipes.md` only for a one-off WP-style location page; use this file whenever the site is built on il-website-build (Astro), which generates city and city-service pages at scale from a structured package.

## Why this exists

il-website-build's `gen-location-pages.mjs` cross-joins services × cities into `/locations/{city-st}/` hubs and `/locations/{city-st}/{service}/` money pages. It enforces a **uniqueness floor** and *skips* any city that doesn't clear it — because thin, near-identical "[service] in [city]" pages get filtered or penalized at scale. This is the same rule the team set in the Content Workshop: *don't make near-identical city pages unless each has unique, valuable content.* Your job here is to produce that unique content in the exact shape the generator consumes.

## IL geo doctrine (apply throughout)

- **City names for money pages** (title, meta, H1, URL, on-page, schema) — specific, higher intent, higher conversion.
- **Region/county for hubs + footer** — the `/locations/` hub and boilerplate say "serving North Shelby County and nearby communities"; individual pages target the city.
- **3–5 geo terms per page, natural.** No cramming a city list into one paragraph. Use variations: "in Inverness," "Inverness-area," "around the 35242 corridor."
- **Earn the page.** A dedicated city page is justified only when you can write genuinely local, valuable content for it (real neighborhoods, local conditions, local proof). If you can't, don't build it yet — let the generator skip it.

## The hard contract (match exactly)

The generator's floor is: **local_blurb ≥ 40 words, landmarks ≥ 2, local_faq ≥ 1.** Aim above the floor (blurb 55–90 words, 2–3 landmarks, 2–3 local FAQs). Output one JSON file per city, at `src/content/locations/{city-st}.json`:

```json
{
  "city": "Inverness",
  "state": "AL",
  "slug": "inverness-al",
  "lat": 33.4187,
  "lng": -86.6836,
  "local_blurb": "55–90 words of genuinely local copy — NOT a name-swap of another city.",
  "landmarks": ["Real local reference", "Another real local reference"],
  "local_faq": [
    { "q": "A question a homeowner in THIS city actually asks", "a": "A localized answer." }
  ]
}
```

- `slug` = `{city-lowercased-hyphenated}-{state-abbrev}` (e.g. `inverness-al`) — matches the URL architecture.
- `lat`/`lng` = the city centroid (for schema `geo` / map).

### What makes `local_blurb` clear the floor (and rank)
Genuinely local means at least two of: named neighborhoods/subdivisions, a local geographic or soil/weather condition that affects the work, the local permit/HOA reality, or real local proof. A blurb that would read identically for any other city with the name swapped is a **fail** — rewrite it.

### `landmarks`
Real, verifiable places or districts locals recognize (a country club, a park, a corridor/road, a shopping district). Used for on-page local relevance and natural entity signals for AEO. Never invent one — if you can't name two real ones, the city isn't ready.

### `local_faq`
Localize the question, not just the answer: permit/HOA specifics for *this* city, local material/soil considerations, "do you serve [neighborhood]." Pull candidates from live PAA (see `seo-geo-aeo.md`) filtered to the metro. These also emit FAQPage schema on the city and money pages.

## City-service localization (the `{{city}}` / `{{state}}` tokens)

Each service's `.md` (in `src/content/services/`) may contain `{{city}}` / `{{state}}` tokens. The generator substitutes them and appends the city's `local_blurb` + `local_faq` to each money page. Localize **lightly and where it matters** — roughly the intro line + one local-relevance sentence — and keep the technical/how-to body evergreen. This is deliberate: rewriting the whole service body per city produces thin, duplicative pages and busts the doorway rule. The city-specific value comes from the appended `local_blurb`/`local_faq`, not from paraphrasing the service copy 20 times.

Example service intro with tokens:
`"Masters Fence Co builds custom wood privacy fences across {{city}} and the surrounding {{state}} communities, and we remove your old fence for free."`

## Hub copy (write once per site)

- **`/locations/` (service-area hub):** region-framed intro ("serving North Shelby County and Greater Birmingham"), the natural city list, and a line inviting a call to confirm coverage. Region terms live here, not on money pages.
- **`/services/` (service index):** short framing of the full service set; links to each service. Not geo-heavy.

## Voice, QA, and VERIFY

- Reuse the client's **Voice Profile** (`voice-profile.md`) so city copy matches the rest of the site.
- Build a per-city line in the **Content Blueprint** (`content-blueprint.md`): city, primary keyphrase ("[service] [city]"), the local angle, and the FAQ/question bank.
- Run **`content_qa.py`** logic on the blurb: readability, no keyword stuffing (≤5 geo terms), no fabricated claims.
- **VERIFY discipline:** flag every client-specific claim with `⚑ VERIFY` — whether Masters has done jobs in that city, HOA-submission handling, who pulls the permit, review counts. Local *geographic* facts (neighborhoods, that a city runs its own permit process) are public and fine; *client* claims are not until confirmed.

## Definition of done (per city)

A city is ready when its JSON clears the floor with genuinely local content, its landmarks are real, its FAQ is localized, and client claims are VERIFY-flagged. Run `npm run gen:locations` — if the city is listed under "generated" (not "skipped"), it's wired. If it's skipped, the report tells you which field fell short; enrich and re-run. Quality over page count.

---

## Worked example — Masters Fence Co, Inverness AL

```json
{
  "city": "Inverness", "state": "AL", "slug": "inverness-al",
  "lat": 33.4187, "lng": -86.6836,
  "local_blurb": "Inverness sits in the heart of the 35242 corridor, where established streets off Valleydale Road and around Inverness Country Club mix mature tree lines with newer builds. Homeowners here usually want wood privacy fencing that holds up in Shelby County's clay soil out back, and HOA-approved aluminum along the front. We build both, set posts deep so gates stay square through wet Alabama winters, and handle the local permit steps.",
  "landmarks": ["Inverness Country Club", "Lake Heather", "Valleydale Road corridor"],
  "local_faq": [
    { "q": "Do you handle HOA approval for fences in Inverness?", "a": "Yes. Many Inverness and Highland Lakes neighborhoods require HOA sign-off, and aluminum or ornamental styles are usually the approved look. We build to your association's spec so it passes the first time. \u2691 VERIFY: confirm Masters handles HOA submissions vs. homeowner." },
    { "q": "What fence holds up best in the 35242 area's clay soil?", "a": "Posts set deep in concrete below the clay-movement line are the key here. That's how we keep panels from leaning and gates from dropping after Alabama's wet winters." }
  ]
}
```
This clears the floor (blurb ~70 words, 3 landmarks, 2 localized FAQs) and reads specifically like Inverness — not a name-swap.
