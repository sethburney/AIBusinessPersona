# Claude + Codex Collaboration

Two AI collaborators write competing versions of each post. The owner picks.

| Role | Who | Writes to |
|---|---|---|
| **Option A** (first draft) | Claude | `content/launch/week-N.md` (generated from `content/launch/_source/launch_content.py`) |
| **Option B** (alternate) | Codex | `content/launch/alternates/week-N-codex.md` |
| **Decision** | Owner | `content/launch/picks.md`, each week |

## Rules for both collaborators

- Read `GUARDRAILS.md` and `content/messaging-framework.md` before writing anything. They are binding.
- Never edit the other collaborator's files. Suggest changes in your own file or in a pull request comment.
- Every option must be production-ready in the same format (see the week files): script, on-screen text, performance notes, Higgsfield prompt, and caption for videos; slide-by-slide copy and caption for carousels.
- Work on a separate branch and open a pull request into `claude/ai-persona-business-education-yw0yla`. The owner merges.

## Briefs

| Brief | For | Status |
|---|---|---|
| [`codex-brief-launch-alternates.md`](codex-brief-launch-alternates.md) | Codex: alternates for weeks 1–3 | Open |
