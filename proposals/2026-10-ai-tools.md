# AI tools: revised proposal (16 October 2026)

**Status: proposal, not yet implemented.** This supersedes the earlier idea of a sixth `coach.md` mode and an executable `trial.md` format. The Kit's live files remain unchanged.

## Decision

Keep three distinct purposes:

- **`coach.md` — learning support.** Keep unchanged. Students investigate, practise, receive hints and reflect while building understanding.
- **`defend.md` — a separate student-facing conversation format.** Students explain and justify work they have *already finished*, without the AI helping them improve or rewrite it. The format is for practice and reflection, not independent assessment evidence.
- **AI tool trial guide — teacher reference, not a prompt.** A normal checklist or template is sufficient for designing classroom trials; no dedicated `trial.md` instruction mode is needed.

## 1. Proposed standalone `defend.md`

**Purpose:** help a student rehearse defending completed work by answering questions about the decisions and reasoning already present in it. This is different from coaching someone through the work.

**Proposed interaction**

1. Ask the student for their completed work, the waypoint and, if available, the task instructions. Use the node file's `success_criteria` or teacher-supplied criteria. Don't invent criteria or assume the work is the student's own.
2. Ask about **specific choices, evidence, methods or claims in the submitted work**, one short open question at a time. Wait for an answer before continuing.
3. Probe the relevant success criteria and follow up when an explanation is incomplete or inconsistent. Avoid questions that smuggle in an answer.
4. **Do not coach, rewrite, repair, suggest answers or produce a better defence.** If the student cannot explain something, note that it remained unclear and move on or invite them to revisit it later with their teacher.
5. Permit uncertainty, corrections and requests to stop. Don't treat confident speech as proof of understanding. The AI can be mistaken.
6. When the student requests a summary or finishes, give a short **descriptive, student-controlled** note covering:
   - What work and waypoint were discussed.
   - Which decisions or reasons the student actually explained.
   - What remained unclear or was not discussed.
   - One optional next question for reflection.
   - A clear limit: this was an unlocked conversation based on student-provided material, **not verified assessment evidence**.

No marks, percentages, mastery judgements or claims of authorship. The student chooses whether to share the summary with a teacher.

**Boundaries:** a prompt can copy the questioning style of an evidence tool, but cannot enforce a locked session, independent teacher transcript, identity checks, data agreements or school controls. Do not present this format as equivalent to Thinking Mode's controlled workflow.

**If approved for implementation:** add `defend.md` as its own format and update only the Kit documentation/index/bundle necessary to make the new format discoverable. Leave `coach.md` and its five modes alone. Observe the tutorials project's existing rule keeping coach prompts off code lessons; decide separately whether and where a defence activity is appropriate.

## 2. Teacher guide: evaluating AI tools (not a prompt)

A practical teacher-facing checklist can live alongside the tools roadmap or a future teacher resource page. It should **not** become an AI mode or require the Kit to open a format file. Teachers can ask an ordinary assistant to adapt it when useful.

### Core trial checklist

| Question | What to decide or record |
|---|---|
| Why trial this? | The problem, tool and intended benefit |
| Compared with what? | Existing practice, another tool, or a general chatbot using a Kit prompt |
| Who and how long? | Participants, duration, consent and school approval |
| Does it work? | Observable outcomes, teacher workload and student experience |
| Does learning last? | A comparable independent check one or two weeks later, where relevant |
| Can we trust it? | Privacy, safety, age and other terms, oversight and equitable access |
| What changes the decision? | Criteria to adopt, revise/retrial or stop |

**Trust check:** verify where student work and transcripts go, retention and training use; protections and incident handling; minimum age and education terms; what teachers can inspect and override; accessibility and school-managed access. Date and source the vendor claims, mark unknowns explicitly, and settle necessary permissions *before* involving students.

### Optional considerations by tool type

- **Help tools:** hint-first behaviour, teacher controls, independent transfer to a new problem, confidence versus actual learning.
- **Evidence tools:** compare questioning and claims with a teacher's conversation about the same finished work; consider whether language proficiency, anxiety or access changes the result. A chatbot prompt is practice, not authenticated evidence.
- **Teacher tools:** time saved, correction and editing burden, accuracy, and whether the teacher can defend decisions.

### Example comparisons

**Thinking Mode (evidence):** compare a teacher's own short conversation about completed work with Thinking Mode's defence workflow and, optionally, a student rehearsal using the proposed Kit `defend.md` in school-approved Copilot. Use the same waypoint and work, review the actual explanations, note disagreements and fairness issues, and retain teacher judgement. Confirm current vendor terms, locking, transcript access and data handling before a school trial. These three conditions do **not** offer equivalent assessment controls.

**Copilot Study and Learn (help):** compare the named mode with ordinary school-approved Copilot using Kit's unchanged `coach.md` on the same waypoint. Check whether Copilot can read Kit URLs; otherwise supply `waypoints-kit-all.md` and the relevant node content. Observe whether students receive hints before answers and can independently solve a new task one or two weeks later. Check trust and access for both options.

**Interpretation:** if a simple prompt produces equally useful behaviour, a dedicated product might not be necessary *for that behaviour*. It may still offer valuable school-level controls or contractual protections that a prompt cannot provide. These examples are trial designs, not vendor endorsements or findings.

## Next steps

1. Review the standalone `defend.md` behaviour against representative finished work before adding it to the live Kit.
2. Keep the trial checklist in teacher guidance, not in the prompt bundle.
3. No edits to `coach.md` are needed.
