# AI tools: proposed Kit additions (16 October 2026)

**Status: proposals only.** Kit v0.2 is under review. This document proposes changes; it does not activate them. See `coach.md`, `HOW-IT-WORKS.md`, and the tutorials handoff `roadmap/ai-tools-handoff.md`.

## A. A sixth coach mode: Defend my work

**Suggested menu text**

> **Defend my work:** Paste finished work. I ask about your choices, one question at a time, without rewriting it. You explain your reasoning, then get a short account of what you explained and what is still unclear.

**Proposed rules for `coach.md`**

1. Ask the student to paste completed work, identify the waypoint, and optionally provide the task and its constraints. Use that waypoint's node-file `success_criteria`, or criteria the teacher provided; do not invent them.
2. Refer to specific decisions, methods, examples or claims in the student's actual work. Ask **one open question at a time**, and wait for the answer. Invite the student to explain why they chose an approach, how they checked it, or how they would respond to a changed condition.
3. Cover relevant success criteria over several turns, without making the dialogue a fixed questionnaire. If an explanation is vague, ask one focused follow-up. Never rewrite, improve or supply a defence of the work for the student.
4. Preserve the existing Kit coaching rules: one question at a time, no giveaways, a reflective check after help, stay within the waypoint, and remember that the AI may misunderstand.
5. Allow corrections and "I don't know". Never present fluency or confidence as proof of understanding. Separate missing explanations from mistaken ones.
6. On request for `summary`, or after an agreed stopping point, provide a brief **descriptive**, student-shareable account:
   - **Waypoint and work discussed:** as supplied.
   - **Explained:** particular decisions or reasons the student actually articulated.
   - **Unclear or not discussed:** gaps, unresolved questions, or criteria not yet probed.
   - **Possible next self-check:** one useful question, if appropriate.
   - **Limit:** This is an unlocked practice conversation using student-selected material; it is not independently verified assessment evidence.
   
   No marks, percentages, claims of authorship, or verdicts of mastery.

**Integration if approved:** add `defend` to the mode commands, add this sixth mode to the opening menu, adapt the `summary` behaviour for it, and regenerate `waypoints-kit-all.md` with the normal bundling script. Do not enable it for code lessons where the tutorials roadmap excludes coach prompts.

**Important distinction:** A prompt can imitate the *questions* of an evidence tool, but cannot create a locked session, a teacher-controlled transcript, school data agreements or independent assurance. This mode is **practice**, not a substitute for teacher assessment.

## B. Proposed format file: `trial.md`

**Trigger:** "Help me plan a trial of [tool]." The Kit offers a small trial plan with options, reasons and editable placeholders. The teacher makes all school-specific decisions. If essential information is missing, ask briefly or leave **[teacher to decide]**. Do not invent student numbers, duration, policy, vendor features or results.

### Fixed core (every trial)

| Element | Prompt for the teacher |
|---|---|
| Question and rationale | What is being tried, for which problem, and why? |
| Comparison | Existing practice, another tool, or a Kit prompt in a general chatbot. Use the *same* waypoint/task where possible. |
| Participation and duration | Who takes part, how many, and for how long? Provide a small-class option. |
| Measures | What observable behaviour, quality, time or student work indicates it helped? Include baseline and follow-up. |
| Delayed check | One or two weeks later, what can participants do **without** the tool? |
| Student and teacher views | Ask what was helpful, confusing, burdensome or unfair; include both perspectives. |
| Can we trust it? | Privacy, safety, terms (especially age and minors), oversight, and fair access: see checklist below. |
| Decision rule | What findings would lead to adopt, revise/retrial or stop? Who decides? |

**Trust checklist — document the evidence source, date and unknowns, not just yes/no answers:**

- **Privacy:** student data, work and transcripts; hosting, retention, deletion, training use, transfers and school agreements.
- **Safety:** scope restrictions, protections for students, escalation and incident handling.
- **Terms:** minimum age; consumer vs education terms; permitted minors, assessment uses and ownership of uploaded work.
- **Oversight:** teacher visibility, controls, ability to override, identifiable vendor accountability.
- **Access and fairness:** school-managed access, devices, accessibility, language and accommodation needs; avoid requiring personal accounts.

Treat missing assurance as a question to resolve **before** a student trial, not evidence that a product is safe. Prefer approved tools and suitable non-AI alternatives.

### Optional parts — choose only what fits

- **Help tool:** compare a hint-first interaction with existing instruction or a Kit coach prompt; observe whether it gives hints before answers, whether the teacher can set limits, and whether the student can solve a **new** task independently one or two weeks later. Record confidence before/after, without treating confidence as learning.
- **Evidence tool:** compare the tool's questions, transcript and claims with a teacher's own short conversation about the **same finished work**. Examine disagreements and fairness for quiet, nervous, multilingual and other students. Ask whether the teacher can inspect and overrule judgements. Do not assume chatbot summaries establish authorship.
- **Teacher tool:** measure preparation/review time saved, edits required, accuracy of outputs and the teacher's ability to justify the final decision.

### Plan output

1. **Question and comparison** (including what must stay constant).
2. **People, timetable and consent/approval gates** (placeholders where not known).
3. **Procedure** (short sequence for baseline, trial, immediate evidence and delayed check).
4. **Measures and capture sheet** (what will be recorded, by whom, without unnecessary personal data).
5. **Trust review** (verified / unverified / unacceptable, with evidence source and follow-up).
6. **Decision thresholds** (adopt, adjust and retry, or do not adopt).
7. **Teacher choices and open questions** (two or three reasonable variants with reasons).

## C. Worked example: Thinking Mode (evidence tool)

**Question:** Does an AI-led defence conversation help a teacher discover what students understand about their *own finished work* beyond what a short teacher conversation already reveals?

**Three conditions, same finished task and waypoint:**

1. A teacher's own short conversation about the student's choices and reasoning.
2. Thinking Mode's work-defence workflow, **only if school approval, age terms and data handling allow it**.
3. Kit's proposed **Defend my work** prompt in school-approved Copilot (not a controlled assessment session).

Use a small, voluntary, approved sample with an equitable alternative; consider changing the order across students to reduce practice effects. Compare the specific criteria each conversation reveals, teacher time, contradictions, unanswered questions, student experience and whose explanations are less well captured. A teacher examines the record and makes all judgements. One or two weeks later, invite students to explain or apply a comparable idea without AI.

**Trust gate:** confirm Thinking Mode's actual lock, transcript access, retention, model/data use, minimum age, terms, teacher override and school approvals **from current vendor documentation and school policy**. Verify whether students can inspect/challenge the record and how the system treats someone who understands but explains poorly. Do not assume an unrestricted Copilot prompt provides locks, independent transcripts or assessment evidence.

**Decision:** pilot only if protections are satisfactory; prefer the tool only if it adds useful, fair evidence beyond the teacher conversation without disproportionate workload. Otherwise use the existing teacher process or practice prompt for rehearsal only.

## D. Worked example: Copilot Study and Learn (help tool)

**Question:** Does Study and Learn help students reason independently better than using Kit's existing coach instructions in ordinary school-approved Copilot?

**Comparison:** the same waypoint, teacher-given starting task and available time; one condition uses Copilot Study and Learn, the other Copilot following Kit `coach.md`. Check **first** whether school Copilot can open Kit URLs. If it cannot, provide the bundled `waypoints-kit-all.md` and the relevant waypoint/node content directly. Confirm the bundle is current; do not pretend pasted files create platform controls.

Track whether each interaction asks before telling, offers hints rather than answers, stays within the waypoint, asks students to check claims, and permits the student to make the decisions. Ask students and teachers about clarity, effort, accessibility and frustration. One or two weeks later give an equivalent **new, unaided task** and compare demonstrated reasoning, not just initial completion or confidence.

**Trust gate:** confirm school tenancy, age suitability, permissions, data retention/training use, oversight and equitable access for both variants. A Kit prompt may reproduce questioning behaviour but does not reproduce product-level configuration, monitoring or contractual assurances.

**Decision:** choose the lighter acceptable option if learning and trust outcomes are comparable; adopt a dedicated mode only where it demonstrably adds relevant benefit or controls.

## Review before enabling

- Check all wording against the Kit's four fixed rules and its current student-mode opening.
- Decide whether summary access in a student conversation should be explicitly student-controlled; do not silently present the note to a teacher.
- Trial the prompts with representative work and mistaken explanations; inspect for leading questions, invented success criteria, rewriting and overconfident summaries.
- Verify product-specific claims and school approvals at the **date of each actual trial**. These examples are plans, not vendor endorsements or reports of results.
