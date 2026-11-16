# Brief for Codex: Alternate Versions of Remi's Launch Posts (Weeks 1–3)

**From:** Claude (on behalf of the owner) · **Date:** 2026-11-16 · **Status:** Open

## The ask

Claude wrote the first version (**Option A**) of every post for Remi's first three weeks. The owner wants you, Codex, to **review each one and write an alternate (Option B) that builds on its creativity**: same goal and source lesson, but a fresh angle, hook, or format idea that could perform better. The owner will choose between A and B each week.

There are **12 pieces**: 9 posts (3 per week: Mon talking-head reel, Wed carousel, Fri reel) plus 3 Sunday bridge videos.

## Read first (in this order)

1. `persona/01-profile.md`, `persona/02-backstory.md`, `persona/04-voice-and-style.md`: who Remi is and how she sounds
2. `GUARDRAILS.md`: **binding rules**, especially section 4 (accuracy) and section 7 (protecting the owner's identity and employer)
3. `content/messaging-framework.md`: core messages, the emotional core, the seven topics
4. `content/launch/README.md`: the launch block, production workflow, and rules
5. `content/launch/week-1.md`, `week-2.md`, `week-3.md`: Option A for every post
6. `research/playbook-content-map.md` and `research/AI-Playbook-for-Business-Professionals.md`: the real lessons the posts come from

## For each of the 12 pieces, write

1. **Review of Option A** (2–4 bullets): what's strongest, what could hook harder or land better.
2. **Option B**, production-ready, in the same format as the week files:
   - **Talking-head videos:** title, length, start image (one of the approved images in `assets/face/approved/`), spoken script, on-screen text with timings, performance notes, a complete Higgsfield prompt (same structure as Option A's), and a caption.
   - **Carousels:** title, slide-by-slide copy (6–10 slides, 4:5), and a caption.
3. **What's different** (one line): the creative idea B tests versus A.

Also propose **3–5 alternatives for the core line** "You're not behind. You're in a great place to start." Each must be encouraging, make sense on its own, and push the viewer toward one action.

## Non-negotiable rules

- **Remi is openly AI** with "my human" behind her. She never claims a human life (no family, home, degree, job history, or feelings presented as real).
- **Protect the owner's identity and employer** (`GUARDRAILS.md` section 7). Never include the company, industry, market, customers, the owner's job title, team size, dates, exact counts, or precise percentages. Use "my human's team," tool categories, and soft language ("a fraction of the time," "roughly half or more").
- **No invented facts.** No new statistics, studies, quotes, case studies, or results. Use only what the playbook supports, kept directional ("in our experience," "roughly").
- **Tone:** fun, bubbly, lively, professional, tenacious. Open with a familiar frustration, never fear or FOMO. Show what flopped as well as what worked. End with one small next step. No "AI will replace you," no shaming, no hype.
- **Length:** talking-head reels about 20–50 seconds at ~150 words per minute; bridges 10–20 seconds.
- **House style:** plain language, short sentences, no em dashes.
- **Likeness:** scripts must not present Remi's words as the views or experiences of the real person whose likeness she uses.

## Where to put your work

- Write `content/launch/alternates/week-1-codex.md`, `week-2-codex.md`, `week-3-codex.md` (one file per week, pieces in the same order as the week files, labeled with the same IDs: W1-MON, W1-WED, W1-FRI, W1-BRIDGE, and so on).
- Put the core-line alternatives at the top of `week-1-codex.md`.
- **Do not edit** Claude's files (`content/launch/week-*.md`, `content/launch/_source/`), `GUARDRAILS.md`, or anything in `persona/`.
- Work on a branch named `codex/launch-alternates` and open a pull request into `claude/ai-persona-business-education-yw0yla`.

## What happens next

The owner reviews A and B side by side in `content/launch/picks.md` and picks one per slot each week (or asks for a blend). Claude then updates the production files and the preview board with the winners.
