# MATH 565 slide conventions

Follow the authoritative shared presentation guidance in
`../classlib/AGENTS.md`. This document records MATH 565 structure, navigation,
implementation details not yet migrated to classlib, and intentional local
exceptions.

# Slide structure

- `#` starts a major section.
- `##` starts an individual slide.
- `###` may be used as a third-level heading within a `##` slide.
- `####` may be used beneath a `###` theme heading for genuinely subordinate
  labels; do not give the theme and its child labels the same heading level.
- Write `#` section headings in title case: capitalize principal words while
  leaving articles, coordinating conjunctions, and short prepositions
  lowercase unless they begin or end the heading.
- Write `##` slide headings and `###` subheadings in sentence case: capitalize
  only the first word and proper nouns, acronyms, and mathematical notation.
- Do not place a `###` heading directly after a `#` section heading; start the
  individual slide with `##` first.
- Use `<h3>` (or our `.h3` helper class if appropriate) when heading-like
  styling is needed without adding another Markdown heading level.

## Deck and section navigation

Each deck follows this opening sequence:

1. The generated title slide identifies the course and deck. Put the deck's
   principal textbook or other overarching text reference, including the
   relevant chapter range, in the title-slide metadata beneath the deck title.
   Do not place this reference on the Course Map slide.
2. The `# Course Map` slide uses two columns:
   - **Course decks** lists and links every deck in course order, with the
     current deck marked using `.alert`.
   - **In this deck** lists and links every `#` section in the current deck,
     in presentation order.
3. The deck's instructional sections follow.

Every instructional `#` section slide must contain a bullet list of all `##`
slide headings that belong to that section, in their presentation order. The
list is a navigational outline for students. It may share the section slide
with introductory text, a figure, a tree, or other useful content. Update the
outline whenever a subordinate slide is added, removed, renamed, or reordered.
Do not include `###` subheadings in the outline. A `#` section with no
subordinate `##` slides does not need an empty list.

When a `#` section slide also contains content, decide its placement case by
case. By default, put brief framing or motivation above the child-slide links
and supporting examples, figures, or secondary material below them. Keep the
links visually prominent and easy to scan; move dense content to a `##` slide
rather than crowding the section slide.

## Cumulative terms index

Maintain the cumulative **Terms to Know** index in Deck 01. After completing
or substantially revising a lecture deck, audit it for important terminology
and add appropriate terms alphabetically. Link each term to the slide where it
first receives substantial treatment, not merely its first mention. Do not
invent links for topics that have not yet been developed. Split the index into
alphabetical ranges as needed, and keep the range headings and the Deck 01
Course Map synchronized with the index structure.

## Course terminology

Write **low discrepancy** without a hyphen, including when it modifies another
noun: low discrepancy sampling, low discrepancy sequence, and randomized low
discrepancy estimator. Preserve hyphens only in technical identifiers, file
names, URLs, and generated anchors where changing them would break references.

Use raw `<h3>` elements for the two Course Map column labels. A Markdown `###`
directly after a `#` heading can alter RevealJS slide structure.

```markdown
# Course Map

::: {.columns}
::: {.column width="45%"}
<h3>Course decks</h3>

- [Current deck](current-deck.html){.alert}
- [Next deck](next-deck.html)
:::

::: {.column width="55%"}
<h3>In this deck</h3>

- [First section](#first-section)
- [Second section](#second-section)
:::
:::
```

Register every deck in `slides/_metadata.yml` with its file, full title, and
short footer title. Each deck supplies `deck-nav-meta` in its YAML front matter
using the adjacent metadata entries. The first deck has no previous target,
the last deck has no next target, and intermediate decks provide both. The
shared theme turns this metadata into the `«` and `»` links at the bottom of
the rendered slides.

# Shared slide theme

The shared
[`hickernell-slides.scss`](../classlib/classlib/quarto/slides/hickernell-slides.scss)
theme is the authoritative source for repository-wide slide styling. Use its
existing features before adding deck-specific CSS.

Course-wide additions belong in `slides/math565-slides.scss`, which is loaded
for every deck through `slides/_metadata.yml`. Use a deck-specific stylesheet
only for a genuine exception that should not affect other MATH 565 decks.

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
  The `.hidden` class hides an element. Add `data-state="goldborder"` to a
  slide heading when the slide should have the theme's gold border.

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

# Converting Fall 2025 Keynote decks

Use the corresponding Fall 2025 Keynote deck as the initial content and
pedagogical reference when converting a lecture to Quarto. Preserve its
mathematical substance, examples, sequence, and emphasis as closely as the new
format reasonably allows before making intentional revisions during
instructor review.

Do not carry forward semester-specific logistics or references to Fall 2025
events. Remove or replace mentions of 2025 homework, assignments, due dates,
tests, announcements, and other dated course administration rather than
presenting them as current Fall 2026 information.

# Mathematics

- Prefer displayed equations.
- Keep notation consistent.
- Use Python-style zero-based indexing for samples, observations, Markov-chain
  states, and low discrepancy sequences: a sample of size $n$ is indexed from
  $0$ through $n-1$. Keep coordinate indices $1,\ldots,d$ and multilevel
  indices $1,\ldots,L$ one-based.
- Avoid overcrowded slides.
- Preserve mathematical accuracy during conversion.
- In plots, render mathematical symbol labels in a serif math font consistent
  with the deck's displayed mathematics; this applies especially to axis
  labels such as $x_1$ and $x_2$.

## Shared LaTeX macros

Treat
[`hickernell-latex-macros.js`](../classlib/classlib/quarto/slides/hickernell-latex-macros.js)
as the authoritative notation registry for RevealJS slides. The macros provide
consistency as well as convenience: changing a shared definition should
update every slide that uses the corresponding semantic command.

- Check the shared macro file before writing out notation directly.
- Use an existing macro whenever its mathematical meaning matches the
  intended notation.
- Do not reproduce a macro's current expansion in slide source. For example,
  write `\Exp`, `\Norm`, `\Prob`, `\Ex`, `\var`, `\cov`, `\reals`, `\vx`, and
  `\dif` rather than spelling out their present typographic definitions.
- Prefer semantic distribution macros such as `\Bern`, `\Bin`, `\Unif`,
  `\Norm`, `\Exp`, `\Gam`, and `\Pois`. For example, write
  `$Y\sim\Exp(\lambda)$`, not `$Y\sim\operatorname{Exp}(\lambda)$`.
- Use `\varrho` for probability mass functions and probability density
  functions, including marginal, joint, and conditional forms. Reserve `\rho`
  for correlation coefficients and other non-PMF/PDF meanings.
- For successive displayed equations, prefer one
  `\begin{gather*} ... \\ ... \end{gather*}` environment instead of multiple
  consecutive `$$ ... $$` blocks.
- When equations need shared alignment points, prefer a standalone
  `\begin{align*} ... \end{align*}` environment rather than placing
  `aligned` inside a displayed equation.
- Use `multline` or `multline*` for a single long equation that must wrap
  across lines, and use `\MoveEqLeft` as needed to position a long first line
  in a multiline display.
- When notation recurs across slides or decks, has a course-wide meaning, or
  may reasonably change later, propose a new shared macro instead of creating
  repeated local notation.
- Do not add a shared macro solely to shorten a one-off expression.

New macros should have a clear semantic name, follow the conventions already
used in the registry, and avoid silently changing an established command's
meaning. When a macro must also work in TeX or PDF output, keep the companion
`hickernell-latex-macros.tex` definition consistent.

# Figures

- Preserve existing figures whenever possible.
- Prefer vector graphics.
- Center figures unless there is a pedagogical reason not to.

## Course tree markers

Small, course-specific tree variants are named in
`slides/tree-markers.yml`. Shared marker defaults, such as width, font scale,
and CSS classes, belong under `defaults`; each entry under `markers` selects
the groups, labels, headings, or mask needed for one teaching context.

The course-wide `slides/math565-slides.scss` imports `tree-markers.scss`, so
all MATH 565 decks can use the tree and its named marker variants without
repeating theme configuration in each deck.

To add a saved marker to a slide, give its heading the
`.tree-marker-slide` class and select the preset with the `tree-marker`
attribute:

```markdown
## Random variables and distributions {.tree-marker-slide tree-marker="probability"}
```

The slide project's `tree-marker.lua` filter calls the existing
`render_tree_marker()` helper at render time, so `slides/tree-markers.yml`
remains authoritative. An unknown marker name stops the render with an error.
New markers need only a new entry under `markers` in that file.

Explicit Python calls remain supported for overview trees and existing slide
sources. Import the course helper once in a deck:

```python
from tree_markers import render_tree_marker
```

Then render the saved variant with an `asis` cell:

````markdown
## Random variables and distributions {.tree-marker-slide}

```{python}
#| echo: false
#| output: asis

print(render_tree_marker("probability"))
```
````

Position the marker element, not the slide `section`. RevealJS positions real
slides absolutely, including the children of a vertical stack. Do not set
`position: relative` or another replacement position on `.tree-marker-slide`;
doing so puts consecutive marked slides into normal document flow and offsets
later slides down the page.

Add and tune named presets as the course develops instead of copying full
`render_tree(...)` calls. Keep the full overview trees as direct renderer
calls when they require a unique composition.

### Asset paths

Published slide HTML lives under `_site/slides/`, while shared tree assets live
under `_site/classlib/`. Therefore, tree renderers and marker presets must use
`../classlib/classlib/quarto/components/trees` as their `asset_base_url`.
Do not use `classlib/classlib/...`, which would resolve beneath
`_site/slides/` on GitHub Pages.

## Image source overlay

For a sourced image, make the image itself an external link and add the
`.image-source` class to that link. The shared slide theme adds a small,
semi-transparent external-link indicator in the image's upper-right corner.
The indicator becomes more visible on hover or keyboard focus and introduces
no caption or visible source text.

Put the display width on the link rather than the nested image; the link is the
overlay's positioning wrapper:

```markdown
[![](assets/images/example.jpg){fig-alt="Concise image description"}](https://example.com/original){.image-source target="_blank" rel="noopener" style="width: 95%;" title="View image source"}
```

Use `fig-alt` for descriptive alternative text without a visible caption,
retain `target="_blank" rel="noopener"` for external sources, and use the same
pattern consistently for future slide conversions. Do not put the description
between `![` and `]`, because Quarto treats that text as a visible figure
caption.

# References

Book and article references must come from the shared metadata databases loaded by
`../classlib/classlib/quarto/slides/hickernell-slides.yml`:

- `../classlib/classlib/quarto/metadata/hickernell-texts.yml` contains books and
  other texts under `texts`.
- `../classlib/classlib/quarto/metadata/hickernell-papers.yml` contains articles
  and papers under `papers`.

Use Quarto metadata shortcodes instead of repeating citation text or publisher
URLs in a deck. For example, use `{{< meta texts.owen.short >}}` for Owen, or
link an article with
`[{{< meta papers.wsj_monte_carlo_2016.full >}}]({{< meta papers.wsj_monte_carlo_2016.publisher_url >}})`.

- Use bibliography citations.
- Avoid raw URLs on slides.
