"""Build the Claude vs Codex side-by-side comparison page.

Usage: python3 -I make_compare.py OUT.html CODEX_W1 CODEX_W2 CODEX_W3 CHECK_RUN.txt FIX_PROMPT.md
"""
import sys, os, re, html
sys.path.insert(0, os.path.dirname(__file__))
from launch_content import WEEKS, HASHTAGS_CORE

OUT, CX1, CX2, CX3, RUN, FIXP = sys.argv[1:7]
E = html.escape
IMG = {"remi_profile_blue.jpg": "img/profile.jpg", "remi_monday_cover_one_point.jpg": "img/desk.jpg", "remi_work_mode_full.jpg": "img/work.jpg"}
IMG_KEY = {"profile": "img/profile.jpg", "desk": "img/desk.jpg", "work": "img/work.jpg"}

# Claude's recommendation per slot (from the review shown to the owner)
REC = {
    "W1-MON": ("Blend", "Codex's frustration-first hook plus Claude's warmth (\"Some worked. Some flopped.\").", "Use \"Yes, I'm AI\" instead of \"an AI persona.\""),
    "W1-WED": ("Blend, mostly Claude", "\"Which stage are you?\" invites comments. Add Codex's \"A draft still needs checks\" slide and its reusable prompt.", "Split Codex's 25-word slide sentence."),
    "W1-FRI": ("Codex", "\"Everyone still needs you to explain it\" is a real pain. Add Claude's sign-off back.", "Claude's fails (\"here's the secret\")."),
    "W1-BRIDGE": ("Codex", "Gives a specific action and includes the core line.", "\"An AI persona\" in the caption."),
    "W2-MON": ("Codex", "The \"return ticket\" hook. Optionally add Claude's \"roughly half or more\" result line.", "Claude's fails (contrast tell, 26-word sentence)."),
    "W2-WED": ("Blend", "Codex's cover fixes Claude's unsupported claim. Keep Claude's 5 rules and the \"Steal this prompt\" slide.", "Claude's cover fails (contrast tell)."),
    "W2-FRI": ("Codex", "Codex tells the incident accurately; Claude's version didn't.", "Change \"Looked sorted!\" to \"Looked fixed!\" and cut \"No shame required.\""),
    "W2-BRIDGE": ("Codex", "Carries \"fix the source\" into outreach prep.", "Keep Claude's \"wincing means you noticed\" if you like it."),
    "W3-MON": ("Blend", "Codex's \"scrolling instead of calling\" opener, then Claude's \"You don't need a database. You need a list.\"", "Split Claude's two 22-word sentences."),
    "W3-WED": ("Codex, lighter wording", "Separates what the team did from general tips. Trim the caveats on slide 8 and in the caption.", "Simplify slide 5 (reads above grade 8)."),
    "W3-FRI": ("Blend", "Codex's \"send button off\" framing and front-facing image, plus Claude's \"Mondays back\" payoff.", "Claude's fails (contrast tell, 28-word sentence)."),
    "W3-BRIDGE": ("Codex", "Welcomes people who only watched the posts.", "Claude's \"That's not behind. That's building.\" is a contrast tell."),
}


def parse_codex(path):
    text = open(path, encoding="utf-8").read()
    core = []
    m = re.search(r"## Core-line alternatives\n\n(.*?)\n\n", text, re.S)
    if m:
        core = [re.sub(r"^\d+\.\s*", "", l).strip() for l in m.group(1).splitlines() if l.strip()]
    pieces = {}
    for block in re.split(r"\n(?=### W\d-)", text)[1:]:
        head = block.splitlines()[0]
        pid = re.match(r"### (W\d-[A-Z]+)", head).group(1)
        p = {"id": pid, "review": [], "script": [], "onscreen": [], "slides": [], "caption": "", "tests": "", "title": "", "format": "", "image": None}
        mode = None
        lines = block.splitlines()
        i = 0
        in_code = False
        cap = []
        while i < len(lines):
            l = lines[i]
            if l.startswith("```"):
                if in_code and mode == "caption":
                    mode = None
                in_code = not in_code
                i += 1
                continue
            if not in_code:
                if l.startswith("**Review of Option A**"): mode = "review"
                elif l.startswith("**Option B**"): mode = "meta"
                elif l.startswith("**Script (spoken)**"): mode = "script"
                elif l.startswith("**On-screen text"): mode = "onscreen"
                elif l.startswith("**Performance notes**") or l.startswith("**Higgsfield"): mode = None
                elif l.startswith("**Caption**"): mode = "caption"
                elif l.startswith("**What Option B tests:**"):
                    p["tests"] = l.split(":**", 1)[1].strip()
                    mode = None
                elif mode == "review" and l.startswith("- "): p["review"].append(l[2:].strip())
                elif mode == "meta" and l.startswith("- **"):
                    k, v = re.match(r"- \*\*(.+?):\*\*\s*(.*)", l).groups()
                    if k == "Title": p["title"] = v
                    if k == "Format": p["format"] = v
                    if k == "Start image":
                        mm = re.search(r"remi_[a-z_]+\.jpg", v)
                        p["image"] = mm.group(0) if mm else None
                elif mode in ("meta",) and l.startswith("| ") and re.match(r"\|\s*\d+\s*\|", l):
                    c = [x.strip() for x in l.strip("|").split("|")]
                    p["slides"].append((c[1], c[2]))
                elif mode == "script" and l.startswith(">"):
                    t = l.lstrip("> ").strip()
                    if t: p["script"].append(t)
                elif mode == "onscreen" and l.startswith("| ") and not re.match(r"\|\s*(Time|---)", l):
                    c = [x.strip() for x in l.strip("|").split("|")]
                    p["onscreen"].append((c[0], c[1]))
            elif mode == "caption":
                cap.append(l)
            i += 1
        p["caption"] = "\n".join(cap).strip()
        pieces[pid] = p
    return core, pieces


def parse_run(path):
    """Group checker output by (side, piece) -> list of (severity, text)."""
    res, side, cur = {}, None, None
    for l in open(path, encoding="utf-8"):
        l = l.rstrip("\n")
        if l.startswith("==="):
            side = "B" if re.search(r"cx\d\.md", l) else "A"
            continue
        m = re.match(r"\s{2}(W\d-[A-Z]+) (.+?): grade ([\d.na/]+), longest (\d+), (PASS|WARN|FAIL)", l)
        if m:
            cur = (side, m.group(1))
            res.setdefault(cur, {"result": "PASS", "flags": []})
            r = m.group(5)
            order = {"PASS": 0, "WARN": 1, "FAIL": 2}
            if order[r] > order[res[cur]["result"]]:
                res[cur]["result"] = r
            continue
        m = re.match(r"\s{4}\S+:\d+ \[(FAIL|WARN)\] (.+?): (.*?) -> .*", l)
        if m and cur:
            hit = m.group(3).strip("'\"")
            label = m.group(2)
            txt = label + (f": “{hit[:70]}{'...' if len(hit) > 70 else ''}”" if hit else "")
            res[cur]["flags"].append((m.group(1), txt))
    return res


core_b, B = {}, {}
for path in (CX1, CX2, CX3):
    c, pcs = parse_codex(path)
    if c: core_b = c
    B.update(pcs)
CHECK = parse_run(RUN)
fix_prompt = open(FIXP, encoding="utf-8").read().split("```text\n", 1)[1].rsplit("\n```", 1)[0]


def check_html(side, pid):
    c = CHECK.get((side, pid), {"result": "PASS", "flags": []})
    chip = f'<span class="chip {c["result"].lower()}">Voice check: {c["result"]}</span>'
    flags = "".join(f'<li class="{s.lower()}"><b>{s}</b> {E(t)}</li>' for s, t in c["flags"])
    return chip + (f'<ul class="flags">{flags}</ul>' if flags else "")


def script_html(lines):
    return '<div class="script">' + "".join(f"<p>{E(l)}</p>" for l in lines) + "</div>"


def onscreen_html(rows):
    if not rows: return ""
    return '<details class="mini"><summary>On-screen text</summary><ul class="ons">' + "".join(
        f'<li><span>{E(t)}</span>{E(x)}</li>' for t, x in rows) + "</ul></details>"


def slides_html(rows):
    return '<ol class="slides">' + "".join(f'<li><b>{E(h)}</b> {E(b)}</li>' for h, b in rows) + "</ol>"


def caption_html(text):
    return f'<details class="mini"><summary>Caption</summary><pre>{E(text)}</pre></details>'


def a_slides(p):
    out = []
    for s in p["slides"]:
        body = " ".join(f"{n}) {x}" for n, x in enumerate(s["items"], 1)) if s["kind"] == "list" else s.get("body", "")
        out.append((s["head"], body))
    return out


def side_a(p):
    is_video = p["type"] == "video"
    words = sum(len(l.split()) for l in p.get("script", []))
    fmt = f"Talking-head reel · ~{round(words / 2.5)} s" if is_video else f"Carousel · {len(p['slides'])} slides"
    img = f'<img class="thumb" src="{IMG_KEY[p["image"]]}" alt="">' if is_video else ""
    body = script_html(p["script"]) + onscreen_html(p["onscreen"]) if is_video else slides_html(a_slides(p))
    return f'''<div class="col a"><div class="who">Claude · Option A</div><div class="ctop">{img}<div><h4>{E(p["title"])}</h4><span class="fmt">{E(fmt)}</span></div></div>{body}{caption_html(p["caption"] + chr(10) + chr(10) + HASHTAGS_CORE)}<div class="vc">{check_html("A", p["id"])}</div></div>'''


def side_b(pid):
    p = B.get(pid)
    if not p:
        return '<div class="col b"><div class="who">Codex · Option B</div><p>Missing.</p></div>'
    is_video = bool(p["script"])
    img = f'<img class="thumb" src="{IMG[p["image"]]}" alt="">' if is_video and p["image"] in IMG else ""
    body = script_html(p["script"]) + onscreen_html(p["onscreen"]) if is_video else slides_html(p["slides"])
    tests = f'<p class="tests"><b>What B tests:</b> {E(p["tests"])}</p>' if p["tests"] else ""
    return f'''<div class="col b"><div class="who">Codex · Option B</div><div class="ctop">{img}<div><h4>{E(p["title"])}</h4><span class="fmt">{E(p["format"].split(",")[0] + (" · " + p["format"].split("about")[1].split("(")[0].strip() if "about" in p["format"] else ""))}</span></div></div>{body}{caption_html(p["caption"])}{tests}<div class="vc">{check_html("B", pid)}</div></div>'''


def slot(p, day_label):
    pid = p["id"]
    pick, why, fix = REC[pid]
    cls = "blend" if pick.lower().startswith("blend") else ("codex" if pick.lower().startswith("codex") else "claude")
    review = B.get(pid, {}).get("review", [])
    rev = '<details class="mini review"><summary>Codex\'s review of Option A</summary><ul>' + "".join(f"<li>{E(r)}</li>" for r in review) + "</ul></details>" if review else ""
    return f'''<article class="slot" id="{pid.lower()}">
  <header class="shead"><span class="sid">{pid}</span><span class="series">{E(day_label)} · {E(p["series"])}</span>
  <span class="pick {cls}">Claude recommends: {E(pick)}</span></header>
  <p class="why">{E(why)} <span class="fix">Voice fix: {E(fix)}</span></p>
  <div class="cols">{side_a(p)}{side_b(pid)}</div>
  {rev}
</article>'''


weeks_html = ""
for w in WEEKS:
    slots = "".join(slot(p, p["day"]) for p in w["posts"]) + slot(w["bridge"], "Sun bridge")
    weeks_html += f'<section class="week" id="week-{w["num"]}"><h2><span>Week {w["num"]}</span> {E(w["name"])}</h2>{slots}</section>'

nav = "".join(f'<a href="#week-{w["num"]}">Week {w["num"]}</a>' for w in WEEKS) + '<a href="#codex-fixes">Send to Codex</a>'
core_list = "".join(f"<li>{E(c)}</li>" for c in core_b)

page = f'''<title>Remi A/B Compare</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: one row per slot, Claude (A) and Codex (B) side by side, recommendation above. Stacks on phones. */
:root {{
  --bg: #F2F5FC; --surface: #FFFFFF; --ink: #1B2340; --muted: #5A6482; --line: #DCE3F2;
  --a: #4C74D9; --a-soft: #E7EDFB; --b: #0E8A6E; --b-soft: #E2F4EE; --blend: #9A5B00; --blend-soft: #FBEFD9;
  --pass: #1E7A44; --warn: #946200; --fail: #B3261E; --accent-ink: #FFFFFF;
  --f-display: "Bricolage Grotesque", "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --f-body: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, Menlo, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0E1322; --surface: #161D33; --ink: #E8ECF8; --muted: #9CA6C4; --line: #28324F;
  --a: #86A3F2; --a-soft: #1D2747; --b: #4FC9A6; --b-soft: #13302A; --blend: #E7B566; --blend-soft: #3A2C14;
  --pass: #63CF8E; --warn: #E7B566; --fail: #F28B82; --accent-ink: #0E1322; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #0E1322; --surface: #161D33; --ink: #E8ECF8; --muted: #9CA6C4; --line: #28324F;
  --a: #86A3F2; --a-soft: #1D2747; --b: #4FC9A6; --b-soft: #13302A; --blend: #E7B566; --blend-soft: #3A2C14;
  --pass: #63CF8E; --warn: #E7B566; --fail: #F28B82; --accent-ink: #0E1322; color-scheme: dark }}
* {{ box-sizing: border-box }}
body {{ background: var(--bg); color: var(--ink); font: 15px/1.55 var(--f-body);
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px }}
.wrap {{ max-width: 1200px; margin: 0 auto; display: grid; gap: 28px }}
h1, h2, h4 {{ font-family: var(--f-display); margin: 0; text-wrap: balance }}
h1 {{ font-size: clamp(28px, 4.6vw, 42px); font-weight: 800 }}
.lede {{ margin: 6px 0 0; color: var(--muted); max-width: 70ch }}
.legend {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px }}
.legend span {{ border-radius: 999px; padding: 3px 12px; font-size: 13px; font-weight: 600 }}
.lg-a {{ background: var(--a-soft); color: var(--a) }} .lg-b {{ background: var(--b-soft); color: var(--b) }} .lg-x {{ background: var(--blend-soft); color: var(--blend) }}
nav {{ display: flex; flex-wrap: wrap; gap: 8px }}
nav a {{ text-decoration: none; color: var(--ink); background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 8px 14px; font-weight: 600; font-size: 14px }}
nav a:hover {{ border-color: var(--a) }}
:focus-visible {{ outline: 2px solid var(--a); outline-offset: 2px }}
.core {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px }}
.panel {{ background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 16px; min-width: 0 }}
.panel h2 {{ font-size: 18px; margin-bottom: 8px }}
.panel ol, .panel ul {{ margin: 0; padding-left: 20px; display: grid; gap: 4px }}
.panel .big {{ font-family: var(--f-display); font-size: 20px; font-weight: 700; margin: 4px 0 }}
.week {{ display: grid; gap: 16px; scroll-margin-top: 12px }}
.week > h2 {{ font-size: clamp(22px, 3.2vw, 30px); border-top: 3px solid var(--ink); padding-top: 12px }}
.week > h2 span {{ font-family: var(--f-mono); font-size: 13px; color: var(--a); font-weight: 400; display: block; text-transform: uppercase; letter-spacing: .05em }}
.slot {{ background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 16px; display: grid; gap: 10px; scroll-margin-top: 12px }}
.shead {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center }}
.sid {{ font-family: var(--f-mono); font-weight: 700; background: var(--ink); color: var(--bg); border-radius: 6px; padding: 2px 8px; font-size: 13px }}
.series {{ font-weight: 600; font-size: 14px }}
.pick {{ margin-left: auto; border-radius: 999px; padding: 3px 12px; font-size: 13px; font-weight: 700 }}
.pick.claude {{ background: var(--a-soft); color: var(--a) }} .pick.codex {{ background: var(--b-soft); color: var(--b) }} .pick.blend {{ background: var(--blend-soft); color: var(--blend) }}
.why {{ margin: 0; font-size: 14px }} .fix {{ color: var(--muted) }}
.cols {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; align-items: start }}
.col {{ border-radius: 12px; padding: 12px; display: grid; gap: 8px; min-width: 0; border: 1px solid var(--line) }}
.col.a {{ border-top: 4px solid var(--a) }} .col.b {{ border-top: 4px solid var(--b) }}
.who {{ font-family: var(--f-mono); font-size: 11.5px; text-transform: uppercase; letter-spacing: .06em }}
.col.a .who {{ color: var(--a) }} .col.b .who {{ color: var(--b) }}
.ctop {{ display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 10px; align-items: center }}
.thumb {{ width: 54px; height: 72px; object-fit: cover; object-position: center top; border-radius: 8px; border: 2px solid var(--ink) }}
.ctop h4 {{ font-size: 16.5px; line-height: 1.2 }}
.fmt {{ font-size: 12px; color: var(--muted) }}
.script p {{ margin: 0 0 6px; font-size: 14px }}
.slides {{ margin: 0; padding-left: 20px; display: grid; gap: 5px; font-size: 13.5px }}
.mini {{ border: 1px solid var(--line); border-radius: 8px; background: var(--bg) }}
.mini summary {{ cursor: pointer; padding: 6px 10px; font-size: 13px; font-weight: 600 }}
.mini pre {{ margin: 0; padding: 0 10px 10px; white-space: pre-wrap; word-break: break-word; font: 12.5px/1.5 var(--f-body) }}
.mini ul {{ margin: 0; padding: 0 10px 10px 28px; font-size: 13px; display: grid; gap: 3px }}
.ons {{ list-style: none; padding-left: 10px !important }}
.ons li {{ display: grid; grid-template-columns: 62px minmax(0, 1fr); gap: 6px }}
.ons span {{ font-family: var(--f-mono); font-size: 11px; color: var(--muted); padding-top: 2px }}
.tests {{ margin: 0; font-size: 13px; color: var(--muted) }}
.chip {{ display: inline-block; border-radius: 6px; padding: 2px 8px; font-size: 12px; font-weight: 700; border: 1px solid currentColor }}
.chip.pass {{ color: var(--pass) }} .chip.warn {{ color: var(--warn) }} .chip.fail {{ color: var(--fail) }}
.flags {{ list-style: none; margin: 6px 0 0; padding: 0; display: grid; gap: 3px; font-size: 12.5px }}
.flags li.fail b {{ color: var(--fail) }} .flags li.warn b {{ color: var(--warn) }}
.review summary {{ color: var(--muted) }}
.codex {{ border: 2px solid var(--b); }}
.copywrap {{ position: relative }}
.copywrap pre {{ margin: 0; white-space: pre-wrap; word-break: break-word; font: 12px/1.5 var(--f-mono); background: var(--bg); border: 1px solid var(--line); border-radius: 8px; padding: 12px; padding-top: 40px; max-height: 460px; overflow: auto }}
.copy {{ position: absolute; top: 8px; right: 8px; font: 600 12.5px var(--f-body); background: var(--b); color: var(--accent-ink); border: 0; border-radius: 6px; padding: 6px 12px; cursor: pointer }}
.steps {{ margin: 8px 0 12px; padding-left: 20px; display: grid; gap: 4px; color: var(--muted); font-size: 14px }}
footer {{ color: var(--muted); font-size: 13px; border-top: 1px solid var(--line); padding-top: 12px }}
@media (max-width: 860px) {{ .cols, .core {{ grid-template-columns: minmax(0, 1fr) }} .pick {{ margin-left: 0 }} }}
</style>

<div class="wrap">
  <header>
    <h1>Remi A/B Compare</h1>
    <p class="lede">Every launch slot with Claude's version and Codex's version side by side, each run through the Human Voice Check (Codex's updated checker), plus Claude's recommendation. Nothing here is final until you pick and both of you read it aloud.</p>
    <div class="legend"><span class="lg-a">Claude · Option A</span><span class="lg-b">Codex · Option B</span><span class="lg-x">Blend = combine both</span></div>
  </header>
  <nav aria-label="Jump to">{nav}</nav>

  <div class="core">
    <div class="panel"><h2>Core line</h2><p class="big">You're not behind. Start small: pick one task to make easier today.</p><p class="fmt">Claude's recommended blend: keeps "You're not behind" and adds Codex's action.</p></div>
    <div class="panel"><h2>Codex's five alternatives</h2><ol>{core_list}</ol></div>
  </div>

  {weeks_html}

  <section class="panel codex" id="codex-fixes">
    <h2>Send to Codex: fixes for pull request #4</h2>
    <ol class="steps"><li>Open Codex in ChatGPT and select the AIBusinessPersona repository.</li><li>Paste this message. Codex updates its open pull request #4.</li><li>Tell Claude when it's done; Claude re-checks before anything merges.</li></ol>
    <div class="copywrap"><button type="button" class="copy" data-target="fixprompt">Copy</button><pre id="fixprompt">{E(fix_prompt)}</pre></div>
  </section>

  <footer>Voice-check results come from Codex's updated checker (pull request #4) run on the current drafts. Reading-level scores are estimates; the read-aloud test is the final word.</footer>
</div>

<script>
document.addEventListener('click', function (e) {{
  var b = e.target.closest('.copy'); if (!b) return;
  var pre = document.getElementById(b.dataset.target); if (!pre) return;
  var done = function () {{ b.textContent = 'Copied'; setTimeout(function () {{ b.textContent = 'Copy'; }}, 1600); }};
  var fallback = function () {{ var r = document.createRange(); r.selectNodeContents(pre); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = 'Selected: press Ctrl/Cmd+C'; }};
  try {{ navigator.clipboard.writeText(pre.textContent).then(done, fallback); }} catch (err) {{ fallback(); }}
}});
</script>
'''
open(OUT, "w", encoding="utf-8").write(page)
print("written", len(page), "| B pieces:", len(B), "| check entries:", len(CHECK), "| core alts:", len(core_b))
