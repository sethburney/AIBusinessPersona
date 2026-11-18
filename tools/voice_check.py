#!/usr/bin/env python3
"""Human Voice Check: score Remi's public copy for reading level and AI tells.

Usage: python3 tools/voice_check.py FILE [FILE ...]

Reads the week files format (pieces under '### W1-MON ...' headings) and checks
only public copy: spoken scripts, on-screen text, slide copy, and captions.
See STYLE-GUIDE.md for the rules. Exit code 1 if any piece has a FAIL.
"""
import re
import sys

TARGET_MAX = 8.0  # no harder than 8th grade; easier is fine for spoken social copy

BANNED = [  # (regex, label, fix)
    (r"\b(isn't|is not|wasn't|aren't|not)\b[^.!?\n]{0,60}[.!?,;]\s*(it's|it is|it was|that's)\b", "\"It's not X, it's Y\" pattern", "say the point directly"),
    (r"\bnot just\b[^.!?\n]{0,60}\bbut\b", "\"Not just X, but Y\" pattern", "say the point directly"),
    (r"\bgame[- ]chang\w*", "hype word", "say what changes"),
    (r"\b(unlock|unleash|supercharge|revolutioni[sz]e|turbocharge)\w*", "hype word", "say what actually happens"),
    (r"\b(cutting[- ]edge|seamless\w*|robust|elevate\w*|next[- ]level)\b", "hype word", "plain description"),
    (r"\b(delve|harness\w*|holistic|synergy|embark\w*|moreover|furthermore|realm)\b", "essay word", "everyday word"),
    (r"\bnavigat\w* the\b", "essay phrase", "everyday words"),
    (r"\blandscape\b", "essay word", "everyday words"),
    (r"here'?s the secret", "stock opener", "open with the frustration"),
    (r"\blet'?s dive in\b|\bdive (in|into)\b", "stock opener", "just start"),
    (r"fast[- ]paced world|in today'?s world", "stock opener", "open with the frustration"),
    (r"\bever wondered\b|\bimagine a world\b", "stock opener", "open with the frustration"),
    (r"at the end of the day|in conclusion|it'?s worth noting|worth noting", "stock closer", "end with the next step"),
    (r"\bno shame required\b", "canned reassurance or aside", "say the useful next step directly"),
    (r"—", "em dash", "comma, period, or two sentences"),
]

WARN = [
    (r"\ban ai persona\b", "formal disclosure", "\"I'm AI\"; keep the disclosure clear"),
    (r"\b(leverage|utili[sz]e|empower\w*|optimi[sz]e)\b", "business word", "use / help / improve"),
    (r"\b(potentially|arguably|somewhat|perhaps)\b", "hedge word", "one honest qualifier at most"),
]

BRITISH = [
    (r"\b(analyse|analysed|analysing|optimise|optimised|optimising|optimisation)\b", "British spelling"),
    (r"\b(colour|favour|honour|behaviour|neighbour|labour)\w*", "British spelling"),
    (r"\b(organis|realis|recognis|prioritis|summaris|categoris|apologis|customis|standardis)\w*", "British spelling (-ise)"),
    (r"\b(centre|metre|theatre|programme|catalogue|whilst|amongst|learnt|spelt|fortnight)\b", "British spelling/word"),

]

# Context matters: these also have ordinary American meanings.
IDIOM_WARN = r"\b(sorted|reckon|brilliant|cheers|mate|keen to|queue up|rubbish)\b"

UNCONTRACTED = r"\b(do not|does not|did not|cannot|can not|will not|would not|should not|is not|are not|was not|were not|it is|you are|we are|they are|I am|that is|there is|let us|I will|you will|we will|have not|has not)\b"


def syllables(word):
    w = re.sub(r"[^a-z]", "", word.lower())
    if not w:
        return 0
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]{1,2}", w)))


def normalize(text):
    return text.replace("\u2019", "'").replace("\u2018", "'")


def sentences(text):
    # A Markdown wrap is not a new sentence. Keep punctuation inside quotes.
    text = re.sub(r"\s+", " ", text).strip()
    return [p.strip() for p in re.split(r'(?<=[.!?])\s+|(?<=[.!?]["\u201d])\s+', text)
            if re.search(r"[A-Za-z]", p)]


def words_of(s):
    return re.findall(r"[A-Za-z][A-Za-z'\u2019-]*", s)


def fk_grade(text):
    sents = sentences(text)
    words = [w for s in sents for w in words_of(s)]
    if not sents or not words:
        return None
    syl = sum(syllables(w) for w in words)
    return 0.39 * (len(words) / len(sents)) + 11.8 * (syl / len(words)) - 15.59


def clean(s):
    s = re.sub(r"\*\(Image:.*?\)\*", "", s)
    s = re.sub(r"!?\[[^]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\*\*([^*]+?)\*\*", lambda m: m.group(1) +
               ("" if m.group(1).endswith((".", "!", "?")) else "."), s)
    return s.replace("**", "").replace("`", "").strip()


def parse(path):
    pieces, cur, mode, in_code = [], None, None, False
    with open(path, encoding="utf-8") as source:
        for lineno, raw in enumerate(source, 1):
            line = raw.rstrip("\n")
            m = re.match(r"^### (W\d+-[A-Z]+)\b(.*)", line)
            if m:
                cur = {"id": m.group(1), "title": m.group(2).strip(" ·:"),
                       "line": lineno, "entries": []}
                pieces.append(cur)
                mode, in_code = None, False
                continue
            if cur is None:
                continue
            if line.startswith("```"):
                in_code = not in_code
                if not in_code and mode == "caption":
                    mode = None
                continue
            if not in_code and line.startswith("**"):
                low = line.lower()
                mode = ("script" if "script (spoken)" in low else
                        "onscreen" if "on-screen text" in low else
                        "caption" if low.startswith("**caption") else None)
                continue
            # Blank lines end caption paragraphs, not ordinary Markdown wraps.
            if not line.strip() and mode == "caption" and cur["entries"]:
                sec, loc, previous = cur["entries"][-1]
                if sec == "caption" and not previous.endswith((".", "!", "?", ":")):
                    cur["entries"][-1] = (sec, loc, previous + ".")
            section, text = None, ""
            if mode == "script" and line.startswith(">"):
                section, text = "script", clean(line.lstrip("> "))
            elif mode == "caption" and in_code:
                if line.strip() and not line.strip().startswith("#"):
                    section, text = "caption", clean(line)
                    if re.match(r"^\d+[.️⃣]", text) and not text.endswith((".", "!", "?")):
                        text += "."
            elif not in_code and line.startswith("|"):
                cells = [c.strip() for c in line.strip("|").split("|")]
                if mode == "onscreen" and len(cells) >= 2:
                    if not re.match(r"^(Time|---)", cells[0]):
                        section, text = "onscreen", clean(cells[-1])
                elif len(cells) >= 3 and cells[0].isdigit():
                    section = "slide " + cells[0]
                    # Separate heading column is public too, except layout labels.
                    heading = cells[-2]
                    text = clean(cells[-1])
                    if heading.lower() not in {"cover", "closer", "prompt", ""} and not re.match(
                            r"^(stage|rule|step) \d+$", heading, re.I):
                        text = clean(heading) + ". " + text
            if section and text:
                cur["entries"].append((section, lineno, text))
    return pieces


def check_text(text, spoken=False):
    text = normalize(text)
    flags = []
    for pat, label, fix in BANNED:
        for m in re.finditer(pat, text, re.I):
            flags.append(("FAIL", label, m.group(0), fix))
    # Catch the actual paired sentence, including an opening subject.
    for m in re.finditer(r"\b(?:mistakes|errors) aren't the problem\.\s*"
                         r"(?:repeating them is|it's)\b", text, re.I):
        flags.append(("FAIL", "stock contrast", m.group(0), "say what to do next"))
    for pat, label in BRITISH:
        for m in re.finditer(pat, text, re.I):
            flags.append(("FAIL", label, m.group(0), "American spelling"))
    for m in re.finditer(IDIOM_WARN, text, re.I):
        flags.append(("WARN", "possible British idiom", m.group(0),
                      "keep ordinary American meanings; otherwise rephrase"))
    for pat, label, fix in WARN:
        for m in re.finditer(pat, text, re.I):
            flags.append(("WARN", label, m.group(0), fix))
    if spoken:
        for m in re.finditer(UNCONTRACTED, text, re.I):
            flags.append(("WARN", "possible stiff phrasing", m.group(0),
                          "try a contraction; keep deliberate emphasis"))
    for sentence in sentences(text):
        n = len(words_of(sentence))
        if n > 20:
            flags.append(("FAIL", f"sentence too long ({n} words)", sentence,
                          "split it without changing the meaning"))
    return flags


def main(paths):
    any_fail = False
    for path in paths:
        try:
            pieces = parse(path)
        except (OSError, UnicodeError) as exc:
            print(f"{path}: [FAIL] cannot read file: {exc}")
            any_fail = True
            continue
        print(f"\n=== {path} ({len(pieces)} pieces) ===")
        if not pieces:
            print("  [FAIL] no supported pieces found; no copy was checked")
            any_fail = True
            continue
        for p in pieces:
            groups = {}
            for section, line, text in p["entries"]:
                groups.setdefault(section, []).append((line, text))
            if not any(k == "script" or k.startswith("slide ") for k in groups):
                print(f"  {p['id']}:{p['line']} [FAIL] missing script or slides")
                any_fail = True
            if "caption" not in groups:
                print(f"  {p['id']}:{p['line']} [FAIL] missing caption")
                any_fail = True
            for section, entries in groups.items():
                if section == "onscreen":
                    entries = [(line, t if t.endswith((".", "!", "?")) else t + ".")
                               for line, t in entries]
                text = " ".join(t for _, t in entries)
                flags = []
                # Scan complete sentences across Markdown wraps, but keep locations.
                for sev, label, hit, fix in check_text(text, spoken=section == "script"):
                    pos = normalize(text).find(hit) if hit else 0
                    offset, line = 0, entries[0][0]
                    for row_line, row_text in entries:
                        if offset > pos:
                            break
                        line = row_line
                        offset += len(row_text) + 1
                    flags.append((sev, label, hit, fix, line))
                grade = fk_grade(text)
                # Short slides/overlays have unstable estimates, but still get checked.
                short = len(words_of(text)) < 30
                if grade is not None and grade > TARGET_MAX:
                    flags.append(("WARN" if short else "FAIL",
                                  f"reads above grade 8 ({grade:.1f})", "",
                                  "simplify; short-copy scores need a human check",
                                  entries[0][0]))
                longest = max((len(words_of(s)) for s in sentences(text)), default=0)
                result = "FAIL" if any(f[0] == "FAIL" for f in flags) else (
                    "WARN" if flags else "PASS")
                any_fail |= result == "FAIL"
                g = "n/a" if grade is None else f"{grade:.1f}"
                print(f"  {p['id']} {section}: grade {g}, longest {longest}, {result}")
                for sev, label, hit, fix, line in flags:
                    print(f"    {path}:{line} [{sev}] {label}: {hit!r} -> {fix}")
    return 1 if any_fail else 0



def self_test():
    """Run dependency-free regression checks without changing repository files."""
    import contextlib
    import io
    import tempfile
    from pathlib import Path

    def fails(text):
        return any(flag[0] == "FAIL" for flag in check_text(text, spoken=True))

    for text in ("That's not behind. That's building.",
                 "That’s not behind. That’s building.",
                 "The magic isn’t the report. It’s the fix.",
                 "Mistakes aren't the problem. Repeating them is.",
                 "No shame required.", "We analyse the colour scheme."):
        assert fails(text), text
    for text in ("You're not behind. You're in a great place to start.",
                 "You’re not behind. You’re in a great place to start.",
                 "Stay human. I'll handle the robot stuff. My human checks it.",
                 "We analyze the color scheme. The analyses are done.",
                 "We sorted the list. It was a brilliant idea."):
        assert not fails(text), text
    assert not fails(" ".join(["word"] * 20) + ".")
    assert fails(" ".join(["word"] * 21) + ".")
    assert check_text("Do not send it yet.", spoken=True)
    assert not check_text("Do not send it yet.", spoken=False)
    assert len(sentences("A sentence wraps\nonto a new line. Next one.")) == 2
    assert len(sentences('She said "Done." Next one.')) == 2
    assert TARGET_MAX == 8.0

    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "sample.md"
        for marker in ("1️⃣", "1.", "10."):
            path.write_text(
                "### W10-MON\n**Script (spoken)**\n> Try a task.\n"
                "**Caption**\n```text\n"
                f"{marker} Build it\n2. Prove it\n"
                "Try one task today.\n```\n", encoding="utf-8")
            piece = parse(path)[0]
            caption = [text for section, _, text in piece["entries"]
                       if section == "caption"]
            assert caption == [f"{marker} Build it.", "2. Prove it.",
                               "Try one task today."], caption
            # A period in a numbered marker also counts as punctuation.
            # Each item and the final sentence must remain separate.
            parts = sentences(" ".join(caption))
            assert parts[-1] == "Try one task today.", parts
            assert any("Build it." in part for part in parts), parts
            assert any("Prove it." in part for part in parts), parts
            with contextlib.redirect_stdout(io.StringIO()):
                assert main([str(path)]) == 0
        path.write_text(
            "### W10-WED\n| # | Slide | Copy |\n"
            "| 1 | Supercharge work | Use a list. |\n"
            "**Caption**\n```text\nShort caption.\n```\n",
            encoding="utf-8")
        assert "Supercharge work" in parse(path)[0]["entries"][0][2]
        with contextlib.redirect_stdout(io.StringIO()):
            assert main([str(path)]) == 1
        for text in ("No supported headings.",
                     "### W1-MON\n**Script (spoken)**\n> Hello there.\n"):
            path.write_text(text, encoding="utf-8")
            with contextlib.redirect_stdout(io.StringIO()):
                assert main([str(path)]) == 1
        with contextlib.redirect_stdout(io.StringIO()):
            assert main([str(path) + "missing"]) == 1
        hard = " ".join(
            ["Organizational implementation requires comprehensive evaluation."] * 8)
        path.write_text(
            "### W1-MON\n**Script (spoken)**\n> Try a task.\n"
            "**Caption**\n```text\n" + hard + "\n```\n",
            encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            assert main([str(path)]) == 1
    print("Voice checker regression checks passed.")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        sys.exit(self_test())
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
