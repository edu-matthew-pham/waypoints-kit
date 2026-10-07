# Plan format

For plans the teacher will keep and change. The plan is a Markdown file the teacher owns: they can save it anywhere (a doc, a Project file, their drive), paste it back into a chat later, and edit it by hand. Keep it light.

## Skeleton

```
# Plan: <standard code> <title>

Class: <label, optional> · Lessons: <N> · Pace: <Consolidating | Steady | Advancing> (a hypothesis) · Updated: <date>

Assumptions: <one or two lines: what you assumed, what the teacher should check>

## Waypoint 1: <label>  [hinge] [width opportunity]
Lessons: <how many> (<one-line reason>)

### Lesson 1.1 (planned)
- Focus: <one sentence, specific to this lesson>
- Minimum width evidence: <what students show; from the waypoint's success criteria>
- Teaching for this class: <concrete moves; name the scaffold, example or misconception>
- Widening: <one or two directions that enrich this waypoint>
- Watch-out: <one sentence for a relief teacher>

## Waypoint 2: <label>
...

## Log
- <date>: <what happened or changed, and what it means for the plan>
```

## Conventions (these are what make a plan easy to change)

- **Waypoints never change.** Same waypoints, same order, every time. Only the number of lessons, the teaching and the widening change.
- **Lesson numbers are `<waypoint>.<n>`** (1.1, 1.2, 2.1). Adding or removing a lesson never renumbers the others.
- **Status** in the lesson heading: `planned`, `taught`, `skipped` or `moved`. Never rewrite a `taught` lesson; record what happened in the Log.
- **The Log is append-only.** It carries what only the teacher knows: how it went, what students did, what changed. Later suggestions should read it.
- **Keep lessons short.** The five fields, one or two lines each. If the teacher wants more on a lesson, expand that lesson only.
- **Mark class-specific gaps** with `[teacher: ...]` rather than inventing them.
- **Specific, not templated.** If a lesson's text could sit unchanged on another lesson, rewrite it. State a hinge's cascade risk once at the waypoint, not in every lesson.
- **Want more depth?** `unit-plan-extended.md` adds optional fields without changing this layout.

## Print-ready layout (only when the teacher asks)

For a plan they'll print or paste into Docs via Waypoints Print. Same content, same fields; only the layout changes. Don't use this in an ordinary chat reply, because the directives below show as raw text anywhere but Print.

- Start with front matter: `---`, `title: <code> <title>: unit plan`, `---`.
- After the header line, a **Lesson overview table**: `| Lesson | Waypoint | Focus | Status |`, one row per lesson. Keep cells short.
- An **Allocation table**: `| Waypoint | Flags | Lessons | Reason |`, one row per waypoint.
- Keep each lesson's fields as a list (long text in table cells prints badly). Wrap each lesson in `:::keep-together` … `:::` so it doesn't split across pages.
- Put `{{break}}` on its own line before each waypoint after the first.
- Leave the Log as a plain list at the end.
- If the teacher brings this version back later to adapt, treat the directives and tables as layout: keep the content, and keep or drop the layout as they prefer.
