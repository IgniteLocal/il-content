# Location Content (feeds the location generator)

`il-website-build` generates per-city and per-city/service pages under `/locations/{city-st}/` and `/locations/{city-st}/{service}/` from `cities.json` plus the service files. Its **uniqueness floor** (`location-floor.mjs`) rejects pages that are thin find-and-replace clones (doorway pages Google and AI both penalize). This recipe is how `il-content` supplies enough genuine local material to clear that floor.

## The rule

A location page must be **substantially unique**, not "same paragraph with the city swapped." Each served city needs real, specific local content: neighborhoods, landmarks, local context, local proof, and city-specific angles. If you can't say anything true and specific about a city, it should be a served-area mention, not its own page (`primary: false` in `cities.json`).

## What to produce per primary city

For each `primary: true` city, supply:

1. **A unique blurb** (goes in `cities.json`) — 1–2 sentences of real local context. Name actual neighborhoods, ZIPs, or landmarks. Example: "We fence homes across Greystone's gated communities and the Highland Lakes area, where HOA-approved aluminum and ornamental styles are the norm." Not: "We proudly serve [City] with quality fencing."

2. **A local intro block** (2–4 sentences) the generator can place near the top of that city's pages — specific to how the service plays out there (housing stock, HOA norms, terrain, common requests).

3. **City-specific angles** to weave into generated pages: local neighborhoods served, any city/HOA rules that matter (heights, materials), the kinds of properties there, and local proof if available (a real project, a neighborhood name from reviews).

4. **A localized FAQ or two** where the answer genuinely differs by city (permit office, HOA norms). Skip if it doesn't differ.

## What NOT to do

- Don't write the same intro for every city with the name swapped — the floor will reject it, and it should.
- Don't invent local landmarks, project counts, or neighborhood names. Pull from intake, reviews, or `⚑ VERIFY`.
- Don't produce the generated pages yourself — you supply the raw local material; `il-website-build` assembles and floor-checks them.

## Output format

Deliver as an addition to the locations handoff:

```json
// cities.json — one entry per served city (primary cities get full pages)
[
  { "city": "Inverness", "state": "AL", "lat": 33.4187, "lng": -86.6836, "primary": true,
    "blurb": "Real, specific 1-2 sentence local context." }
]
```

```yaml
# locations/{city-st}.md  (optional, per primary city — extra unique local copy for the generator)
---
city: "Inverness"
state: "AL"
localIntro: "2-4 sentences specific to fencing in Inverness — housing, HOA norms, terrain."
neighborhoods: ["Inverness", "Highland Lakes", "Riverchase"]
localAngles: ["HOA-approved aluminum common here", "sloped lots need stepped panels"]
needsVerification: ["confirm neighborhoods served", "local project example"]
---
```

## Quick check before handoff

- Would a local reader recognize this as written about *their* city, not a template? If not, add specificity or demote the city to `primary: false`.
- Is every local fact real or flagged `needsVerification`?
- Does each primary city have enough unique material to clear the floor (roughly a unique blurb + intro + 2–3 real local angles)?
