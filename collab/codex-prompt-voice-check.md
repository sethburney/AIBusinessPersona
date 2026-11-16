# Prompt to paste into Codex (Human Voice Check review)

```text
You're working in the GitHub repository sethburney/AIBusinessPersona, on branch claude/ai-persona-business-education-yw0yla.

TASK
Review and strengthen the "Human Voice Check," the standard that makes every Remi post sound like a real person, in plain American English, at a 6th–8th grade reading level or easier. Full brief: collab/codex-brief-voice-check-review.md.

READ FIRST
STYLE-GUIDE.md, tools/voice_check.py, GUARDRAILS.md, content/messaging-framework.md, content/launch/week-1.md to week-3.md, and your own alternates on branch codex/launch-alternates (content/launch/alternates/week-1-codex.md to week-3-codex.md).

DO
1. Run python3 tools/voice_check.py on all six week files. Report false positives and false negatives.
2. Read every script in both Claude's and your versions as if out loud. List every line no real person would say, with a plain rewrite. Be as hard on your own work as on Claude's.
3. Add any missing banned patterns, American English checks, or spoken-rhythm rules to STYLE-GUIDE.md. Keep it short and usable by non-technical people.
4. Improve tools/voice_check.py where it's cheap and reliable. Keep it one dependency-free Python file.

RULES
Keep the grade-8 ceiling and the five-check process. Keep Remi's signature lines ("You're not behind," "Stay human. I'll handle the robot stuff," "my human"). No em dashes. Plain American English.

OUTPUT
Put your findings in collab/voice-check-review-codex.md. You may edit STYLE-GUIDE.md and tools/voice_check.py; list every change in the pull request description. Don't edit any other file. Commit on a new branch named codex/voice-check-review and open a pull request into claude/ai-persona-business-education-yw0yla.
```
