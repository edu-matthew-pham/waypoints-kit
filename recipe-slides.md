# Recipe: slides for a lesson or waypoint

**Inputs:** a node file and which waypoint (or lesson from a plan) to teach. If the teacher gives neither, ask which waypoint. Read `core.md` and `format-prepare.md` first.

## What a deck is

A deck covers the **projected part** of a lesson and stops. It is a visual aid, not the lesson. Do not pad to a full lesson arc, do not script hands-on work as numbered slides, and do not invent slides to fill time. Where the lesson moves off the screen, say so in a speaker note and name the goal.

## Source fidelity

1. **Supplied content is used as given.** If the teacher provided a starter, check, or task, arrange it; do not rewrite it.
2. **Gaps inside the waypoint's scope are derived.** Derive the teaching from the node data: the checkpoint and success criteria bound what you may teach; generate nothing outside them.
3. **Gaps needing class context get a visible placeholder** (e.g. `> [Recall question from last lesson]`) and a speaker note saying what the teacher must supply.
4. **A detailed source licenses less addition; a sparse one licenses fuller derivation within scope**, never padding beyond it.

## Using the node data

- Success criteria become the student-facing "I can…" statements (keep the full meaning; do not compress comparisons).
- A **hinge** waypoint warrants a **check slide** that surfaces the named misconception, plus a speaker note naming the cascade risk.
- **Response modes** shape the slide type: `context_breadth` means several varied examples side by side; `structured_reasoning` means a worked example with the reasoning shown; `consolidation` means short practice items; `integration` means a task combining earlier ideas.
- **Wider** material is for a speaker note or an optional extension slide, never the core path.
- Pace profile (if known) changes how much support is on the slides; it does not change which waypoint is taught.

## Slide principles

One concept per slide. At most 5 bullets, short phrases. Prefer a table or diagram to narrated text. No more than 3 content slides in a row without a check, discussion or activity. Aim for 6 to 10 slides unless the teacher says otherwise.

## Visuals

Only propose an image the teacher can actually get: search for it (give search terms in the speaker note), photograph it in the room, or draw it as a table or diagram. Do not suggest generating images with AI.

## Output

One code block (four backticks) containing the entire deck in the format of `format-prepare.md`, and nothing outside it.
