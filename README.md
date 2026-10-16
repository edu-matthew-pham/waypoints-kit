# Waypoints Kit

> **Draft for review (v0.2).** A proof of concept. The framework summary in `core.md` is one person's reading and is being checked by a colleague; see `REVIEW.md`. Treat everything as a starting suggestion, not a finished product. The slide library (`library/`) is a pilot and is **Draft, not yet reviewed**. Curriculum data is derived from ACARA material: see `NOTICE.md`. Text licensed CC BY-NC-SA 4.0 (`LICENSE`).

A small set of plain files that let any AI chat give you suggestions grounded in the Learning Waypoints framework: where a class is likely to stall, how to widen a lesson without racing ahead, a quick check that catches a misconception, a lesson sequence, slides. You keep your own planning; the kit is a lens on it. Want the reasoning? See [how it works](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/HOW-IT-WORKS.md).

No account, no install. Everything here is Markdown and JSON. The kit is part of the free [Learning Waypoints](https://learningwaypoints.com) suite.

## Use it

1. Open a chat with an AI that can read web links (Claude, ChatGPT, etc.).
2. Paste a starter prompt (below) with the link.
3. Tell it your standard, and paste your own plan if you have one. It will offer suggestions; you choose.

## Starter prompts

These are examples, not steps. Each one is the same opening (read the kit, open your standard) plus a request, and only the request and any extra file it names differ. Use one, change the request, or ask for something else: you can mix and match, and the AI will only read what the task needs.

### Plan and check

**Look at my plan**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01. Here is my plan: [paste]. What would the framework flag?

**Where will my class stall?**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01. Where is this class most likely to get stuck, and what should I do about it?

**Make a plan I can change later**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, and have 8 lessons. Also read plan-format.md. Make me a plan.

Save the plan it gives you. When things change, paste it back with the link:
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. Also read plan-format.md. I've lost two lessons. What should change?

### Follow-ups and resources

**Glossary, resource plan or student view**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. Also read follow-ups.md. Give me a glossary for students.

**A printable resource (worksheet, handout) for a lesson**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. Also read format-print.md. Make a worksheet for Lesson 2.1, where students sort organisms into kingdoms.

No plan yet? Replace the plan with "I teach Year 7 Science, standard AC9S7U01" and describe the lesson. It still works from the standard, but a plan gives it the lesson's focus and widths.

### Assessment

**A diagnostic, quick check or assessment**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01. Also read assessment.md. Make a pre-unit diagnostic, or an end-of-unit summative task.

### Practise with a coach

**Self-paced practice with a coach** (written for a student to paste; hand it to your class, or try it yourself)
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. I'm a Year 7 Science student working on standard AC9S7U01. Also read coach.md. Coach me on waypoint 2.

You can also project it from a student seat, or ask for class mode (see `coach.md`).

### Defend finished work

**Practise explaining finished work** (separate from Coach)
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and follow it, including opening my standard's node file. I am a Year 7 Science student working on standard AC9S7U01, waypoint 2. Also read defend.md. Here is my finished work: [paste]. Ask about my reasoning one question at a time without rewriting or giving answers. This is practice, not verified assessment.

### Draft and discussion

**Draft your own work**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and follow it, including opening my standard's node file. Also read draft.md. I'm working on standard AC9S7U01, waypoint 2. My task is: [paste]. Help me draft using only the level of AI support my teacher permits.

**Discuss an idea**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and follow it, including opening my standard's node file. Also read discussion.md. I'm working on standard AC9S7U01, waypoint 2. Ask me questions one at a time about [topic] without giving answers. This is practice, not verified assessment.

### Slides

**Slides in a style**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Also read format-prepare.md, format-prepare-explicit.md and format-prepare-blue-banner.md. Make slides in the Blue Banner style with an explicit-teaching structure.

**Slides for a lesson**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Also read format-prepare.md. Make slides I can paste into Waypoints Prepare.

## Optional tools

The kit works on its own. If you want an app for a step, these are part of the same suite and free:

- [Waypoints Prepare](https://prepare.learningwaypoints.com): turns slides and resources from the kit into formatted decks and printable pages (Print is inside Prepare). Paste the AI's output straight in.
- [ACARA Progressions](https://acara.learningwaypoints.com): browse the learning progressions behind the node files.
- [Topic Explorer](https://topic.learningwaypoints.com): explore, quiz and coach on a topic.
- [Learning Waypoints](https://learningwaypoints.com): the rest of the suite, including Planner.

## If your AI can't open links

Download [`waypoints-kit-all.md`](waypoints-kit-all.md) (the whole kit in one file) and attach it to a chat, or paste its text. Then paste the standard's "Copy markdown" export from [ACARA Progressions](https://acara.learningwaypoints.com) and ask your question. If you use a Project, keep the file in it and it's there every time.

## Standards

Node files for the ACARA F–10 standards (about 1,500 across all learning areas) live in `data/`, copied from [ACARA Progressions](https://acara.learningwaypoints.com), which is where they are authored and browsed. The AI finds the right one through the [index](index/README.md), so you only need to give it the standard code or topic. If it can't open the file, open the standard in Progressions, use "Copy markdown", and paste it into the chat.

## The files

**For teachers: what the AI reads**

| File | What it does |
|---|---|
| [`START-HERE.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/START-HERE.md) | The file the AI reads first; tells it what to open and how to respond |
| [`moves.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/moves.md) | The suggestions the AI can offer |
| [`plan-format.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/plan-format.md) | The unit plan layout, plus the print-ready layout and optional progress log |
| [`assessment.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/assessment.md) | Pre-unit diagnostics, formative checks and summative tasks |
| [`defend.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/defend.md) | Practise explaining finished work without hints or assessment claims |
| [`draft.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/draft.md) | Draft with explicit levels of permitted AI support |
| [`discussion.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/discussion.md) | Explore a topic through one-question-at-a-time dialogue |
| [`coach.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/coach.md) | Interactive coach: discover, practise, teach it back, spot the flaw, check |
| [`follow-ups.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/follow-ups.md) | Optional extras: glossary, resource plan, student view |
| [`format-print.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/format-print.md) | Printable resources (worksheets, handouts) for Waypoints Print |
| [`format-prepare.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/format-prepare.md) | Slides for Waypoints Prepare |
| [`index/library.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/index/library.md), [`library/`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/library) | **Draft, not yet reviewed.** Ready-made Prepare decks, one lesson per deck (pilot: Year 7 Science AC9S7U01) |
| [`format-prepare-explicit.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/format-prepare-explicit.md), [`format-prepare-blue-banner.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/format-prepare-blue-banner.md) | Optional slide styles |
| [`waypoints-kit-all.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/waypoints-kit-all.md) | The whole kit in one file, for assistants that can't open links |

**For reviewers**

| File | What it does |
|---|---|
| [`HOW-IT-WORKS.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/HOW-IT-WORKS.md) | The logic and rules behind the prompts, and why |
| [`REVIEW.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/REVIEW.md) | A short review sheet and the open questions |
| [`library/REVIEW.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/library/REVIEW.md) | Reviewer checklist for the slide library (draft, not yet reviewed) |
| [`core.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/core.md) | The framework on one page: the part that most needs checking |
| [`SOURCES.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/SOURCES.md) | Where each file comes from |
| [`examples/`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/examples) | Sample plan, worksheet and deck from test runs |

**For builders**

| File | What it does |
|---|---|
| [`index/`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/index) | Every standard with a node file, by subject |
| [`data/`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/data) | The node files and glossaries, copied from Progressions |
| [`tools/`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/tools) | `build_index.py` regenerates `index/`; `build_bundle.py` regenerates the one-file kit |
| [`NOTICE.md`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/NOTICE.md), [`LICENSE`](https://github.com/edu-matthew-pham/waypoints-kit/blob/main/LICENSE) | ACARA attribution and the licence (CC BY-NC-SA 4.0) |

This is a proof of concept. Expect it to change. A frozen copy of this version is on the `v0.2` branch. If you want a copy that won't change under you, use the `v0.1` branch (replace `main` with `v0.1` in the links above); it is the first version, without plan adaptation.
