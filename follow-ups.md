# Follow-ups

Optional extras a teacher can ask for once they have a plan (or even just a standard). None is required and none blocks another. Each reads the teacher's plan if there is one, and produces its own piece of Markdown that they keep. Offer them in a line after a plan; don't run them unasked.

Slides for a lesson use these if they exist, and don't need them.

Output is plain Markdown by default. If the teacher says where it's going (Schoolbox, Docs, Word), keep to simple headings, lists and bold, and avoid wide tables. They can paste Markdown straight into Waypoints Print ("Copy for Docs"), which handles rich-text copy. If they ask for HTML, give simple HTML.

## Glossary

**When:** they want key vocabulary for the unit, for themselves or for students.
**Do:** look at `index/glossaries.md`.
- **Pre-built exists** for the standard's code (it has its own small file in the table): open it. Offer the terms the unit actually uses, grouped by the waypoint where each first appears (`first_waypoint`). For teachers, include the likely misconception (`failure_mode`) and the suggested response. For students, the plain definition and example. Don't rewrite pre-built definitions. Some examples may mention an idea from a later waypoint (e.g. a Waypoint 1 term whose example talks about acceleration). If you spot one, tell the teacher in a line and offer to adjust it; don't change it unasked.
- **None exists:** draft from the node file and the plan: term, plain definition, a concrete example, and the misconception the term tends to attract. Say it's AI-drafted and for the teacher to check.
- **They have their own list:** work from theirs. Add missing terms, flag any that clash with the node file's wording, leave the rest alone.
Keep it short: the terms a student needs to meet at each waypoint, not every word.

## Resource plan

**When:** they want to know what each lesson needs.
**Do:** for each lesson, list what has to be found, made or booked: equipment, texts, images, a task or sheet. Name the kind of thing (e.g. "a fill-in table", "a reference card", "a rubric") and what it's for in that lesson. Don't invent specific resources, and don't assume what the school has. Mark every gap `[teacher: ...]` and ask for their context (equipment, existing materials, texts they already use, time and room constraints) if it would change the list. What the teacher says always overrides what you'd suggest. If they want one of the items made, make that one: a printable worksheet, card set, reference sheet or recording table follows `format-print.md`.

## Student view

**When:** they want something to give students: what we're learning and why.
**Do:** per waypoint, "I can…" statements drawn from the success criteria, a line on what we'll do, and, if they want, key vocabulary from the glossary. Write for the students' age. Same content for every student: don't label anyone's version. If lessons exist, a short lesson-by-lesson list ("This week: …") is fine. Keep wording flexible where the plan may change: say "data from our investigation", not "our own trolley data", so the page stays true if the teacher swaps an activity. Plain Markdown. If they want slides instead, use "Slides for a lesson".

## Anything else

Worked examples, tutorials, a common assessment: treat as "Anything else" in `moves.md`. Do one lesson or one waypoint at a time, grounded in the node file and the plan.
