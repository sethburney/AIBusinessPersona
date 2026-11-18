# Prompt to paste into Codex (cross-review of final launch copy)

```text
You're working in the GitHub repository sethburney/AIBusinessPersona, on branch claude/ai-persona-business-education-yw0yla.

TASK
Cross-review the final launch copy for weeks 1–3 (check 3 of the Human Voice Check). The owner approved the picks; Claude wrote the final versions by blending Claude's and your drafts. You are the second set of eyes before the owner and wife read everything aloud.

READ FIRST
STYLE-GUIDE.md, GUARDRAILS.md (especially section 7), content/launch/picks.md (what was picked and why), and the final copy in content/launch/week-1.md, week-2.md and week-3.md. Your earlier drafts are in content/launch/alternates/ for reference.

DO
1. Run: python3 tools/voice_check.py content/launch/week-1.md content/launch/week-2.md content/launch/week-3.md (all should pass; report anything that doesn't).
2. Read every script out loud in your head, plus every slide, on-screen line and caption. Flag any line that still sounds machine-written, unclear, British, too formal, or too flat. Give a plain rewrite for each.
3. Check the rules: no identifying details about the owner or employer, no invented facts or figures, one next step per post, at least one playful line per script, Remi clearly AI, the script never presented as the real person's own words.
4. Check that each Higgsfield prompt's script matches the spoken script exactly.
5. Say what you'd keep. If a slot is ready as is, say so.

RULES
No em dashes. Plain American English. Don't edit the week files or anything in content/launch/_source/ (they're generated). Only create collab/final-copy-review-codex.md.

OUTPUT
Write your findings in collab/final-copy-review-codex.md, one section per slot (W1-MON through W3-BRIDGE), each marked "Ready" or "Change," with exact current text and your proposed text. Commit on a new branch named codex/final-copy-review and open a pull request into claude/ai-persona-business-education-yw0yla. Claude applies accepted changes to the source.
```
