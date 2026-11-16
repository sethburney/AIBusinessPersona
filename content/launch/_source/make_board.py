import sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
from launch_content import WEEKS, IMAGES, HASHTAGS_CORE, higgsfield_prompt, seconds, words

OUT = sys.argv[1]
IMG_SRC = {"profile": "img/profile.jpg", "desk": "img/desk.jpg", "work": "img/work.jpg"}
E = html.escape


def copy_block(label, text, open_=False):
    bid = f"c{abs(hash(text)) % 10**8}"
    return (f'<details class="drawer"{" open" if open_ else ""}><summary>{E(label)}</summary>'
            f'<div class="copywrap"><button type="button" class="copy" data-target="{bid}">Copy</button>'
            f'<pre id="{bid}">{E(text)}</pre></div></details>')


def video_card(p, bridge=False):
    first = p["onscreen"][0][1]
    script = "".join(f"<p>{E(l)}</p>" for l in p["script"])
    timeline = "".join(f'<li><span class="t">{E(t)}</span><span>{E(x)}</span></li>' for t, x in p["onscreen"])
    cap = p["caption"] + "\n\n" + HASHTAGS_CORE
    return f'''
<article class="card video{' bridge' if bridge else ''}" id="{p['id'].lower()}">
  <header class="card-head">
    <span class="day">{E(p['day'])}</span>
    <span class="series">{E(p['series'])}</span>
    <span class="fmt">Talking-head reel · ~{seconds(p['script'])} s</span>
  </header>
  <h3>{E(p['title'])}</h3>
  <div class="video-body">
    <figure class="phone">
      <img src="{IMG_SRC[p['image']]}" alt="Remi start image for {E(p['title'])}" loading="lazy">
      <figcaption class="overlay">{E(first)}</figcaption>
      <span class="play" aria-hidden="true">▶</span>
    </figure>
    <div class="video-text">
      <div class="script"><h4>Script</h4>{script}</div>
      <div class="timeline"><h4>On-screen text</h4><ul>{timeline}</ul></div>
    </div>
  </div>
  {copy_block("Higgsfield prompt", higgsfield_prompt(p))}
  {copy_block("Caption", cap)}
  <p class="source">Source: {E(p['source'])}</p>
</article>'''


def slide_html(s, i, n):
    k = s["kind"]
    num = f'<span class="snum">{i}/{n}</span>'
    if k == "cover":
        return (f'<div class="slide s-cover" style="background-image:url({IMG_SRC[s["image"]]})">{num}'
                f'<div class="cov-text"><span class="handle">@remitobor</span><h5>{E(s["head"])}</h5><p>{E(s["body"])}</p>'
                f'<span class="swipe">Swipe →</span></div></div>')
    if k == "step":
        return (f'<div class="slide s-step">{num}<span class="pill">{E(s["label"])}</span>'
                f'<h5>{E(s["head"])}</h5><p>{E(s["body"])}</p></div>')
    if k == "text":
        return f'<div class="slide s-text">{num}<h5>{E(s["head"])}</h5><p>{E(s["body"])}</p></div>'
    if k == "list":
        items = "".join(f"<li>{E(x)}</li>" for x in s["items"])
        return f'<div class="slide s-text">{num}<h5>{E(s["head"])}</h5><ol>{items}</ol></div>'
    if k == "rule":
        return f'<div class="slide s-rule">{num}<span class="rlabel">{E(s["head"])}</span><h5>{E(s["body"])}</h5></div>'
    if k == "prompt":
        return (f'<div class="slide s-prompt">{num}<span class="plabel">{E(s["head"])}</span>'
                f'<p class="pbody">“{E(s["body"])}”</p></div>')
    if k == "end":
        return (f'<div class="slide s-end">{num}<h5>{E(s["head"])}</h5><p>{E(s["body"])}</p>'
                f'<span class="sign">@remitobor 🤖</span></div>')
    return ""


def carousel_card(p):
    n = len(p["slides"])
    slides = "".join(slide_html(s, i, n) for i, s in enumerate(p["slides"], 1))
    cap = p["caption"] + "\n\n" + HASHTAGS_CORE
    return f'''
<article class="card carousel" id="{p['id'].lower()}">
  <header class="card-head">
    <span class="day">{E(p['day'])}</span>
    <span class="series">{E(p['series'])}</span>
    <span class="fmt">Carousel · {n} slides · 4:5</span>
  </header>
  <h3>{E(p['title'])}</h3>
  <div class="slides" role="region" aria-label="Slides for {E(p['title'])}" tabindex="0">{slides}</div>
  {copy_block("Caption", cap)}
  <p class="source">Source: {E(p['source'])}</p>
</article>'''


def week_section(w):
    posts = "".join(video_card(p) if p["type"] == "video" else carousel_card(p) for p in w["posts"])
    return f'''
<section class="week" id="week-{w['num']}">
  <div class="week-head">
    <span class="wk">Week {w['num']}</span>
    <h2>{E(w['name'])}</h2>
    <p class="goal">{E(w['goal'])}</p>
  </div>
  <div class="posts">{posts}</div>
  <div class="bridge-row"><span class="bridge-label">Sunday bridge · You're Not Behind</span>{video_card(w['bridge'], bridge=True)}</div>
</section>'''


CODEX_PROMPT = 'You\'re working in the GitHub repository sethburney/AIBusinessPersona, on branch claude/ai-persona-business-education-yw0yla.\n\nTASK\nWrite alternate versions (Option B) of Remi\'s 12 launch posts for weeks 1–3. The full brief is in collab/codex-brief-launch-alternates.md (also GitHub issue #1).\n\nREAD FIRST\nGUARDRAILS.md (binding), content/messaging-framework.md, persona/01-profile.md, persona/02-backstory.md, persona/04-voice-and-style.md, content/launch/README.md, content/launch/week-1.md, content/launch/week-2.md, content/launch/week-3.md, research/playbook-content-map.md.\n\nFOR EACH PIECE (W1-MON, W1-WED, W1-FRI, W1-BRIDGE, W2-MON, W2-WED, W2-FRI, W2-BRIDGE, W3-MON, W3-WED, W3-FRI, W3-BRIDGE)\n1. Review Claude\'s Option A in 2–4 bullets: what\'s strongest, what could hook harder.\n2. Write a production-ready Option B that builds on A\'s creativity: same goal and source lesson, a fresh hook or angle.\n   - Videos: title, length, start image from assets/face/approved/, spoken script, on-screen text with timings, performance notes, a complete Higgsfield prompt (same structure as Option A\'s), and a caption.\n   - Carousels: 6–10 slides of copy (4:5) and a caption.\n3. One line on what Option B tests that A doesn\'t.\n\nALSO\nPropose 3–5 alternatives to the core line "You\'re not behind. You\'re in a great place to start." Each must be encouraging, make sense on its own, and push the viewer toward one action. Put them at the top of week-1-codex.md.\n\nRULES\n- Remi is openly AI with "my human" behind her. She never claims a human life (family, home, degree, job history).\n- Protect the owner\'s identity: no company, industry, market, customers, job title, team size, dates, exact counts, or precise percentages. Say "my human\'s team" and use soft language ("a fraction of the time," "roughly half or more").\n- No invented statistics, studies, quotes, or results. Only use what the playbook supports, kept directional.\n- Tone: fun, bubbly, professional, encouraging. Open with a familiar frustration, never fear or FOMO. Show what flopped as well as what worked. End with one small next step.\n- Reels 20–50 seconds (about 150 words per minute). Bridges 10–20 seconds. Plain language, short sentences, no em dashes.\n\nOUTPUT\nCreate content/launch/alternates/week-1-codex.md, week-2-codex.md and week-3-codex.md, with pieces in the same order and IDs as the week files. Don\'t edit any other file. Commit on a new branch named codex/launch-alternates and open a pull request into claude/ai-persona-business-education-yw0yla.'

n_videos = sum(1 for w in WEEKS for p in w["posts"] if p["type"] == "video") + len(WEEKS)
n_car = sum(1 for w in WEEKS for p in w["posts"] if p["type"] == "carousel")
nav = "".join(f'<a href="#week-{w["num"]}">Week {w["num"]}<span>{E(w["name"])}</span></a>' for w in WEEKS)
weeks = "".join(week_section(w) for w in WEEKS)

page = f'''<title>Remi Launch Board</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap">
<style>
/* Layout: a production board. Brand header, the pipeline strip, then one band per week with post cards. Carousel slides are fixed-color mockups of the real posts. */
:root {{
  --bg: #F2F5FC; --surface: #FFFFFF; --ink: #1B2340; --muted: #5A6482; --line: #DCE3F2;
  --accent: #4C74D9; --accent-ink: #FFFFFF; --pink: #F4C2CF; --soft: #E7EDFB;
  --brand-blue: #4C74D9; --brand-navy: #1B2340; --brand-pink: #F4C2CF; --brand-pale: #EEF2FB; --brand-white: #FFFFFF;
  --f-display: "Bricolage Grotesque", "Avenir Next", "Segoe UI", system-ui, sans-serif;
  --f-body: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  --f-mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0E1322; --surface: #161D33; --ink: #E8ECF8; --muted: #9CA6C4; --line: #28324F;
  --accent: #7F9DF0; --accent-ink: #0E1322; --pink: #E7A3B6; --soft: #1C2541; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #0E1322; --surface: #161D33; --ink: #E8ECF8; --muted: #9CA6C4; --line: #28324F;
  --accent: #7F9DF0; --accent-ink: #0E1322; --pink: #E7A3B6; --soft: #1C2541; color-scheme: dark }}
* {{ box-sizing: border-box }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--f-body); font-size: 15px; line-height: 1.55;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 28px 64px }}
.wrap {{ max-width: 1180px; margin: 0 auto; display: grid; gap: 36px }}
h1, h2, h3, h4, h5 {{ font-family: var(--f-display); text-wrap: balance; margin: 0 }}
a {{ color: var(--accent) }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px }}

/* Header */
.masthead {{ display: grid; grid-template-columns: auto 1fr; gap: 22px; align-items: center }}
.masthead img {{ width: 112px; height: 112px; border-radius: 50%; object-fit: cover; border: 4px solid var(--surface); box-shadow: 0 0 0 2px var(--accent) }}
.eyebrow {{ font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 600 }}
.masthead h1 {{ font-size: clamp(30px, 5vw, 46px); font-weight: 800; line-height: 1.05; margin-top: 4px }}
.masthead .tag {{ margin: 8px 0 0; font-size: 17px; color: var(--muted); max-width: 62ch }}
.masthead .tag strong {{ color: var(--ink) }}
.stats {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px }}
.stats span {{ background: var(--soft); border-radius: 999px; padding: 4px 12px; font-size: 13px; font-weight: 600; font-variant-numeric: tabular-nums }}

/* Pipeline */
.pipeline {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 0; background: var(--surface); border: 1px solid var(--line); border-radius: 14px; overflow: hidden }}
.pipeline div {{ padding: 14px 14px 16px; border-right: 1px solid var(--line); min-width: 0 }}
.pipeline div:last-child {{ border-right: 0 }}
.pipeline b {{ display: block; font-family: var(--f-display); font-size: 15px }}
.pipeline small {{ color: var(--muted); font-size: 12.5px; line-height: 1.4; display: block; margin-top: 2px }}
.pipeline .n {{ font-family: var(--f-mono); font-size: 11px; color: var(--accent) }}
.pipeline .done {{ background: var(--soft) }}

/* Rules */
.rules {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px }}
.rule-card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 18px; min-width: 0 }}
.rule-card h2 {{ font-size: 18px; margin-bottom: 8px }}
.rule-card ul {{ margin: 0; padding-left: 18px; color: var(--muted); font-size: 14px; display: grid; gap: 4px }}
.rule-card.core {{ background: var(--accent); color: var(--accent-ink); border-color: var(--accent) }}
.rule-card.core h2 {{ font-size: 24px; line-height: 1.15 }}
.rule-card.core p {{ margin: 8px 0 0; font-size: 14px; opacity: .92 }}
.todo li::marker {{ content: "☐  " }}

/* Week nav */
.weeknav {{ display: flex; flex-wrap: wrap; gap: 10px }}
.weeknav a {{ text-decoration: none; color: var(--ink); background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 10px 14px; font-family: var(--f-display); font-weight: 700; display: grid }}
.weeknav a span {{ font-family: var(--f-body); font-weight: 500; font-size: 12.5px; color: var(--muted) }}
.weeknav a:hover {{ border-color: var(--accent) }}

/* Weeks */
.week {{ display: grid; gap: 18px; scroll-margin-top: 16px }}
.week-head {{ display: grid; gap: 4px; border-top: 3px solid var(--ink); padding-top: 14px }}
.wk {{ font-family: var(--f-mono); font-size: 12px; color: var(--accent); letter-spacing: .05em; text-transform: uppercase }}
.week-head h2 {{ font-size: clamp(24px, 3.4vw, 32px); font-weight: 800 }}
.goal {{ margin: 0; color: var(--muted); max-width: 70ch }}
.posts {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; align-items: start }}
.posts .video {{ order: 1 }}
.posts .carousel {{ order: 2; grid-column: 1 / -1 }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 16px; display: grid; gap: 12px; min-width: 0 }}
.card-head {{ display: flex; flex-wrap: wrap; gap: 6px; align-items: center; font-size: 12px }}
.day {{ background: var(--ink); color: var(--bg); border-radius: 6px; padding: 2px 8px; font-weight: 700; font-family: var(--f-mono) }}
.series {{ font-weight: 600 }}
.fmt {{ color: var(--muted); margin-left: auto }}
.card h3 {{ font-size: 19px; line-height: 1.2 }}
h4 {{ font-size: 12px; text-transform: uppercase; letter-spacing: .07em; color: var(--muted); font-family: var(--f-body); font-weight: 600; margin: 0 0 6px }}

/* Video */
.video-body {{ display: grid; grid-template-columns: 112px minmax(0, 1fr); gap: 14px; align-items: start }}
.phone {{ margin: 0; position: relative; aspect-ratio: 9 / 16; width: 112px; max-width: 100%; border-radius: 14px; overflow: hidden; border: 3px solid var(--ink); background: var(--soft) }}
.phone img {{ width: 100%; height: 100%; object-fit: cover; object-position: center top; display: block }}
.phone .overlay {{ position: absolute; left: 6px; right: 6px; top: 16%; background: var(--brand-white); color: var(--brand-navy); font-family: var(--f-display); font-weight: 700; font-size: 10px; line-height: 1.2; padding: 4px 5px; border-radius: 4px; text-align: center }}
.phone .play {{ position: absolute; left: 50%; bottom: 10px; transform: translateX(-50%); width: 28px; height: 28px; border-radius: 50%; background: var(--brand-white); color: var(--brand-navy); display: grid; place-items: center; font-size: 11px }}
.script p {{ margin: 0 0 6px; font-size: 14px }}
.timeline ul {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 3px; font-size: 13px }}
.timeline li {{ display: grid; grid-template-columns: 58px minmax(0, 1fr); gap: 6px }}
.timeline .t {{ font-family: var(--f-mono); font-size: 11px; color: var(--accent); padding-top: 2px; font-variant-numeric: tabular-nums }}
.video-text {{ display: grid; gap: 10px; min-width: 0 }}

/* Drawers */
.drawer {{ border: 1px solid var(--line); border-radius: 10px; background: var(--bg) }}
.drawer summary {{ cursor: pointer; padding: 8px 12px; font-weight: 600; font-size: 13.5px }}
.copywrap {{ position: relative; padding: 0 10px 10px }}
.copywrap pre {{ margin: 0; white-space: pre-wrap; word-break: break-word; font-family: var(--f-mono); font-size: 12px; line-height: 1.5; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 12px; max-height: 340px; overflow: auto }}
.copy {{ position: absolute; top: 6px; right: 16px; font: 600 12px var(--f-body); background: var(--accent); color: var(--accent-ink); border: 0; border-radius: 6px; padding: 5px 10px; cursor: pointer }}
.source {{ margin: 0; font-size: 12px; color: var(--muted) }}

/* Bridge */
.bridge-row {{ display: grid; gap: 8px }}
.bridge-label {{ font-family: var(--f-mono); font-size: 12px; color: var(--muted); text-transform: uppercase; letter-spacing: .05em }}
.card.bridge {{ background: var(--soft); border-style: dashed; max-width: 760px }}

/* Carousel mockups: fixed brand colors, the post looks the same in any theme */
.slides {{ display: flex; gap: 10px; overflow-x: auto; padding-bottom: 8px; scroll-snap-type: x mandatory }}
.slide {{ flex: 0 0 216px; aspect-ratio: 4 / 5; border-radius: 10px; padding: 16px 14px; position: relative; display: flex; flex-direction: column; gap: 8px; scroll-snap-align: start; overflow: hidden; box-shadow: 0 1px 0 var(--line) }}
.slide h5 {{ font-size: 18px; line-height: 1.12; font-weight: 800 }}
.slide p, .slide ol {{ margin: 0; font-size: 11.5px; line-height: 1.45 }}
.slide ol {{ padding-left: 16px; display: grid; gap: 4px }}
.snum {{ position: absolute; top: 9px; right: 11px; font-family: var(--f-mono); font-size: 9.5px; opacity: .7 }}
.s-cover {{ background-color: var(--brand-navy); background-size: cover; background-position: center top; color: var(--brand-white); justify-content: flex-end; padding: 0 }}
.s-cover .cov-text {{ background: linear-gradient(transparent, rgba(27,35,64,.94) 30%); padding: 40px 14px 14px; display: grid; gap: 6px }}
.s-cover .snum {{ color: var(--brand-white) }}
.handle {{ font-family: var(--f-mono); font-size: 9.5px; opacity: .85 }}
.swipe {{ font-size: 10px; font-weight: 600; color: var(--brand-pink) }}
.s-step {{ background: var(--brand-pale); color: var(--brand-navy) }}
.pill {{ align-self: flex-start; background: var(--brand-blue); color: var(--brand-white); border-radius: 999px; padding: 2px 9px; font-size: 10px; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; margin-top: 12px }}
.s-text {{ background: var(--brand-white); color: var(--brand-navy); border: 1px solid #DCE3F2; padding-top: 30px }}
.s-rule {{ background: var(--brand-blue); color: var(--brand-white); justify-content: center }}
.s-rule .rlabel {{ font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; opacity: .85 }}
.s-rule h5 {{ font-size: 24px }}
.s-prompt {{ background: var(--brand-navy); color: var(--brand-white) }}
.plabel {{ color: var(--brand-pink); font-family: var(--f-display); font-weight: 800; font-size: 15px; margin-top: 12px }}
.pbody {{ font-family: var(--f-mono); font-size: 10px !important; line-height: 1.5 !important }}
.s-end {{ background: var(--brand-pink); color: var(--brand-navy); justify-content: center }}
.s-end h5 {{ font-size: 21px }}
.sign {{ font-family: var(--f-mono); font-size: 10.5px; font-weight: 600; margin-top: 4px }}

.codex {{ background: var(--surface); border: 2px solid var(--accent); border-radius: 16px; padding: 18px; display: grid; gap: 12px }}
.codex h2 {{ font-size: 22px; margin-top: 2px }}
.codex p {{ margin: 6px 0 0; color: var(--muted); max-width: 70ch }}
.codex .copywrap pre {{ max-height: 420px }}
footer {{ color: var(--muted); font-size: 13px; border-top: 1px solid var(--line); padding-top: 14px }}

@media (max-width: 980px) {{
  .posts {{ grid-template-columns: minmax(0, 1fr) }}
  .rules {{ grid-template-columns: minmax(0, 1fr) }}
  .pipeline {{ grid-template-columns: repeat(3, minmax(0, 1fr)) }}
  .pipeline div:nth-child(3) {{ border-right: 0 }}
  .pipeline div:nth-child(-n+3) {{ border-bottom: 1px solid var(--line) }}
}}
@media (max-width: 520px) {{
  .masthead {{ grid-template-columns: minmax(0, 1fr) }}
  .masthead img {{ width: 84px; height: 84px }}
  .pipeline {{ grid-template-columns: repeat(2, minmax(0, 1fr)) }}
  .pipeline div {{ border-right: 0; border-bottom: 1px solid var(--line) }}
  .video-body {{ grid-template-columns: 92px minmax(0, 1fr) }}
  .phone {{ width: 92px }}
  .fmt {{ margin-left: 0; width: 100% }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior: auto !important }} }}
</style>

<div class="wrap">
  <header class="masthead">
    <img src="img/profile.jpg" alt="Remi, the AI persona">
    <div>
      <span class="eyebrow">@remitobor · Launch block · Weeks 1–3</span>
      <h1>Remi Launch Board</h1>
      <p class="tag"><strong>You're not behind. You're in a great place to start.</strong> Three weeks of posts built on <strong>Build It, Prove It, Hand It Off</strong>, ready to go to Higgsfield.</p>
      <div class="stats"><span>{len(WEEKS)} weeks</span><span>{n_videos} talking-head videos</span><span>{n_car} carousels</span><span>Mon · Wed · Fri + Sun bridge</span></div>
    </div>
  </header>

  <div class="pipeline" aria-label="Production steps">
    <div class="done"><span class="n">01 · done</span><b>Script</b><small>Script, on-screen text, direction, caption</small></div>
    <div class="done"><span class="n">02 · done</span><b>Imagery</b><small>Approved Remi stills; carousel copy and mockups</small></div>
    <div><span class="n">03</span><b>Higgsfield</b><small>Start image + prompt + Remi's voice → lip-synced video</small></div>
    <div><span class="n">04</span><b>Review</b><small>Lips, face, hands, no stray text or people</small></div>
    <div><span class="n">05</span><b>Edit</b><small>On-screen text, captions, music</small></div>
    <div><span class="n">06</span><b>Post</b><small>Caption, AI label on, log it</small></div>
  </div>

  <div class="rules">
    <div class="rule-card core"><h2>You're not behind. You're in a great place to start.</h2><p>Open with a real frustration, show what worked and what flopped, end with one small next step. No fear, no hype, no shaming.</p></div>
    <div class="rule-card"><h2>Keep it anonymous</h2><ul><li>"My human's team," never the company, industry or market</li><li>No job title, team size, dates or exact figures</li><li>Blur distinctive incidents; keep the lesson</li><li>Mock data only, never real screens</li></ul></div>
    <div class="rule-card"><h2>Before anything posts</h2><ul class="todo"><li>✓ Likeness approved, incl. talking video and Higgsfield</li><li>Pick and record Remi's Higgsfield voice</li><li>Decide: GitHub repository private or public</li><li>AI label on, every post</li></ul></div>
  </div>

  <section class="codex" id="send-to-codex">
    <div><span class="eyebrow">Claude + Codex</span><h2>Send to Codex</h2>
    <p>Paste this into Codex with the repository selected. Codex writes an Option B for every post; you pick A or B each week in <code>content/launch/picks.md</code>.</p></div>
    {copy_block("Prompt for Codex", CODEX_PROMPT, open_=True)}
  </section>

  <nav class="weeknav" aria-label="Weeks">{nav}</nav>

  {weeks}

  <footer>Drafts for review. Figures are directional and softened on purpose. Full packages live in <code>content/launch/</code> in the project repository; this board and those files come from the same source.</footer>
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
open(OUT, "w").write(page)
print("written", len(page))
