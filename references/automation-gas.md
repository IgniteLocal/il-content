# GAS Automation

How to run this skill's methodology inside a Google Apps Script (GAS) stack — Ignite Local's primary automation environment — without recreating the drift the skill just eliminated.

## The one rule that matters

**Keep the methodology canonical in this skill. GAS calls it by reference; it never re-embeds it.** The failure mode to avoid: copying voice rules, banned phrases, or page recipes into GAS prompt strings. The moment that happens, you have two sources of truth that will drift apart, which is exactly the problem this skill was built to fix. GAS orchestrates; the models, guided by this skill, do the language.

So: store the skill's reference files (or a distilled prompt-module version of them) in one versioned home — a Drive folder, a repo, or the skill itself — and have GAS fetch the relevant module text at call time and pass it into the model. Update the method in one place; every GAS run picks it up.

## What GAS is good at (let it do these)

- **Read the intake + interview** from Drive (Docs/PDF) for the client.
- **Call DataForSEO** for keyword volume/difficulty, SERP results, and People-Also-Ask.
- **Route each step to the right model** (see below) with the correct reference module injected.
- **Run the QA script** (`content_qa.py` logic) on each draft — deterministic, no model needed.
- **Write outputs to Google Docs** in the client's folder, formatted for the editor.
- **Route to the editor** and track status through the pipeline (first draft → editor → dev → SEO QA → R1/R2).

## What the models do (language only)

- **GPT or Claude — research synthesis:** expand seeds, classify intent, cluster keywords, map keyphrases to pages, generate the question bank from PAA. (Either model is fine here; both reason well on top of real data.)
- **Claude via this skill — drafting + voice:** the Voice Profile, Content Blueprint narrative, page/blog drafting, refreshes. This is where the skill's guidelines matter most.
- **No model — QA:** meta lengths, slug format, banned-phrase and em-dash scan, keyphrase placement, reading level. Deterministic in `content_qa.py`. Never spend a model call on what a script does more reliably.

## A reference pipeline (New Content Package)

1. GAS reads the intake from Drive → builds the **Voice Profile** (Claude + `voice-profile.md` module) → writes it to the client folder.
2. GAS calls DataForSEO for volumes, SERP, and PAA per service → passes results to the model for **gap analysis + taxonomy** (`content-gap-analysis.md` module).
3. Model builds the **Content Blueprint** on the real data (`content-blueprint.md` module) → GAS writes the table to Docs for WPC/client review.
4. On approval, GAS loops the taxonomy, drafting each page (Claude + `writing-guidelines.md` + `seo-geo-aeo.md` + `conversion.md` + `page-recipes.md`, with the Voice Profile and Blueprint row injected).
5. GAS runs the QA script on each draft, appends the checklist, and routes to the editor.

## Guardrails

- **Do not auto-publish client-facing content end to end.** Automate to a strong, research-grounded first draft; keep the human editor and SEO QA gates. For work with a client's name on it, the review step is cheap insurance against the one hallucinated stat that torches trust.
- **Pass real data, never invented data,** into drafting calls. If DataForSEO is unavailable for a step, mark those figures directional in the output rather than letting the model guess.
- **Version the modules.** When you change a rule (a new banned phrase, a slug convention), change it in the canonical module and let GAS pick it up — never patch it in a prompt string.
