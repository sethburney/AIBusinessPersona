# Launch Block: Weeks 1–3

Three weeks of Remi content, pre-built and ready for production. Each week has three posts (Mon, Wed, Fri) plus a short Sunday **bridge video** into the next week.

| Week | Theme | Mon (reel) | Wed (carousel) | Fri (reel) | Sun bridge |
|---|---|---|---|---|---|
| [1](week-1.md) | Launch: meet Remi | Same task, every week? Start here. | Ask → Build → Delegate | Can your process run without you explaining it? | Into messy data week |
| [2](week-2.md) | Clean data | The error with a round-trip ticket | 5 rules for a CRM your team will keep clean | Remi's Oops: great fix, wrong place | Into outreach week |
| [3](week-3.md) | Outreach | The scroll before the call | Before you send another "just checking in" | An AI assistant with the send button off | Three weeks in |

**Status (2026-11-18):** Final copy, picked from Claude's and Codex's versions (`picks.md`), passing the Human Voice Check. Waiting on Codex's cross-review and the read-aloud sign-offs (`read-aloud.md`).

**Totals:** 8 talking-head videos (5 posts + 3 bridges) and 3 carousels.

## Production workflow

| Step | What happens | Who / where |
|---|---|---|
| 1. Script and direction | Script, on-screen text, performance notes, caption: already written in each week file | Done (Claude) |
| 2. Imagery | Carousels: design slides from the copy in the brand style below; cover uses an approved Remi image. Videos: start image is an approved Remi image | Owner (Canva or similar), or ask Claude for slide files |
| 3. Higgsfield | Upload the start image, paste the **Higgsfield prompt** block, select Remi's saved voice, generate | Owner in Higgsfield |
| 4. Review | Lips match the words; face, hair and outfit stay consistent; no stray text, logos, rings or extra people; hands look normal | Owner (and wife for likeness) |
| 5. Edit | Add the on-screen text at the listed times, captions for sound-off viewers, light background music | Owner (CapCut, Instagram, TikTok editor) |
| 6. Post | Paste the caption, turn on the platform's AI-generated label, post | Owner |
| 7. Log | Add the post to the tracker in `content/content-calendar.md` | Owner or Claude |

**Higgsfield notes (from public sources, 2026-11; verify in the app):** Higgsfield's talking-avatar tools turn a photo plus a script or audio into a lip-synced video, with built-in voice generation. Front-facing, unobstructed portraits and clean audio reportedly give the best lip-sync, which is why most videos use the front-facing profile image. The exact field names in Higgsfield's form may differ from the prompt blocks here; paste each section into the matching field. Its "Soul ID" feature can train a reusable character from many photos; **confirm with her before using it** (a saved, trained avatar is still listed separately in `persona/07-likeness-consent.md`).

**Pick Remi's voice once.** Choose one Higgsfield voice that matches the voice direction in the prompts, record its name in `persona/04-voice-and-style.md`, and use it for every video.

## Standing rule 1: protect the owner's identity and employer

The ideas, what was built, and what was learned can be shared. Anything that could identify the company or the owner cannot. When in doubt, generalize one more level.

| Never include | Use instead |
|---|---|
| Company name, industry, business model, market, products, customers, locations | "My human's team," "a growing company" |
| The owner's job title, team size, org structure | "My human," "a sales team," "a handful of reps" |
| Exact counts and precise figures (number of touches, notes, jobs, reviews, percentages) | Soft language ("dramatically," "roughly half or more," "most") or broad ranges |
| Project dates or a timeline that maps to the owner's career | "Recently," "over a few months" |
| Distinctive incidents told in identifying detail | The lesson and the rule, with details blurred |
| Real dashboards, CRM screens, documents, or data | Clearly fake mock data, or typography only |
| The full tool stack in combination | Tool categories ("the CRM," "an AI assistant") |

Every week file was written to this rule. Specific playbook figures were softened (for example, a stated 50–75% became "roughly half or more"), and identifying details such as team size and touch counts were removed.

## Standing rule 2: "You're not behind. Start small: pick one task to make easier today."

The emotional core of the channel. Every piece should leave the viewer more confident than before.

- **Open with recognition, not fear.** Name the frustration ("every month-end, somebody finds a deal entered wrong") rather than warning people they're falling behind.
- **Normalize mistakes.** Flops and Oops stories show that everyone gets it wrong; the point is the rule that came out of it.
- **Always end with one small next step** the viewer can take this week.
- **Bridge videos** between weeks (and later, between campaigns) recap the wins and repeat the message: "You're not behind. Start small: pick one task to make easier today."
- **Banned:** fear-of-missing-out framing ("AI will replace you if..."), shaming, hype, and "everyone else is already doing this."

## Brand style for carousels and covers

- **Size:** 1080 × 1350 (4:5)
- **Colors:** cornflower blue (#4C74D9), deep navy text (#1B2340), white, soft pink accent (#F4C2CF), pale blue background (#EEF2FB)
- **Type:** Bricolage Grotesque (headlines), Inter (body), both free on Google Fonts
- **Remi photo:** cover slide only, from `assets/face/approved/`
- **Last slide:** always the "You're not behind" closer and @remitobor

See every slide mocked up on the **Remi Launch Board** (private artifact): https://claude.ai/artifact/GTtvHwMf7WFfg1sbvZKo16

## Before any of this is published

- [x] Wife approved use of her likeness, including talking video and Higgsfield uploads (per owner, 2026-11-16)
- [ ] Still separate: paid brand deals, a saved/trained avatar (Soul ID), cloning her real voice
- [ ] Remi's Higgsfield voice chosen and recorded
- [ ] Owner's call: GitHub repository private or public (public exposes the owner's username, commit email, and playbook; see `GUARDRAILS.md`, section 7)
- [ ] Owner comfortable sharing each lesson (employer)

## Editing these posts

Every week file is generated from one source (`_source/launch_content.py`), which also builds the preview board (`_source/make_board.py`). To change a script, edit the source and re-run `python3 -I _source/make_markdown.py .` from this folder, so the files and the board stay in sync.
