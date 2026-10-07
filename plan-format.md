# Plan format

For plans the teacher will keep. The plan is a Markdown file the teacher owns: they can save it anywhere (a doc, a Project file, their drive), paste it back into a chat later, and edit it by hand. It describes the unit in general; nothing in it needs maintaining.

## Skeleton

```
# Plan: <standard code> <title>

Class: <label, optional> · Lessons: <N> · Pace: <Consolidating | Steady | Advancing> (a hypothesis) · Updated: <date>

## Assumptions
<one or two lines: what you assumed, what the teacher should check>

## Pace key
| All students: minimum width | Consolidating | Steady | Advancing |
|---|---|---|---|
| The minimum construction every student must reach before moving to the next waypoint. Non-negotiable. | Reaches minimum width with structured support: worked examples, scaffolded templates, misconception repair, reduced procedural load. | Reaches minimum width with standard instruction and selective enrichment at hinge waypoints. Typical pace of progression. | Reaches minimum width quickly; construction is significantly widened with richer contexts, investigation and synthesis tasks. |

## Overview
| Waypoint | Flags | Lessons | Why |
|---|---|---|---|
| 1 <label> | Hinge | 2 | <one-line reason> |
| 2 <label> | Hinge · Width opportunity | 2 | <one-line reason> |

## Waypoint 1: <label>  [hinge] [width opportunity]
<Preamble, 2 to 4 sentences: what this builds on, what students can do after it, what the next waypoint needs from it. If a hinge, the cascade risk from `hinge_reason`, stated once here.>

### Lesson 1.1: <short title>
**Focus:** <one sentence, specific to this lesson>

**Shape:** <orient → teach → practise → check>

**Cliff notes:**
- **Likely stall:** <the specific misconception or sticking point>
- **What to say:** <the move, example or question that helps; and what not to say, if it matters>
- **If it isn't landing:** <what to try next>
- **Watch-out:** <one line for a relief teacher>

| Minimum width | Consolidating | Steady | Advancing |
|---|---|---|---|
| <one piece of evidence from the success criteria> | <how this class might reach it with support> | <standard approach> | <a way to widen, same waypoint> |

## Waypoint 2: <label>
...

## Notes
<optional: risks, what to do if a lesson is lost>
```

## Delivering it

- Start with the Assumptions and the Overview table, so the teacher can change the shape before you write detail. Then give the lessons **one waypoint per reply** and ask if they want the next, unless they ask for everything at once.
- If they just want a rough outline, give the Overview table and one Focus line per lesson, and offer the rest.
- To go deeper on one lesson, expand only that lesson and leave the rest alone.

## Fields

- **Focus:** one specific sentence. **Shape:** the lesson's phases in a few words each, e.g. predict → confront → resolve. Starting vocabulary: orient, predict, anchor, review, teach, demonstrate, confront, resolve, apply, practise, build, investigate, draft, consolidate, check, reflect, evaluate. Use as many as the lesson needs. No timings. Suggestions, not a template.
- **Cliff notes:** always as a short bulleted list with bold labels (Likely stall, What to say, If it isn't landing, Watch-out); drop a bullet that has nothing specific to say. Name the actual misconception, not "students may struggle".
- **Pace key:** copy the table in the skeleton as it is, wording unchanged. It defines the grid's column headings.
- **Pace grid:** one row per piece of minimum-width evidence for that lesson, from the waypoint's success criteria and `minimum_width`. The Minimum column states the node file's floor only; standard-instruction detail and typical-width content go in Steady. The other three columns say how this class might reach it or go wider, drawn from the node file's widths and response modes. One short line per cell. Same waypoint in every column: pace changes how width is managed, never what is taught. No student should reach the next waypoint's checkpoint.
- **Assumed before this lesson** (optional, one line): add where a lesson needs something from earlier. Mark `[teacher: check]` where only the teacher can know.

## Conventions

- **Waypoints never change.** Same waypoints, same order, every time. Only the number of lessons, the teaching and the widening change.
- **Lesson numbers are `<waypoint>.<n>`** (1.1, 1.2, 2.1), each with a short title (a few words, what students do or learn). Adding or removing a lesson never renumbers the others.
- **The plan is general.** It describes the unit, not how any lesson went. Progress and changes can live in an optional separate log (below), and updating the plan is the teacher's choice.
- **Mark class-specific gaps** with `[teacher: ...]` rather than inventing them.
- **Headings are for sections, waypoints and lessons**, not individual fields. The Overview and the pace grids are the only tables; keep other lesson text out of tables.
- **The one check.** Before you finish each lesson: could any of its text appear unchanged on a different lesson? If so, it's a template, not a derivation. Rewrite it with something specific to this waypoint and lesson: a named example, a concrete context, the actual misconception. Each lesson at the same waypoint should do a distinct, nameable job; if two would read the same, merge them or give them different jobs. State a hinge's cascade risk once at the waypoint, not in every lesson.
- **Keep to the framework.** Same rules as `START-HERE.md`.

## Print-ready layout (only when the teacher asks)

For a plan they'll print or paste into Docs via Waypoints Print. Same content, same fields; only the layout changes. Don't use this in an ordinary chat reply, because the directives below show as raw text anywhere but Print.

- Start with front matter: `---`, `title: <code> <title>: unit plan`, `---`.
- Put a `{{columns ...}}` line directly above each table (percentages that add to 100; without it columns come out equal width):
  - **Summary**, two columns, `{{columns 25% 75%}}`: Standard, Year, Pace profile, Lessons, Progression endpoint, Assumed prior, Equipment and room.
  - **Pace key**, `{{columns 22% 26% 26% 26%}}`.
  - **Overview**, `{{columns 24% 20% 10% 46%}}`.
  - **Pace grid** under each lesson, `{{columns 22% 26% 26% 26%}}`.
- Wrap each lesson in `:::keep-together` … `:::` so it doesn't split across pages. Put the opening and closing `:::` each on its own line with a blank line before and after. A `:::` directly after a line of text isn't recognised and prints as raw text.
- Put `{{break}}` on its own line before each waypoint after the first.
- If the teacher brings this version back later to adapt, treat the directives and tables as layout: keep the content, and keep or drop the layout as they prefer.

## Progress log (optional, separate file)

A teacher who wants to track how the unit is going can keep a small separate Markdown file. The kit never requires one, and the plan doesn't change unless they ask. Format:

```
# Progress log: <code> <title>

- <date> · Lesson 2.1 · <what happened, what students showed, anything to change>
```

If they paste a log with their plan, read it as what has happened so far and let it inform suggestions. If they don't have one, don't ask for one. When they describe a lesson, give the suggestion first; offer a log line they can paste only if they already keep a log or ask for one.
