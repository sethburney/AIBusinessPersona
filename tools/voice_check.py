#!/usr/bin/env python3
"""Human Voice Check: score Remi's public copy for reading level and AI tells.

Usage: python3 tools/voice_check.py FILE [FILE ...]

Reads the week files format (pieces under '### W1-MON ...' headings) and checks
only public copy: spoken scripts, on-screen text, slide copy, and captions.
See STYLE-GUIDE.md for the rules. Exit code 1 if any piece has a FAIL.
"""
import re
import sys

TARGET_MAX = 8.9  # no harder than 8th grade; easier is fine for spoken social copy

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
    (r"—", "em dash", "comma, period, or two sentences"),
]

WARN = [
    (r"\ban ai persona\b", "clinical disclosure", "\"your AI work bestie\" or skip it"),
    (r"\b(leverage|utili[sz]e|empower\w*|optimi[sz]e)\b", "business word", "use / help / improve"),
    (r"\b(potentially|arguably|somewhat|perhaps)\b", "hedge word", "one honest qualifier at most"),
]

BRITISH = [
    (r"\b(colour|favour|honour|behaviour|neighbour|labour)\w*", "British spelling"),
    (r"\b(organis|realis|recognis|prioritis|summaris|categoris|apologis|customis|standardis)\w*", "British spelling (-ise)"),
    (r"\b(centre|metre|theatre|programme|catalogue|whilst|amongst|learnt|spelt|fortnight)\b", "British spelling/word"),
    (r"\b(sorted|reckon|brilliant|cheers|mate|keen to|queue up|rubbish)\b", "British idiom"),
]

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


def sentences(text):
    parts = re.split(r"(?<=[.!?…])\s+|\n+", text)
    return [p.strip() for p in parts if re.search(r"[A-Za-z]", p)]


def words_of(s):
    return re.findall(r"[A-Za-z][A-Za-z'’-]*", s)


def fk_grade(text):
    sents = sentences(text)
    words = [w for s in sents for w in words_of(s)]
    if not sents or not words:
        return None
    syl = sum(syllables(w) for w in words)
    return 0.39 * (len(words) / len(sents)) + 11.8 * (syl / len(words)) - 15.59


def clean(s):
    s = re.sub(r"\*\(Image:.*?\)\*", "", s)
    s = re.sub(r"\*\*([^*]+?)([.!?])?\*\*", lambda m: m.group(1) + (m.group(2) or "."), s)  # slide headline ends a sentence
    s = s.replace("**", "").replace("`", "")
    return s.strip()


def parse(path):
    pieces, cur, mode, in_code = [], None, None, False
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        m = re.match(r"^### (W\d-[A-Z]+)\b(.*)", line)
        if m:
            cur = {"id": m.group(1), "title": m.group(2).strip(" ·:"), "copy": [], "caption": [], "onscreen": []}
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
        if mode == "script" and line.startswith(">"):
            t = clean(line.lstrip("> "))
            if t:
                cur["copy"].append(t)
        elif mode == "onscreen" and line.startswith("|") and not re.match(r"^\|\s*(Time|---)", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2:
                cur["onscreen"].append(clean(cells[-1]))
        elif mode == "caption" and in_code:
            if line.strip() and not line.strip().startswith("#"):
                cur["caption"].append(line.strip())
        elif line.startswith("|") and not in_code:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 3 and cells[0].isdigit():
                cur["copy"].append(clean(cells[-1]))
    return pieces


def check_text(text, spoken):
    flags = []
    for pat, label, fix in BANNED:
        for m in re.finditer(pat, text, re.I):
            flags.append(("FAIL", label, m.group(0), fix))
    for pat, label in BRITISH:
        for m in re.finditer(pat, text, re.I):
            flags.append(("FAIL", label, m.group(0), "American English"))
    for pat, label, fix in WARN:
        for m in re.finditer(pat, text, re.I):
            flags.append(("WARN", label, m.group(0), fix))
    if spoken:
        for m in re.finditer(UNCONTRACTED, text, re.I):
            flags.append(("WARN", "no contraction (stiff out loud)", m.group(0), "use the contraction"))
    for s in sentences(text):
        n = len(words_of(s))
        if n > 25:
            flags.append(("FAIL", f"sentence too long ({n} words)", s[:70] + "...", "split it"))
        elif n > 20:
            flags.append(("WARN", f"long sentence ({n} words)", s[:70] + "...", "consider splitting"))
    return flags


def main(paths):
    any_fail = False
    for path in paths:
        pieces = parse(path)
        print(f"\n=== {path} ({len(pieces)} pieces) ===")
        print(f"{'Piece':<11}{'Copy grade':>11}{'Caption grade':>15}{'Longest':>9}  Result")
        details = []
        for p in pieces:
            copy = "\n".join(p["copy"])
            cap = "\n".join(p["caption"])
            g_copy, g_cap = fk_grade(copy), fk_grade(cap)
            longest = max((len(words_of(s)) for s in sentences(copy + "\n" + cap)), default=0)
            flags = check_text(copy, spoken=True) + check_text(cap, spoken=False) + check_text("\n".join(p["onscreen"]), spoken=False)
            if g_copy is not None and g_copy > TARGET_MAX:
                flags.append(("FAIL", f"copy reads above grade 8 ({g_copy:.1f})", "", "shorter sentences, simpler words"))
            if g_cap is not None and g_cap > TARGET_MAX:
                flags.append(("WARN", f"caption reads above grade 8 ({g_cap:.1f})", "", "shorter sentences, simpler words"))
            if g_copy is not None and g_copy < 1.5 and len(words_of(copy)) > 30:
                flags.append(("WARN", f"copy may read choppy (grade {g_copy:.1f})", "", "vary sentence length"))
            fails = sum(1 for f in flags if f[0] == "FAIL")
            warns = len(flags) - fails
            any_fail |= fails > 0
            res = "PASS" if not flags else (f"FAIL ({fails}F/{warns}W)" if fails else f"WARN ({warns})")
            fmt = lambda g: "n/a" if g is None else f"{g:.1f}"
            print(f"{p['id']:<11}{fmt(g_copy):>11}{fmt(g_cap):>15}{longest:>9}  {res}")
            if flags:
                details.append((p["id"], flags))
        for pid, flags in details:
            print(f"\n  {pid}:")
            for sev, label, hit, fix in flags:
                hit_s = f' "{hit}"' if hit else ""
                print(f"    [{sev}] {label}:{hit_s} -> {fix}")
    return 1 if any_fail else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
