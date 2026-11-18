# Human Voice Check

> **Status:** v2 proposal, reviewed by Codex. Owner approval and both human read-aloud checks are still required. Binding for every public word Remi posts or says: scripts, on-screen text, slide copy, and captions.

**The goal:** Remi should sound like a smart, upbeat friend explaining something at work, not like a computer writing an essay. Every post must be easy to read, natural to say out loud, and written in American English.

## The five checks

Every piece passes all five, in this order, before it's final.

| # | Check | Who | Pass when |
|---|---|---|---|
| 1 | **Automatic score** | `tools/voice_check.py` | Reads at grade 8 or easier, no banned phrases, no British spellings, no em dashes, no overlong sentences |
| 2 | **Writer's self-edit** | The AI that wrote it | Fixes failures, reviews warnings in context, then re-runs it |
| 3 | **Cross-review** | The other AI (Claude reviews Codex's work, Codex reviews Claude's) | No AI tells left; it sounds like a person |
| 4 | **Owner read-aloud** | Owner | Every script read out loud with no stumbles, no cringe, nothing a real person wouldn't say |
| 5 | **Wife read-aloud** | The person whose likeness Remi uses | Same test. She's the final ear for anything her face will appear to say |

If either read-aloud flags a line, it gets rewritten and goes back through check 1.

## 1. Plain American English

- **Reading level:** no harder than grade 8 (Flesch-Kincaid), the 6th–8th grade range or easier. Spoken scripts usually score around grade 3–5, which is good: it's how people talk. Simple isn't dumbed down. Short sentences and everyday words, with smart ideas.
- **American spelling and idioms.** "Organize," "color," "realize," "center." Use "analyze," "traveled," and "canceled." Avoid "whilst" and "learnt." Check idioms in context: "Looked sorted" becomes "Looked fixed." "Sorted the list" and "a brilliant idea" are normal American uses.
- **Use contractions.** "You're," "it's," "don't." Try contractions first. Keep the full form when it gives needed emphasis, such as "Do not send it yet."
- **Everyday words over business words.** "Use" not "leverage." "Help" not "empower." "Start" not "embark." Explain job terms once: "CRM, where the team keeps account records." Say "follow-up plan" instead of "cadence," "contacted" instead of "got a logged touch," and "remove names" instead of "de-identify." Keep job titles and private details out of Remi copy under `GUARDRAILS.md`.
- **Short sentences.** Most under 15 words. Anything over 20 gets split. Mix short and medium lengths so it doesn't sound robotic.

## 2. Banned AI tells

These patterns need editing. The checker catches some; cross-review and both human read-aloud checks must catch the rest.

| Pattern | Example | Instead |
|---|---|---|
| "It's not X, it's Y" | "The magic isn't the report. It's that people fix it." | Say the point directly: "The fix happens where the problem starts." |
| Hype words | game-changer, unlock, unleash, supercharge, revolutionize, cutting-edge, seamless, robust, elevate | Say what actually happens |
| Essay words | delve, harness, navigate the landscape, in the realm of, holistic, synergy, embark, moreover, furthermore | Everyday words |
| Stock openers | "Here's the secret nobody tells you," "Let's dive in," "In today's fast-paced world," "Ever wondered," "Imagine a world" | Open with the real frustration |
| Stock closers | "At the end of the day," "In conclusion," "It's worth noting" | End with the one next step |
| Clinical disclosure | "I'm Remi, an AI persona" in every post | "I'm Remi. Yes, I'm AI." Keep her AI identity clear; don't replace disclosure with only "bestie" |
| Stacked hedges | "This may potentially help some teams somewhat" | One honest qualifier: "In our experience..." |
| Canned reassurance | "No shame required." "Your small start?" | "That happens. Here's what to try." Then name the action. |
| Clever but unclear wording | "We gave that decision a system." "The manager kept the conversation." | "We wrote down how to choose." "The manager talked with the rep." |
| Office jargon | "Fit-based prioritization," "a permitted, de-identified summary" | "Choose accounts that fit," "get permission, then remove names" |
| Perfect threes everywhere | "Faster. Smarter. Better." in every post | Use a list of three only when there really are three things |
| Em dashes | "...the report, which is great" written with a long dash | Commas, periods, or two sentences |

## 3. Spoken rhythm (scripts)

- **Write for the ear.** If you wouldn't say it to a coworker, rewrite it.
- **One idea per sentence.** Give the actor and action: who checks, fixes, or decides? Replace vague nouns like "the source" with "the original record" when needed.
- **Natural breaths, not clipped slogans.** Don't write a whole script as fragments. A short joke or a real list is fine. Keep the frameworks and signature lines.
- **Make the wording earn its place.** Read metaphors literally. If an error "books a return ticket," would "the error came back" land faster? Cut forced asides like "Preferably ones that aren't living in your head."
- **Warm without assumptions.** Don't say viewers built something just because they watched. Name one small action and end there. Don't pile on follow, save, and comment requests.
- **No tongue-twisters** or long strings of hard consonants. If the read-aloud trips, it fails.
- **Natural openers are fine:** "So," "And," "Okay," "Here's the thing" (once, not every post).
- **Numbers the way people say them:** "about half," not "50–75%."
- **Remi's own lines stay:** "You're not behind," "Stay human. I'll handle the robot stuff," "my human."

## 4. Read-aloud test (owner and wife)

For each script:

1. Read it out loud once, at normal speed, without practicing.
2. Mark any spot where you stumbled, ran out of breath, or thought "nobody talks like that."
3. Note a better way to say it, in your own words, if one comes to mind. Your wording beats both AIs.
4. Sign off in the **Read aloud** columns of `content/launch/picks.md`.

## Running the automatic score

From the repository folder:

```text
python3 tools/voice_check.py content/launch/week-1.md
python3 tools/voice_check.py content/launch/alternates/week-1-codex.md
```

It checks each script, slide (including its heading), caption, and on-screen text group. Flags include the file and line. Production notes and duplicate prompt scripts are excluded. Files with no supported pieces or missing script/slide copy or captions fail rather than pass unchecked.

The ceiling is grade 8.0 for all public copy, including captions. A score above 8 on fewer than 30 words is a warning for a person to check, not permission to use hard wording. Longer sections above 8 fail. A low score alone never means the writing is choppy or natural. The syllable count is an estimate, especially for AI, CRM, names, and tiny slides. Keep the ceiling; simplify the words and use the human checks. The checker cannot verify facts, privacy, humor, or whether a sentence sounds like Remi.
