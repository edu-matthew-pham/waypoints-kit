# Reviewing the slide library

> **Draft, not yet reviewed.** Every deck in `library/`, the library index (`index/library.md`) and the README entry carry this label in the first slide's speaker note, the index and the README. Remove it only after a second teacher has been through the decks.

Seven Waypoints Prepare decks for Year 7 Science AC9S7U01 (Classification and Biodiversity), written to the node file `data/science/y7_science_AC9S7U01.json`. Open each deck in [Waypoints Prepare](https://prepare.learningwaypoints.com) (paste the file) so the Blue Banner layout renders. Speaker notes hold the tier tags and the first slide's slide map.

## For each deck, ask

1. **Is the science correct?** Facts, examples and answers. The "Check these facts" list below is where I am least sure.
2. **Does it match the node file's minimum width?** The slides tagged `[MINIMUM]` should teach what the waypoint's minimum width says, nothing less and nothing from a later waypoint. Typical and wider slides should enrich the same waypoint, not teach the next one.
3. **Do the hinge decks do their job?** Waypoints 2 and 3 are hinges. Part 1 builds the idea. Part 2 consolidates it with more examples, has a check at minimum width, and names the cascade risk to waypoint 4 (see the first slide's note).
4. **Do the slides read well to students?** Wording at Year 7 level, one idea per slide, nothing that overflows or is hard to read from the back of the room.

## Check these facts

- Slater: 14 legs (seven pairs); the decks use "more than 6 legs".
- Giant panda: reclassification wording in Waypoint 5. Scientists debated its placement for a long time, so the deck says "some scientists" on the worked example; check against a current source.
- Fungi: the history-and-DNA claim in Waypoint 5 (once grouped with plants).
- Coral treated as a fixed animal; Euglena and virus wording in Waypoint 2.
- Five-kingdom scheme as used by the node file, versus six kingdoms or the three domains. Check it is what your school teaches.
- Habitats in the Waypoint 1 table.
- Dichotomous keys A to F: step counts for keys A and B (18 against 16) and the deliberately flawed Key D, where earthworm and slug dead-end.
- True/false balance: each deck's checks should not all have the same answer.

## Things only a teacher can judge

- Kickstarter questions are built from the previous waypoint's minimum width, not from your actual lesson. Each has a `[teacher: ...]` note to swap it.
- Timing is a guess. The first note gives minimum, typical and wider blocks; check them against your lesson length.
- Waypoint 4 is long for one lesson (suggested split in its first note and in the index). Waypoints 1 and 5 are light at minimum width.
- Waypoint 2 success criterion 2 is typical width in the node file; check that part 1 does not lean on it.
- Placeholders: every `[teacher: ...]` should be something a teacher would reasonably fill or delete.

## When you have reviewed

Edit the decks for anything wrong, then remove "Draft, not yet reviewed" from: the first slide's speaker note in each deck, `index/library.md`, the library line in `README.md`, and this file. Regenerate the bundle with `python3 tools/build_bundle.py`.
