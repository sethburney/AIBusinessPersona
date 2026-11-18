# Human Voice Check: Codex review

## Recommendation

Keep the five checks and the grade-8 ceiling. Strengthen the human edit, not just the word list. Both versions contain easy words arranged into speech that sounds written. My Option B has more forced metaphors, formal disclosures, and vague process language than it should.

I reviewed every spoken script as if speaking it, including the duplicate script in each generation prompt. This is an editorial read-through, not an audio recording or either required human read-aloud. No launch copy was changed. All rewrites below are proposals for a later production edit. Update the spoken script and its duplicate prompt together if a rewrite is chosen.

## Inputs and baseline run

Option A came from `claude/ai-persona-business-education-yw0yla`. Option B came from `codex/launch-alternates`. I used the current base-branch checker before modifying it. Inputs were the six week files specified in the brief.

Command, from a workspace containing both sets:

```text
python3 tools/voice_check.py content/launch/week-1.md content/launch/week-2.md content/launch/week-3.md content/launch/alternates/week-1-codex.md content/launch/alternates/week-2-codex.md content/launch/alternates/week-3-codex.md
```

Baseline exit status: 1. All six files parsed into four pieces each. Across 24 pieces: 7 PASS, 11 WARN, 6 FAIL. These are checker results, not editorial approvals.

| Piece | A copy / caption grade | A result | B copy / caption grade | B result |
|---|---|---|---|---|
| W1-MON | 3.0 / 3.3 | PASS | 3.2 / 2.8 | WARN |
| W1-WED | 1.7 / 3.1 | PASS | 4.0 / 4.5 | WARN |
| W1-FRI | 3.3 / 2.5 | FAIL | 2.7 / 2.8 | PASS |
| W1-BRIDGE | 0.8 / 3.7 | WARN | 3.0 / 4.6 | WARN |
| W2-MON | 4.4 / 4.6 | FAIL | 4.9 / 4.4 | WARN |
| W2-WED | 4.3 / 1.6 | FAIL | 4.9 / 4.6 | PASS |
| W2-FRI | 4.1 / 4.2 | PASS | 3.3 / 3.9 | FAIL |
| W2-BRIDGE | 2.6 / 2.9 | PASS | 0.8 / 4.0 | WARN |
| W3-MON | 5.9 / 3.5 | WARN | 2.9 / 3.9 | WARN |
| W3-WED | 2.2 / 4.2 | PASS | 6.1 / 7.9 | WARN |
| W3-FRI | 5.7 / 4.2 | FAIL | 5.6 / 7.8 | WARN |
| W3-BRIDGE | 1.7 / 2.4 | FAIL | 1.3 / 3.8 | WARN |

### False positives and overbroad rules

- A W3-BRIDGE: “That's not behind. That's building.” fails twice, in script and caption. This is the approved reassurance expressed as a contrast. Keep it allowed. That does not excuse claiming viewers have built something when they have only watched.
- A W1-BRIDGE and B W2-BRIDGE/W3-BRIDGE: a low grade triggers “may read choppy.” A low score cannot establish choppiness. These short bridges may need rhythm edits, but the formula is not the evidence.
- “An AI persona” is accurate disclosure. Repetition sounds formal, so a warning is useful. The old suggestion to “skip it” is unsafe as general voice advice: keep her AI identity clear. Use “I'm AI” where it fits.
- “Sorted” in B W2-FRI really does sound British in “Looked sorted!” Keep that editorial finding. But a rule that fails “sorted the list” or “a brilliant idea” rejects ordinary American English. Move ambiguous idioms to warnings.
- A full-form phrase such as “Do not send it yet” can be deliberate emphasis. Keep contractions as a context warning, not an automatic rewrite.
- The existing “landscape” and “unlock” rules can flag literal uses such as a landscape photo or unlocking an account. They remain house-style flags in this narrow patch; a reviewer must distinguish literal meaning from hype. Do not expand this into a ban on every metaphor.

### False negatives and coverage gaps

- A W2-FRI's “Mistakes aren't the problem. Repeating them is.” escapes the contrast regex. Added that paired pattern.
- B W1-FRI's forced aside and B W2-FRI's “No shame required” pass the voice tests despite sounding canned. The latter is now caught. Forced asides remain a human edit rather than an exact-match ban on one whole sentence.
- B's “gave that decision a system,” “carry the correction forward,” and “kept the conversation” score easily but hide the action. The rewrites below name who does what.
- A's “ideal customer profile,” “centrally,” and B's “permitted, de-identified summary” need simpler words even when a whole piece scores below grade 8.
- Separate B slide-heading cells were skipped. Heading copy is public. The revised parser includes it, while excluding layout labels such as Cover and Closer.
- All carousel copy was treated as spoken, causing inappropriate contraction warnings. The revised checker reserves that warning for scripts.
- Scores were pooled across slides and never calculated for overlays. A simple slide could hide a hard one. Sections are now scored separately.
- Newlines counted as sentence endings, so wrapping one long sentence could make it look easier. Wrapping now preserves the sentence; paragraph and list boundaries still separate caption blocks.
- The declared ceiling was 8.9, not 8.0. Captions over the ceiling only warned. Both are corrected for sections with enough words to score; short sections still need human judgment.
- Curly apostrophes bypassed some phrase patterns. They are normalized before matching.
- A file without supported pieces, or a piece without script/slide text or a caption, could pass with nothing checked. These now fail visibly.
- The old output promised source locations but printed only excerpts. Flags now include the file, line, and section.

## Script read-through: Option A

These are the lines I would change for voice, clarity, or listener assumptions. “No real person would say” is an editorial test, not a claim that a phrase is impossible in conversation. Lines not listed can stay for voice, subject to the normal factual and human reviews.

| Piece | Original line or connected passage | Plain rewrite |
|---|---|---|
| W1-MON | If you've been watching everyone talk about AI and thinking, “I'm already behind”... you're not. | Keep this thought, but lead with work: “Still doing the same task every week? Let's start there. You're not behind.” |
| W1-MON | My human has spent years building real sales and marketing systems, and lately, building them with AI. | “The lessons come from work my human's team has done with AI.” |
| W1-MON | One simple idea at a time, so you can actually use it at work. | “I'll show you one idea you can try at work.” |
| W1-FRI | Here's the secret nobody tells you about AI at work: it doesn't make you efficient by itself. Systems do. | “Still explaining the same task to AI? Write down the steps so you can use them again.” |
| W1-FRI | Prove it: track one number that tells you it's actually working. | “Prove it: check that the result is right and see if it saves time.” |
| W1-FRI | Over the next few weeks we'll do this with messy CRM data, outreach and more, using what really happened when my human's team tried it. | “We'll start with messy account records and follow-up. I'll share what helped my human's team and what went wrong.” |
| W1-FRI | You don't need to do all of it. Just the next step. | “Start by writing down the first step of one task.” Keep the signature sign-off after it. |
| W1-BRIDGE | Next week: messy CRM data. | “Next week, we'll tackle messy account records.” The rest of this bridge sounds natural; its low grade alone is not a problem. |
| W2-MON | Every month-end, somebody finds a deal entered wrong. No product. Wrong price. Missing term. | “The report's due, and the deal details are wrong again. Maybe a price is wrong or a detail is missing.” |
| W2-MON | They built a report that rebuilds itself from the CRM every morning and flags bad data on every deal, pointing to the exact record to fix. | “Their report updates from the team's account records. It flags missing or wrong details and shows which record needs fixing.” |
| W2-MON | The magic isn't the report. It's that people fix the problem where it starts. | “People fix the original record. The next update uses the corrected details.” |
| W2-MON | Do that every week, and your data actually gets cleaner instead of getting patched every month. | “That helped my human's team stop patching the same errors.” |
| W2-MON | In our experience, month-end cleanup dropped by roughly half or more. | “My human's team estimated that cleanup took roughly half as long or less.” Keep the estimate framing; do not make it a promise. |
| W2-FRI | The lesson became a permanent rule: change the process that builds the report, never just the report. | “Here's the rule now: put the checks in the steps that build the report.” |
| W2-FRI | Mistakes aren't the problem. Repeating them is. Write the rule down once, and you won't make it twice. | “That can happen. Write down the fix so it's easier to catch next time.” The original ending also promises too much. |
| W2-BRIDGE | If your CRM made you wince this week, good news: wincing means you noticed. That's step one. | “Noticed a problem in your account records? That's a place to start.” |
| W2-BRIDGE | Next week: outreach. How to stop deciding who to call every morning, and start actually calling. | “Next week, we'll make it easier to choose who to call. Write down what makes an account a good fit.” |
| W3-MON | Your reps have hundreds of accounts in the CRM, and every morning they spend time deciding who to call instead of calling. | “Does your team spend the morning choosing who to call? A short list can help.” |
| W3-MON | Decide the “who” once, centrally. AI scored every account against the ideal customer profile. | “The team wrote down what makes an account a good fit. AI used that to sort the list.” |
| W3-MON | Reps spend their time on the “how,” not the “who.” | “Reps can spend more time getting ready for the call.” |
| W3-MON | In our experience, the time spent deciding who to contact dropped dramatically, and more effort landed on the best-fit accounts. | “My human's team spent less time choosing who to call. More of their effort went to accounts that fit.” |
| W3-MON | Try it this week: write down what your best customers have in common, and ask AI to score your list against it. | “Start by writing down what makes an account a good fit.” |
| W3-FRI | A handful of reps. One manager. And every Monday, a mountain of reports. | “Got a pile of reports to read before you can help your team?” Also removes team-size framing. |
| W3-FRI | Every Monday morning it reads their notes and activity, keeps a running profile, and tells the manager the one thing that would help each rep most this week. | “It reads the rep's notes and activity. It keeps notes from earlier reviews and suggests where the manager could help.” |
| W3-FRI | Here's the important part. By design, it observes and reports only. | “It only reads and reports what it finds.” Keep the concrete no-messages/no-edits limits after this. |
| W3-FRI | AI does the reading. The human keeps the relationship. | “AI reads the notes. The manager talks with the rep.” |
| W3-FRI | That's not replacing managers. That's giving them their Mondays back. | “Start by asking AI to draft a short summary from notes you're allowed to share.” |
| W3-BRIDGE | You've got your stage, a clean-data checklist, and a focus list. That's not behind. That's building. | “We've covered a task to try, a data check, and a short account list. Pick one to try this week.” Don't assume completion. |
| W3-BRIDGE | Next up: leads that actually convert. See you Monday. | “Next, we'll look at which leads are worth a closer look.” This avoids implying a promised result. |

W1-MON's greeting, A W1-BRIDGE's coffee joke, and the signature lines can stay. The bridge copy is allowed to be brief. WED slots are carousels, not missing spoken scripts; see the separate public-copy notes below.

## Script read-through: Option B, my own work

| Piece | Original line or connected passage | Plain rewrite |
|---|---|---|
| W1-MON | My human brings the real work experience and checks everything I share. | “My human shares what their team learned and checks every post.” |
| W1-MON | Here, we turn those little work headaches into simple AI skills. | “I'll show you how AI can help with those tasks.” |
| W1-MON | We'll show what helped my human's team, what flopped, and the rule that came out of the mess. The robot stuff comes with a reality check. | “I'll show you what helped my human's team and what went wrong. My human checks the advice.” |
| W1-MON | You don't need a shiny new tool collection. | Cut it. It introduces a problem the opening didn't raise. |
| W1-MON | Write down one task you're tired of repeating. That's our starting line. | “Write down one task you're tired of repeating.” End on the action. |
| W1-FRI | Made a clever AI process, but everyone still needs you to explain it? | “Built something with AI, but your team still needs you to explain each step?” |
| W1-FRI | That process needs instructions. Preferably ones that aren't living in your head. | “Write down the steps so someone else can follow them.” |
| W1-FRI | Here's the loop behind the lessons from my human's team. | “Here's how we'll work through the lessons from my human's team.” |
| W1-FRI | Hand it off: write down who runs it, what they check, and when a person decides. | “Hand it off: name who does the task and what they check. Say what needs approval.” |
| W1-FRI | Your small start? Write the first step of one repeating task. | “Write the first step of a task you do often.” |
| W1-BRIDGE | Same report, same little doubt about the numbers? | “Still double-checking the same report?” |
| W1-BRIDGE | We've met Ask, Build, Delegate. Next: messy data. | “We covered asking AI for help and saving the steps. Next, we'll look at messy account records.” |
| W2-MON | Fixed that missing field already? And now it's back? | “Filled in that blank already? Why is it blank again?” The missing value, not the missing field, is the problem. |
| W2-MON | Apparently, that error booked a return ticket. | Cut it. “The error came back” is already clear from the hook. |
| W2-MON | I'm Remi, an AI persona. | “I'm Remi. Yes, I'm AI.” Same fix for B W3-MON and the formal disclosure repeated in captions. |
| W2-MON | Their report rebuilt itself from the CRM, the system holding their account and deal records. | “Their report updated from the system where the team keeps account and deal records.” |
| W2-MON | Patching the report left the original problem waiting underneath. | “Changing the report didn't fix the original record.” |
| W2-MON | Fixing the source meant the next refresh could carry the correction forward. | “Once they fixed the original record, the next report used the right details.” |
| W2-MON | Less patching. Better starting data. | Cut it. The previous line already explains the benefit. |
| W2-FRI | They added data checks straight into a published report. Looked sorted! | “They added checks right in the finished report. It looked fixed!” |
| W2-FRI | The rule became: change the process that builds the report, never just the report. | “Here's the rule now: put the checks in the steps that build the report.” |
| W2-FRI | A mistake can give you a useful rule. No shame required. | “That can happen. Here's what to check next.” |
| W2-FRI | Your next step: write down where one recurring report gets rebuilt. | “Find the steps that update a report you use often.” |
| W2-BRIDGE | Still spotting the same data mess? You've found a starting point. | “Seeing the same error again? Start there.” |
| W2-BRIDGE | Fix the source. Keep the check. | “Fix the original record and keep checking for that error.” |
| W2-BRIDGE | Next: outreach with a focus list. | “Next, we'll make a short list of accounts to contact.” |
| W3-MON | So many options. Still no next call. | “You've got plenty of accounts, but it's hard to choose.” |
| W3-MON | My human's team gave that decision a system. | “My human's team wrote down how to choose.” |
| W3-MON | AI ranked accounts against a written description of a good fit. | “The team wrote down what makes an account a good fit. AI used that to sort the list.” |
| W3-MON | The team could spend less time deciding where to start and more time working the list. | “The team spent less time choosing who to contact.” |
| W3-MON | AI helped sort. People still checked the choices. | “AI sorted the accounts, and people checked the list.” |
| W3-FRI | Here's a useful boundary from my human's team. | “Here's what my human's team let the assistant do.” |
| W3-FRI | Their rep assistants read activity and notes, kept a running profile, and briefed the manager on what might help. | “The assistants read each rep's notes and activity. They kept notes from earlier reviews and suggested where the manager could help.” |
| W3-FRI | Think helpful reading buddy, with the send button off. | “The assistant could read and report. It couldn't send messages.” Avoid implying a literal product setting. |
| W3-FRI | The manager checked the brief and kept the conversation. | “The manager checked the summary and talked with the rep.” |
| W3-FRI | That's the job: help a person prepare. | Cut it. The previous line now makes the job clear. |
| W3-FRI | Try asking AI for a draft summary of one rep's activity, with permission and identifying details removed. | “Get permission to use the notes, then remove names and private details. Ask AI for a short summary.” |
| W3-BRIDGE | A repeating task. A data check. A focus list. Those are starting points. | “You could start with a task you repeat, a data check, or an account list.” |
| W3-BRIDGE | Next: making sense of leads. | “Next, we'll look at which leads are worth a closer look.” |

B's “Saved the posts, haven't tried them? That's okay” and “You're not behind. Choose one idea to try” can stay. The full script needs fewer fragments between those lines. Keep the existing clear statements that AI doesn't message people, edit records, or act on its own.

## Other public-copy fixes

These extend the review to slides, overlays, and captions; they are not extra scripts.

| Where | Original | Plain rewrite |
|---|---|---|
| A W1-WED cover/caption | Most people use AI at stage 1. / Most people stop at stage 1. | “Still asking AI to do the same task from scratch?” Avoid ranking the audience. |
| A W1-WED slide 5 | Where the payoff lives | “Save the steps you use again.” |
| A W2-WED cover | Your CRM isn't messy because your team is lazy. It's messy because nobody wrote down what “clean” means. | “Does everyone agree on what a complete account record needs?” Also avoids claiming one cause. |
| A W2-WED slide 6 | A few minutes every Monday beats a cleanup weekend every quarter. | “Check for missing details each week.” Don't imply a measured tradeoff. |
| A W3-WED cover | The anatomy of a multi-touch cadence. | “A simple plan for follow-up.” |
| A W3-WED slides | Focus list first. / Give every touch a job. / Set exit rules. / Grade the week. | “Choose who to contact.” / “Give each message a purpose.” / “Decide when to stop.” / “Check who got contacted.” |
| B W1-WED slide 2 | This is an illustration, not a new result from my human's team. | “Here's an example using a weekly report.” Keep the example label without production commentary. |
| B W1-WED slide 7 | Add this to the end of a task you've already checked: Write down the steps we used, including my corrections, so I can reuse them. | “After you check the work, ask: Write down the steps we used. Include my corrections so I can use them again.” |
| B W2-WED heading | Define done | “Agree on what's needed.” |
| B W2-WED slide 7 | Review recurring flags regularly. | “Check the errors that keep showing up.” |
| B W3-WED slide 4 | Illustrative rewrite: Instead of Just checking in, try Is [the priority they shared] still something you'd like help with? | “Example: Is [the problem you mentioned] still something you'd like help with?” |
| B W3-WED slide 5 | Suggested check: choose channels appropriate to the relationship and permission, rather than copying one message everywhere. | “Try this: use a way of contacting them that fits the relationship and what they've agreed to.” |
| B W3-WED slide 6 | Don't invent familiarity, a problem, or proof. | “Don't pretend you know them or make up facts.” |
| B W3-WED slide 8 | Focus accounts got a logged touch. | “The team recorded which accounts they contacted.” |
| B W3-WED caption | The playbook supports a focus list, mixed-channel outreach, drafts, and an activity review. The message and stop checks here are suggestions to try, not measured results from my human's team. | “My human's team used account lists, draft messages, and a weekly check. The message tips here are ideas to try.” Keep the source distinction. |
| B W3-FRI overlay | Try one permitted, de-identified summary. | “Get permission. Remove private details. Try one summary.” |
| B W3-FRI caption | With permission and identifying details removed, ask AI to draft a summary of one rep's activity. | “Get permission to use the notes. Remove names and private details. Then ask AI for a short summary.” |
| B recurring caption disclosure | I'm Remi, openly AI. | “I'm Remi. Yes, I'm AI.” It is fine to repeat a clear disclosure; vary the rest of the caption. |

## Changes and validation

The style guide keeps the five checks in the same order and preserves all signature lines. It adds direct actor/action wording, simpler job terms, natural breaths, fewer forced metaphors and canned asides, one next step, and context for American idioms and contractions. It makes clear which judgments the checker cannot make.

The Python file stays dependency-free. Changes: strict 8.0 threshold; long captions fail above it; short sections warn above it; remove low-score choppiness warnings; normalize apostrophes; catch the missed mistake/repetition contrast and “No shame required”; preserve the approved not-behind reassurance; add analyze/optimize spelling variants; downgrade ambiguous British idioms to warnings; keep disclosure explicit in warning advice; include separate slide headings; use spoken-only contraction warnings; score slides and overlays separately; preserve wrapped sentences; handle caption paragraphs/lists; print source locations; fail visibly on unreadable/unsupported/missing-copy inputs.

The revised run on the unchanged six files still exits 1, as it should. It newly catches A W2-FRI's contrast, A W3-MON's sentences over 20 words, B W1-WED's 25-word instruction, and B W2-FRI's canned reassurance. A W3-BRIDGE's approved reassurance no longer fails. Short-copy grade warnings now surface A W2-WED slide 6 (8.7), A W3-WED cover (9.1), and B W3-WED slide 5 (9.3), which were hidden by pooled scores. These need human attention; short-sample estimates are not exact grade assessments.

Focused Python regression checks passed for: straight/curly signature lines; curly contrast detection; actual British spellings versus American spelling and the noun “analyses”; American senses of sorted/brilliant; deliberate contraction warnings only in spoken copy; 20/21-word boundary; wrapped and quoted sentences; multi-digit week IDs; slide-heading inclusion; no duplicate production-prompt scanning; all six files yielding 24 pieces; unreadable files; unsupported headings; and missing captions. All checks ran with the standard library. Scratch checks are not additional repository files.

Limitations: syllable estimates are approximate, especially for abbreviations. The parser supports these launch Markdown formats, not arbitrary Markdown. Phrase regexes cannot judge facts, privacy, tone, or every stock contrast. Human checks must still catch the awkward lines listed above. No owner or wife sign-off is implied.
