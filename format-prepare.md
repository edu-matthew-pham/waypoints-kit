# Format: what Prepare accepts (Marp Markdown)

Output **one code block fenced with four backticks** containing the whole deck, and nothing outside it. (Four, because the deck may contain three-backtick blocks; the fence lets the teacher copy exact bytes.)

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

## Do not

- Do not wrap the deck in an explanation or add text outside the code block.
- Do not use `*` lists except for check-slide answer reveals.
