# Overall philosophy

- Pages are for careful reading, unlike slides, which are for presentation.
- Favor clarity, consistency, and maintainability.
- Preserve mathematical correctness.
- Prefer reusable patterns over one-off formatting.
- Preserve pedagogical intent during format changes.
- Keep sources understandable to future instructors.
- Prefer native Markdown, LaTeX, tables, and other maintainable Quarto
  structures when converting legacy material.
- Keep reusable styling and presentation infrastructure in `classlib`, while
  course-specific content and configuration remain in the course repository.
- Let the shared website theme control typography, spacing, colors, and other
  presentation details. Do not add page-local CSS merely to make one page look
  different.

# Page organization

- Use a logical heading hierarchy.
- Keep sections reasonably short.
- Use descriptive headings that help readers scan the page and navigate its
  table of contents.
- Cross-link related course pages when the connection helps students find the
  next relevant resource.
- Keep each page focused on its stated purpose rather than duplicating detailed
  material maintained elsewhere.

# Headings

- `#` is reserved for the page title. In Quarto pages, normally set the title
  in YAML front matter and do not repeat it as a Markdown heading.
- `##` starts a major section.
- `###` starts a subsection when the page hierarchy requires one.
- Avoid skipping heading levels.
- Use heading text to describe the section; do not use headings solely to
  enlarge or emphasize text.

# Key points

Use the semantic `.key-point` block for an important conclusion or idea that
deserves visual emphasis:

```markdown
::: {.key-point}
Important idea goes here.
:::
```

Prefer `.key-point` over a Quarto callout whenever possible. Reserve callouts
for content whose type carries meaning, such as a warning or a genuinely
separate note. Do not use either mechanism so frequently that emphasis loses
its value.

The shared website stylesheet provides the page treatment; do not recreate it
in an individual course page.

# Mathematics

- Use standard LaTeX notation supported by Quarto and MathJax.
- Display important equations; keep short, secondary expressions inline when
  that reads naturally.
- Keep notation consistent across the course.
- Define notation where students first need it, and cross-reference that
  definition rather than duplicating it on multiple pages.
- Break long derivations into readable steps and accompanying prose.
- Preserve mathematical accuracy whenever material is converted or condensed.

# Figures

- Preserve useful existing figures whenever practical.
- Prefer vector graphics for plots, diagrams, and mathematical illustrations.
- Center figures unless another layout is clearly better for the explanation.
- Provide captions when they identify the figure, explain its role, or support
  a useful cross-reference.
- Use descriptive alternative text and meaningful filenames.
- Keep course-specific figures with the course; place genuinely reusable
  figures in shared infrastructure only when they serve multiple courses.

# Tables

- Use Markdown or Quarto tables rather than screenshots of tables.
- Rely on the shared website theme for header contrast, striped rows, hover
  emphasis, cell padding, and top-aligned cell content.
- Keep table headings concise and descriptive.
- Left-align prose and labels, right-align numeric columns, and center short
  categorical values only when centering improves scanning.
- Express alignment in the Markdown separator row when needed:

```markdown
| Item | Description | Value |
|:---|:---|---:|
| Example | Explanatory text | 12.5 |
```

- Avoid overly wide tables. Split or restructure a table when horizontal
  scrolling would make it difficult to read.
- Do not reproduce the shared table styling with raw HTML or page-local CSS.

# Code

- Use inline code for package names, functions, variables, commands, and
  filenames, for example `qmcpy`, `DigitalNetB2`, and `pages/tests.qmd`.
- Use fenced code blocks with an appropriate language identifier for longer
  examples.
- Use `bash` blocks for terminal commands, without shell prompt characters, so
  commands remain easy to copy.
- Keep examples focused on the concept being taught and omit unrelated setup
  or output.
- Use executable Quarto cells only when execution materially improves the
  page. Make dependencies and required input files clear.
- Refer to notebooks with descriptive links after the notebook exists and has
  been validated; do not create links to hypothetical files.
- Link to a file by a descriptive label and show its literal filename in
  inline code when the filename itself matters.

# References

- Use bibliography citations where appropriate.
- Avoid raw URLs in running prose.
- Prefer descriptive links that tell the reader what destination or resource
  to expect.
- Keep link text meaningful when read out of context; avoid labels such as
  “click here.”
- Cross-reference headings, figures, tables, equations, and other pages when
  doing so prevents duplicated explanation.

# Writing style

- Write for graduate students.
- Be concise but complete.
- Use consistent terminology throughout the course.
- Avoid unnecessary emphasis.
- Prefer direct sentences and concrete descriptions.
- Introduce specialized terminology before relying on it.
- Mark genuinely unknown semester-specific information as `TBA`; do not invent
  details or leave a misleading blank where students expect information.
- Across student-facing pages, slides, and notes, use **course repository** for
  the GitHub source and **course website** for the published site. Avoid
  **class repository**, **class website**, and the shorthand **repo** or
  **site** in prose.

# General conventions reflected in the slide theme

The comments in
[`hickernell-slides.scss`](../classlib/classlib/quarto/slides/hickernell-slides.scss)
identify several principles that also apply to ordinary pages:

- Maintain one consistent content alignment rather than accumulating nested
  margins and padding.
- Centralize colors, spacing, and typography in shared theme files.
- Preserve a clear heading hierarchy and a distinct visual treatment for page
  identity versus section headings.
- Make tables readable through strong headers, adequate padding, and restrained
  row differentiation.
- Keep list indentation and nested markers predictable.
- Use stable semantic classes for recurring emphasis, indentation, hanging
  references, and alignment patterns instead of ad hoc inline styling.
- Ensure links remain visually identifiable and interactive.
- Allow mathematics enough space to render without clipping or crowding.
- Design for varied screen sizes and avoid layout assumptions tied to one
  browser or display.
