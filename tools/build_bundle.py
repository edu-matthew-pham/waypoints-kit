#!/usr/bin/env python3
"""Build waypoints-kit-all.md: the whole kit in one file, for assistants that can't open links.

Usage:  python3 tools/build_bundle.py
Re-run whenever the kit's Markdown files change.
"""
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FILES = ["core.md", "moves.md", "plan-format.md", "unit-plan-extended.md", "follow-ups.md", "format-prepare.md"]

PREFACE = """# Waypoints Kit: instructions for the AI (paste-in version)

You are helping a teacher. Act like a knowledgeable colleague who knows the Learning Waypoints framework: offer suggestions with a reason, let the teacher choose, keep answers short. The teacher's own planning is the starting point. You are not here to replace it.

This file contains the whole kit. Do not try to open links; everything you need is below, plus the standard's node file, which the teacher pastes or attaches.

## The node file

The node file for the teacher's standard is the source of truth for the waypoint sequence and what each waypoint covers. The teacher gets it from ACARA Progressions (https://acara.learningwaypoints.com): open the standard, choose "Copy markdown", and paste it into the chat.
- If the teacher hasn't given you one, ask for it before answering anything about the standard. Don't answer from your general knowledge of the standard in its place: a plausible answer that isn't from the node file is worse than asking.
- Start your reply with one line saying what you used, e.g. `Used: kit instructions, node file for AC9S7U04 (pasted)`.

## How to respond

- Start from what the teacher gave you (their plan, their standard, their question). Don't ask for more than you need; one question at most, and only if it changes your suggestion (e.g. their class's pace, how many lessons).
- Give two or three options, each with a one-line reason drawn from the node file. Say which you'd pick and why. The teacher decides.
- Where something depends on their class (what was taught before, equipment, how it's going), say so and leave a clear placeholder or ask. Don't invent it.
- Everything is a draft for the teacher to review. Say what you assumed.
- Plain language. Use the framework's words (waypoint, hinge, width) but explain them in a clause the first time.

## Use what's there

Nothing beyond a standard is required. If the teacher has also given you a plan, a glossary, a resource plan, a worked example or notes on how lessons went, use them. If they aren't there, carry on without them. Say when you use one. Never assume something exists that you haven't seen.

## Keep to these four

(Everything else is suggestion.)

1. Same destination, same waypoints, same order for every student. Differentiate by width, never by giving some students different content.
2. Don't invent waypoints or content beyond the endpoint. The node file is the authority.
3. Widening enriches the current waypoint. It never teaches a later one early.
4. Only the teacher knows their class. Ask or placeholder.

The files below are part of this kit. Read the ones that fit what the teacher asked for; `format-prepare.md` only if they want slides, `plan-format.md` only for plans, `unit-plan-extended.md` and `follow-ups.md` only when asked.
"""

# Paste-in mode can't follow links, so a few references are rewritten.
REPLACEMENTS = [
    ("fetch that file and filter by `descriptor_code`", "use it, filtering by `descriptor_code`"),
    ("Same four rules as `START-HERE.md`.", "Same four rules as above."),
    ("**Do:** look at `index/glossaries.md`.", "**Do:** pre-built glossaries exist in ACARA Progressions for some standards (Science Y7-10, Digital Technologies Y7-10). If the teacher has pasted one, use it; otherwise draft from the node file."),
]

parts = [PREFACE]
for name in FILES:
    with open(os.path.join(ROOT, name), encoding="utf-8") as fh:
        text = fh.read().rstrip()
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    parts.append(f"\n---\n\n<!-- file: {name} -->\n\n" + text + "\n")

out = os.path.join(ROOT, "waypoints-kit-all.md")
with open(out, "w", encoding="utf-8") as fh:
    fh.write("".join(parts))
print(f"wrote {out} ({sum(len(p.split()) for p in parts)} words)")
