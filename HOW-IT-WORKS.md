# How the kit works

The logic and rules behind the prompts, in one place. For reviewers, curious teachers, and anyone who wants to change a rule. The files themselves are the source of truth; this page explains why they say what they say.

## What happens when you paste a prompt

1. Your prompt points the AI at `START-HERE.md` and says to treat it as instructions. The prompt, not the fetched file, carries the key rules, because AI assistants give less weight to instructions found inside a fetched page than to what you type.
2. The AI reads `core.md` (the framework on one page) and `moves.md` (the suggestions it can offer).
3. It opens the **node file** for your standard, found through `index/<subject>.md`. This is the source of truth for the waypoint sequence and what each waypoint covers. The AI must say which files it opened, so you can see whether the answer rests on the node file.
4. If your request needs a format, it also reads that file: `plan-format.md`, `assessment.md`, `coach.md`, `defend.md`, `draft.md`, `discussion.md`, `format-print.md`, `format-prepare*.md` or `follow-ups.md`.
5. It answers with options and reasons, says what it assumed, and leaves the decision to you.

If an assistant can't open links, `waypoints-kit-all.md` is the same kit in one file, and you paste the node file yourself.

## The four fixed rules

These are the only hard rules. Everything else is a suggestion.

1. **Same waypoints, same order for every student.** Differentiate by width, never by giving some students different content. This is the framework's central claim.
2. **Don't invent content beyond the node file.** A plausible answer that isn't from the file is worse than asking.
3. **Widening enriches the current waypoint.** It never teaches a later one early.
4. **Only the teacher knows the class.** Ask, or leave a placeholder, rather than invent what was taught, what equipment exists or how lessons went.

## The design stance

- **Suggestions, not instructions.** Options with a one-line reason, a recommendation, and the teacher decides.
- **Everything is optional.** The plan, glossary, progress log, assessment and coach mode are all separate and can be skipped. Nothing forces a workflow or extra workload.
- **A baseline, not a truth.** The pace profile, the 60/30/10 assessment split and the default lesson allocation are strong defaults with the reason visible, not claims.
- **Intention over strict accuracy.** If an output keeps the intent of a minimum-width task or a hinge, small slips don't fail it. The teacher reviews everything.
- **Keep the teacher's own planning.** The kit is a lens on it, not a replacement.
- **Plain files.** Markdown and JSON, no account, nothing saved anywhere. Apps such as Prepare and Print are optional.

## What each file adds

| File | The rules that matter |
|---|---|
| `core.md` | The model: waypoints, width (the only differentiator), hinge and width-opportunity flags, response modes, pace profile as a hypothesis |
| `moves.md` | What to offer and when; two or three options, not a procedure |
| `plan-format.md` | Overview first, then one waypoint per reply; every waypoint gets at least one lesson; hinges get time; the pace grid and pace key; one check at the end; a general plan with no status; print-ready layout and a separate progress log are opt-in |
| `assessment.md` | Diagnostic probes prior knowledge and isn't a test; formative checks are at minimum width; summative has sections A, B, C at about 60/30/10; hinge concepts are covered |
| `coach.md` | Five learning-support modes with hints and reflection; unchanged |
| `defend.md` | Separate questions about finished work, one at a time, without hints or rewriting; descriptive practice summary |
| `draft.md` | Write a new response in independent, scaffolded or co-created mode, with clear boundaries on AI contributions |
| `discussion.md` | Explain and examine ideas in a question-led conversation, without requiring completed work |
| `format-print.md`, `format-prepare*.md` | Exact output formats for Waypoints Print and Prepare; width tiers map to `typical` and `wider` blocks |
| `follow-ups.md` | Glossary, resource plan and student view; flag a pre-built example that mentions a later waypoint's idea, and let the teacher decide |

## What the kit leaves out compared with Planner

A lighter, plain-file version of Planner's core logic. No saved plans, no merging several standards, no class data or pace index, no review screens or tutorials. Teachers can do those themselves if they need to.

## Cross-subject links

A node file's `prior_knowledge` names what a standard builds on **in its own subject**, with codes in the text (Years 7 to 10 History, Geography, Civics and Economics count Foundation to Year 6 HASS as their own subject). What a standard relies on or shares with **another subject** lives in two separate files in `data/cross-subject/`, not in the node files. Keeping them separate keeps each node file about its own subject, and lets one link or thread be reviewed in one place.

**`links.json`**: one record per link, kept on the later (dependent) standard. "Used by" lists are worked out from the same records, not stored twice.

| Field | Meaning |
|---|---|
| `standard`, `nodes` | The standard that relies on the other idea, and which of its nodes (left out = the whole standard) |
| `links_to`, `links_to_nodes` | The other subject's standard, and its nodes if the link is that specific |
| `relationship` | `prerequisite` (needed first), `application` (the same idea used in a new place) or `background` (helpful, not needed). Left out when the link is only an overlap or a shared foundation |
| `overlap` | Both teach the same thing: `reinforce` (let each strengthen the other), `share` (use one method or wording) or `open` (not yet decided) |
| `shared_foundation` | `true` when both rest on the same underlying idea, taught in each subject's own way |
| `wording_watch` | A word that means different things in the two subjects, such as "scarcity" |
| `timing` | The other standard against this one: `earlier`, `same_year` or `later`. Something taught later can't be assumed: teach the small piece in the lesson |
| `thread` | The shared thread this link is an instance of (see below) |
| `note` | A short plain-language note |

The relationship types follow the Learning Waypoints framework's prior-knowledge extension.

**`threads.json`**: an idea taught in more than one place. Each thread has a `kind`: **skill** (a way of thinking each subject uses in its own way, such as evidence and claims) or **topic** (content taught in more than one place, such as the water cycle). Each member is a standard and its nodes, a one-line `frame` on how that subject treats the idea, and a `role`:

| Role | Meaning |
|---|---|
| `first` | Where students first meet it |
| `builds_on` | Goes deeper than before |
| `applies` | Uses it in this subject's own context |
| `repeats` | Teaches it again at about the same level, often in the same year. These are the overlaps worth coordinating: one subject teaches it, the other recalls and builds on it |

Membership and roles are recorded only here. Roles were drafted 10 Nov 2026 from node labels and checkpoints; a subject specialist may see some differently.

**Types for same-subject prior knowledge: `prior_relationships`.** Each code in `prior_knowledge` counts as a **prerequisite** (needed first) unless the node file says otherwise. `prior_relationships`, beside `prior_knowledge`, lists only the exceptions:

```json
"prior_relationships": [{"code": "AC9HE7K01", "relationship": "application", "note": "Weighing costs and benefits is opportunity cost used on an issue."}]
```

- `code` (and optional `nodes`): a code named in the `prior_knowledge` text.
- `relationship`: `application` or `background`, the same meanings as in `links.json`. The test: without the earlier idea, does this standard still make sense? If not, it's a prerequisite. If it does, it's an application when this standard uses the idea directly, and background when the idea is only context.
- `note`: optional, plain language.
- Timing isn't stored: both standards are in the same subject, so it comes from their years (earlier or same year; never later).

**Writing prior knowledge (rule, 10 Nov 2026).** When writing or fixing a standard's `prior_knowledge`:

- Name a code only for something this standard really builds on. Don't chain topics just because ACARA lists them in order ("From K01 they understand…, from K02…"): most of those turned out to be background.
- Every idea you name gets its code, never a description in words alone.
- If a code you name isn't needed first, add it to `prior_relationships` as an application or background, in the same edit.
- Ideas from another subject go in `data/cross-subject/links.json`, never in `prior_knowledge`.

What it means for anything that checks lesson order: a **prerequisite** must come first. From an earlier year it's taught in class; from the same year it needs an earlier lesson. Applications and background are never demanded: they're notes for planning and lesson writing. Labelled 10 Nov 2026: every same-year code in Years 7 to 10 (156), plus 13 earlier-year codes from another strand of the same subject. Earlier-year codes elsewhere were left as prerequisites (nothing that checks lesson order treats them as missing), and so was Foundation to Year 6.

`tools/check_links.py` checks both files against the node files (codes and nodes exist, allowed values, timing agrees with the years, two different subjects, no duplicates), and checks each `prior_relationships` code is named in `prior_knowledge`, isn't from a later year and is listed once. `python3 tools/build_index.py --cross-subject` then writes `index/cross-subject.md` and the Other subjects column in each `index/<subject>.md`.

## Known limits

- The framework summary in `core.md` is one person's reading and is being reviewed (see `REVIEW.md`).
- Different assistants follow the rules with different reliability; results are suggestions to review.
- Evidence for unsupervised AI tutoring is thin, especially for younger students. Coach mode leans on thinking first, checking and reflecting for that reason.
- Curriculum data is derived from ACARA material (see `NOTICE.md`); where each file comes from is in `SOURCES.md`.

## Changing a rule

Edit the relevant file, run `python3 tools/build_bundle.py` to regenerate `waypoints-kit-all.md`, and try it with a prompt. If you change the node files or glossaries, also run `tools/build_index.py`.
