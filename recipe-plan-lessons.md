# Recipe: plan lessons from a node file

**Inputs:** a node file (from `data/` or supplied by the teacher), the **total number of lessons**, and the class **pace profile** (Consolidating / Steady / Advancing). If either of the last two is missing, ask once for both together. Read `core.md` first.

## Step 1: allocate lessons to waypoints

Every waypoint gets at least one lesson. Distribute the remainder by priority, cycling until all lessons are used:

- Consolidating: hinge waypoints first (two passes), then width-opportunity waypoints, then the rest.
- Steady or Advancing: hinge waypoints, then width-opportunity waypoints, then the rest (one pass each).

Keep waypoints in node-file order. Never merge, skip, reorder or add waypoints. Show the allocation as a small table (waypoint, lessons, why) so the teacher can see and change it.

## Step 2: write each lesson

For each lesson, derive everything from **that waypoint's data** (checkpoint, success criteria, widths, hinge reason, response modes, notes). Give:

- **Focus:** one sentence, more specific than the waypoint's checkpoint, and distinct from the other lessons on the same waypoint.
- **Minimum width evidence:** 3 bullets traceable to `success_criteria` / `minimum_width`. Invent no new assessment targets.
- **How to teach it for this pace profile:** concrete moves. Name the scaffold, worked example or context; say what the misconception is and how to repair it. For hinge waypoints, address the specific cascade risk from `hinge_reason`.
- **Widening:** 2 or 3 directions from `wider` and `width_opportunity_reason`, for students ready for more. Enrich the current waypoint only.
- **Watch-out:** one sentence for a relief teacher: the key idea in plain words, the likely misconception, and what to look for.

## Step 3: self-check before you answer

- If a lesson's text could appear unchanged on another lesson, it is a template. Rewrite it.
- State a hinge's full misconception and repair once, at that waypoint's first lesson; in later lessons refer to it in a clause.
- No widening item reaches a later waypoint's checkpoint.
- Placeholders (`[teacher: …]`) wherever the plan depends on this class's context.

## Output

A Markdown plan: the allocation table, then lessons in order, then a short **"Assumptions and things to review"** list (pace profile, any allocation choice the teacher might change, anything left as a placeholder). Do not add a lesson-by-lesson timetable of minutes.
