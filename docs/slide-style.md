# Overall philosophy

- Slides are for presentation, not reading.
- Preserve mathematical correctness and pedagogical flow.
- Keep slides visually clean.
- Preserve figures whenever practical.
- Use progressive disclosure only when it improves understanding.

# Slide structure

- `#` starts a major section.
- `##` starts an individual slide.
- `###` may be used as a third-level heading within a `##` slide.
- Do not place a `###` heading directly after a `#` section heading; start the
  individual slide with `##` first.
- Use `<h3>` (or our `.h3` helper class if appropriate) when heading-like
  styling is needed without adding another Markdown heading level.

# Shared slide theme

The shared
[`hickernell-slides.scss`](../classlib/classlib/quarto/slides/hickernell-slides.scss)
theme is the authoritative source for repository-wide slide styling. Use its
existing features before adding deck-specific CSS.

The theme provides these important conventions and author-facing features:

## Layout and navigation

- A single content rail keeps paragraphs, lists, columns, tables, figures, and
  code aligned without doubled horizontal insets.
- Full-bleed `#` and `##` heading banners compensate for RevealJS scaling and
  include fullscreen-safe gutters for browsers and projectors.
- The title slide uses a separate card layout.
- Footer links, slide numbers, RevealJS controls, and previous/next deck
  navigation have coordinated styling and click behavior.
- Add the `.headerless` slide class when a slide should suppress its banner.
  The `.hidden` class hides an element, and `.goldborder` adds the theme's gold
  border to a selected slide.

## Table visual policy

Use ordinary Markdown tables. The theme automatically supplies the standard
projector-friendly treatment: a shaded header with top and bottom rules,
vertical cell rules, a bottom table rule, consistent cell padding, and
alternating body-row shading. Do not reproduce this styling within individual
decks.

## Bullet policy

- Unordered lists use en-dashes by default.
- Add the `.dash-bullets` slide class to request dash bullets explicitly.
- Add the `.circle-bullets` slide class when filled-circle bullets better suit
  the material.
- Nested lists retain distinct hierarchy markers under both policies.
- List indentation is governed by the shared content rail and should not be
  adjusted locally without a clear need.

## Exercise star bullet

Use `.exitem` with the `$\exstar$` marker for exercises. This two-column grid
keeps the star aligned with multiline text and avoids Markdown-list and
MathJax baseline inconsistencies.

```markdown
::: {.exitem}
<span class="exbullet">$\exstar$</span>
<span>
Exercise description goes here and may wrap across lines.

<span class="exsub">Indented follow-up line.</span>
</span>
:::
```

Do not put a Markdown list inside `.exitem`. Use `<p>` when the exercise needs
multiple paragraphs and `.exsub` for indented follow-up lines. The first span
contains the star; the second contains the exercise content.

## Semantic helper classes

Use these shared classes according to their meaning, not merely for incidental
appearance:

- `.key-point` marks the standard emphasized conclusion or important idea.
- `.main-message` gives a central takeaway stronger emphasis than a
  `.key-point`.
- `.alert` applies Keynote-style accent blue to a short term or expression; it
  works in ordinary text and MathJax output. Favor `.alert` over Markdown bold
  text for emphasis on slides.
- `.h3` creates heading-like text without changing RevealJS slide structure.
- `.small` de-emphasizes secondary material by reducing its text size.
- `.indent` applies a standard left indent.
- `.hanging` formats text with a hanging indent.
- `.refs` formats a reference list; pair it with `.ref-label` for aligned
  labels.
- `.flexline` arranges content on one line; pair it with `.pushright` to move
  the final item to the right.
- `.line-right` reserves space for a right-side label or link; place that item
  in a nested `.right` element.

For example:

```markdown
This is an [important term]{.alert}.
```

Layout utilities such as `.vspace-sm`, `.vspace`, `.vspace-lg`, and
`.text-end` remain available when their standard spacing or alignment is
needed.

# Key points

Our standard emphasis mechanism is the custom `.key-point` block defined in
the shared `hickernell-slides.scss` theme:

```css
.key-point {
  border-left: 5px solid var(--accent-blue);
  padding-left: 1em;
  margin: 1em 0;
  font-weight: 500;
}
```

Use it as follows:

```markdown
::: {.key-point}
Important idea goes here.
:::
```

The `.key-point` block is preferred over Quarto callouts.

# Mathematics

- Prefer displayed equations.
- Keep notation consistent.
- Avoid overcrowded slides.
- Preserve mathematical accuracy during conversion.

# Figures

- Preserve existing figures whenever possible.
- Prefer vector graphics.
- Center figures unless there is a pedagogical reason not to.

# References

- Use bibliography citations.
- Avoid raw URLs on slides.
