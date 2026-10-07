# Waypoints Kit

> **Draft for review (v0.2).** A proof of concept. The framework summary in `core.md` is one person's reading and is being checked by a colleague; see `REVIEW.md`. Treat everything as a starting suggestion, not a finished product. Curriculum data is derived from ACARA material: see `NOTICE.md`. Text licensed CC BY-NC-SA 4.0 (`LICENSE`).

A small set of plain files that let any AI chat give you suggestions grounded in the Learning Waypoints framework: where a class is likely to stall, how to widen a lesson without racing ahead, a quick check that catches a misconception, a lesson sequence, slides. You keep your own planning; the kit is a lens on it.

No account, no install. Everything here is Markdown and JSON.

## Use it

1. Open a chat with an AI that can read web links (Claude, ChatGPT, etc.).
2. Paste a starter prompt (below) with the link.
3. Tell it your standard, and paste your own plan if you have one. It will offer suggestions; you choose.

## Starter prompts

**Look at my plan**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01. Here is my plan: [paste]. What would the framework flag?

**Where will my class stall?**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01. Where is this class most likely to get stuck, and what should I do about it?

**Make a plan I can change later**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, and have 8 lessons. Also read plan-format.md. Make me a plan.

Save the plan it gives you. When things change, paste it back with the link:
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. Also read plan-format.md. I've lost two lessons. What should change?

**Glossary, resource plan or student view**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. Also read follow-ups.md. Give me a glossary for students.

**A worksheet or handout**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01. Also read format-print.md. Make a worksheet for the lesson where students sort organisms into kingdoms.

**Slides in a style**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Also read format-prepare.md, format-prepare-explicit.md and format-prepare-blue-banner.md. Make slides in the Blue Banner style with an explicit-teaching structure.

**Slides for a lesson**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Also read format-prepare.md. Make slides I can paste into Waypoints Prepare.

## If your AI can't open links

Download [`waypoints-kit-all.md`](waypoints-kit-all.md) (the whole kit in one file) and attach it to a chat, or paste its text. Then paste the standard's "Copy markdown" export from [ACARA Progressions](https://acara.learningwaypoints.com) and ask your question. If you use a Project, keep the file in it and it's there every time.

## Standards

Node files for the ACARA F–10 standards (about 1,500 across all learning areas) live in `data/`, copied from [ACARA Progressions](https://acara.learningwaypoints.com), which is where they are authored and browsed. The AI finds the right one through the [index](index/README.md), so you only need to give it the standard code or topic. If it can't open the file, open the standard in Progressions, use "Copy markdown", and paste it into the chat.

## What's here

- `START-HERE.md`: the file the AI reads first.
- `waypoints-kit-all.md`: the whole kit in one file, for assistants that can't open links.
- `core.md`: the framework on one page.
- `moves.md`: the suggestions the AI can offer.
- `plan-format.md`: a plan layout that's easy to save and change.
- `follow-ups.md`: optional extras: glossary, resource plan, student view.
- `format-print.md`: the exact Markdown for printable resources (worksheets, handouts) in Waypoints Print.
- `format-prepare.md`: the exact slide format Waypoints Prepare accepts.
- `format-prepare-explicit.md`, `format-prepare-blue-banner.md`: optional slide styles (explicit-teaching structure; Blue Banner theme), copied from Prepare.
- `REVIEW.md`: review sheet for checking the framework summary.
- `NOTICE.md`, `LICENSE`: ACARA attribution and the licence (CC BY-NC-SA 4.0).
- `index/`: every standard with a node file, by subject.
- `data/`: the node files and glossaries, copied from Progressions.
- `examples/`: sample output.
- `tools/`: `build_index.py` regenerates `index/` from the Progressions data; `build_bundle.py` regenerates `waypoints-kit-all.md`.

This is a proof of concept. Expect it to change. A frozen copy of this version is on the `v0.2` branch. If you want a copy that won't change under you, use the `v0.1` branch (replace `main` with `v0.1` in the links above); it is the first version, without plan adaptation.
