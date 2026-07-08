#!/usr/bin/env python3
"""
content_qa.py — mechanical QA for Ignite Local content deliverables.

Checks the things a script does better than eyeballing:
  - meta title / meta description lengths
  - URL slug format
  - banned AI-tell phrases and em dashes
  - primary keyphrase placement (H1, first ~100 words, meta title, slug)
  - a rough reading-level estimate (Flesch-Kincaid grade)

It does NOT judge quality, voice, truthfulness, or conversion. Pair it with
references/qa-rubric.md for human judgment.

Usage:
  python content_qa.py path/to/deliverable.md
  python content_qa.py --stdin < deliverable.md

The parser expects the house metadata block (labeled lines like
"Primary Keyphrase:", "Meta Title:", "Meta Description:", "URL:") followed by
a Markdown body (# H1, ## H2). It degrades gracefully if fields are missing.

No third-party dependencies. Python 3.8+.
"""

import argparse
import re
import sys

# ---- Config -----------------------------------------------------------------

META_TITLE_MAX = 60          # pixel-safe target
META_DESC_MIN = 140
META_DESC_MAX = 160          # house docs run to ~168; flag above 160
FIRST_N_WORDS = 100          # window to check for the primary keyphrase

BANNED_PHRASES = [
    # AI-tell adjectives / intensifiers
    "top-notch", "top notch", "industry-leading", "industry leading",
    "cutting-edge", "cutting edge", "seamless", "unparalleled",
    "state-of-the-art", "state of the art", "next-level", "next level",
    "revolutionary", "world-class", "world class", "game-changing",
    "game changer", "second to none", "best-in-class", "best in class",
    "premier", "unrivaled", "elevate your", "unlock", "unleash", "robust",
    "bespoke", "curated", "meticulous", "nestled", "in the heart of",
    "boasts", "testament to",
    # SEO / marketing filler
    "look no further", "your go-to", "go-to solution", "tried and true",
    "must-have", "highly sought-after", "highly sought after",
    "crafted with care", "designed to perfection", "exceed expectations",
    "exceeding expectations", "tailored to your needs", "one-stop shop",
    "when it comes to", "rest assured", "we've got you covered",
    "take it to the next level", "at the end of the day",
    "in today's fast-paced world", "in today's world",
]

# Openers that scream "AI intro"
BANNED_OPENERS = ["in today's", "in the world of", "whether you're", "when it comes to"]

GREEN, RED, YELLOW, BOLD, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[1m", "\033[0m"


# ---- Parsing ----------------------------------------------------------------

# Frontmatter keys (content-as-code handoff) mapped to the human-readable labels
FRONTMATTER_ALIASES = {
    "Meta Title": ["title", "metaTitle", "meta_title"],
    "Meta Description": ["description", "metaDescription", "meta_description"],
    "Primary Keyphrase": ["primaryKeyphrase", "primary_keyphrase", "keyphrase"],
    "Primary Keyword Phrase": ["primaryKeyphrase", "primary_keyphrase", "keyphrase"],
    "URL": ["slug", "url", "permalink"],
    "Secondary Keyphrases": ["secondaryKeyphrases", "secondary_keyphrases", "secondary"],
}


def _frontmatter(text):
    """Parse a leading YAML-ish frontmatter block into a dict (light parser, known keys)."""
    m = re.match(r"^\s*---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^\s*([A-Za-z0-9_]+)\s*:\s*(.+?)\s*$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip("\"'")
    return fm


def grab(label, text):
    """Return the value after a labeled metadata line, or a frontmatter alias, or None."""
    m = re.search(rf"^\s*{re.escape(label)}\s*:\s*(.+?)\s*$", text, re.IGNORECASE | re.MULTILINE)
    if m:
        return m.group(1).strip()
    fm = _frontmatter(text)
    for alias in FRONTMATTER_ALIASES.get(label, []):
        if alias in fm:
            return fm[alias]
    return None


def strip_count_annotation(value):
    """Remove a trailing '(NN chars)' annotation if present."""
    if not value:
        return value
    return re.sub(r"\s*\(\s*\d+\s*chars?\s*\)\s*$", "", value, flags=re.IGNORECASE).strip()


def get_h1(text):
    m = re.search(r"^\s*#\s+(.+?)\s*$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def get_h2s(text):
    return re.findall(r"^\s*##\s+(.+?)\s*$", text, re.MULTILINE)


def get_body(text):
    """Everything from the H1 onward (the prose we reading-level check)."""
    m = re.search(r"^\s*#\s+.+$", text, re.MULTILINE)
    return text[m.start():] if m else text


def first_n_words(text, n):
    # strip markdown headings/markup for the window check
    clean = re.sub(r"[#>*_`\[\]]", " ", text)
    words = clean.split()
    return " ".join(words[:n]).lower()


KP_STOPWORDS = {"in", "the", "a", "an", "of", "for", "and", "to", "your", "on", "at", "with"}


def _norm(w):
    """Normalize a word for matching: strip a trailing plural 's'."""
    return w[:-1] if len(w) > 3 and w.endswith("s") else w


def _sig_tokens(kp):
    """Significant keyphrase tokens: drop stopwords and bare 2-letter state
    codes (e.g. 'AL'), which a city name already implies."""
    return [t for t in re.findall(r"[a-z0-9']+", kp.lower())
            if t not in KP_STOPWORDS and len(t) > 2]


def phrase_present(keyphrase, haystack):
    """
    True if the keyphrase concept appears in the haystack: either as an exact
    substring, or with all significant tokens present as words (stop words like
    'in' may be inserted, plurals and state codes tolerated). This mirrors real
    SEO practice — "wood privacy fence in Birmingham" contains "wood privacy
    fence Birmingham".
    """
    kp = keyphrase.lower().strip()
    hay = haystack.lower()
    if kp in hay:
        return True
    tokens = [_norm(t) for t in _sig_tokens(kp)]
    if not tokens:
        return False
    hay_words = {_norm(w) for w in re.findall(r"[a-z0-9']+", hay)}
    return all(t in hay_words for t in tokens)


# ---- Reading level ----------------------------------------------------------

def count_syllables(word):
    word = re.sub(r"[^a-z]", "", word.lower())
    if not word:
        return 0
    vowels = "aeiouy"
    count, prev_vowel = 0, False
    for ch in word:
        is_vowel = ch in vowels
        if is_vowel and not prev_vowel:
            count += 1
        prev_vowel = is_vowel
    if word.endswith("e") and count > 1:
        count -= 1
    return max(count, 1)


def flesch_kincaid_grade(text):
    prose = re.sub(r"[#>*_`\[\]|]", " ", text)
    sentences = [s for s in re.split(r"[.!?]+", prose) if s.strip()]
    words = re.findall(r"[A-Za-z']+", prose)
    if not sentences or not words:
        return None
    syllables = sum(count_syllables(w) for w in words)
    wps = len(words) / len(sentences)
    spw = syllables / len(words)
    return round(0.39 * wps + 11.8 * spw - 15.59, 1)


# ---- Checks -----------------------------------------------------------------

class Report:
    def __init__(self):
        self.rows = []
        self.fails = 0
        self.warns = 0

    def add(self, status, label, detail=""):
        self.rows.append((status, label, detail))
        if status == "FAIL":
            self.fails += 1
        elif status == "WARN":
            self.warns += 1

    def render(self):
        icon = {"PASS": f"{GREEN}✓ PASS{RESET}", "FAIL": f"{RED}✗ FAIL{RESET}", "WARN": f"{YELLOW}! WARN{RESET}", "INFO": "  INFO"}
        for status, label, detail in self.rows:
            line = f"  {icon[status]}  {label}"
            if detail:
                line += f"  {detail}"
            print(line)
        print()
        summary = f"{self.fails} fail(s), {self.warns} warning(s)"
        color = RED if self.fails else (YELLOW if self.warns else GREEN)
        print(f"{BOLD}{color}Result: {summary}{RESET}")
        if self.fails:
            print(f"{RED}Fix all FAILs before handoff.{RESET} See references/qa-rubric.md for the full human review.")
        elif self.warns:
            print(f"{YELLOW}Review WARNs, then run the human rubric.{RESET} See references/qa-rubric.md.")
        else:
            print("Mechanical checks clean. Now run the human rubric in references/qa-rubric.md.")


def run_checks(text):
    r = Report()
    lower = text.lower()

    # Primary keyphrase
    keyphrase = grab("Primary Keyphrase", text) or grab("Primary Keyword Phrase", text)
    if keyphrase:
        kp = keyphrase.lower()
        r.add("INFO", f"Primary keyphrase: \"{keyphrase}\"")
        h1 = get_h1(text)
        if h1:
            ok = phrase_present(keyphrase, h1)
            r.add("PASS" if ok else "FAIL", "Keyphrase in H1",
                  "" if ok else f"(H1: \"{h1}\")")
        else:
            r.add("WARN", "No H1 (#) found to check")
        window = first_n_words(get_body(text), FIRST_N_WORDS)
        r.add("PASS" if phrase_present(keyphrase, window) else "FAIL",
              f"Keyphrase in first {FIRST_N_WORDS} words")
        mt = strip_count_annotation(grab("Meta Title", text))
        if mt:
            r.add("PASS" if phrase_present(keyphrase, mt) else "WARN", "Keyphrase in meta title")
        slug = grab("URL", text)
        if slug and slug.strip() != "/":
            slug_words = {_norm(w) for w in re.findall(r"[a-z0-9']+", slug.lower())}
            sig_tokens = [_norm(t) for t in _sig_tokens(kp)]
            # A clean slug carries the service HEAD of the keyphrase (usually the
            # first 1-2 words); trailing geo (city/region) is optional in slugs.
            head = sig_tokens[:2]
            missing = [t for t in head if t not in slug_words]
            ok = bool(head) and not missing
            r.add("PASS" if ok else "WARN", "Keyphrase head in URL slug",
                  "" if ok else "(slug missing: " + ", ".join(missing) + ")")
    else:
        r.add("WARN", "No 'Primary Keyphrase:' line found — skipping placement checks")

    # Meta title length
    mt = strip_count_annotation(grab("Meta Title", text))
    if mt:
        n = len(mt)
        r.add("PASS" if n <= META_TITLE_MAX else "FAIL", "Meta title length",
              f"({n} chars, max {META_TITLE_MAX})")
    else:
        r.add("WARN", "No 'Meta Title:' line found")

    # Meta description length
    md = strip_count_annotation(grab("Meta Description", text))
    if md:
        n = len(md)
        if n < META_DESC_MIN:
            r.add("WARN", "Meta description length", f"({n} chars, aim {META_DESC_MIN}-{META_DESC_MAX})")
        elif n > META_DESC_MAX:
            r.add("FAIL", "Meta description length", f"({n} chars, over {META_DESC_MAX})")
        else:
            r.add("PASS", "Meta description length", f"({n} chars)")
    else:
        r.add("WARN", "No 'Meta Description:' line found")

    # URL slug format
    slug = grab("URL", text)
    if slug:
        problems = []
        if slug != "/" :
            if slug != slug.lower():
                problems.append("uppercase")
            if "_" in slug:
                problems.append("underscore")
            if "|" in slug:
                problems.append("pipe")
            if " " in slug:
                problems.append("space")
            if re.search(r"/\d{4}(/|-|$)", slug):
                problems.append("date")
            if re.search(r"[^a-z0-9\-/]", slug.lower()):
                problems.append("special char")
        r.add("PASS" if not problems else "FAIL", "URL slug format",
              "" if not problems else "(" + ", ".join(problems) + ")")

    # Banned phrases
    hits = sorted({p for p in BANNED_PHRASES if p in lower})
    r.add("PASS" if not hits else "FAIL", "Banned phrases",
          "" if not hits else "(" + ", ".join(hits) + ")")

    # Em dashes
    em = text.count("—")
    r.add("PASS" if em == 0 else "FAIL", "Em dashes", "" if em == 0 else f"({em} found — replace with commas/periods/parens)")

    # Banned openers (check the first body sentence)
    body = get_body(text)
    first_para = ""
    for line in body.splitlines():
        s = line.strip()
        if s and not s.startswith("#") and not re.match(r"^(URL|Primary|Meta|Secondary|Recommended|Suggested|Supports)\b", s, re.IGNORECASE):
            first_para = s.lower()
            break
    opener_hit = next((o for o in BANNED_OPENERS if first_para.startswith(o)), None)
    r.add("PASS" if not opener_hit else "WARN", "Opening line",
          "" if not opener_hit else f"(starts with \"{opener_hit}...\" — throat-clearing)")

    # Question-style H2s (AEO)
    h2s = get_h2s(text)
    if h2s:
        q = sum(1 for h in h2s if "?" in h)
        r.add("INFO", f"H2s: {len(h2s)} total, {q} question-style",
              "(question H2s aid AEO; not all must be questions)")

    # Reading level
    grade = flesch_kincaid_grade(get_body(text))
    if grade is not None:
        if grade <= 9.5:
            r.add("PASS", "Reading level (FK grade)", f"({grade})")
        elif grade <= 12:
            r.add("WARN", "Reading level (FK grade)", f"({grade}; target ~8-9, ok if regulated vertical)")
        else:
            r.add("FAIL", "Reading level (FK grade)", f"({grade}; simplify)")

    return r


# ---- Main -------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Mechanical QA for Ignite Local content.")
    ap.add_argument("path", nargs="?", help="Path to the deliverable (.md / .txt).")
    ap.add_argument("--stdin", action="store_true", help="Read content from stdin.")
    args = ap.parse_args()

    if args.stdin or not args.path:
        text = sys.stdin.read()
        source = "stdin"
    else:
        with open(args.path, encoding="utf-8") as f:
            text = f.read()
        source = args.path

    if not text.strip():
        print("No content to check.")
        sys.exit(2)

    print(f"\n{BOLD}Content QA — {source}{RESET}\n")
    report = run_checks(text)
    report.render()
    sys.exit(1 if report.fails else 0)


if __name__ == "__main__":
    main()
