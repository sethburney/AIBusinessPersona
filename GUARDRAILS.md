# Guardrails

These rules protect the persona's credibility and the owner's reputation. Settle them before building the story and the face.

## 1. AI disclosure

An AI persona with a human-looking face and a backstory can be read as a real person. If followers later find out it is AI, the loss of trust can undo the whole project, especially for an account whose topic *is* AI.

**Decision needed:** how will the persona disclose that it is AI?

| Option | Description | Tradeoff |
|---|---|---|
| Fully transparent | Bio and profile say plainly it is an AI persona, and who runs it | Most trustworthy; some reach may be lost to people who prefer "real" voices |
| Transparent character | Openly AI, but with a consistent personality and fictional story told as fiction | Keeps the storytelling while staying honest |
| Undisclosed | Presented as a real human | High risk: platform rule violations, possible legal exposure, reputational damage if exposed. **Not recommended.** |

**Chosen approach:** _TBD_

## 2. Platform rules (to verify)

Major platforms have policies on AI-generated images, video, and synthetic people, and these change often. Before launch, check the current rules for each platform we use and record the date checked.

| Platform | Policy link / summary | Date checked |
|---|---|---|
| _TBD_ | | |

## 3. Backstory honesty

- The backstory must not claim real-world credentials the persona does not have (for example, a fake degree, a real employer, or client results that did not happen).
- Any "experience" in the story is fiction and should be framed that way, or written so it cannot be mistaken for a real résumé.
- The persona must not impersonate, resemble, or imply endorsement by a real person or company.

## 4. Content accuracy

- Every claim about an AI tool's features, pricing, or limits is checked against the vendor's current documentation before posting, with the date checked.
- No invented statistics, studies, quotes, or case studies. Every number has a source.
- When something is an opinion or a guess, the post says so.
- Tool features change quickly. Evergreen posts get a review date.
- Impact figures from the owner's playbook are directional estimates, not audited results. Keep them as ranges with "roughly" or "in our experience," and never turn them into promises.
- Posts about the owner's work projects stay company-neutral and need the owner's comfort (and, if required, the employer's permission) before sharing.

## 4b. Human voice

Every public word passes the Human Voice Check in `STYLE-GUIDE.md`: plain American English at a grade 8 reading level or easier, no AI tells, an automatic score, cross-review by the other AI, and read-aloud by the owner and the owner's wife.

## 5. Sponsorships and affiliate links

If the persona ever promotes a product for pay or commission, the post must disclose it clearly, following the platform's rules and applicable advertising law. _Details TBD if this becomes relevant._

## 6. Face and likeness

- The persona's face must be generated or created, not based on a real, identifiable person without their written consent.
- Reference photos of real people may guide **style only** (lighting, hair style, wardrobe, mood), unless that person has consented to their likeness being used.
- **Current status:** Remi's face is modeled on the owner's wife, who has given consent. Recommended: put that consent in writing (what it covers, which platforms, whether it covers paid brand deals, and what happens if she later wants it withdrawn). Keep that record private, outside this repository.
- Do not commit photos of real people to this repository. Never use images of children as references or in persona content.
- Keep a record of how the face was made (tool, date, prompts) in `persona/05-visual-identity.md`.
- Consent scope is tracked in `persona/07-likeness-consent.md`. Uploading her photos to a new AI tool, building a saved avatar, generating her voice, and paid endorsements each need her confirmation first.

## 7. Protecting the owner's identity and employer

The owner's ideas, what was built, and what was learned can be shared. Anything that could identify the company, the owner, or the owner's employer cannot.

- **Never include:** company name, industry, business model, market, products, customers, locations; the owner's job title, team size, or org structure; exact counts and precise figures; project dates or timelines; distinctive incidents in identifying detail; real dashboards, CRM screens, documents, or data; the full tool stack in combination.
- **Instead:** "my human's team," tool categories, soft language or broad ranges, the lesson and the rule with details blurred, and clearly fake mock data.
- **When in doubt, generalize one more level.** The full do/don't table is in `content/launch/README.md`.

**Identity risks outside the content (owner's decision):**

- **This GitHub repository is public.** It shows the owner's GitHub username, the commit email address, the owner's playbook, and the likeness files. Anyone who connects Remi to this repository could identify the owner and, from the playbook, possibly the employer. **Recommended: make the repository private** (Settings → General → Danger Zone → Change visibility). Git history keeps old files even after they're deleted, so making it private is the real fix.
- **Remi's face is the owner's wife.** People who know her may recognize her, and through her, the owner. This can't be fully removed while the likeness is used; it's worth weighing against the anonymity goal.
- **Account details:** register Remi's accounts with a business email and name rather than personal ones where the platforms allow it.
