# Quarto Publication Patterns

## Project Shape

Use `_quarto.yml` for project-level metadata and options. Use document YAML front matter for file-specific metadata. A typical scholarly project keeps source files, `references.bib`, optional CSL files, figure assets, templates, and rendered outputs under the concrete project folder.

Single article or report:

```yaml
---
title: "Article Title"
author:
  - name: "Author Name"
    affiliation: "Institution"
date: today
abstract: |
  Concise abstract text.
keywords:
  - keyword one
  - keyword two
bibliography: references.bib
csl: style.csl
format:
  html:
    toc: true
  pdf:
    documentclass: article
  docx: default
---
```

Book or thesis project:

```yaml
project:
  type: book

book:
  title: "Book or Thesis Title"
  author: "Author Name"
  chapters:
    - index.qmd
    - chapters/introduction.qmd
    - chapters/literature-review.qmd
    - chapters/methods.qmd
    - references.qmd

bibliography: references.bib
format:
  html:
    theme: cosmo
  pdf:
    documentclass: scrreprt
  docx: default
```

## Markdown and Blocks

- Use headings with `#`, `##`, and `###`. Keep heading levels stable because section numbering and cross-references depend on them.
- Leave a blank line before lists. Quarto follows Pandoc Markdown and list parsing can fail without the blank line.
- Use footnotes as `Text with note.[^n]` and define `[^n]: Note text.`.
- Use fenced divs for structured blocks:

```markdown
::: {.callout-note}
Important note content.
:::
```

## Citations

Declare bibliography files in YAML:

```yaml
bibliography:
  - references.bib
csl: apa.csl
```

Use Pandoc citation syntax:

```markdown
Prior work established the baseline [@smith2020].
Several methods are relevant [see @smith2020, pp. 12-14; @lee2022].
Smith [-@smith2020] argues that ...
```

Rules:

- Match citation keys exactly to the bibliography.
- Do not fabricate bibliography entries unless the user asks for placeholders.
- Use CSL only when the style file exists or the task includes creating or adding it.
- For Typst output, verify current citation-processing behavior from official Quarto docs before changing citation settings.

## Cross-References

Every cross-reference target needs a unique identifier with the right prefix.

Figures:

```markdown
![Descriptive caption](figures/model-architecture.png){#fig-model-architecture fig-alt="Model architecture diagram"}

As shown in @fig-model-architecture, ...
```

Tables:

```markdown
| Method | Score |
|---|---:|
| Baseline | 0.82 |

: Evaluation summary {#tbl-evaluation-summary}

See @tbl-evaluation-summary.
```

Equations:

```markdown
$$
y = Ax
$$ {#eq-linear-map}

Equation @eq-linear-map defines the map.
```

Sections:

```markdown
## Literature Review {#sec-literature-review}

See @sec-literature-review.
```

Rules:

- Use prefixes such as `fig-`, `tbl-`, `eq-`, `sec-`, and `lst-`.
- Avoid underscores in labels, especially for PDF/LaTeX rendering.
- Keep labels stable after publication because links and references may depend on them.

## Scholarly Front Matter

Use structured authors and affiliations when metadata quality matters:

```yaml
author:
  - name: "Author Name"
    orcid: 0000-0000-0000-0000
    email: author@example.org
    affiliation:
      - name: "Institution Name"
        city: "City"
        country: "Country"
abstract: |
  Abstract text can span multiple lines.
keywords:
  - Quarto
  - scholarly publishing
license: "CC BY"
funding: "The author(s) received no specific funding for this work."
```

Use `citation:` metadata for the document itself when creating citable articles or when DOI, journal, volume, issue, or container metadata must render in citation exports.

## Appendices

Mark appendix sections with the `.appendix` class when they should appear in the appendix area:

```markdown
## Acknowledgments {.appendix}

Acknowledgment text.
```

For HTML articles, Quarto can generate appendix areas for references, footnotes, reuse/license, and citation metadata when those are present.

## Output Format Notes

- HTML: use for review, web publication, search, and interactive preview.
- PDF: check engine and template assumptions before adding LaTeX-specific settings.
- DOCX: use a reference document for institutional style requirements.
- Typst: use when the project intentionally targets Typst layout; verify Typst-specific options.
- EPUB: useful for books; verify cover image and chapter metadata.

Prefer format-specific YAML blocks:

```yaml
format:
  html:
    toc: true
    number-sections: true
  pdf:
    toc: true
    number-sections: true
  docx:
    toc: true
```

## Validation Commands

Run from the concrete project root:

```bash
quarto check
quarto preview
quarto render
quarto render index.qmd
quarto render --to pdf
quarto render --to docx
```

Use `quarto preview` while authoring. Use `quarto render` before handoff or publication. For books, render the full project after global configuration changes.

