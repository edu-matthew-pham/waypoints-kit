# Waypoints Kit

A small set of plain files that let any AI chat give you suggestions grounded in the Learning Waypoints framework: where a class is likely to stall, how to widen a lesson without racing ahead, a quick check that catches a misconception, a lesson sequence, slides. You keep your own planning; the kit is a lens on it.

No account, no install. Everything here is Markdown and JSON.

## Use it

1. Open a chat with an AI that can read web links (Claude, ChatGPT, etc.).
2. Paste a starter prompt (below) with the link.
3. Tell it your standard, and paste your own plan if you have one. It will offer suggestions; you choose.

## Starter prompts

**Look at my plan**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/v0.1/START-HERE.md and follow it. I teach Year 7 Science, standard AC9S7U01. Here is my plan: [paste]. What would the framework flag?

**Where will my class stall?**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/v0.1/START-HERE.md and follow it. I teach Year 7 Science, standard AC9S7U01. Where is this class most likely to get stuck, and what should I do about it?

**Slides for a lesson**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/v0.1/START-HERE.md and follow it. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Make slides I can paste into Waypoints Prepare.

## Standards

Node files for the ACARA F–10 standards (about 1,500 across all learning areas) are served by [ACARA Progressions](https://acara.learningwaypoints.com). The AI finds the right one through the [index](index/README.md), so you only need to give it the standard code or topic. If it can't fetch the file, open the standard in Progressions, use "Copy markdown", and paste it into the chat.

A few node files are also kept in `data/` as a fallback.

## What's here

- `START-HERE.md`: the file the AI reads first.
- `core.md`: the framework on one page.
- `moves.md`: the suggestions the AI can offer.
- `format-prepare.md`: the exact slide format Waypoints Prepare accepts.
- `index/`: every standard with a node file, by subject.
- `data/`: a few node files kept as a fallback.
- `examples/`: sample output.
- `tools/`: `build_index.py` regenerates `index/` from the Progressions data.

This is a proof of concept. Expect it to change.
