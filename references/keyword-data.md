# Keyword Data (real numbers for keyword + SERP research)

Every volume, difficulty score, People-Also-Ask question and competitor you cite comes from the client's
**Keyword Data sheet**. Never estimate a number that isn't in it.

## Where it comes from

The CRM pulls it from DataForSEO: Master Database → select the client's CRM row → **More ▸ Client Automation ▸ Pull
Keyword Data**. It writes a Google Sheet named **`Keyword Data – <Client Name>`** in the client's Drive folder and
refreshes it in place on every re-run (the run date is on the Summary tab).

**Getting it into this conversation:** search Google Drive for `Keyword Data – <client>` if a Drive connector is
available; otherwise ask the user to share the link or attach an export. If the sheet doesn't exist, ask the user to
run **Pull Keyword Data** first. Do not proceed with invented figures; if the user insists, mark every number
`directional` and say why.

## Tabs and how to use them

| Tab | Columns | Use it for |
|---|---|---|
| Summary | location used, services, cities, cost, notes | Check the location (city, state or national) and any notes before trusting the numbers |
| Local Keywords | service, keyword, monthly volume at the client's location, difficulty 0–100, CPC, competition | **Focus keyphrase (FKP) selection** for service and location pages |
| Keyword Ideas | service seed, keyword, US monthly volume, difficulty, intent, CPC (competitor, manufacturer, product-line and retailer brand terms already removed) | Secondary keyphrases, blog topics, gaps in the taxonomy. Never target another company's brand name |
| SERP Top 10 | search, position, title, domain, URL | Who ranks today; which page types win (directories vs local businesses) |
| People Also Ask | search, question | The question bank: answer-first H2s and FAQ blocks |
| AI Overview | search, shown yes/no, cited title/domain/URL | Which searches trigger an AI Overview and what gets cited — the GEO/AEO target |
| Local Pack | search, business, rating, reviews, domain | The map-pack competitors for the content gap analysis |
| City Plan | suggested tier, **Final tier**, city, state, miles, population, listed by client, searches/mo per service, why | Which cities get location pages and money pages — see `location-content.md`. Written by **Plan City Pages** (separate CRM menu item); use **Final tier**, not the suggestion |

## Choosing focus keyphrases from it

- **Local intent beats national volume.** "roof repair hoover al" with 20 searches beats "roof repair" with 40,000 a
  local business can't win. Volumes in Local Keywords are for the client's location; Keyword Ideas are national.
- **Low or blank local volume is normal** for small cities (Google Ads reports small numbers as 0 or blank). Pick by
  intent and difficulty, and note it in the Blueprint rather than inflating it.
- **Difficulty:** under ~30 is realistic for a new local site, 30–50 needs strong content and links, over 50 is a
  long-term target, not a launch FKP.
- **One FKP per page, no cannibalizing:** two pages never share a primary keyphrase.
- Record each choice in the Content Blueprint with its volume, difficulty and the tab it came from, so the editor and
  SEO can audit it.

## Market facts

Pricing ranges, timelines, permits and codes are not in this sheet. Pull them from live results and flag
`⚑ VERIFY` against the client's real numbers, as before.
