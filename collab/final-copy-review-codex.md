# Final launch copy: Codex cross-review

## Result

Check 3 review: **4 Ready, 8 Change**. Keep the approved picks. The changes below are narrow edits within those picks, not a request to choose A or B again.

I read all nine spoken scripts as if speaking them, all 26 slides, every on-screen line, and every caption. This was an editorial read-through, not either required human read-aloud. Ready means ready for those human checks, not cleared to publish.

Read first: STYLE-GUIDE.md, GUARDRAILS.md including section 7, picks.md, and all three final week files. I also checked the earlier alternates, launch README, and playbook Lessons 6, 7, 8, and 11 for the claims discussed below. Only this review file is added.

## Automatic and prompt checks

Ran the requested command against the fetched base-branch files:

```text
python3 tools/voice_check.py content/launch/week-1.md content/launch/week-2.md content/launch/week-3.md
```

Exit status **0**. No FAIL results. One WARN: W3-MON caption, “sorted” in “AI sorted the list.” This is normal American usage and can stay. All other checked sections pass. Script grades range from 0.9 to 3.8. The highest section score is 5.2. Easy scores don't settle the factual or voice issues below.

All **nine of nine** Higgsfield prompt scripts match the spoken scripts exactly after removing Markdown quote markers and blank separator lines. Words, punctuation, capitalization, and line order match. All nine prompts also include the explicit reminder that Remi is an AI character and the script is not a statement by the real person whose likeness she uses. No mismatch needs fixing in the current files. After accepted edits, regenerate and repeat this comparison.

## Shared rules

- No company, industry, market, customers, owner job title, team size, private project dates, precise results, or real data appear in the public copy I reviewed. Week labels and teaching-step counts describe this content, not the employer's history.
- Keep CRM. It fits this audience. No British wording needs a change.
- All nine scripts have a playful picture, joke, or allowed signature line. Keep the coffee line, round-trip ticket, “Poof,” scrolling hook, reading buddy, and reassurance. Do not flatten the scripts to improve a score.
- Remi says “I'm AI” or “your AI work bestie” in seven scripts. W2-BRIDGE and W3-BRIDGE rely on the visible AI disclosure required by the launch workflow. Carousel images also need that label. A prompt's private KEEP instruction does not replace a public disclosure. Retain the platform AI label on every post; this review does not verify the live publishing settings.
- The individual readiness calls below assume that standing disclosure workflow. No script claims the real likeness subject's life, job, or views. All nine prompts explicitly separate the character's speech from that person.
- Treat tutorial steps and permission/privacy prerequisites as parts of one exercise. Two unrelated closing assignments are different; W2-FRI and W2-BRIDGE need the changes below.
- Add @remitobor to the three last slides, as the existing launch README requires. This is a production detail, not a new action for viewers.
- Facts requiring changes: an absolute guarantee about AI, an unsupported every-list review claim, and an overstated Monday payoff. The cleanup estimate in W2-MON is supported and already softened.

## W1-MON: Ready

**Keep:** The familiar-task hook, quick AI disclosure, and “Some work. Some flop.” feel warm and direct. Keep the approved blend.

**Exact current text to keep:** “You're not behind. Start small: pick one task to make easier today.”

**Proposed text:** Unchanged. This slot is ready as written.

**Rules and voice:** The task choice and request to name it form one response, not competing tasks. “Let's level up together” supplies the signature/playful beat. No identifying employer details or unsupported results.

**Prompt check:** Exact match in the current file. Keep both script copies unchanged.

## W1-WED: Change

**Keep:** Keep the three-stage structure, the checks slide, and “AI drafts. A human decides.” The comment-your-stage CTA is clear.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Slide 1 (content/launch/week-1.md:93) | Still starting AI from scratch every time? | Still explaining the same task to AI? | People start a task or explanation from scratch, not AI itself. |
| Slide 3 (content/launch/week-1.md:95) | You save the steps, a template, and your fixes. AI runs the task the same way every time. | You save the steps, a template, and your fixes. Next time, give AI those steps and check its work. | Saved instructions help consistency but don't guarantee identical execution. |
| Slide 9 (content/launch/week-1.md:101) | You're not behind. Start small. | You're not behind. Start small. @remitobor | The launch README requires the handle on the last slide. Keep the existing comment CTA after this line. |
**Rules and voice:** No invented results or identifying details. The caption's experience-based statement reflects the playbook's Ask/Build/Delegate arc. The four-step teaching example is a method, not private project counts. Carousel: no spoken-script playfulness or prompt comparison applies.

**Prompt check:** Not applicable: carousel.

## W1-FRI: Ready

**Keep:** Keep “Let's get those steps out of your head and onto the page” and the robot sign-off. The framework is simple without going flat.

**Exact current text to keep:** “Start by writing the first step of one task you do often.”

**Proposed text:** Unchanged. This slot is ready as written.

**Rules and voice:** One CTA across script, overlay, and caption. “Your AI work bestie” identifies Remi as AI; the steps retain human checks. No invented implementation result or identifying detail.

**Prompt check:** Exact match in the current file. Keep both script copies unchanged.

## W1-BRIDGE: Ready

**Keep:** Keep the coffee/checklist line. It is a clear character joke, not a claim that Remi drinks coffee. The recap and next-week preview flow naturally.

**Exact current text to keep:** “Pick that report. Bring your coffee. I'll bring the checklist.”

**Proposed text:** Unchanged. This slot is ready as written.

**Rules and voice:** The practical action is choosing a report. Coffee is a playful invitation, not another work assignment. “Your AI work bestie” is explicit. No assumption that viewers completed the week's work.

**Prompt check:** Exact match in the current file. Keep both script copies unchanged.

## W2-MON: Ready

**Keep:** Keep the round-trip-ticket joke. It is easy to picture and gives Remi personality. The original-record explanation is clear.

**Exact current text to keep:** “In our experience, cleanup took about half as long, sometimes less.”

**Proposed text:** Unchanged. This slot is ready as written.

**Rules and voice:** This is a soft, experience-qualified estimate consistent with Lesson 11, not an audited or promised result. Keep it. One CTA: ask AI for one recurring-blank check. “Your AI work bestie” identifies Remi. No identifying details. The generalized recurring-error incident stays within the permitted lesson.

**Prompt check:** Exact match in the current file. Keep both script copies unchanged.

## W2-WED: Change

**Keep:** Keep the agreed-definition cover, one shared rulebook, original-record fix, and human approval at the end of the prompt. The five-rule format is easy to follow.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Slide 4 (content/launch/week-2.md:99) | Have a report flag missing or wrong fields every day. AI flags the gap. It never makes up the missing detail. | Have a report flag missing or wrong fields every day. Tell AI to flag gaps, not fill them in. Check the results. | “It never” falsely guarantees AI behavior. Make this a rule and retain human review. |
| Slide 8 (content/launch/week-2.md:103) | You're not behind. Start small. | You're not behind. Start small. @remitobor | Restore the required last-slide handle. Keep the existing write-one-rule CTA. |
**Rules and voice:** One final action: write one clean-record rule; the prompt is supporting material, not an additional save/comment demand. No private counts or identifying facts. The rule count describes the post, not the team. Carousel: spoken playfulness and prompt-script matching do not apply.

**Prompt check:** Not applicable: carousel.

## W2-FRI: Change

**Keep:** Keep “Looked great!” and “Poof.” This is a good short Oops story with the correct failure: checks added to the finished report disappeared.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Spoken script and duplicate prompt (content/launch/week-2.md:138) | That kind of mistake happens. Write down the fix so it's easier to catch next time. | That kind of mistake happens. The rule gives you something to check next time. | “Write down the fix” is a second assignment before “find the steps.” Make this an observation so the final action stays singular. |
**Rules and voice:** Keep the final find-the-update-steps CTA and caption unchanged. Lesson 11 and Rules we learned the hard way support the incident. No identifying detail, new figure, or human-life claim. “I'm AI” is explicit.

**Prompt check:** Exact match in the current file. Apply accepted spoken changes to the generated prompt script too.

## W2-BRIDGE: Change

**Keep:** Keep the approved wince joke and the good-fit preparation step. It connects the weeks without shaming anyone.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Spoken script and duplicate prompt (content/launch/week-2.md:206) | Fix the original record, and keep checking for that error. | This week, we saw why the original record matters. | The original is another direct assignment before the good-fit action. Make it a recap so the final action stays singular. |
**Rules and voice:** One next step after the rewrite: write down what makes an account a good fit. The joke stays. No identifying details or unsupported result. This bridge does not say Remi is AI in its script/caption; retain the required visible platform AI label. See the shared disclosure note.

**Prompt check:** Exact match in the current file. Apply accepted spoken changes to the generated prompt script too.

## W3-MON: Change

**Keep:** Keep the scrolling opener and the short-list punchline. Keep CRM. “Sorted” in the caption is ordinary American English and needs no rewrite.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Spoken script and duplicate prompt (content/launch/week-3.md:30) | AI used that to sort the list. People checked it. | AI used that to sort the list. | Lesson 6 documents ranking and focus lists, but doesn't establish that the team checked each output. Don't present our recommended review as a documented event. |
| Caption (content/launch/week-3.md:83) | People checked every list. | Each rep had a place to start. | “Every” adds an unsupported universal claim. Keep the supported benefit without adding an event or another task. |
**Rules and voice:** Keep the single CTA about defining good fit. Human review is sensible advice, but the playbook does not confirm this specific historical claim. If the owner later confirms it, the historical sentence can stay. The proposed wording can be used without that confirmation. The soft time-saving result is supported by Lesson 6. No company, team-size, or private market details. “Your AI work bestie” is clear.

**Prompt check:** Exact match in the current file. Apply accepted spoken changes to the generated prompt script too.

## W3-WED: Change

**Keep:** Keep “Give that message a job,” the concrete example question, and the caption's distinction between the team's work and ideas to try. The stop rules are good advice and aren't presented as measured results.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Slide 9 (content/launch/week-3.md:107) | You're not behind. Start small. | You're not behind. Start small. @remitobor | Restore the launch README's required last-slide handle. Keep the existing rewrite-one-follow-up action. |
**Rules and voice:** Otherwise ready as written. Lesson 6 supports the focus list, channel mix, and weekly activity check. The example question is labeled “Try” with a placeholder, not a fabricated quote from a real customer. No identifying details. One final CTA, with the other steps teaching the method. Carousel: spoken playfulness and script/prompt matching do not apply.

**Prompt check:** Not applicable: carousel.

## W3-FRI: Change

**Keep:** Keep the report-pile hook, “reading buddy, with the send button off,” and the firm read/report-only boundary. The metaphor is backed by concrete limits, so it doesn't imply a particular product switch.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Spoken script and duplicate prompt (content/launch/week-3.md:144) | And managers got their Mondays back. | My human's team spent much less time on the weekly review. | The playbook supports a large reduction in review time, not getting an entire Monday back. Use a soft claim tied to the documented task. |
| On-screen text, 24–29 s (content/launch/week-3.md:155) | Managers get their Mondays back | Less time on the weekly review | Match the narrower supported payoff. |
| Spoken script and duplicate prompt (content/launch/week-3.md:146) | Try it: get permission, remove names, and ask AI to summarize one week of notes. | Try it: get permission, remove private details, and ask AI to summarize a week's notes. | Names alone do not cover identifying details in notes. Keep this as prerequisites for one summary exercise. |
| On-screen text, 29–end (content/launch/week-3.md:156) | Get permission. Remove names. Try one summary. | Get permission. Remove private details. Try one summary. | Match the safer script wording. |
| Caption (content/launch/week-3.md:194) | Get permission, remove names, and try one AI summary of a week's notes. | Get permission, remove private details, and try one AI summary of a week's notes. | Keep the same single exercise across formats. |
**Rules and voice:** Lesson 7 supports assistants per rep, the weekly read/report rhythm, and the human relationship. The proposed payoff stays directional. “Your AI work bestie” is clear. No identifying employer details; the privacy rewrite strengthens the viewer exercise.

**Prompt check:** Exact match in the current file. Apply accepted spoken changes to the generated prompt script too.

## W3-BRIDGE: Change

**Keep:** Keep the welcoming saved-but-not-tried opening, the choice of starting points, and “You're not behind.” It welcomes beginners without assuming results.

| Location | Exact current text | Proposed text | Why |
|---|---|---|---|
| Spoken script and duplicate prompt (content/launch/week-3.md:214) | Next week, we'll look at which leads are worth a closer look. | Next week: leads worth your time. | Remove the repeated look/closer look phrasing and trim a bridge currently listed at 21 seconds. |
| On-screen text, 10–15 s (content/launch/week-3.md:224) | Next: leads worth a closer look | Next: leads worth your time | Keep the preview aligned with the spoken wording. |
| Caption (content/launch/week-3.md:256) | Next week: which leads are worth a closer look. | Next week: leads worth your time. | Keep the preview consistent. |
**Rules and voice:** The current script is 53 words, about 21 seconds at 150 words per minute. This edit removes six words, giving about 19 seconds before delivery pauses. One CTA: choose an idea to try. The reassurance supplies the allowed signature-line beat. No invented audience wins or future conversion promise. Retain the platform AI label because this bridge doesn't state the AI identity in script/caption.

**Prompt check:** Exact match in the current file. Apply accepted spoken changes to the generated prompt script too.

## Handoff

Claude should apply accepted edits in the source and regenerate the week files and preview. Then rerun the voice checker and the nine script comparisons. Keep the approved slot choices. The owner and wife's read-alouds remain the next checks; no sign-off on their behalf is implied.
