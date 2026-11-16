# Brief for Codex: Review and Strengthen the Human Voice Check

**From:** Claude (on behalf of the owner) · **Date:** 2026-11-16 · **Status:** Open

## Why

The owner wants every post to sound like a real person, in plain American English, at a 6th–8th grade reading level or easier. Claude drafted the standard and an automatic checker. Your job is to review both, catch what Claude missed, and make them stronger, so the standard isn't just one AI's habits.

## Read first

1. `STYLE-GUIDE.md`: the Human Voice Check (the standard)
2. `tools/voice_check.py`: the automatic checker
3. `GUARDRAILS.md` and `content/messaging-framework.md`: tone and rules the standard must fit
4. `content/launch/week-1.md` to `week-3.md` (Claude's Option A) and `content/launch/alternates/week-1-codex.md` to `week-3-codex.md` (your Option B, on branch `codex/launch-alternates`)

## Your tasks

1. **Run the checker** on all six week files (`python3 tools/voice_check.py <file>`). Report false positives (flagged but fine) and false negatives (sounds machine-written but not flagged).
2. **Find the tells the checker misses.** Read every script in both A and B as if out loud. List lines that no real person would say, with a plain rewrite. Be as hard on your own Option B as on Claude's Option A. (Claude's first read flagged, for example, "No shame required," "Preferably ones that aren't living in your head," and Claude's own "The magic isn't the report. It's that...")
3. **Strengthen the standard.** Add banned patterns, American English checks, or spoken-rhythm rules you think are missing. Keep it short and usable by non-technical people.
4. **Improve the checker** where it's cheap and reliable (new patterns, fewer false positives). Keep it a single dependency-free Python file.

## Rules

- Keep the 6th–8th grade ceiling and the five-check process (automatic score, self-edit, cross-review, owner read-aloud, wife read-aloud).
- Keep Remi's signature lines allowed: "You're not behind," "Stay human. I'll handle the robot stuff," "my human."
- No em dashes. Plain language. American English.

## Where to put your work

- Branch `codex/voice-check-review`, pull request into `claude/ai-persona-business-education-yw0yla`.
- You may edit `STYLE-GUIDE.md` and `tools/voice_check.py` in that pull request. Mark every change in the pull request description so the owner can see what you changed.
- Put your findings (task 1 and task 2) in `collab/voice-check-review-codex.md`.
- Don't edit any other file.
