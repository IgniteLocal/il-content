# QA Rubric — The Gate Before Handoff

Nothing leaves your hands until it passes this. Run `scripts/content_qa.py` for the mechanical checks (lengths, slug format, banned phrases, em dashes, keyphrase placement, reading-level estimate), then apply judgment for the rest. This exists because the pipeline had recurring quality issues (generic copy, AI tells) that a consistent gate prevents.

## How to run the script

```bash
python scripts/content_qa.py path/to/deliverable.md
# or pipe/paste content:
python scripts/content_qa.py --stdin < deliverable.md
```

It flags mechanical problems. It does not judge quality — you do that with the rubric below.

## The rubric

Score each item pass / fix. Any "fix" gets fixed before handoff.

### 1. Reflects the client (voice + truth)
- [ ] Reads like a knowledgeable human in the trade, not an AI, not an agency brochure.
- [ ] 8th–9th grade reading level (or justified higher for a regulated vertical).
- [ ] Varied sentence rhythm; no monotone AI cadence.
- [ ] **Zero banned phrases. Zero em dashes.**
- [ ] Every client-specific claim (years, license #, reviews, guarantees, stats, awards) is either verified or flagged `⚑ VERIFY:` — **nothing invented.**
- [ ] Real E-E-A-T signals used where available.

### 2. Converts
- [ ] Transactional pages answer what/who/where/why/next-step in the top third.
- [ ] One clear primary CTA, matched to how the client takes business, repeated at decision points.
- [ ] Objection handling / risk reversal present where relevant (guarantees, free estimate, licensed/insured).
- [ ] Proof placed near a CTA.
- [ ] Blog CTA is light-touch and links to the pillar page (didn't turn the blog into a sales pitch).

### 3. Ranks + gets cited (SEO + GEO/AEO)
- [ ] Correct search intent for the page type.
- [ ] Primary keyphrase in H1, first ~100 words, meta title, URL slug, and body, naturally — no stuffing.
- [ ] No keyphrase cannibalization across pages/posts.
- [ ] Secondary keyphrases woven in.
- [ ] **Answer-first** sections; **question-style H2s** matching real queries.
- [ ] Extractable formats used where they fit (steps, tables, definitions, ranges).
- [ ] Entities named explicitly and consistently (business, services, locations).
- [ ] Recommended schema type noted; FAQ block + FAQPage schema where valuable.
- [ ] Internal links with descriptive anchors; cluster links up to pillar.

### 4. Metadata + mechanics
- [ ] Meta title ≤ 60 chars, count annotated, `[Power word] [service] in|serving|near [location] | Brand`, power word true for the client.
- [ ] Meta description ~150–160 chars, benefit + area + CTA, count annotated.
- [ ] URL slug = the full primary keyphrase slugified (utility pages keep `/about`, `/contact`, `/faq`, `/blog`); no dates/underscores/pipes.
- [ ] Complete metadata block present.
- [ ] Formatted text, not HTML/design comp (unless asked).

### 5. Handoff-ready
- [ ] All `⚑ VERIFY:` notes consolidated for the editor/account manager.
- [ ] Refreshes include the "WHAT CHANGED" block; keyphrase/slug changes flagged for redirects.
- [ ] Reads as a coherent deliverable the editor can humanize and the developer can build.

## The out-loud test

Before you call it done, read the opening and one body section out loud in your head as if speaking to the customer. If any sentence sounds like SEO, a brochure, or a robot, fix it. That instinct catches what the checklist can't.
