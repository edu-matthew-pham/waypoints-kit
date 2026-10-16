# How the kit works

The logic and rules behind the prompts, in one place. For reviewers, curious teachers, and anyone who wants to change a rule. The files themselves are the source of truth; this page explains why they say what they say.

## What happens when you paste a prompt

1. Your prompt points the AI at `START-HERE.md` and says to treat it as instructions. The prompt, not the fetched file, carries the key rules, because AI assistants give less weight to instructions found inside a fetched page than to what you type.
2. The AI reads `core.md` (the framework on one page) and `moves.md` (the suggestions it can offer).
3. It opens the **node file** for your standard, found through `index/<subject>.md`. This is the source of truth for the waypoint sequence and what each waypoint covers. The AI must say which files it opened, so you can see whether the answer rests on the node file.
4. If your request needs a format, it also reads that file: `plan-format.md`, `assessment.md`, `coach.md`, `defend.md`, `format-print.md`, `format-prepare*.md` or `follow-ups.md`.
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
| `defend.md` | Separate questions about finished work, one at a time, without hints or rewriting; student-controlled descriptive practice summary, not assessment evidence |
| `format-print.md`, `format-prepare*.md` | Exact output formats for Waypoints Print and Prepare; width tiers map to `typical` and `wider` blocks |
| `follow-ups.md` | Glossary, resource plan and student view; flag a pre-built example that mentions a later waypoint's idea, and let the teacher decide |

## What the kit leaves out compared with Planner

A lighter, plain-file version of Planner's core logic. No saved plans, no merging several standards, no class data or pace index, no review screens or tutorials. Teachers can do those themselves if they need to.

## Known limits

- The framework summary in `core.md` is one person's reading and is being reviewed (see `REVIEW.md`).
- Different assistants follow the rules with different reliability; results are suggestions to review.
- Evidence for unsupervised AI tutoring is thin, especially for younger students. Coach mode leans on thinking first, checking and reflecting for that reason.
- Curriculum data is derived from ACARA material (see `NOTICE.md`); where each file comes from is in `SOURCES.md`.

## Changing a rule

Edit the relevant file, run `python3 tools/build_bundle.py` to regenerate `waypoints-kit-all.md`, and try it with a prompt. If you change the node files or glossaries, also run `tools/build_index.py`.
