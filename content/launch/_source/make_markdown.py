import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from launch_content import WEEKS, IMAGES, HASHTAGS_CORE, higgsfield_prompt, seconds, words

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)


def video_md(p, bridge=False):
    img_file, img_desc = IMAGES[p["image"]]
    out = [f"### {p['id']} · {p['day']} · {p['series']}: {p['title']}", ""]
    out += [f"- **Format:** Talking-head reel, 9:16, about {seconds(p['script'])} s ({words(p['script'])} words)",
            f"- **Start image:** `assets/face/approved/{img_file}` ({img_desc})",
            f"- **Source:** {p['source']}",
            "- **Status:** Ready for Higgsfield", ""]
    out += ["**Script (spoken)**", ""]
    out += [f"> {line}" + ("\n>" if i < len(p["script"]) - 1 else "") for i, line in enumerate(p["script"])]
    out += ["", "**On-screen text (add in editing)**", "", "| Time | Text |", "|---|---|"]
    out += [f"| {t} | {x} |" for t, x in p["onscreen"]]
    out += ["", "**Higgsfield prompt (copy and paste)**", "", "```text", higgsfield_prompt(p), "```", ""]
    out += ["**Caption**", "", "```text", p["caption"], "", HASHTAGS_CORE, "```", ""]
    return out


def carousel_md(p):
    out = [f"### {p['id']} · {p['day']} · {p['series']}: {p['title']}", ""]
    out += [f"- **Format:** Carousel, {len(p['slides'])} slides, 4:5 (1080 × 1350)",
            "- **Design:** Brand template (see README): cornflower blue, white and soft pink; Remi photo on the cover only",
            f"- **Source:** {p['source']}",
            "- **Status:** Ready to design", "", "| # | Slide | Copy |", "|---|---|---|"]
    for i, s in enumerate(p["slides"], 1):
        if s["kind"] == "list":
            body = " ".join(f"{n}. {it}" for n, it in enumerate(s["items"], 1))
        else:
            body = s.get("body", "")
        label = s.get("label", {"cover": "Cover", "end": "Closer", "prompt": "Prompt"}.get(s["kind"], ""))
        if s["kind"] == "end":
            body += " @remitobor"
        head = f"**{s['head']}**"
        if s.get("image"):
            body += f" *(Image: `assets/face/approved/{IMAGES[s['image']][0]}`)*"
        out.append(f"| {i} | {label} | {head} {body} |")
    out += ["", "**Caption**", "", "```text", p["caption"], "", HASHTAGS_CORE, "```", ""]
    return out


for w in WEEKS:
    md = [f"# Week {w['num']}: {w['name']}", "",
          f"> **Pillar:** {w['pillar']} · **Goal:** {w['goal']}",
          "> Generated from the launch content source; see `README.md` in this folder for the workflow and rules.", ""]
    md += ["| Day | Series | Post | Format |", "|---|---|---|---|"]
    for p in w["posts"] + [w["bridge"]]:
        fmt = "Talking-head reel" if p["type"] == "video" else "Carousel"
        md.append(f"| {p['day']} | {p['series']} | {p['title']} | {fmt} |")
    md.append("")
    for p in w["posts"]:
        md += video_md(p) if p["type"] == "video" else carousel_md(p)
    md += ["## Bridge video", ""] + video_md(w["bridge"], bridge=True)
    open(os.path.join(OUT, f"week-{w['num']}.md"), "w").write("\n".join(md))
print("ok")
