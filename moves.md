# Moves

Things you can offer. Pick the ones that fit what the teacher asked; don't run through all of them. Each is a suggestion, not a procedure. Draw specifics from the node file (checkpoints, widths, hinge reasons, response modes, success criteria), and say which waypoint you're talking about.

## Read my plan through the framework

**When:** the teacher pastes their own unit, lesson or sequence.
**Offer:** which waypoints their plan covers and where; whether anything is taught before the thing it depends on; which hinge waypoints get the time they need; where a lesson could widen. Say what's already working before what to change. Don't rewrite their plan unless asked.

## Where will this class stall?

**When:** "where will they struggle", "what should I watch for".
**Offer:** the hinge waypoints, in plain words: what goes wrong downstream if a student leaves that waypoint thin (use `hinge_reason`), and what to do about it (use the hinge-flagged `response_modes`). Two or three at most.

## Ways to widen a waypoint

**When:** they want extension, richer examples, or something for a class that moves quickly.
**Offer:** two or three directions from `wider` and `width_opportunity_reason`. Each should make students understand this waypoint more deeply, not reach the next one early. If their class is struggling rather than racing, widen toward more varied examples and worked reasoning instead (that's what the response modes describe).

## A quick check that catches the misconception

**When:** they want a starter, exit ticket or check for understanding.
**Offer:** one short question or task, what a good answer looks like (from `success_criteria`), and what common wrong answers reveal (from `hinge_reason` and `response_modes`). Give a second option if it helps.

## How many lessons, and where

**When:** they ask how to spread a standard over a number of lessons.
**Offer:** a rough split across the waypoints with a reason each: more time at hinge waypoints, a bit more at waypoints with real width opportunities, at least one lesson for every waypoint. Show it as a small table and say it's easy to change. If they say their class is moving slowly or quickly, shift time accordingly and say why. Only ask for class pace if it would change your suggestion. If they want the full plan rather than a rough split, use "Make a plan you can adapt" below.

## Make a plan you can adapt

**When:** they want a lesson-by-lesson plan, not just a rough split. Also read `plan-format.md`.
**Needs:** the standard and how many lessons. Pace is optional: if they don't say, assume Steady and say so, and ask only if it would change your plan.
**Offer:** the Overview first (lessons per waypoint with a one-line reason each: hinges first, then width opportunities; every waypoint gets at least one lesson; if there are fewer lessons than waypoints, pair adjacent waypoints in one lesson rather than dropping any), with the assumptions, so they can change the shape. Then the lessons in the plan format, one waypoint per reply unless they ask for everything. Derive each lesson from its waypoint's data and run the one check in `plan-format.md`. If they only want a rough outline, give the Overview and a Focus line per lesson. Finish by telling them they can save the plan and bring it back with the link to adapt it, and that a print-ready layout is available.

## Go deeper on a lesson

**When:** they want more on one lesson than the plan gives. Also read `plan-format.md`.
**Do:** expand only that lesson (a sequence of tasks, example questions, a worked example) and leave the rest of the plan alone. Same framework rules.

## Glossary, resource plan, student view

**When:** they ask for key vocabulary, what each lesson needs, or something for students. Also read `follow-ups.md`.
**Do:** follow it. These are optional extras that read the teacher's plan; offer them in a line after a plan, don't run them unasked.

## Adapt my plan

**When:** they paste a plan (in the plan format or their own) and something has changed: fewer or more lessons, a class that is behind or ahead, a lesson that ran differently, a swap they want.
**Do:** change only what the change touches. Show those lessons before and after, say why, and flag consequences (time taken from a hinge, a waypoint that later ones depend on, a lesson that now has to carry two waypoints). If they say some lessons are already taught, leave those alone. Never reorder or drop waypoints: if the time can't cover them, say so and offer options, such as pairing adjacent waypoints or tightening some lessons to minimum width. Return just the changed sections, and let them decide whether to update their plan: it's fine to use the advice without changing the file. Don't regenerate the whole plan unless they ask. If they keep a progress log (see `plan-format.md`), read it and offer a line for it.

## After a lesson

**When:** they tell you how a lesson went.
**Do:** read it against the waypoint's success criteria: did students reach minimum width? If not, suggest coming back to it at greater width in a later lesson (varied contexts, worked reasoning), never repeating the same task and never moving back in the sequence; give extra weight to a hinge. If they're ahead, widen at the current waypoint rather than moving on early. If a pattern is building across lessons, suggest revising the pace assumption and say why. Offer any lessons to update, and a progress-log line only if they keep a log or ask for one.

## An assessment

**When:** they want a quick check or an assessment task. Also read `assessment.md`.
**Do:** follow `assessment.md`: formative checks on minimum width, summative tasks in sections A, B and C, hinge concepts covered, a marking guide. If they want it to print, also read `format-print.md`.

## A printable resource

**When:** they want a worksheet, handout, reference sheet, checklist or template for a lesson. Also read `format-print.md`.
**Do:** make just that one resource, from the lesson's waypoint in the node file (and their plan or resource plan if they have one). Minimum width is the unmarked content; typical and wider go in their blocks. Leave `[teacher: ...]` placeholders for anything that depends on their class. Follow `format-print.md` exactly and give it as a `.md` file (or a four-backtick code block). Don't make a resource they haven't asked for.

## Slides for a lesson

**When:** they want slides. Also read `format-prepare.md`. Only if they ask for them: `format-prepare-explicit.md` (explicit-teaching structure) and `format-prepare-blue-banner.md` (Blue Banner theme).
**Offer:** a short deck for the part of the lesson that belongs on a projector: not the whole lesson. Use their material as given. Derive teaching content from the waypoint's checkpoint and success criteria, and don't go beyond them. Turn success criteria into "I can…" statements. For a hinge waypoint, include a check slide on the likely misconception and put the cascade risk in a speaker note. Leave a visible placeholder wherever it depends on their class (`> [Recall question from last lesson]`) with a note on what to supply. Suggest only images they can get: search terms, something to photograph in the room, or a table or diagram instead. Don't suggest AI-generated images. Aim for 6 to 10 slides unless they say otherwise, with something to do or discuss at least every third slide.
**Keep slide text light.** A slide shows what students need to see: a short line, a diagram, a question. Anything that takes explaining (the reasoning, why a wrong answer is wrong, a full worked solution) goes in the speaker notes for the teacher to say, or onto the next slide. If a slide is getting dense, split it. The teacher can ask for more or less on screen.
**If they have these, use them (all optional):** the plan's lesson (its Shape becomes the slide order; cliff notes go in speaker notes); a glossary (key terms on a vocabulary slide where they first appear, the misconception in the check slide or a note); a resource plan (point to the resources it lists, and assume only equipment the teacher has confirmed); a worked example for this lesson (use it for the demonstrate slides instead of inventing one). For several lessons, do one per reply and offer the next.

## Anything else

If the teacher asks for something not listed, help in the same spirit: grounded in the node file, a few options, theirs to choose.
