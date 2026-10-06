# Waypoints Kit

A small set of plain files that let any AI chat give you suggestions grounded in the Learning Waypoints framework: where a class is likely to stall, how to widen a lesson without racing ahead, a quick check that catches a misconception, a lesson sequence, slides. You keep your own planning; the kit is a lens on it.

No account, no install. Everything here is Markdown and JSON.

## Use it

1. Open a chat with an AI that can read web links (Claude, ChatGPT, etc.).
2. Paste a starter prompt (below) with the link.
3. Tell it your standard, and paste your own plan if you have one. It will offer suggestions; you choose.

## Starter prompts

**Look at my plan**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and follow it. I teach Year 7 Science, standard AC9S7U01. Here is my plan: [paste]. What would the framework flag?

**Where will my class stall?**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and follow it. I teach Year 7 Science, standard AC9S7U01. Where is this class most likely to get stuck, and what should I do about it?

**Slides for a lesson**
> Read https://raw.githubusercontent.com/edu-matthew-pham/waypoints-kit/main/START-HERE.md and follow it. I teach Year 7 Science, standard AC9S7U01, waypoint 2. Make slides I can paste into Waypoints Prepare.

## Standards in the kit

- `AC9S7U01`: Year 7 Science, Classification and Biodiversity (`data/`)

For other standards, export the node data from [ACARA Progressions](https://progressions.learningwaypoints.com) ("Copy markdown") and paste it into the chat.

## What's here

- `START-HERE.md`: the file the AI reads first.
- `core.md`: the framework on one page.
- `moves.md`: the suggestions the AI can offer.
- `format-prepare.md`: the exact slide format Waypoints Prepare accepts.
- `data/`: node files (the waypoint sequence for a standard).
- `examples/`: sample output.

This is a proof of concept. Expect it to change.
