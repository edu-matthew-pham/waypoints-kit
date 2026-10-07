# Optional style: Blue Banner theme

Use this only when the teacher asks for the Blue Banner style. It is a partner school's in-house slide convention, registered in Waypoints Prepare as the `custom-blue-banner` theme; the deck renders in that style only in Prepare (elsewhere it falls back to plain Marp). Read `format-prepare.md` first: this file adds to it. **Where anything here conflicts with `format-prepare.md` or with style preferences the teacher gives, this file wins** (for example: no badge pills, no `*` fragments, single images in a grid). When the explicit-teaching structure (`format-prepare-explicit.md`) is also in use, its stages express through this theme's vocabulary: Kickstarter → `kickstarter`, LIs/SCs → `lisc`, I Do/We Do eyebrows on plain or callout slides, You Do → `youdo`, checks → `cfu`; the eyebrow names the stage. Everything not covered here (grids, images, mermaid, speaker notes, slide count) follows the general rules unchanged.

Two kinds of rule below. **[FIRM]** rules are the theme's mechanical contract — a class name or directive that doesn't exist in the CSS produces an unstyled slide with no error, so these are not negotiable. **[HOUSE EXEMPLAR]** shapes show how the convention fills each slide type; follow them as the working default, but the *content* always comes from the lesson material, and the shape may flex where the material demands it.

### Frontmatter and banner [FIRM]

- Write `theme: custom-blue-banner` in the frontmatter instead of `theme: default`. Keep `html: true`.
- **Do not use badge pills anywhere in this deck.** The banner replaces them entirely.
- **Every slide carries a banner**, written as a spot directive immediately after the slide separator. The value is markdown: **bold the eyebrow**, then write the title after it.

```
<!-- _header: '**Kickstarter** NO NOTES ALLOWED: What can you recall?' -->
```

The bolded eyebrow is the navy block: the slide's *role* in the lesson (Kickstarter, Vocabulary, I Do: Worked Ex. 1, We Do, You Do, Check for Understanding) — short, 1–4 words. Everything after it is the slide's *content title*. With the banner carrying the title, do not repeat it as a `##` heading in the body. Use no HTML and no `&nbsp;` in the banner — the theme owns the spacing.

- Typed slides also carry a class directive on the line above or below the header:

```
<!-- _class: kickstarter -->
```

Only these class names exist: `kickstarter`, `lisc`, `vocab`, `compare`, `defpair`, `rules`, `strengths`, `limits`, `youdo`, `cfu`, and the callouts `callout`, `callout-navy`, `callout-err`, `callout-info`, `callout-ok` (plus the `verdict-false` modifier, composed only with `callout-ok`). One callout class per slide, composable with one slide-type class. Any other class name silently does nothing.

### Single images [FIRM]

Under this theme a single image sits in a `grid-2x1` beside its supporting text — never `![bg right]` split layout, never bare inline.

### Question → answer pair-slides [HOUSE EXEMPLAR]

Where the general rules use a `*` fragment to hide an answer, this deck uses a **pair of slides** instead: the question slide, then a full answers slide whose banner title begins `✓ ` and (for kickstarters) whose class becomes `kickstarter answers`. Fragments (`*` lists) are not used in this deck. Model answers restate each question's answer fully — they are revision material, not just the letter.

### The slide envelope [FIRM]

Every slide is directives then body. Placeholders in square brackets below mark what you replace — the structure around them is the part to copy:

```
<!-- _class: [slide type] -->
<!-- _header: '**[Eyebrow]** [Slide title]' -->

[body]
```

### Slide type shapes [HOUSE EXEMPLAR]

Six types have a structure you cannot infer from a description — those are shown as skeletons. The rest are ordinary markdown and are described in prose. The skeletons teach **shape only**: fill them from the lesson material, and do not treat the number of rows or items as fixed.

**kickstarter** — silent recall starter. A `grid-2x3` with an uneven column split: a short level-tag cell beside each question panel, difficulty rising down the rows. Cells alternate tag, question, tag, question:

```
<!-- _class: kickstarter -->

:::: grid-2x3 {{columns 16% 84%}}

> [Level]

> [Question — easiest]

> [Level]

> [Question — harder]

> [Level]

> [Question — hardest]

::::
```

The tag is the same on every row — it names a constant (the level the questions are pitched at), and the theme escalates the panel shading to show rising difficulty, so do not vary the tag to signal that. Three rows is typical, not required; add a row pair for a fourth question. Follow with its answers pair-slide (`_class: kickstarter answers`, same grid, full model answers).

**defpair** — two contrasted definitions beside one diagram. Note the fence depth: the outer grid uses `::::`, the inner `:::`.

```
<!-- _class: defpair -->

:::: grid-2x1

::: grid-1x2

> **[TERM A]**
>
> **Definition:** [text]
>
> **[Second aspect]:** [text]

> **[TERM B]**
>
> **Definition:** [text]
>
> **[Second aspect]:** [text]

:::

![]([image url or placeholder])

::::
```

**cfu** — multiple-choice check. Bold question line, then a list whose items open with the bold letter:

```
<!-- _class: cfu -->

**[Question]**

- **A** [option]
- **B** [option]
- **C** [option]
- **D** [option]
```

**cfu answer slide** — repeat the question and options unchanged, then add the answer blockquote. The correct option is marked by bolding **its text as well as its letter** — that second bold is what the theme highlights, so it is the only difference between the two slides' option lists:

```
<!-- _class: cfu callout-ok -->

**[Question]**

- **A** [option]
- **B** **[correct option]**
- **C** [option]
- **D** [option]

> **✓ Answer: B** — [why it is right, and briefly why each distractor is not]
```

**lisc** — learning intention & success criteria, two panels in a grid:

```
<!-- _class: lisc -->

:::: grid-2x1

> **Learning Intention**
>
> [We are learning to...]

> **Success Criteria — I can:**
>
> ✓ **[Verb]** [criterion]
>
> ✓ **[Verb]** [criterion]

::::
```

**vocab** — concept + definitions, two panels in a grid:

```
<!-- _class: vocab -->

:::: grid-2x1

> **[Label]:** [dense explanation]
>
> **[Label]:** [dense explanation]

> **KEY VOCABULARY**
>
> **[term]** — [short definition]
>
> **[term]** — [short definition]

::::
```

The remaining types are plain markdown:

**rules** — numbered conventions. An ordered list; each item opens `**SHORT ALL-CAPS RULE NAME** — ` then the rule. The theme renders the numbers as navy circles.

**strengths / limits** — model evaluation, one slide each, kept separate. A `### ✓ Strengths: ...` (or `### ✗ Limitations: ...`) band heading, then 3–4 `-` bullets.

**youdo** — independent practice. `### CORE TASKS` band then `- **Task N.**` bullets; `### Challenge Tasks` band then the stretch tasks.

**callout family** — a slide whose key line needs a treatment: `callout` (gold note), `callout-navy` (reversed emphasis band), `callout-err` (misconception / common error), `callout-info` (side information), `callout-ok` (correct-answer confirmation). The styled element is the slide's top-level `>` blockquote.

**True/False check** — `cfu callout-navy`: the statement as a top-level blockquote, `## True or False?`, then a `grid-2x1` of two blockquotes, each an emoji line above the word (`👍` / TRUE, `👎` / FALSE).

**True/False answer slide** — unlike the MC answer, the vote boxes are **not repeated**. The answer slide is `callout-ok` (no `cfu`): the statement restated as a bold paragraph, then a blockquote whose first line is the verdict and whose following paragraph explains:

```
<!-- _class: callout-ok -->

**"[Statement]"**

> **✓ TRUE**
>
> **Why?** [reason, with a concrete example]
```

For a FALSE verdict, add the `verdict-false` class and use ✗:

```
<!-- _class: callout-ok verdict-false -->

**"[Statement]"**

> **✗ FALSE**
>
> **Why?** [reason, with a concrete example]
```

The band follows the verdict — green ✓ TRUE, red ✗ FALSE.

The boxes are the voting surface; once the vote is done they have no job on screen, and the verdict band replaces them.

**We Do question sets** stay plain-classed: a two-column markdown table, `| # | Question |`, with bold `**Q1**`-style numbering and a challenge item marked `*Challenge:*`, followed by full model-answer pair-slides.

### Emphasis conventions [HOUSE EXEMPLAR]

`✓` marks success criteria and model-answer titles. Within physics-style content, keep any established colour semantics in prose (e.g. naming conventions like "weight red, normal force blue") in the speaker note, not as inline HTML.

*Copied from Waypoints Prepare's slide-generation prompt (the "Blue Banner style" option) in October 2026. Prepare is the source of truth; if it changes, this file may lag.*
