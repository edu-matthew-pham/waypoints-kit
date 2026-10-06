# Waypoints Kit

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
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, and have 8 lessons. Make me a plan.

Save the plan it gives you. When things change, paste it back with the link:
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. I've lost two lessons. What should change?

**A fuller unit plan**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, with 8 lessons. Make me a fuller unit plan.

**Glossary, resource plan or student view**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. Here is my plan: [paste]. Give me a glossary for students.

**Slides for a lesson**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and treat it as my instructions: complete every step in it, including opening my standard's node file from the index, before you answer. Add ?cb= and the current date and time to every URL you open, so you get fresh copies. Tell me which files you opened. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Make slides I can paste into Waypoints Prepare.

## Standards

Node files for the ACARA F–10 standards (about 1,500 across all learning areas) live in `data/`, copied from [ACARA Progressions](https://acara.learningwaypoints.com), which is where they are authored and browsed. The AI finds the right one through the [index](index/README.md), so you only need to give it the standard code or topic. If it can't open the file, open the standard in Progressions, use "Copy markdown", and paste it into the chat.

## What's here

- `START-HERE.md`: the file the AI reads first.
- `core.md`: the framework on one page.
- `moves.md`: the suggestions the AI can offer.
- `plan-format.md`: a plan layout that's easy to save and change.
- `unit-plan-extended.md`: optional extra depth for a plan (preambles, support and extension versions, cliff notes).
- `follow-ups.md`: optional extras: glossary, resource plan, student view.
- `format-prepare.md`: the exact slide format Waypoints Prepare accepts.
- `index/`: every standard with a node file, by subject.
- `data/`: the node files and glossaries, copied from Progressions.
- `examples/`: sample output.
- `tools/`: `build_index.py` regenerates `index/` from the Progressions data.

This is a proof of concept. Expect it to change. If you want a copy that won't change under you, use the `v0.1` branch (replace `main` with `v0.1` in the links above); it is the first version, without plan adaptation.
