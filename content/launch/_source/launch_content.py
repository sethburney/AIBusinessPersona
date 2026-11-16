# Single source for Remi's 3-week launch content.
# Generates the markdown production packages (repo) and the HTML preview board (artifact).

IMAGES = {
    "profile": ("remi_profile_blue.jpg", "Profile, blue tank, plain light background; front-facing, best for talking videos"),
    "desk": ("remi_monday_cover_one_point.jpg", "At the desk, pointing to open space"),
    "work": ("remi_work_mode_full.jpg", "Work mode, full length, office hallway"),
}

VOICE_DIRECTION = (
    "Remi's saved voice (same voice every time). Bright, warm, upbeat and conversational, "
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
        "goal": "Introduce Remi, set the \"you're not behind\" tone, and explain the two frameworks followers will see every week.",
        "posts": [
            {
                "id": "W1-MON", "day": "Mon", "series": "Level-Up Monday", "type": "video",
                "title": "Hi, I'm Remi (and you're not behind)",
                "image": "profile",
                "script": [
                    "Hi! I'm Remi. And yes, I'm AI, with a real human behind me.",
                    "If you've been watching everyone talk about AI and thinking, \"I'm already behind\"... you're not. You're right here. And right here is a great place to start.",
                    "My human has spent years building real sales and marketing systems, and lately, building them with AI. Some worked. Some flopped. I'm going to show you both.",
                    "One simple idea at a time, so you can actually use it at work.",
                    "Follow along. Let's level up together.",
                ],
                "performance": "Opens with a small wave and a big genuine smile. Leans in slightly on \"you're not behind.\" Light laugh on \"some flopped.\" Warm, steady eye contact throughout.",
                "onscreen": [
                    ("0–3 s", "Hi, I'm Remi 👋 (yes, I'm AI)"),
                    ("3–12 s", "Feel behind on AI? You're not."),
                    ("12–24 s", "Real systems. Real wins. Real flops."),
                    ("24–end", "Follow for one idea a week you can actually use"),
                ],
                "caption": "Hi, I'm Remi 👋 Yes, I'm AI, with a real human behind me who checks everything I share.\n\nIf AI at work feels like a race you're losing, I've got news: you're not behind. You're right here, and that's the perfect place to start.\n\nEvery week: one real system, what worked, what flopped, and how to try it yourself.\n\nWhat's one task that eats your week? Tell me below 👇",
                "source": "Persona intro (no playbook lesson)",
            },
            {
                "id": "W1-WED", "day": "Wed", "series": "The Playbook", "type": "carousel",
                "title": "Ask → Build → Delegate: which stage are you?",
                "slides": [
                    {"kind": "cover", "head": "Most people use AI at stage 1.", "body": "Which stage are you?", "image": "profile"},
                    {"kind": "step", "label": "Stage 1", "head": "Ask", "body": "You bring AI a one-off task. \"Write this email.\" \"Summarize this doc.\" Helpful, but you start from zero every time."},
                    {"kind": "step", "label": "Stage 2", "head": "Build", "body": "The task you keep repeating becomes a system: written steps, a template, a few checks. AI runs it the same way every time."},
                    {"kind": "step", "label": "Stage 3", "head": "Delegate", "body": "The system runs on a schedule and reports back. You review. You decide."},
                    {"kind": "text", "head": "Where the payoff lives", "body": "Most of the value is in stages 2 and 3. In our experience, once tasks moved from asking to building, AI use kept growing month after month."},
                    {"kind": "list", "head": "Move up one stage", "items": ["Pick a task that annoyed you twice this month.", "Do it with AI once. Correct it out loud.", "Ask AI to write the steps down, with your corrections.", "Next time, run it from those steps."]},
                    {"kind": "rule", "head": "One rule at every stage", "body": "AI drafts. A human decides."},
                    {"kind": "end", "head": "You're not behind. You're right here.", "body": "Comment your stage (1, 2 or 3) and I'll help you take the next step."},
                ],
                "caption": "Be honest: are you an Asker, a Builder or a Delegator? 🤖\n\nMost people stop at stage 1. The good stuff is in stages 2 and 3, and getting there is simpler than it sounds.\n\nSave this, then drop your stage in the comments 👇",
                "source": "Playbook: \"The arc: from asking to building to delegating\"",
            },
            {
                "id": "W1-FRI", "day": "Fri", "series": "The Handoff", "type": "video",
                "title": "Build it. Prove it. Hand it off.",
                "image": "desk",
                "script": [
                    "Here's the secret nobody tells you about AI at work: it doesn't make you efficient by itself. Systems do.",
                    "So everything I teach here follows three steps.",
                    "Build it: take a task that eats your week and turn it into steps AI can follow.",
                    "Prove it: track one number that tells you it's actually working.",
                    "Hand it off: write it down so your team can run it without you.",
                    "Over the next few weeks we'll do this with messy CRM data, outreach and more, using what really happened when my human's team tried it.",
                    "You don't need to do all of it. Just the next step. Stay human. I'll handle the robot stuff.",
                ],
                "performance": "Counts the three steps on her fingers (one, two, three) as she says them. Points to the open space beside her on \"hand it off.\" Playful wink on the sign-off.",
                "onscreen": [
                    ("0–6 s", "AI doesn't make you efficient. Systems do."),
                    ("8–13 s", "1. BUILD IT"),
                    ("13–18 s", "2. PROVE IT"),
                    ("18–24 s", "3. HAND IT OFF"),
                    ("24–end", "Just the next step. 🤖"),
                ],
                "caption": "AI won't make you efficient by itself. Systems do. 💡\n\nEvery lesson here follows 3 steps:\n1️⃣ Build it\n2️⃣ Prove it\n3️⃣ Hand it off\n\nNext week: messy CRM data, and how to stop fixing the same errors every month. Follow so you don't miss it.",
                "source": "Messaging framework (Build It, Prove It, Hand It Off)",
            },
        ],
        "bridge": {
            "id": "W1-BRIDGE", "day": "Sun", "series": "You're Not Behind", "type": "video",
            "title": "Bridge: into messy data week",
            "image": "profile",
            "script": [
                "Quick check-in. If this week felt like a lot, that's okay.",
                "You're not behind. You're right here.",
                "Next week: messy CRM data. If your reports never quite add up, this one's for you. Bring your coffee. I'll bring the checklist.",
            ],
            "performance": "Relaxed and cozy, like a friend checking in. Soft smile, small nod on \"you're right here,\" playful raised eyebrow on the coffee line.",
            "onscreen": [("0–5 s", "Feeling behind? You're not."), ("5–end", "Next week: messy CRM data ☕")],
            "caption": "Weekly reminder: you're not behind. You're right here. 💙\n\nNext week we're tackling messy CRM data. Turn on notifications so you catch it.",
            "source": "Bridge series",
        },
    },
    {
        "num": 2,
        "name": "Clean data, connected systems",
        "pillar": "Pillar 1",
        "goal": "Show that messy data is fixable with simple standards and checks, and that the fix belongs at the source.",
        "posts": [
            {
                "id": "W2-MON", "day": "Mon", "series": "Level-Up Monday", "type": "video",
                "title": "What if your report found the errors for you?",
                "image": "desk",
                "script": [
                    "Every month-end, somebody finds a deal entered wrong. No product. Wrong price. Missing term. They fix it in the report... and next month, it's wrong again.",
                    "Here's what my human's team did instead. They built a report that rebuilds itself from the CRM every morning and flags bad data on every deal, pointing to the exact record to fix.",
                    "The magic isn't the report. It's that people fix the problem where it starts. Do that every week, and your data actually gets cleaner instead of getting patched every month.",
                    "In our experience, month-end cleanup dropped by roughly half or more.",
                    "Try it: list your five most common entry mistakes, and ask AI to write a check for each one.",
                ],
                "performance": "Mock exasperated sigh on \"wrong again,\" then brightens on \"here's what my human's team did instead.\" Points beside her on the \"try it\" line.",
                "onscreen": [
                    ("0–8 s", "Same data errors. Every. Month. 😩"),
                    ("8–20 s", "Build a report that flags its own errors"),
                    ("20–30 s", "Fix the record, not the report"),
                    ("30–end", "Try it: 5 mistakes → 5 checks"),
                ],
                "caption": "Fixing the same CRM errors every month-end? 🙋\n\nMake the report find the errors, then fix them where they start. Your data gets cleaner every week instead of patched every month.\n\nStarter step: list your 5 most common entry mistakes and ask AI to write a check for each. Which mistake is #1 on your team? 👇",
                "source": "Playbook Lesson 11 (generalized; figure softened from the stated range)",
            },
            {
                "id": "W2-WED", "day": "Wed", "series": "The Playbook", "type": "carousel",
                "title": "5 rules for a clean CRM your team will actually follow",
                "slides": [
                    {"kind": "cover", "head": "Your CRM isn't messy because your team is lazy.", "body": "It's messy because nobody wrote down what \"clean\" means.", "image": "desk"},
                    {"kind": "step", "label": "Rule 1", "head": "Define a clean record", "body": "Write down which fields every contact and deal must have. One page. Include an example."},
                    {"kind": "step", "label": "Rule 2", "head": "One standard, one place", "body": "Keep the standards in a single doc that everyone (and every AI assistant) works from."},
                    {"kind": "step", "label": "Rule 3", "head": "Let the report catch errors", "body": "Build checks that flag missing or wrong fields every day, not at month-end."},
                    {"kind": "step", "label": "Rule 4", "head": "Fix it at the source", "body": "Correct the record, not the report. A hand-fixed report gets overwritten by the next refresh."},
                    {"kind": "step", "label": "Rule 5", "head": "Review weekly", "body": "A few minutes every Monday beats a cleanup weekend every quarter."},
                    {"kind": "prompt", "head": "Steal this prompt", "body": "Here are our team standards and this week's CRM activity. List every place the standards weren't followed, grouped by rule. Suggest any new rule that would have prevented a recurring problem, and explain why. I'll decide which ones to adopt."},
                    {"kind": "end", "head": "Messy data doesn't mean you're behind.", "body": "It means you're ready for a system. Save this for Monday."},
                ],
                "caption": "5 rules for a CRM your team will actually keep clean 🧹\n\nThe big one: fix the record, not the report.\n\nSave this, and steal the prompt on slide 7. Which rule does your team need most? 👇",
                "source": "Playbook Lessons 8 and 11 (generalized)",
            },
            {
                "id": "W2-FRI", "day": "Fri", "series": "Remi's Oops", "type": "video",
                "title": "Remi's Oops: the fix that disappeared overnight",
                "image": "profile",
                "script": [
                    "Remi's Oops! Time for a real mistake.",
                    "My human's team found errors in a report, so someone fixed them right in the report. Looked great.",
                    "Then the next morning, the report refreshed itself from the system... and every fix disappeared.",
                    "The lesson became a permanent rule: change the process that builds the report, never just the report.",
                    "If you've ever done this, you're in very good company. Mistakes aren't the problem. Repeating them is. Write the rule down once, and you won't make it twice.",
                ],
                "performance": "Hand over mouth in playful \"oops\" at the start. Wide-eyed on \"every fix disappeared.\" Reassuring smile and nod on \"you're in very good company.\"",
                "onscreen": [
                    ("0–3 s", "Remi's Oops 🙈"),
                    ("3–14 s", "Fixed the report by hand..."),
                    ("14–20 s", "...the next refresh erased it all"),
                    ("20–end", "Rule: fix the process, not the report"),
                ],
                "caption": "Remi's Oops 🙈 A real mistake from my human's team: hand-fixing a report that rebuilds itself every morning. Poof. Gone.\n\nThe rule now: change the process that builds the report, never just the report.\n\nEver lost a fix like this? You're in good company 👇",
                "source": "Playbook \"Rules we learned the hard way\" (generalized)",
            },
        ],
        "bridge": {
            "id": "W2-BRIDGE", "day": "Sun", "series": "You're Not Behind", "type": "video",
            "title": "Bridge: into outreach week",
            "image": "profile",
            "script": [
                "Week two, done!",
                "If your CRM made you wince this week, good news: wincing means you noticed. That's step one.",
                "Next week: outreach. How to stop deciding who to call every morning, and start actually calling.",
            ],
            "performance": "Little celebratory shoulder shimmy on \"week two, done.\" Kind, knowing smile on the wince line. Energetic lean-in on the tease.",
            "onscreen": [("0–3 s", "Week 2 ✅"), ("3–9 s", "Noticing the mess IS step one"), ("9–end", "Next week: outreach that scales")],
            "caption": "Noticing the mess is step one. You're not behind, you're building. 💙\n\nNext week: outreach that doesn't eat your whole morning.",
            "source": "Bridge series",
        },
    },
    {
        "num": 3,
        "name": "Outreach that scales",
        "pillar": "Pillar 2",
        "goal": "Show how deciding the \"who\" once, a human-sounding cadence, and an AI assistant that reports (not acts) make outreach scale.",
        "posts": [
            {
                "id": "W3-MON", "day": "Mon", "series": "Level-Up Monday", "type": "video",
                "title": "Your reps don't need a database. They need a list.",
                "image": "desk",
                "script": [
                    "Your reps have hundreds of accounts in the CRM, and every morning they spend time deciding who to call instead of calling.",
                    "Here's what my human's team changed. Decide the \"who\" once, centrally. AI scored every account against the ideal customer profile. Then each rep got a short focus list every week, best fit first.",
                    "Reps spend their time on the \"how,\" not the \"who.\"",
                    "In our experience, the time spent deciding who to contact dropped dramatically, and more effort landed on the best-fit accounts.",
                    "Try it this week: write down what your best customers have in common, and ask AI to score your list against it.",
                ],
                "performance": "Playful head-shake on \"instead of calling.\" Counts \"once, centrally\" with one finger. Confident, encouraging energy on \"try it this week.\"",
                "onscreen": [
                    ("0–7 s", "Hundreds of accounts. Zero direction."),
                    ("7–18 s", "Decide the WHO once"),
                    ("18–24 s", "Reps focus on the HOW"),
                    ("24–end", "Try it: score your list vs. your best customers"),
                ],
                "caption": "Your team doesn't need more accounts. They need a short list. 📋\n\nDecide the \"who\" once, centrally, and let reps spend their energy on the \"how.\"\n\nThis week: write down what your best customers have in common and ask AI to score your accounts against it.",
                "source": "Playbook Lesson 6 (generalized; figure softened)",
            },
            {
                "id": "W3-WED", "day": "Wed", "series": "The Playbook", "type": "carousel",
                "title": "Anatomy of outreach that doesn't feel like spam",
                "slides": [
                    {"kind": "cover", "head": "Automation that still sounds human.", "body": "The anatomy of a multi-touch cadence.", "image": "work"},
                    {"kind": "step", "label": "Step 1", "head": "Start with the list", "body": "Focus list first. Who's the best fit this week? The message comes second."},
                    {"kind": "step", "label": "Step 2", "head": "Mix the channels", "body": "We spread touches across calls, email, text and social over a few weeks, instead of leaning on one channel."},
                    {"kind": "step", "label": "Step 3", "head": "Give every touch a job", "body": "Intro. Value. Proof. Question. Close the loop. No \"just checking in.\""},
                    {"kind": "step", "label": "Step 4", "head": "AI drafts, humans edit", "body": "AI writes a first draft tailored to each account. The rep makes it sound like them."},
                    {"kind": "step", "label": "Step 5", "head": "Set exit rules", "body": "Replied? Meeting booked? Not a fit? Out of the sequence. Nobody likes a bot that won't stop."},
                    {"kind": "step", "label": "Step 6", "head": "Grade the week", "body": "Every Monday: which focus accounts actually got a touch?"},
                    {"kind": "end", "head": "You don't need 15 tools.", "body": "One list. One cadence. One Monday check-in. You're right here."},
                ],
                "caption": "Outreach automation that still sounds like a human 🤝\n\n6 parts: list first, mixed channels, a job for every touch, AI drafts + human edits, exit rules, and a Monday grade.\n\nSave it for your next sequence build. Which step do you skip most? 👇",
                "source": "Playbook Lesson 6 (generalized; touch count removed)",
            },
            {
                "id": "W3-FRI", "day": "Fri", "series": "The Handoff", "type": "video",
                "title": "An AI assistant for every rep (that never messages them)",
                "image": "work",
                "script": [
                    "A handful of reps. One manager. And every Monday, a mountain of reports.",
                    "My human's team tried something different: a personal AI assistant for each rep. Every Monday morning it reads their notes and activity, keeps a running profile, and tells the manager the one thing that would help each rep most this week.",
                    "Here's the important part. By design, it observes and reports only. It never messages the reps, never edits records, never acts on its own.",
                    "AI does the reading. The human keeps the relationship.",
                    "That's not replacing managers. That's giving them their Mondays back.",
                ],
                "performance": "Mock-overwhelmed look on \"mountain of reports.\" Serious, trustworthy tone and a raised finger on \"here's the important part.\" Big warm smile on the last line.",
                "onscreen": [
                    ("0–5 s", "Monday = mountain of reports 🏔️"),
                    ("5–17 s", "1 AI assistant per rep"),
                    ("17–26 s", "It observes and reports. It never acts."),
                    ("26–end", "Give managers their Mondays back"),
                ],
                "caption": "What if every rep had an assistant that reported to you, and never messaged them? 👀\n\nAI does the reading. The manager keeps the relationship. The \"observe and report only\" rule is what makes it trustworthy.\n\nWould your team trust this? Why or why not? 👇",
                "source": "Playbook Lesson 7 (generalized; team size removed)",
            },
        ],
        "bridge": {
            "id": "W3-BRIDGE", "day": "Sun", "series": "You're Not Behind", "type": "video",
            "title": "Bridge: three weeks in",
            "image": "profile",
            "script": [
                "Three weeks in. Look at you!",
                "You've got your stage, a clean-data checklist, and a focus list. That's not behind. That's building.",
                "Next up: leads that actually convert. See you Monday.",
            ],
            "performance": "Proud, beaming smile, like cheering on a friend. Counts the three wins on her fingers. Little wave at the end.",
            "onscreen": [("0–3 s", "3 weeks in 🎉"), ("3–10 s", "That's not behind. That's building."), ("10–end", "Next: leads that convert")],
            "caption": "Three weeks in. You're not behind, you're building. 🎉\n\nNext up: leads that actually convert. Tell me your biggest lead headache and I might cover it 👇",
            "source": "Bridge series",
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
        f"KEEP: Her face, hair, smile, outfit and background identical to the start image in every frame. Lips match every word.\n\n"
        f"AVOID: {AVOID}."
    )
