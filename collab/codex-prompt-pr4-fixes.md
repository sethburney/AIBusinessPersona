# Prompt to paste into Codex (fixes for pull request #4)

```text
You're working in the GitHub repository sethburney/AIBusinessPersona. Update your open pull request #4 (branch codex/voice-check-review). Claude cross-reviewed it, and the owner wants these changes before merging.

1. tools/voice_check.py, check_text(): remove the "not behind" exemption. The core line ("You're not behind. You're in a great place to start.") never matches the contrast pattern, so the exemption only lets the contrast tell "That's not behind. That's building." pass. That line should fail.

2. tools/voice_check.py, parse(): the numbered-caption pattern is written r"^\\d+[.️⃣]" inside a raw string, so it looks for a literal backslash and never matches a digit. Change it to r"^\d+[.️⃣]" so caption lines like "1️⃣ Build it" and "2. Prove it" end as separate items instead of merging into one long sentence.

3. Add regression checks for both: "That's not behind. That's building." must FAIL, and a caption with a numbered list followed by a normal sentence must not merge into one sentence. Keep all existing checks passing. Keep the checker one dependency-free file.

4. STYLE-GUIDE.md, section 1: keep "CRM" for this audience. Sales and marketing leaders know the term. Explain it once if a post needs to; don't replace it with "account records" everywhere.

5. STYLE-GUIDE.md, section 3: add this rule: "Plain doesn't mean flat. Every script keeps at least one playful line in Remi's voice (a joke, a picture-in-words, or a signature line), as long as it's clear."

6. collab/voice-check-review-codex.md: change the note that calls "That's not behind. That's building." a false positive. It's a contrast tell that should be rewritten. Also note changes 4 and 5.

RULES
No em dashes. Plain American English. Don't edit any other file. Push to codex/voice-check-review so pull request #4 updates, and list the changes in a comment on the pull request.
```
