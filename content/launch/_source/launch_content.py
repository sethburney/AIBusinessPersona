# Single source for Remi's 3-week launch content.
# Generates the markdown production packages (repo) and the HTML preview board (artifact).

IMAGES = {
    "profile": ("remi_profile_blue.jpg", "Profile, blue tank, plain light background; front-facing, best for talking videos"),
    "desk": ("remi_monday_cover_one_point.jpg", "At the desk, pointing to open space"),
    "work": ("remi_work_mode_full.jpg", "Work mode, full length, office hallway"),
}

VOICE_DIRECTION = (
    "Remi's saved stock voice (same voice every time; never a clone of a real person's voice). Bright, warm, upbeat and conversational, "
    "with a smile in it. Natural pace, about 150 words per minute. Clear and confident, never salesy."
)

AVOID = (
    "other people, on-screen text, captions, subtitles, logos, brand names, rings, "
    "distorted hands, extra fingers, exaggerated or rubbery mouth movement, robotic stillness, "
    "changes to her face, hair, outfit or background"
)

HASHTAGS_CORE = "#AIforBusiness #WorkSmarter #SalesOps #MarketingOps #AItools #RemiTobor"

WEEKS = [
    {
        "num": 1,
        "name": "Launch: meet Remi",
        "pillar": "Intro",
        "goal": "Introduce Remi, set the \"you're not behind\" tone, and explain the frameworks followers will see every week.",
        "posts": [
            {
                "id": "W1-MON", "day": "Mon", "series": "Level-Up Monday", "type": "video",
                "title": "Same task, every week? Start here.",
                "image": "profile",
                "script": [
                    "Still redoing the same email, report, or checklist every single week?",
                    "Hi! I'm Remi. And yes, I'm AI, with a real human behind me.",
                    "My human builds real sales and marketing systems with AI.",
                    "Some work. Some flop. I'll show you both.",
                    "One idea at a time, so you can use it at work this week.",
                    "You're not behind. Start small: pick one task to make easier today.",
                    "Tell me which one. Let's level up together.",
                ],
                "performance": "Knowing eyebrow lift on the opening question. Small wave and a big smile on \"Hi!\" Light laugh on \"Some flop.\" Leans in a little on \"You're not behind.\" Warm smile to finish.",
                "onscreen": [
                    ("0–4 s", "Same task. Every week. 😩"),
                    ("4–9 s", "Hi, I'm Remi 👋 (yes, I'm AI)"),
                    ("9–17 s", "Real systems. Real wins. Real flops."),
                    ("17–end", "Pick one task to make easier today"),
                ],
                "caption": "Doing the same task every week? Let's start there. 👋\n\nI'm Remi. Yes, I'm AI, and my human checks everything I share. Every week: one real system, what worked, and what flopped.\n\nYou're not behind. Tell me one task you'd love to make easier 👇",
                "source": "Final: blend (Codex hook + Claude warmth). Persona intro.",
            },
            {
                "id": "W1-WED", "day": "Wed", "series": "The Playbook", "type": "carousel",
                "title": "Ask → Build → Delegate: which stage are you in?",
                "slides": [
                    {"kind": "cover", "head": "Still explaining the same task to AI?", "body": "Meet the 3 stages. Which one are you in?", "image": "profile"},
                    {"kind": "step", "label": "Stage 1", "head": "Ask", "body": "You ask AI for a one-off task. \"Write this email.\" \"Summarize this doc.\" Handy. But next time, you start over."},
                    {"kind": "step", "label": "Stage 2", "head": "Build", "body": "You save the steps, a template, and your fixes. Next time, give AI those steps and check its work."},
                    {"kind": "step", "label": "Stage 3", "head": "Delegate", "body": "The task runs on a schedule and reports back. You review it. You decide."},
                    {"kind": "text", "head": "A draft still needs checks", "body": "A polished answer can still miss something. Make checking the work part of your saved steps."},
                    {"kind": "list", "head": "Move up one stage", "items": ["Pick a task that bugged you twice this month.", "Do it with AI once. Fix what it gets wrong.", "Ask AI to write down the steps.", "Next time, start from those steps."]},
                    {"kind": "prompt", "head": "Steal this prompt", "body": "Write down the steps we just used. Include my corrections so I can use them again."},
                    {"kind": "rule", "head": "One rule at every stage", "body": "AI drafts. A human decides."},
                    {"kind": "end", "head": "You're not behind. Start small.", "body": "Comment your stage (1, 2, or 3). I'll help you with the next step."},
                ],
                "caption": "Are you an Asker, a Builder, or a Delegator? 🤖\n\nIn our experience, stages 2 and 3 are where AI saves the most time. Getting there is simpler than it sounds.\n\nTell me your stage in the comments 👇",
                "source": "Final: blend, mostly Claude (Codex's checks slide and prompt added). Playbook: Ask, Build, Delegate.",
            },
            {
                "id": "W1-FRI", "day": "Fri", "series": "The Handoff", "type": "video",
                "title": "Can your process run without you explaining it?",
                "image": "desk",
                "script": [
                    "Built something with AI, but your team still needs you to explain every step?",
                    "Let's get those steps out of your head and onto the page.",
                    "I'm Remi, your AI work bestie. Every lesson here follows three steps.",
                    "Build it: give AI clear steps for a task you repeat.",
                    "Prove it: check that the result is right, and see if it saves time.",
                    "Hand it off: write down who runs it and what they check.",
                    "A fast draft can still be wrong. So we'll share the flops too.",
                    "Start by writing the first step of one task you do often.",
                    "Stay human. I'll handle the robot stuff.",
                ],
                "performance": "Knowing smile on the opening question. A small nod for each of the three steps. Keeps hands low. Playful wink on the sign-off.",
                "onscreen": [
                    ("0–6 s", "Still explaining every step?"),
                    ("8–14 s", "BUILD IT · clear steps"),
                    ("14–20 s", "PROVE IT · check the result"),
                    ("20–26 s", "HAND IT OFF · who runs it"),
                    ("26–end", "Write the first step today ✍️"),
                ],
                "caption": "Your best process shouldn't live only in your head. ✍️\n\nEvery lesson here follows 3 steps:\n1️⃣ Build it\n2️⃣ Prove it\n3️⃣ Hand it off\n\nStart by writing the first step of one task you do often.",
                "source": "Final: Codex, with Claude's sign-off. Messaging framework: Build It, Prove It, Hand It Off.",
            },
        ],
        "bridge": {
            "id": "W1-BRIDGE", "day": "Sun", "series": "You're Not Behind", "type": "video",
            "title": "Bridge: into messy data week",
            "image": "profile",
            "script": [
                "Still double-checking the same report?",
                "This week, we covered asking AI for help and saving the steps.",
                "Next week, we'll tackle messy CRM data.",
                "I'm Remi, your AI work bestie. You're not behind.",
                "Pick that report. Bring your coffee. I'll bring the checklist.",
            ],
            "performance": "Relaxed and cozy, like a friend checking in. Soft smile on the opening. Small nod on \"You're not behind.\" Playful raised eyebrow on the coffee line.",
            "onscreen": [("0–3 s", "Still double-checking that report?"), ("3–8 s", "Week 1: Ask → Build → Delegate"), ("8–end", "Next week: messy CRM data ☕")],
            "caption": "Still double-checking the same report? Hold that thought. ☕\n\nNext week: messy CRM data, and simple checks that catch errors for you.\n\nPick one report you keep double-checking.",
            "source": "Final: Codex, with Claude's coffee line. Bridge series.",
        },
    },
    {
        "num": 2,
        "name": "Clean data, connected systems",
        "pillar": "Pillar 1",
        "goal": "Show that messy data is fixable with simple standards and checks, and that the fix belongs in the original record.",
        "posts": [
            {
                "id": "W2-MON", "day": "Mon", "series": "Level-Up Monday", "type": "video",
                "title": "The error with a round-trip ticket",
                "image": "desk",
                "script": [
                    "Filled in that blank already? Why is it blank again?",
                    "Looks like that error bought a round-trip ticket.",
                    "I'm Remi, your AI work bestie. Here's what helped my human's team.",
                    "Their report updated itself from the CRM every morning.",
                    "It flagged missing or wrong details and showed which record to fix.",
                    "Once they fixed the original record, the next report used the right details.",
                    "In our experience, cleanup took about half as long, sometimes less.",
                    "Try one small thing: ask AI to write a check for one blank that keeps coming back.",
                ],
                "performance": "Mock-surprised eyebrows on \"blank again?\" Light laugh on the round-trip ticket. Slows down a little to explain the report. Encouraging nod on the last line.",
                "onscreen": [
                    ("0–5 s", "Fixed it… and it's back? 😩"),
                    ("5–15 s", "The report flags what's wrong"),
                    ("15–22 s", "Fix the original record"),
                    ("22–end", "Write one check for a repeat error"),
                ],
                "caption": "That error came back because the original record still had it. 🧹\n\nMy human's team let the report flag bad data. Then they fixed it where it started. AI flags it. A person fixes it.\n\nAsk AI to write a check for one blank that keeps coming back.",
                "source": "Final: Codex, with Claude's directional result line. Playbook Lesson 11 (generalized).",
            },
            {
                "id": "W2-WED", "day": "Wed", "series": "The Playbook", "type": "carousel",
                "title": "5 rules for a CRM your team will actually keep clean",
                "slides": [
                    {"kind": "cover", "head": "Does your team agree on what \"clean\" means?", "body": "5 rules for a CRM your team will actually keep clean.", "image": "desk"},
                    {"kind": "step", "label": "Rule 1", "head": "Write down \"clean\"", "body": "List the fields every contact and deal needs. One page, with an example."},
                    {"kind": "step", "label": "Rule 2", "head": "One rulebook", "body": "Keep the standard in one shared place. People and AI tools use the same version."},
                    {"kind": "step", "label": "Rule 3", "head": "Let checks find the gaps", "body": "Have a report flag missing or wrong fields every day. Tell AI to flag gaps, not fill them in. Check the results."},
                    {"kind": "step", "label": "Rule 4", "head": "Fix the original record", "body": "Fixing the report leaves the record wrong. The next refresh brings the error right back."},
                    {"kind": "step", "label": "Rule 5", "head": "Check every week", "body": "Look at the errors that keep showing up, and fix why they happen."},
                    {"kind": "prompt", "head": "Steal this prompt", "body": "Here are our team standards and this week's CRM activity. List every place the standards weren't followed, grouped by rule. Suggest any new rule that would have prevented a repeat problem, and explain why. I'll decide which ones to adopt."},
                    {"kind": "end", "head": "You're not behind. Start small.", "body": "Write one clean-record rule this week, with an example."},
                ],
                "caption": "\"Clean\" is easier to keep when everyone means the same thing. 🧹\n\n5 rules, plus a prompt to steal on slide 7.\n\nStart small: write one clean-record rule this week.",
                "source": "Final: blend (Codex's cover and no-made-up-data rule + Claude's 5 rules and prompt). Playbook Lessons 8 and 11 (generalized).",
            },
            {
                "id": "W2-FRI", "day": "Fri", "series": "Remi's Oops", "type": "video",
                "title": "Remi's Oops: great fix, wrong place",
                "image": "profile",
                "script": [
                    "Ever fixed a report and watched your fix vanish?",
                    "Welcome to Remi's Oops! I'm AI, and this one comes from my human's team.",
                    "They added data checks right into a finished report. Looked great!",
                    "Then the report refreshed overnight. Poof. The checks were gone.",
                    "The fix was in the wrong place.",
                    "Here's the rule now: put the checks in the steps that build the report.",
                    "That kind of mistake happens. Now there's a rule to catch it.",
                    "Your move: find the steps that update one report you use often.",
                ],
                "performance": "Sympathetic smile on the opening. Bright \"Looked great!\" then a surprised pause before \"Poof.\" Clear and steady on the rule. Kind nod to finish. Hands stay low.",
                "onscreen": [
                    ("0–4 s", "Remi's Oops 🙈"),
                    ("4–12 s", "Checks added to the finished report…"),
                    ("12–18 s", "…gone after the refresh"),
                    ("18–end", "Rule: put checks where the report gets built"),
                ],
                "caption": "Great fix. Wrong place. 🙈\n\nMy human's team added checks to a finished report, and the next refresh wiped them out. The rule now: put checks in the steps that build the report.\n\nFind the steps that update one report you use often.",
                "source": "Final: Codex (accurate to the playbook), with \"sorted\" and the canned line removed. Playbook: Rules we learned the hard way.",
            },
        ],
        "bridge": {
            "id": "W2-BRIDGE", "day": "Sun", "series": "You're Not Behind", "type": "video",
            "title": "Bridge: into outreach week",
            "image": "profile",
            "script": [
                "Week two, done!",
                "If your CRM made you wince this week, good news. Wincing means you noticed.",
                "This week, we saw why the original record matters.",
                "Next week: outreach, and a short list of who to call.",
                "You're not behind. Write down what makes an account a good fit.",
            ],
            "performance": "Little celebratory shoulder shimmy on \"Week two, done!\" Kind, knowing smile on the wince line. Brightens on the preview. Encouraging nod at the end.",
            "onscreen": [("0–3 s", "Week 2 ✅"), ("3–8 s", "Noticing is step one"), ("8–end", "Next: a short list of who to call")],
            "caption": "Noticing the mess is step one. 💙\n\nNext week: outreach, starting with a short list of who to call.\n\nWrite down what makes an account a good fit.",
            "source": "Final: Codex, with Claude's wince line. Bridge series.",
        },
    },
    {
        "num": 3,
        "name": "Outreach that scales",
        "pillar": "Pillar 2",
        "goal": "Show how a written good-fit definition, a short weekly list, human-sounding follow-ups, and an AI assistant that only reports make outreach easier.",
        "posts": [
            {
                "id": "W3-MON", "day": "Mon", "series": "Level-Up Monday", "type": "video",
                "title": "The scroll before the call",
                "image": "desk",
                "script": [
                    "Open the CRM to make a call... and just keep scrolling?",
                    "So many accounts. Still no call.",
                    "I'm Remi, your AI work bestie. My human's team fixed this one.",
                    "First, they wrote down what makes an account a good fit.",
                    "AI used that to sort the list. People checked it.",
                    "Then each rep got a short focus list every week, best fit first.",
                    "A short list beats a giant database.",
                    "In our experience, the team spent a lot less time deciding who to call.",
                    "Start by writing down what makes an account a good fit for you.",
                ],
                "performance": "Playful searching glance to the side, then back to camera on \"Still no call.\" Warm and clear on the steps. Confident little smile on \"A short list beats a giant database.\"",
                "onscreen": [
                    ("0–5 s", "Scrolling instead of calling? 📱"),
                    ("5–14 s", "Write down what a good fit looks like"),
                    ("14–22 s", "AI sorts. People check."),
                    ("22–end", "A short list beats a giant database"),
                ],
                "caption": "The scroll before the call is real. 📋\n\nMy human's team wrote down what a good-fit account looks like. AI sorted the list, and each rep got a short weekly focus list. Each rep had a place to start, and people made the final call.\n\nStart by writing down what makes an account a good fit.",
                "source": "Final: blend (Codex's scrolling opener + Claude's list punchline, rewritten without the contrast pattern). Playbook Lesson 6 (generalized).",
            },
            {
                "id": "W3-WED", "day": "Wed", "series": "The Playbook", "type": "carousel",
                "title": "Before you send another \"just checking in\"",
                "slides": [
                    {"kind": "cover", "head": "Staring at another \"just checking in\" draft?", "body": "Give that message a job.", "image": "work"},
                    {"kind": "step", "label": "Step 1", "head": "Start with who", "body": "My human's team began with a short focus list of accounts that fit. The message came second."},
                    {"kind": "step", "label": "Step 2", "head": "Give each message a purpose", "body": "Ask: what does this help the reader do? A question, a useful detail, or a clear next step beats filler."},
                    {"kind": "step", "label": "Step 3", "head": "Make the question specific", "body": "Try: \"Is [the problem you mentioned] still something you'd like help with?\" Only use details they really shared."},
                    {"kind": "step", "label": "Step 4", "head": "Pick the right channel", "body": "My human's team mixed calls, email, text, and social. Use what fits the relationship and what they've agreed to."},
                    {"kind": "step", "label": "Step 5", "head": "AI drafts. A person edits.", "body": "Check every detail and make it sound like you. Don't pretend you know them or make up facts."},
                    {"kind": "step", "label": "Step 6", "head": "Know when to stop", "body": "Replied? Booked a meeting? Asked you to stop? Pause the follow-up plan and let a person take over."},
                    {"kind": "step", "label": "Step 7", "head": "Check the week", "body": "Every Monday, my human's team checked which focus accounts got contacted."},
                    {"kind": "end", "head": "You're not behind. Start small.", "body": "Rewrite one \"just checking in\" as a useful question."},
                ],
                "caption": "Your follow-up deserves a better job than \"just checking in.\" 💬\n\nMy human's team used focus lists, AI drafts, and a weekly check. The message tips here are ideas to try.\n\nRewrite one filler follow-up as a useful question.",
                "source": "Final: Codex, with lighter caveats. Playbook Lesson 6 (generalized; message tips labeled as ideas).",
            },
            {
                "id": "W3-FRI", "day": "Fri", "series": "The Handoff", "type": "video",
                "title": "An AI assistant with the send button off",
                "image": "profile",
                "script": [
                    "Got a pile of reports to read before you can help your team?",
                    "I'm Remi, your AI work bestie. Here's what my human's team tried.",
                    "Each rep got an AI assistant. Every Monday, it read their notes and activity.",
                    "Then it suggested where the manager could help most.",
                    "Here's the important part: it could read and report. That's it.",
                    "No messages to reps. No edits to records. Think reading buddy, with the send button off.",
                    "The manager checked the summary and talked with the rep.",
                    "And those Monday reviews got a whole lot shorter.",
                    "Try it: get permission, remove private details, and ask AI to summarize a week's notes.",
                ],
                "performance": "Mock-overwhelmed look on \"a pile of reports.\" Clear, even emphasis on each limit. Playful half-smile on \"send button off.\" Big warm smile on \"a whole lot shorter.\" Hands stay low.",
                "onscreen": [
                    ("0–5 s", "A pile of reports every Monday? 🏔️"),
                    ("5–15 s", "1 AI assistant per rep"),
                    ("15–24 s", "It reads and reports. That's it."),
                    ("24–29 s", "Shorter Monday reviews 🙌"),
                    ("29–end", "Get permission. Remove private details. Try one summary."),
                ],
                "caption": "What if every rep had an assistant that only reads and reports? 👀\n\nNo messages. No edits. The manager checks the summary and talks with the rep.\n\nGet permission, remove private details, and try one AI summary of a week's notes.",
                "source": "Final: blend (Codex's framing and front-facing image + Claude's Monday payoff, softened to match the playbook). Playbook Lesson 7 (generalized).",
            },
        ],
        "bridge": {
            "id": "W3-BRIDGE", "day": "Sun", "series": "You're Not Behind", "type": "video",
            "title": "Bridge: three weeks in",
            "image": "profile",
            "script": [
                "Three weeks in! Saved the posts but haven't tried them yet? That's okay.",
                "You could start with a task you repeat, a data check, or a short account list.",
                "Next week: leads worth your time.",
                "You're not behind. Start small: pick one idea to try this week.",
            ],
            "performance": "Proud, beaming smile on \"Three weeks in!\" Warm and welcoming on \"That's okay.\" Brightens on the preview. Small reassuring nod at the end.",
            "onscreen": [("0–4 s", "3 weeks in 🎉"), ("4–10 s", "Saved it? That counts."), ("10–15 s", "Next: leads worth your time"), ("15–end", "Pick one idea to try")],
            "caption": "Three weeks in. Saving the posts counts as a start. 🎉\n\nNext week: leads worth your time.\n\nPick one idea from these posts to try this week.",
            "source": "Final: Codex, with Claude's three-weeks-in opener. Bridge series.",
        },
    },
]


def words(lines):
    return sum(len(l.split()) for l in lines)


def seconds(lines):
    return round(words(lines) / 2.5)


def higgsfield_prompt(p):
    img_file, img_desc = IMAGES[p["image"]]
    script = "\n".join(p["script"])
    return (
        f"TALKING AVATAR (LIP-SYNC), 9:16 vertical, about {seconds(p['script'])} seconds\n\n"
        f"START IMAGE: {img_file} ({img_desc}). Use it as the avatar and first frame.\n\n"
        f"VOICE: {VOICE_DIRECTION}\n\n"
        f"SCRIPT (speak exactly, with natural pauses between lines):\n{script}\n\n"
        f"PERFORMANCE: She talks straight to camera like a friend over coffee. Natural blinking, small head movements, "
        f"expressive eyebrows. {p['performance']}\n\n"
        f"CAMERA: Steady chest-up framing with a very slow, subtle push-in.\n\n"
        f"KEEP: Her face, hair, smile, outfit and background identical to the start image in every frame. Lips match every word. "
        f"Keep hands low and the face unobstructed. Remi is an AI character; the script is not a statement by the real person whose likeness she uses.\n\n"
        f"AVOID: {AVOID}."
    )
