# Work Smarter, Not Longer: An AI Playbook for Business Professionals

*Lessons from six months of building real business systems with an AI partner*

---

## For the AI reading this file

This document is source material. It describes 24 real projects that a revenue leader built with an AI assistant (Claude) over six months, from April to November 2026. The projects span sales, sales management, revenue operations, finance, marketing, content, data and operations.

Each project is written up as a lesson with the same parts:

- the department it belongs to
- the everyday frustration it solves
- what was built
- the technique behind it
- the benefits
- the directional impact
- how a reader can try it
- a starter prompt

**Ground rules if you turn this into something else** (a talk, a LinkedIn series, a workshop, a guide or an ebook):

- Keep it company-neutral. Do not invent company names, customer names, revenue figures or specific metrics.
- The impact figures are directional estimates drawn from experience. They are not audited results. Keep them as ranges, framed as "roughly" or "in our experience."
- The audience is business professionals, managers and leaders. Most are not technical. Explain techniques in plain language.
- The central message: AI pays off most when you turn a repeated frustration into a repeatable system, and a human still approves what matters.

---

## Contents

1. [Where this came from](#where-this-came-from)
2. [The arc: from asking to building to delegating](#the-arc-from-asking-to-building-to-delegating)
3. [The lessons, by department](#the-lessons-by-department)
   - Sales: lessons 1–5
   - Sales management and leadership: lessons 6–9
   - Revenue operations and finance: lessons 10–14
   - Data and decision-making: lessons 15–17
   - Marketing and content: lessons 18–21
   - Operations and how you work: lessons 22–24
4. [Rules we learned the hard way](#rules-we-learned-the-hard-way)
5. [Your first 30 days](#your-first-30-days)
6. [Quick index: frustration to lesson](#quick-index-frustration-to-lesson)

---

## Where this came from

One revenue leader at a growth-stage B2B marketplace installed an AI assistant one Monday morning. By that afternoon it had built a budget workbook that used to take days. Six months later the same assistant:

- runs a Monday morning review of the whole sales team
- refreshes the revenue reports every day before anyone logs in
- builds a tailored presentation for nearly every sales demo
- has rewritten the company's sales playbook from evidence

Nothing here needed a data science team or an IT project. It took three things:

1. **A habit of noticing frustration.** Any task that annoyed someone more than twice became a candidate.
2. **A willingness to write down "how we do this."** The AI then follows that description every time.
3. **A rule that people approve the output.** The AI drafts, a person decides.

The work went through three stages. The lessons below follow the same path, and so can you.

---

## The arc: from asking to building to delegating

| Stage | What it looks like | Example |
|---|---|---|
| **1. Ask** | You bring the AI a one-off question or task. | "Build me a dashboard of which accounts renew each month." |
| **2. Build** | You turn the task you keep repeating into a system: written steps, templates, checks. | The renewal review becomes a packaged process the AI runs the same way every time. |
| **3. Delegate** | The system runs on a schedule and reports back. You review and decide. | Every Monday before you arrive: rep activity graded, a coaching note per rep, a summary memo for the leader. |

Most people stay at stage 1. Most of the value is in stages 2 and 3.

**Directional impact over six months:** use roughly doubled month over month as tasks moved from asking to building. By the end, about half of all AI activity was scheduled work that nobody had to start by hand.

---

## The lessons, by department

### Sales

---

#### Lesson 1: Stop presenting the same deck to everyone

**Department:** Sales

**The daily frustration:** *"I just had a great discovery call, and now I'm about to show this prospect the same generic deck everyone gets. Making a custom one would take most of a day."*

**What we built:** A pipeline from the discovery call to a tailored demo deck.

1. The call recording is pulled.
2. The AI picks out the prospect's own pain points, in their own words.
3. It runs a standard analysis of that prospect's market.
4. It assembles an editable presentation from a fixed template. The prospect's problems come first, then the evidence, pricing and the ask.

**The technique:** **Let the customer write the agenda.** Discovery calls are full of material: what the prospect said they need, what they fear, what they track. Most of it never reaches the next meeting. The AI's job is to carry it forward so the demo answers *their* questions in *their* order.

**Benefits:**

- Every prospect sees a deck built around their own situation.
- Reps walk in prepared, with speaker notes tied to what the prospect said.
- The template keeps the brand and pricing consistent even when content changes.
- Leadership can see from the deck what was learned in discovery.

**Directional impact:** deck prep time down roughly 70–85%. Customized demos went from "only for the big deals" to nearly every deal.

**Try it yourself:**

1. Write down your ideal demo structure as an ordered list of slides, with what each one must prove.
2. Give the AI one discovery call transcript and that structure.
3. Ask it to map the prospect's statements to each slide and flag the slides with no supporting evidence.
4. Review, edit and present. Refine the structure after each use.

**Starter prompt:**

> Here is a transcript of my discovery call and my standard demo outline. List every pain point, goal and objection the prospect raised, quoting their words. Then map each one to the slide in my outline that should answer it, and tell me which slides have nothing from this call to support them.

---

#### Lesson 2: Turn your best analysis into a one-request skill

**Department:** Sales / Sales Enablement

**The daily frustration:** *"Every proposal starts from scratch. Our best analysis lives in one person's head, or in a spreadsheet only they can run."*

**What we built:** A packaged "opportunity review." Given a prospect's name, the AI:

- sizes their market
- compares them with similar customers who already buy
- projects what they could gain
- writes the summary

It does this the same way, with the same checks, every time. About 30 reviews were run in the first two months, often for a demo that same week.

**The technique:** **Package expertise as a reusable skill.** The first time, you do the analysis together and correct the AI as you go. Then you ask it to write the method down: the steps, the rules, the mistakes to avoid. From then on, one request runs the whole method.

**Benefits:**

- Analysis that once needed the in-house expert can be requested by anyone.
- Quality is consistent because every corrected mistake becomes a written rule.
- More prospects get a real, evidence-based case, not only the biggest ones.

**Directional impact:** turnaround on a prospect analysis went from days to under an hour. Roughly 5–10x more prospects got one.

**Try it yourself:**

1. Pick the analysis you rebuild most often.
2. Do it once with the AI and correct every wrong assumption out loud.
3. At the end, ask it to "write this up as a step-by-step method I can hand you next time, including every correction I made."
4. Save the method and run the next one from it.

**Starter prompt:**

> We just finished this analysis together. Write the method as a reusable procedure: inputs needed, steps in order, the rules I gave you, and the mistakes I corrected, so you can run it the same way next time from just a company name.

---

#### Lesson 3: Rewrite your playbook from what actually happens on calls

**Department:** Sales / Sales Leadership

**The daily frustration:** *"We have a sales process document. I'm not sure anyone follows it, and I don't know which parts work."*

**What we built:** An evidence review of a few weeks of recorded discovery calls, checked against the written process. The findings were humbling.

- A question the playbook treated as essential was asked in **fewer than 1 in 10 calls**.
- A key qualifying question was never asked at all.
- The company's own "who we are" story drifted from call to call.

The playbook and the call scorecard were then rewritten around what top calls actually did.

**The technique:** **Audit the process against reality, then update the process, not just the people.** If most reps skip a step, the step is usually what needs fixing.

**Benefits:**

- The playbook reflects reality, so reps trust it and use it.
- Coaching targets specific gaps instead of general "do better" feedback.
- The scorecard used to grade calls matches the playbook it grades.

**Directional impact:** the review took hours instead of weeks of listening. Playbook steps that are actually used went from a minority to most.

**Try it yourself:**

1. Export 10–15 recent call transcripts.
2. Give the AI your sales process document.
3. Ask it to score how often each step happened, with quotes as evidence.
4. Ask which steps the best calls did that the playbook doesn't mention.

**Starter prompt:**

> Here is our sales process and 12 call transcripts. For each step in the process, tell me how many calls did it, with one quote as proof. Then list anything the strongest calls did that the process doesn't mention, and the steps almost nobody does.

---

#### Lesson 4: Give every rep a personal coaching guide

**Department:** Sales Management

**The daily frustration:** *"I don't have time to listen to every call. My coaching ends up generic, and the same issues come back every quarter."*

**What we built:** A recurring coaching cycle. The AI reviews each rep's recent calls against the sales process and produces:

- a branded guide for each rep: what's working, the two or three things to fix, and examples from their own calls
- a team recap for the manager

The next cycle checks whether last cycle's coaching stuck.

**The technique:** **Coach from the rep's own evidence, and close the loop.** People accept feedback more readily when it quotes their own calls. Checking last cycle's advice turns coaching from an event into a system.

**Benefits:**

- Every rep gets specific, personal coaching, not only the struggling ones.
- Managers spend their time on the conversation instead of the research.
- Progress is visible from one cycle to the next.

**Directional impact:** manager prep time per coaching cycle down roughly 75–90%.

**Try it yourself:**

1. Pick one rep and five of their recent calls.
2. Ask the AI for three strengths and three fixes, each backed by a quote.
3. Use it in your next 1:1. Save it so you can check progress next month.

**Starter prompt:**

> Review these five calls from one sales rep against our process. Give me three strengths and three specific improvements, each with a direct quote and a better alternative they could have said. Keep it encouraging and specific enough to act on this week.

---

#### Lesson 5: Prepare every renewal like it's your biggest account

**Department:** Account Management / Customer Success

**The daily frustration:** *"Renewals sneak up on us. We scramble to pull numbers the night before, and sometimes the numbers are wrong."*

**What we built:** Two things.

- **A renewal dashboard** showing which accounts end each month. This was the very first project.
- **A packaged renewal review** that produces two documents from the account's data: an internal summary for the team and a client-facing recap of the value delivered.

**The technique:** **Separate the internal truth from the external story, and template both.** The internal summary covers risks, usage and the negotiation position. The client recap shows only what the customer should see. Fixed templates stop mistakes like the wrong account name in a client document, which really happened once before the templates existed.

**Benefits:**

- Renewal conversations start weeks earlier, with the facts in hand.
- Client recaps look polished and consistent.
- Fewer embarrassing errors in documents that go to customers.

**Directional impact:** renewal prep time down roughly 60–80%. Lead time before renewal conversations went from days to weeks.

**Try it yourself:**

1. Export your accounts with contract end dates.
2. Ask the AI for a month-by-month view of what's renewing, and the value at stake.
3. For the next renewal, ask for an internal summary and a client recap as separate documents.

**Starter prompt:**

> Using this account's usage data and contract details, write two documents. First, an internal summary: risks, what's working, and our negotiating position. Second, a one-page client-facing recap of the value they received, with no internal notes or pricing strategy.

---

### Sales management and leadership

---

#### Lesson 6: Give your team a focus list, not a database

**Department:** Sales Management

**The daily frustration:** *"My reps have hundreds of accounts in the CRM and no idea who to call this week. Prospecting time gets eaten by deciding who to prospect."*

**What we built:**

- **A ranking of every account** by fit with the ideal customer profile.
- **A weekly focus list per rep**, in a shared spreadsheet they can annotate.
- **A structured outreach cadence** of 15 touches across calls, email, text and social, with drafted messages.
- **A weekly activity grade** pulled from the CRM showing which focus accounts got a logged touch.

**The technique:** **Decide the "who" once, centrally, so reps spend their time on the "how."** Ranking by fit and handing out a short weekly list removes the daily decision that stalls prospecting.

**Benefits:**

- Reps start each week knowing exactly who to contact.
- The best-fit accounts get worked first, instead of the most familiar ones.
- Managers see activity against the plan, not just total activity.

**Directional impact:** time spent deciding who to contact down roughly 80%. A higher share of activity landed on best-fit accounts.

**Try it yourself:**

1. Write down what your best customers have in common.
2. Ask the AI to score your account list against that profile.
3. Give each rep their top 25 for the week. Next Monday, check which ones were touched.

**Starter prompt:**

> Here is a description of our best customers and an export of our accounts. Score each account A to D on how well it matches. Then build a weekly list of 25 accounts per rep, best fit first, skipping anyone with an active contract or contacted in the last 90 days.

---

#### Lesson 7: Give every rep an assistant that reports to you

**Department:** Sales Management

**The daily frustration:** *"I want to help each rep individually, but I have five of them and every Monday I'm buried in reports."*

**What we built:** A personal AI assistant for each rep that runs every Monday morning. It reads the rep's notes and their CRM activity from last week, keeps a running profile of their habits and accounts, and tells the manager how to help them this week. By design, the assistants **observe and report only**. They never message reps, edit records or act on their own.

**The technique:** **Use AI as a chief of staff, not a replacement manager.** The assistant does the reading and pattern-spotting. The human keeps the relationship and the judgment. The "observe and report only" boundary is what makes it safe to trust.

**Benefits:**

- Managers walk into Monday with a short, specific note on each rep.
- Patterns like stalled accounts or skipped follow-ups show up early.
- Reps get more relevant help without feeling watched by a bot.

**Directional impact:** weekly manager review time down roughly 60–75%, with more individual attention per rep.

**Try it yourself:**

1. Each week, export one rep's activity and notes.
2. Ask the AI what changed, what's stuck, and the single most useful thing you could do for them.
3. Keep a running profile document. Give it to the AI each week so it remembers.

**Starter prompt:**

> Here is my rep's activity log and notes from last week, plus their profile from previous weeks. Summarize what changed, which accounts look stuck, and the one thing I could do this week that would help them most. Update the profile with anything new.

---

#### Lesson 8: Put the rules above the agents

**Department:** Sales Leadership

**The daily frustration:** *"Everyone has their own way of doing things: cleaning up contacts, researching accounts, deciding who the decision maker is. There's no standard, so the data's a mess."*

**What we built:** A "Chief Sales Officer" agent that sits above the rep assistants. It holds the team's written standards: what a clean contact record is, what good account research includes, how to identify the decision maker, when to follow up. It reviews the week, proposes new rules, and the rep assistants apply the rules the leader approves. **Every rule is signed off by the leader and discussed with the team first.**

**The technique:** **Write standards down once, at the top, and let them flow down.** When standards live in one place, every assistant, report and new hire works from the same definitions. The AI suggests rules, and a person decides them.

**Benefits:**

- One source of truth for "how we do things here."
- New standards reach every rep's assistant the moment they're approved.
- A weekly review board shows open decisions, so nothing waits forever.

**Directional impact:** policy drift and duplicate effort across reps noticeably reduced. A weekly leadership review that once took hours now takes about 30 minutes.

**Try it yourself:**

1. List the five things your team does inconsistently.
2. Write one clear rule for each, with an example.
3. Give those rules to the AI with your team's work and ask where they aren't being followed.

**Starter prompt:**

> Here are our team standards and this week's CRM activity. List every place the standards weren't followed, grouped by rule. Suggest any new rule that would have prevented a recurring problem, and explain why. I'll decide which ones to adopt.

---

#### Lesson 9: Tell the true story of your own work

**Department:** Leadership / Any role

**The daily frustration:** *"I've been busy for months, but when my boss asks what I've accomplished, I struggle to explain it."*

**What we built:** A retrospective of six months of work, rebuilt from the files, dates and history left behind:

- an eight-chapter timeline from the very first session
- the milestones
- every project and its current status
- the mistakes that became rules
- the decisions still waiting

**The technique:** **Reconstruct from evidence, not memory.** Your work leaves traces: file dates, documents, versions, emails. An AI can read them and build an honest timeline, including the parts you forgot and the parts that didn't work.

**Benefits:**

- A clear, credible story of impact for reviews, board updates or your own reflection.
- It surfaces stalled work and pending decisions you'd lost track of.
- It shows patterns in your own work, such as where your time actually goes.

**Directional impact:** a retrospective that would take days to assemble by hand took an afternoon.

**Try it yourself:**

1. Point the AI at a folder of your work from the last quarter.
2. Ask for a timeline, a list of projects with status, and what's waiting on you.

**Starter prompt:**

> Using the files and dates in this folder, build a timeline of what I worked on this quarter. List each project, when it started, and whether it's done, running, stalled or waiting on a decision. Point out where most of my time went and what I've left unfinished.

---

### Revenue operations and finance

---

#### Lesson 10: Organize your pipeline by how you sell, not what you sell

**Department:** Revenue Operations

**The daily frustration:** *"Our CRM has a pipeline for every product. Nobody can answer 'how much new business did we close?' without a spreadsheet and an argument."*

**What we built:** A redesign from several product-based pipelines to two pipelines based on the sales motion: **New Business** and **Renewal**. Products became line items on the deal, each tagged with a revenue type: new, renewal or upsell. The AI wrote the methodology and process maps for the CRM developers, then helped migrate the open deals.

**The technique:** **Model the motion, tag the money.** Stages should describe what the salesperson is doing. Revenue categories belong on the line items, where one deal can hold a new product, a renewal and an upsell at once.

**Benefits:**

- Leadership questions like "new versus renewal revenue" have one clean answer.
- Reps follow one consistent set of stages.
- Reporting no longer misses deals filed in the "wrong" pipeline.

**Directional impact:** pipeline reporting reconciliation down roughly 50–70%. Fewer deals missing from reports.

**Try it yourself:**

1. List your current pipelines and stages.
2. Ask the AI to design a structure around your actual sales motions.
3. Ask where each product, discount and revenue type should live.

**Starter prompt:**

> Here are our current CRM pipelines, stages and products. Propose a simpler structure organized by sales motion. Show where products and revenue type (new, renewal, upsell) should live so one deal can carry several, and list the reports that become easier or break.

---

#### Lesson 11: Build a ledger that checks its own data

**Department:** Revenue Operations / Finance

**The daily frustration:** *"Every month-end, someone finds a deal entered wrong: no product, wrong price, missing term. We fix it in the report, and next month it's wrong again."*

**What we built:** A live closed-deals ledger that rebuilds itself from the CRM every morning. It flags data problems on every deal: a missing product, a blank revenue type, a missing term, a price that doesn't match the price book. The flags point to the record that needs fixing.

**The technique:** **Make the report find the errors, and fix them at the source.** A report that flags bad data trains the team to enter it right. One firm rule came from experience: **change the build process, never just the published report.** A hand-edited report gets overwritten by the next refresh, and the fix disappears.

**Benefits:**

- Data quality improves every week instead of being patched every month.
- Month-end close is faster and less contentious.
- Everyone trusts the number because the checks are visible.

**Directional impact:** month-end cleanup time down roughly 50–75%. Recurring entry errors fell steadily.

**Try it yourself:**

1. List the five most common CRM entry mistakes.
2. Ask the AI to write a check for each one.
3. Run it on last month's deals and send each owner their list.

**Starter prompt:**

> Here are our closed deals with their line items. Check every deal against these rules: has a product, revenue type set, contract term set, unit price matches our price list. Output a table of every violation with the deal owner, so each person gets a fix list.

---

#### Lesson 12: Make commissions boring (in a good way)

**Department:** Finance / Sales Operations

**The daily frustration:** *"Commission time means a week of spreadsheets, disputes and 'that's not what I was promised.' Nobody can explain how a number was calculated."*

**What we built:**

- **A reproducible commission ledger** that calculates every payment line item by line item, using the plan rules as they are actually paid.
- **A quarterly workbook** with one self-contained statement per rep.
- **A walk-through for edge cases**, such as an account changing hands, that explains a specific calculation to the rep.
- **A model of an alternative plan** based on invoiced revenue, checked against the accounting system to see how closely the CRM predicts what is billed.

**The technique:** **Write the plan as rules, then let the rules do the math.** Once rules are explicit, every number can be traced, explained and re-run. Comparing CRM expectations with actual invoices shows whether the CRM can be trusted for pay at all.

**Benefits:**

- Fewer disputes, because every number has a traceable explanation.
- The quarterly run takes hours, not days.
- Leaders can model a plan change before announcing it.

**Directional impact:** quarterly commission prep time down roughly 60–80%. Disputes noticeably reduced.

**Try it yourself:**

1. Write your commission plan as numbered rules, including the edge cases.
2. Give the AI the rules and one quarter of deals.
3. Ask for a statement per rep and a list of deals the rules don't clearly cover.

**Starter prompt:**

> Here is our commission plan written as rules, and last quarter's deals. Calculate each rep's commission line by line, show your work, and list every deal where the rules are ambiguous so I can make a decision before we pay.

---

#### Lesson 13: Forecast with conventions, not vibes

**Department:** Finance / Leadership

**The daily frustration:** *"The forecast changes depending on who builds it. Leadership doesn't trust it, so every meeting becomes a debate about the number."*

**What we built:** A living revenue forecast for leadership. It shows booked revenue, a base case, and the assumptions behind each part. Along the way the AI documented how the CRM actually behaves: how renewal placeholders are created, which owners are inactive, which test records must always be excluded. Each became a written convention the forecast follows.

**The technique:** **Write down the conventions behind the number.** Most forecast fights are really fights about hidden assumptions. When the conventions are explicit and every refresh follows them, the conversation moves from "is this right?" to "what do we do about it?"

**Benefits:**

- Leadership meetings spend time on decisions, not reconciliation.
- Forecasts from different months can be compared, because the method didn't change.
- New people can update the forecast without reinventing it.

**Directional impact:** forecast preparation down roughly 50%. Time in meetings spent on decisions rather than debating the number noticeably up.

**Try it yourself:**

1. Ask the AI to build your forecast, and to list every assumption it had to make.
2. Decide each assumption once and save the list.
3. Rebuild next month's forecast with the same list.

**Starter prompt:**

> Build a revenue forecast from these open and closed deals. Before you calculate anything, list every assumption you need to make (what counts as a renewal, how to treat stale deals, what to exclude) and ask me to decide each one. Save my answers as rules for next time.

---

#### Lesson 14: Let the dashboards update themselves

**Department:** Operations / Leadership

**The daily frustration:** *"Every Monday someone spends hours copying numbers into the same dashboard. By the time it's ready, it's already old."*

**What we built:** Self-refreshing team pages for company health, quarterly OKRs, weekly inquiries, paid search and content. Each one rebuilds on a schedule before the team arrives. Over time, about fourteen recurring jobs ran every morning or every Monday with no one starting them.

**The technique:** **Automate the refresh, not just the report.** A dashboard someone must remember to update eventually stops being updated. A scheduled agent that rebuilds it, along with a written runbook, keeps it alive.

**Benefits:**

- Leaders see current numbers first thing, every time.
- The hours spent copying numbers go to analyzing them.
- One source of truth replaces several versions of the same spreadsheet.

**Directional impact:** manual reporting time for recurring dashboards cut by roughly 90–100%.

**Try it yourself:**

1. List the reports you rebuild every week or month.
2. For one of them, write the steps you follow as a runbook.
3. Ask the AI to turn the runbook into a scheduled job that rebuilds the report and tells you what changed.

**Starter prompt:**

> Here are the exact steps I follow every Monday to update our team dashboard. Turn them into a written runbook, then into a scheduled task that pulls the data, rebuilds the dashboard, and gives me a three-line summary of what changed since last week.

---

### Data and decision-making

---

#### Lesson 15: Find out where your numbers are lying to you

**Department:** Data / Analytics / Leadership

**The daily frustration:** *"We make decisions on our dashboards, but sometimes the numbers just don't feel right, and nobody has time to dig in."*

**What we built:** A series of data-truth audits on the metrics leadership relied on. Some of what they found:

- A traffic metric was mostly bots, more than half in some periods.
- "Unique visitors" were really page requests.
- A database change multiplied lead counts by several times, inflating every trend chart.
- A retired tracking type made one metric look like it had collapsed.
- A reporting filter quietly missed most closed deals because they sat in different stages.

**The technique:** **Before you trust a metric, ask how it's counted.** Ask the AI to trace a number back to its source: what one row means, what's filtered in and out, and what changed over time. Then save each finding as a permanent rule so it's never rediscovered the hard way.

**Benefits:**

- Decisions rest on numbers that mean what everyone thinks they mean.
- External claims (to customers, investors, the press) hold up to scrutiny.
- One fix to a definition corrects every report that uses it.

**Directional impact:** in our experience, about one in three widely used metrics had a definition problem worth fixing. Some were overstated by a factor of two or more.

**Try it yourself:**

1. Pick the three metrics you quote most often.
2. For each, ask the AI to explain what is counted and what could inflate or deflate it.
3. Check one suspicious trend against a second source.

**Starter prompt:**

> Here is how this metric is calculated and the raw data behind it. Explain in plain language what one row represents, what's included and excluded, and every way this number could be misleading: duplicates, bots, definition changes, missing records. Then test the biggest risk against the data.

---

#### Lesson 16: Open the black box

**Department:** Data / Operations

**The daily frustration:** *"There's a report our system emails us every week. No one knows how it's calculated, but we make decisions on it."*

**What we built:** Rebuilds of several black-box reports from their underlying data: a weekly system-generated inquiry report, a customer analytics export, and a third-party scoring tool used as a lead magnet. Each was decoded field by field, rebuilt so it could be explained, and documented. In one case this led to building our own version of the scoring tool, tuned to our market.

**The technique:** **Reverse-engineer, then own.** Give the AI the report and the raw data. Ask it to work out how one produces the other and document every rule it finds. Once you understand it, you can fix it, extend it or replace it.

**Benefits:**

- Fewer decisions based on numbers nobody can explain.
- Defects in automated reports get found and documented.
- Freedom to replace a vendor's tool with one that fits your business.

**Directional impact:** dependence on unexplained reports dropped sharply. Each rebuilt report has its rules written down, so it can be explained to anyone.

**Try it yourself:**

1. Take one report you receive but don't fully understand.
2. Give the AI the report and whatever raw data you can export.
3. Ask it to reproduce one row and explain the rule behind each column.

**Starter prompt:**

> Here is a report we receive weekly and the raw data I can export. Work out how the report is calculated column by column, reproduce last week's numbers, and document any place where your result doesn't match. Tell me which numbers I should and shouldn't trust.

---

#### Lesson 17: When something drops, find the cause before you react

**Department:** Leadership / Marketing / Sales

**The daily frustration:** *"Leads fell off a cliff in one region. Everyone has a theory, and we're about to make changes without knowing why."*

**What we built:** A set of root-cause investigations into sudden changes. In each case the AI tested each possible cause against the data and ruled them out one by one.

- A regional lead collapse traced to an ad campaign that had been paused months earlier.
- A customer's drop in results traced to a change made to their own listing settings.
- One market's dip traced to how ad budget rotated between regions.

**The technique:** **List every hypothesis, then rule them out with evidence.** Ask the AI to write down every plausible cause before looking for answers, then test each one against the data. The "ruled out" list matters as much as the answer, because it ends the debate.

**Benefits:**

- Fixes target the actual cause, not the loudest theory.
- Fewer expensive overreactions, like cutting a channel that wasn't the problem.
- A documented answer you can share with a customer or the team.

**Directional impact:** time from noticing a problem to knowing its cause went from weeks of debate to a day or two of investigation.

**Try it yourself:**

1. Describe the drop: what, where, when.
2. Ask the AI to list every possible cause, including changes you made yourself.
3. Give it the data and ask it to rule each cause in or out, with evidence.

**Starter prompt:**

> Our results dropped sharply in this area starting around this date. List every plausible cause, including changes we made ourselves and outside factors. Then, using this data, rule each one in or out with evidence. End with the most likely cause and what would confirm it.

---

### Marketing and content

---

#### Lesson 18: Connect ad spend to what the sales team actually sees

**Department:** Marketing

**The daily frustration:** *"Our ad agency reports clicks and conversions. Our sales team says the leads are bad. Nobody connects the two."*

**What we built:** A daily briefing that joins ad platform data with CRM outcomes. It shows cost per real contact by campaign and by market, which markets are underserved, and which spend is going to accounts that no longer pay. It refreshes every morning with a short summary.

**The technique:** **Judge marketing by the downstream outcome, not the platform's own metric.** The ad platform grades its own homework. Joining spend to what the CRM records shows what the money actually produces.

**Benefits:**

- Budget moves toward campaigns that produce real customers.
- Marketing and sales argue less, because they look at the same numbers.
- Problems like rising cost or wasted spend show up within days, not quarters.

**Directional impact:** wasted or misdirected spend identified early. Reallocation decisions made weekly instead of quarterly.

**Try it yourself:**

1. Export last month's ad spend by campaign and your CRM contacts with their source.
2. Ask the AI to join them and calculate cost per qualified contact.
3. Ask which campaigns look good on the platform but poor in the CRM.

**Starter prompt:**

> Here's last month's ad spend by campaign and our CRM contacts with their source. Join them, calculate cost per real contact and per qualified contact for each campaign, and show me which campaigns look good in the ad platform but bad in the CRM.

---

#### Lesson 19: Run a real experiment instead of a debate

**Department:** Marketing / SEO

**The daily frustration:** *"We've argued for months about whether rewriting our website pages is worth it. Everyone has an opinion, and no one has proof."*

**What we built:** A 90-day matched experiment. A set of rebuilt pages was paired with similar pages left unchanged. Rankings and AI-search citations are tracked for both, with a fixed baseline, scheduled checkpoints, and a tracker the AI checks twice a day.

**The technique:** **Turn the argument into a test with a control group.** Pick matched pairs, change only one side, decide the success measure in advance, and set a readout date. The AI handles the tedious parts: pairing, baselining, tracking and reminders.

**Benefits:**

- A decision based on evidence, not seniority or opinion.
- A clear readout date that ends the debate.
- A reusable method for the next "should we?" question.

**Directional impact:** an effort that would have needed an analyst's dedicated time runs mostly unattended. The decision on a large rollout gets made on evidence, not assumption.

**Try it yourself:**

1. Write down the change you're debating and how you would measure success.
2. Ask the AI to pick matched test and control groups.
3. Set a baseline today and a readout date. Let the AI track it.

**Starter prompt:**

> We're debating whether [change] works. Design a simple matched test: how to choose test and control groups so they're comparable, what to measure, the baseline to capture today, and the checkpoints. Keep it small enough to run in 90 days.

---

#### Lesson 20: Produce content at scale without sounding like a template

**Department:** Marketing / Content

**The daily frustration:** *"We need hundreds of pages and posts. When we speed up, everything starts to sound the same, and search engines notice."*

**What we built:** A content system with built-in quality checks:

- a single brand system: voice, rules and design tokens
- a similarity check that flags copy too close to other pages
- a "swap test": if a paragraph still reads true with another city's name, it gets rewritten around a local fact
- a plain-English editor agent that rewrites every draft in a warm, spoken voice before a person sees it
- sourced, dated facts
- a rule that a person approves every piece

**The technique:** **Let the AI draft, but make it pass your checks before you see it.** Speed comes from the AI. Quality comes from explicit checks that catch the things you would otherwise catch by hand: repetition, jargon, unsourced claims, off-brand tone.

**Benefits:**

- Volume goes up and quality holds.
- Reviewers spend time on judgment, not catching repeated phrases.
- The brand voice stays consistent across many writers, human and AI.

**Directional impact:** drafting time per piece down roughly 70–80%. Reviewer time spent on mechanical fixes down noticeably.

**Try it yourself:**

1. Write your top five "never do this" content rules.
2. Create an "editor" instruction that rewrites drafts against those rules.
3. Run every draft through the editor before a human reads it.

**Starter prompt:**

> You are my editor. Here are our brand voice rules and our banned phrases. Rewrite this draft so it sounds like a knowledgeable person talking: lead with what matters to the reader, cut filler and jargon, keep every fact. Then list anything that could be true of any company or city and should be made specific.

---

#### Lesson 21: Track how AI search sees you, and who it cites instead

**Department:** Marketing / Brand / Strategy

**The daily frustration:** *"Customers are asking ChatGPT instead of Google. I have no idea whether we show up, or who's showing up instead."*

**What we built:**

- **A repeatable panel** of real customer questions asked across AI answer engines in waves, tracking how often the company is cited.
- **Competitor teardowns** when a new player appeared. One took apart how a brand-new site on an old domain became the first source AI search cited for cost questions: page structure, data presentation and crawler access.

**The technique:** **Measure your AI visibility like you measure search rankings.** Pick the questions your customers ask, ask them on a schedule, and record who gets cited. When someone overtakes you, study what they did differently.

**Benefits:**

- An early warning when your share of AI answers slips.
- Specific, copyable reasons competitors get cited.
- A baseline to measure whether your content changes work.

**Directional impact:** a visibility decline that would have gone unnoticed was caught within one measurement cycle.

**Try it yourself:**

1. Write 20 questions your customers ask before buying.
2. Ask them in two or three AI assistants, in a fresh chat with no history.
3. Record who is cited. Repeat monthly.

**Starter prompt:**

> Here are 20 questions our customers ask before buying. For each, tell me what an AI assistant would likely cite. Then help me design a monthly tracking sheet: question, engine, date, who was cited, whether we appeared, and what the cited sources have that we don't.

---

### Operations and how you work

---

#### Lesson 22: Give every file one owner

**Department:** Operations / Team Management

**The daily frustration:** *"There are four versions of the same document. Someone edited the old one. Now we don't know which is right."*

**What we built:** A workspace reorganized so each project has one folder with one owner. Shared files live in one shared place with a written ownership list. Old versions move to a dated archive instead of being deleted or left lying around. Access is enforced by folder permissions, not by asking people to be careful.

**The technique:** **Enforce ownership by structure, not instructions.** People and AI both make mistakes when duplicates exist. A structure where the wrong file can't be reached prevents the mistake.

**Benefits:**

- No more "which version is right?"
- Several people, and several AI assistants, can work at once without overwriting each other.
- Old work is preserved without cluttering current work.

**Directional impact:** version-confusion errors went to nearly zero. Onboarding a second operator took a single dry run.

**Try it yourself:**

1. Find the three documents most often duplicated or edited in the wrong place.
2. Give each one owner and one location, and archive the rest with a date in the name.
3. Write a one-page "who writes what" list.

**Starter prompt:**

> Here is a list of our shared files and folders. Group them by project, flag duplicates and likely outdated copies, and propose a structure where each file has exactly one owner and one location, with an archive for old versions. Draft a short ownership list for the team.

---

#### Lesson 23: Turn every correction into a permanent rule

**Department:** Any role

**The daily frustration:** *"I keep correcting the same mistakes, whether it's a new hire, a vendor or the AI. Nothing sticks."*

**What we built:** A memory and rulebook discipline. Every time the leader corrected the AI, the correction became a saved rule with the reason behind it. Some examples:

- "never loosen a workflow to get around missing data"
- "always compare against a control group"
- "never describe the website in consumer copy"

About 150 such notes built up over six months. Each new piece of work started from all of them.

**The technique:** **Capture the rule and the reason, at the moment of correction.** A correction teaches once. A written rule with its reason teaches every time after, and the reason lets the rule be applied sensibly to new situations.

**Benefits:**

- The same mistake rarely happens twice.
- Your judgment scales: it's written down and applied consistently.
- New team members or assistants get up to speed from the rulebook.

**Directional impact:** repeat corrections dropped sharply over the first two months, as most recurring issues became written rules.

**Try it yourself:**

1. Keep a "rules" document for each area of your work.
2. Every time you correct something, add: the rule, why, and an example.
3. Give the document to any AI or new hire before they start.

**Starter prompt:**

> I'm about to correct you. When I do, write it as a permanent rule: the rule in one line, why it matters, and how to apply it in similar cases. Add it to my rulebook and check new work against the rulebook before showing it to me.

---

#### Lesson 24: Build a decision queue so work doesn't wait on you

**Department:** Leadership

**The daily frustration:** *"My team is waiting on me for approvals. I didn't know half of them were pending."*

**What we built:** This one came out of the retrospective. It showed that the AI could produce work faster than one leader could approve it. Several finished items were sitting unreviewed, among them a playbook draft, a compensation model, a scoring method and a large batch of ready-to-publish pages. The fix is a weekly decision queue: each pending decision with a one-line summary, a recommendation, and a yes/no/change response.

**The technique:** **When work speeds up, the bottleneck moves to decisions. Make decisions easy.** Batch them, recommend an answer for each, and review them on a fixed schedule.

**Benefits:**

- Finished work actually ships.
- The team stops waiting and guessing.
- Leaders see everything that needs them in one place.

**Directional impact:** expect roughly 30–50% faster time from "ready" to "shipped" once decisions run on a weekly rhythm.

**Try it yourself:**

1. Ask the AI to list everything waiting on your approval across your projects.
2. For each, ask for a one-line summary and a recommendation.
3. Spend 30 minutes every Monday clearing the queue.

**Starter prompt:**

> Go through my open projects and list every item waiting on my decision. For each, give me one line on what it is, what happens if I approve it, and your recommendation. Sort by how much other work is blocked behind it.

---

## Rules we learned the hard way

Each of these came from something going wrong once.

| What happened | The rule now |
|---|---|
| A client-facing summary went out with the wrong company's name on it. | Client documents come from fixed templates with an account check. Never write them freehand. |
| Two copies of the same instructions drifted apart, and the old one was used. | One owner per file. Old versions go to a dated archive and are never read as current. |
| Data checks were added by hand to a published report, and the next automatic refresh erased them. | Change the process that builds the report, never just the report. |
| Teammates typed comments into a shared review page, but nothing saved because they only had view access. | Check sharing permissions before asking a team to review anything. |
| The AI proposed loosening a workflow rule to get around missing data. | Fix the data. Never relax the rule that protects it. |
| A large automated scan of the company's own website slowed it down for staff. | Test on a handful of pages, one at a time, before anything at scale. |
| Projections looked impressive until we noticed the whole market had grown on its own. | Every "improvement" claim needs a comparison group that didn't get the change. |

**The principle underneath all of these:** the AI's speed makes mistakes travel faster too. Put the checks in the system, not in your memory.

---

## Your first 30 days

**Week 1: Ask.** Pick the three tasks that frustrate you most each week. Do each one with the AI once. Correct it out loud.

**Week 2: Write it down.** For the task you repeat most, ask the AI to write the method as a step-by-step procedure, including every correction. Start a rulebook.

**Week 3: Check your numbers.** Pick the one metric you quote most and ask the AI to explain exactly how it's counted (Lesson 15). Fix what you find.

**Week 4: Schedule one thing.** Turn one weekly report into something that refreshes itself and sends you a three-line summary (Lesson 14). Set up a 30-minute Monday decision queue (Lesson 24).

**What to expect:** small at first. Then each system makes the next one easier, because the rules, templates and definitions you've written are reused. Our own use roughly doubled each month for the first several months, and most of the long-term value came from work that eventually ran without anyone starting it.

---

## Quick index: frustration to lesson

| If your daily frustration is… | Start with |
|---|---|
| Generic decks and long demo prep | Lesson 1 |
| Every proposal starts from scratch | Lesson 2 |
| A sales process nobody follows | Lesson 3 |
| No time to coach each rep | Lesson 4 |
| Renewals sneaking up on you | Lesson 5 |
| Reps unsure who to call | Lesson 6 |
| Buried in Monday reports | Lesson 7 |
| Everyone does it their own way | Lesson 8 |
| Can't explain what you've accomplished | Lesson 9 |
| The CRM can't answer simple revenue questions | Lesson 10 |
| The same data errors every month-end | Lesson 11 |
| Commission disputes | Lesson 12 |
| A forecast nobody trusts | Lesson 13 |
| Hours spent updating dashboards | Lesson 14 |
| Numbers that don't feel right | Lesson 15 |
| Reports no one can explain | Lesson 16 |
| A sudden drop and too many theories | Lesson 17 |
| Marketing and sales disagree on lead quality | Lesson 18 |
| Endless debates without proof | Lesson 19 |
| Content that sounds templated | Lesson 20 |
| Not knowing if AI search mentions you | Lesson 21 |
| Too many versions of the same file | Lesson 22 |
| Correcting the same mistakes again and again | Lesson 23 |
| Work waiting on your approval | Lesson 24 |

---

*About the figures in this document: impact ranges are directional estimates from six months of hands-on use. They are not audited results, and every team will see different numbers. Specific company data, customer names and financial figures have been left out on purpose.*
