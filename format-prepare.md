# Format: what Prepare accepts (Marp Markdown)

Put the whole deck in **one code block fenced with four backticks**, so the teacher can copy it exactly. (Four, because the deck may contain three-backtick blocks.) You can add a short note before or after the block, but nothing goes inside it except the deck. This is the one place the kit is strict, because Prepare needs valid Marp.

## Structure

```
---
marp: true
theme: default
html: true
---

# Title slide

---

## Next slide
```

- Frontmatter first, exactly as above (`html: true` is required for badges).
- Slides are separated by `---` on its own line, with a blank line before and after.
- Speaker notes: HTML comments, `<!-- Speaker note: ... -->`.
- Standard Markdown: `#` headings, `**bold**`, `>` blockquotes, `| tables |`, Mermaid in three-backtick `mermaid` blocks.

## Lists: markers carry meaning

- `-` lists show immediately. **Use `-` for every list.**
- `*` lists reveal one item per click. Use `*` only for a hidden answer line on a check slide.

## Badges (interactive slides only)

Place immediately after the slide separator, before the heading. Content slides stay plain.

Check:
```
<span style="background:#dcfce7; color:#1a1a1a; border:1.5px solid #22c55e; padding:6px 18px; border-radius:8px; font-size:1em; font-weight:500;">✅ Check</span>
```
Activity: same pattern, background `#fef3c7`, border `#f59e0b`, text `✍️ Activity`.
Discussion: background `#dbeafe`, border `#3b82f6`, text `💬 Discussion`.

## Images (placeholders)

Always a split layout with a trailing size, and a descriptive label:

```
![bg right:40% 90%](https://placehold.co/600x800?text=Dichotomous+key+of+six+leaves)
```

- `right:40%` is the panel width; the trailing ` 90%` is how much of the panel the image fills (without it Marp crops the image).
- The `text=` label describes the intended visual, `+` for spaces. Put search terms or "photograph from your room" in the speaker note.

## Grids (several images, or text beside images)

A split layout holds one image; for several, or for text beside images, use a grid container. `grid-NxM` is N columns by M rows (each 1 to 4); write exactly as many items as cells.

```
::: grid-3x2
![](https://placehold.co/500x400?text=Specimen+A)
![](https://placehold.co/500x400?text=Specimen+B)
![](https://placehold.co/500x400?text=Specimen+C)
![](https://placehold.co/500x400?text=Specimen+D)
![](https://placehold.co/500x400?text=Specimen+E)
![](https://placehold.co/500x400?text=Specimen+F)
:::
```

- Inside a grid use inline images `![](url)`, never `![bg ...]`.
- Match placeholder shape to cell shape (near-square for `grid-2x2`, wide and short for a `grid-1x3` stack).
- Never put a caption or other text on a line inside a grid; it takes a cell. Captions go above, below or in the speaker note. One image-sourcing note per slide.
- Text above or below a grid needs no container; keep it to a line or two.
- Text beside a grid needs a grid inside a grid: `::::` outside, `:::` inside (the outer fence must be longer), and never indent a nested container. Go no deeper than one level.
- Uneven columns: `:::: grid-2x1 {{columns 35% 65%}}`, one value per column, on the fence line of the grid being sized. Default to equal columns.
- One image: use a split layout, not `grid-1x1`. Meaningful rows and columns: a table. A relationship or process: Mermaid.

## Do not

- Do not put explanation inside the code block.
- Do not use `*` lists except for check-slide answer reveals.

## Optional styles

Only if the teacher asks: `format-prepare-explicit.md` (a Kickstarter → I Do → We Do → You Do → check structure) and `format-prepare-blue-banner.md` (the Blue Banner theme). They add to this file.
