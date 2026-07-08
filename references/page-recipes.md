# Page Recipes

Structure recipes per page type. Each is a starting skeleton, not a rigid mold — adapt to the client's real services and proof. All recipes assume the always-on quality bar (`writing-guidelines.md`), answer-first GEO structure (`seo-geo-aeo.md`), and conversion structure (`conversion.md`) are already applied.

Every page leads with its metadata block (URL, primary keyphrase, meta title + count, meta description + count, secondary keyphrases, recommended schema, internal links) before the body.

**Routing note (Astro stack):** `il-website-build` uses a dual-hub route structure — `/services/{service}/`, `/locations/`, `/locations/{city-st}/`, and generated `/locations/{city-st}/{service}/`. Recommend slugs that fit it (a service page slug like `/wood-privacy-fences` maps to the services hub), but the build owns final routing. When emitting for the build, each recipe below becomes a `pages/*.md` or `services/*.md` file with YAML frontmatter — see `references/handoff.md`.

---

## Home
Intent: transactional/navigational. Broadest core keyphrase + primary city.
- **H1** — core service + city, names what they do for whom.
- **Above the fold** — what / who / where / why (one differentiator) / primary CTA. (Top third; see conversion §1.)
- **Services overview** — brief blurb per core service, each linking to its service page.
- **Why choose us** — real differentiators + E-E-A-T (years, licenses, guarantees, reviews).
- **Proof** — ratings/review count, badges, notable work (verified only).
- **Service area** — named city + surrounding towns.
- **Closing CTA.**
- Schema: `LocalBusiness` (specific subtype) + `BreadcrumbList`.

## Service page
Intent: transactional. Specific service + city.
- **H1** — the specific service + city.
- **Above the fold** — the problem this solves, for whom, where, why this business, CTA.
- **What's included / how it works** — the service concretely; steps or scope (extractable).
- **Answer-first sections** on the real questions (cost factors, timeline, what to expect, options), question-style H2s.
- **Why this business for this service** — proof, guarantees, credentials specific to it.
- **Related services** — internal links.
- **Optional FAQ block** (FAQPage schema) — high AEO value.
- **Closing CTA.**
- Schema: `Service` (+ `FAQPage` if FAQ block) + `BreadcrumbList`.

## Location page
Intent: transactional, localized. Service + specific location.
- Same spine as a service/home page, **localized**: this location's geography, neighborhoods, local proof, local projects.
- **Must be genuinely unique** — never a find-and-replace clone of another location page (that's a doorway page and gets penalized).
- Schema: `LocalBusiness` or `Service` with `areaServed` set to the location + `BreadcrumbList`.

## About
Intent: trust/navigational. Trust/entity keyphrase.
- **H1** — about + entity phrase (e.g., "local pressure washing company").
- **Story** — origin, years, what they stand for (real, specific, human).
- **Team / credentials** — named people, licenses, certifications, training.
- **Proof** — reviews, memberships, community involvement, notable work.
- **Soft CTA** after trust is established.
- Schema: `AboutPage` / `LocalBusiness` + `BreadcrumbList`.

## FAQ page
Intent: informational, very high AEO value.
- **H1** — "[Service/Business] FAQ" or a question-cluster title.
- **Real customer questions** as H2/H3, each with an **answer-first, self-contained** answer (1–3 sentences, then optional detail). Pull the real long-tail questions people ask.
- First person, as the business answering.
- Light "still have questions? call us" close.
- Schema: `FAQPage` (required here) + `BreadcrumbList`.

## Contact
Intent: transactional. Action keyphrase (e.g., "book/appointment/quote + city").
- **H1** — action + business/city.
- **All contact methods** — clickable phone, form, email, address, hours, response expectation.
- **Service area** named.
- **Short form** (name, phone, service, zip). Recommend trimming long forms.
- Schema: `LocalBusiness` with full NAP + `BreadcrumbList`.

## Blog (landing/index)
Intent: informational. Blog-topic keyphrase (e.g., "[trade] tips [city]").
- Brief intro framing the value of the resource.
- Links to posts, organized by cluster/topic where possible.
- Schema: `Blog` + `BreadcrumbList`.

## Blog post
Covered in `blog-production.md` — question-style H1, answer-first body, extractable formats, optional FAQ block, one pillar-page CTA. Schema: `Article`/`BlogPosting` (+ `HowTo` / `FAQPage` where they fit).
