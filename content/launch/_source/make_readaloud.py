"""Build the read-aloud sign-off sheet (scripts only) from the launch source.

Usage: python3 -I _source/make_readaloud.py .   (run from content/launch)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from launch_content import WEEKS, seconds

OUT = sys.argv[1]
md = [
    "# Read-Aloud Sign-Off",
    "",
    "Check 4 and 5 of the Human Voice Check (`STYLE-GUIDE.md`). Every talking video gets read out loud by the owner and by the owner's wife before it goes to Higgsfield.",
    "",
    "**How:** read each script once at normal speed, without practicing. Mark anywhere you stumbled, ran out of breath, or thought \"nobody talks like that.\" Write a better way to say it in your own words; your wording beats both AIs. Then check your box.",
    "",
    "Carousels aren't read aloud, but a quick read of the slide copy is welcome.",
    "",
]
for w in WEEKS:
    md += [f"## Week {w['num']}: {w['name']}", ""]
    for p in w["posts"] + [w["bridge"]]:
        if p["type"] != "video":
            continue
        md += [f"### {p['id']} · {p['title']} (~{seconds(p['script'])} s)", ""]
        md += [f"> {line}" + ("\n>" if i < len(p["script"]) - 1 else "") for i, line in enumerate(p["script"])]
        md += ["", "- [ ] Owner read aloud",
               "- [ ] Wife read aloud",
               "- Lines to change (and how you'd say it):", "", ""]
open(os.path.join(OUT, "read-aloud.md"), "w", encoding="utf-8").write("\n".join(md))
print("ok")
