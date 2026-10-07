# Plan format

For plans the teacher will keep and change. The plan is a Markdown file the teacher owns: they can save it anywhere (a doc, a Project file, their drive), paste it back into a chat later, and edit it by hand. Keep it light.

## Skeleton

```
# Plan: <standard code> <title>

Class: <label, optional> · Lessons: <N> · Pace: <Consolidating | Steady | Advancing> (a hypothesis) · Updated: <date>

## Assumptions
<one or two lines: what you assumed, what the teacher should check>

## Overview
| Waypoint | Flags | Lessons | Why |
|---|---|---|---|
| 1 <label> | Hinge | 2 | <one-line reason> |
| 2 <label> | Hinge · Width opportunity | 2 | <one-line reason> |

## Waypoint 1: <label>  [hinge] [width opportunity]
**Lessons:** <how many> (<one-line reason>)

### Lesson 1.1: <short title>
**Focus:** <one sentence, specific to this lesson>

- **Minimum width evidence:** <what students show; from the waypoint's success criteria>
- **Teaching for this class:** <concrete moves; name the scaffold, example or misconception>
- **Widening:** <one or two directions that enrich this waypoint>
- **Watch-out:** <one sentence for a relief teacher>

## Waypoint 2: <label>
...

## Notes
<optional: risks, what to do if a lesson is lost>
```

## Conventions (these are what make a plan easy to change)

- **Waypoints never change.** Same waypoints, same order, every time. Only the number of lessons, the teaching and the widening change.
- **Lesson numbers are `<waypoint>.<n>`** (1.1, 1.2, 2.1), each with a short title (a few words, what students do or learn) so the plan scans. Adding or removing a lesson never renumbers the others.
- **The plan is general.** It describes the unit, not how any lesson went. Nothing in it needs the teacher to maintain it. Progress and changes can live in an optional separate log (below), and updating the plan is the teacher's choice.
- **Keep lessons short.** Focus as a bold lead line, then the other four as bold-labelled bullets, one or two lines each. Use headings for the sections (Assumptions, Overview, Notes) and the waypoints and lessons, not for individual fields. The summary table at the top is the only table; keep lesson text out of tables. If the teacher wants more on a lesson, expand that lesson only.
- **Mark class-specific gaps** with `[teacher: ...]` rather than inventing them.
- **Specific, not templated.** If a lesson's text could sit unchanged on another lesson, rewrite it. State a hinge's cascade risk once at the waypoint, not in every lesson.
- **Want more depth?** `unit-plan-extended.md` adds optional fields without changing this layout.

## Print-ready layout (only when the teacher asks)

For a plan they'll print or paste into Docs via Waypoints Print. Same content, same fields; only the layout changes. Don't use this in an ordinary chat reply, because the directives below show as raw text anywhere but Print.

- Start with front matter: `---`, `title: <code> <title>: unit plan`, `---`.
- Tables, each with a `{{columns ...}}` line directly above it (percentages that add to 100; without it columns come out equal width):
  - The **allocation table** is already in the plan; give it `{{columns 24% 20% 10% 46%}}` (Waypoint, Flags, Lessons, Why).
  - **Summary**, two columns, `{{columns 25% 75%}}`: Standard, Year, Pace profile, Lessons, Progression endpoint, Assumed prior, Equipment and room.
  - **Lesson overview**, `{{columns 10% 20% 70%}}`: `| Lesson | Waypoint | Focus |`, one row per lesson.
- Keep each lesson's fields as a list (long text in table cells prints badly). Wrap each lesson in `:::keep-together` … `:::` so it doesn't split across pages.
- Put `{{break}}` on its own line before each waypoint after the first.
- **Pace grid (only if they ask for it).** Under a lesson, one table: `| Minimum width | Consolidating | Steady | Advancing |` with `{{columns 22% 26% 26% 26%}}`, one row per piece of minimum-width evidence for that lesson. Minimum is the floor from the node file. The other three say how this class might reach it or go wider, drawn from the node file's widths and response modes. One short line per cell, and the same waypoint in every column: pace changes how width is managed, never what is taught. If a pace grid is present, drop the "If the class needs more support / ready for more" lines it repeats.
- If the teacher brings this version back later to adapt, treat the directives and tables as layout: keep the content, and keep or drop the layout as they prefer.

## Progress log (optional, separate file)

A teacher who wants to track how the unit is going can keep a small separate Markdown file. The kit never requires one, and the plan doesn't change unless they ask. Format:

```
# Progress log: <code> <title>

- <date> · Lesson 2.1 · <what happened, what students showed, anything to change>
```

If they paste a log with their plan, read it as what has happened so far and let it inform suggestions. If they don't have one, don't ask for one. When they describe a lesson, give the suggestion first; offer a log line they can paste only if they already keep a log or ask for one.
