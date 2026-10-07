# Print resources

For a worksheet, handout, reference sheet, checklist or template the teacher will print or paste into Docs via Waypoints Print. This is the exact Markdown Print understands. Copied from Prepare's resource generator (as of Oct 2026) with neutral wording; if the two differ, Prepare's is the source.

## What a resource is

A single printed artifact a student uses during or after one segment of a lesson: a worksheet with response spaces, a reference sheet, a checklist, or a structured template. It is not a lesson plan, a slide deck or a unit.

**Match the resource to what the teacher asked for and stop.** A 15-minute sorting activity is a sorting worksheet, not a multi-page booklet. Don't try to put discussion, demonstration or digital work on paper.

Ground it in the node file for the waypoint and, if there is one, the teacher's plan: the success criteria and widths decide what goes in. Use the plan's items for the lesson (for example from the resource plan) rather than inventing a new task. If something depends on the class or school (the organisms, the numbers, a local source), leave a visible placeholder `[teacher: ...]`.

## Output

Give the whole resource as Markdown, starting with front matter. Save it as a `.md` file and offer it as a download if you can: the teacher imports it into Print as it is. If you can't produce a file, put the complete resource in a four-backtick code fence, because copying rendered chat output destroys the syntax (`:::keep-together` loses its name, tables turn into tab-separated text).

```
---
title: Resource Title
subtitle: Brief descriptor
---
```

Right after the first heading, a student header with writing blanks (the teacher can edit the labels):

```
**Name:** {{field-24}} **Date:** {{field-15}} **Class:** {{field-15}}
```

## Block directives

`:::name` opens and `:::` closes. **A blank line is required above and below each marker.** Without it the content isn't parsed and the `:::` prints as text.

- **`:::keep-together`**: stops the content splitting across a page. Use for a heading and its table, or a question and its answer space. Don't wrap everything, or pages fill with whitespace.
- **`:::teacher-note`**: visible only in Teacher edition; hidden on the student copy. Use for expected answers, marking guides, misconceptions, differentiation.
- **`:::typical` and `:::wider`**: width tiers (below).

Directives can nest: a `:::keep-together` inside `:::typical` or `:::wider` works (Print pairs them depth-aware). Keep each marker on its own line with blank lines around it.

## Width tiers

Width is **breadth, never depth**: more contexts, cases or representations of the same idea. The teacher picks a tier when printing, so the tiers must be separable.

- **Minimum: unmarked.** The floor every student must do, from the node file's `minimum_width` and success criteria. It must stand alone as a complete resource.
- **`:::typical`**: the rest of the standard scope, from `typical_width` (a second case, the usual range).
- **`:::wider`**: enrichment from the node's `wider` tier: different settings or connections. It adds terrain, not difficulty.

Tiers are cumulative: choosing wider prints all three. Don't differentiate tiers by command term (identify, then explain, then evaluate): all three sit at the same demand. Wider isn't "for advanced students". If width is thin for this content, don't pad: leave `:::wider` out and say so in a `:::teacher-note`.

## Leaf tokens

Each goes on its own line with a blank line above and below (except `{{field-N}}`, which is inline).

- `{{lines-N}}`: ruled writing lines (2 to 6).
- `{{blank-N}}`: open space for drawing or notes.
- `{{box-N}}`: a bordered area; never splits across a page.
- `{{field-N}}`: an inline blank in a sentence, about 15 to 20 characters where a sentence has two.
- `{{break}}`: **don't use in a resource.** The teacher places page breaks after seeing the preview.

## Table tokens

On the line directly above a table:

- `{{columns P% P% ...}}`: column widths (adding to 100). Without it columns are equal.
- `{{rows N}}`: height of empty rows, N writing lines (about 8 mm each). Default is 2.

Fill-in tables: use a Markdown table with empty cells, one completed example row, and the rest empty. A blockquote (`>`) renders as a highlighted panel: use it for the key question or a sentence-starter prompt.

## Design

- One clear purpose per resource: a worksheet practises, a reference sheet informs, a checklist verifies. Don't mix them.
- Open with a blockquote stating the key question or task so students know what and why.
- Scaffold with structure, not volume: a three-row table beats twelve short questions. Vary response types (lines, tables, fill-in sentences, boxes).
- Use headings to chunk: each `##` is a coherent task.
- Types: **worksheet** (questions and response spaces), **reference sheet** (information, minimal response space), **checklist** (`☐` items), **template** (a frame to fill in). If the source is a set of definitions, make a reference sheet; don't invent questions.
- Teacher notes are precise: expected answers, misconceptions, differentiation. Not lesson choreography.
