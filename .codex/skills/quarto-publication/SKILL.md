---
name: quarto-publication
description: Quarto scholarly and literature publishing workflow for creating, editing, validating, and organizing .qmd/.ipynb projects, theses, books, journal-style manuscripts, reports, bibliographies, citations, cross-references, front matter, appendices, PDF/HTML/DOCX/Typst output, and publication-ready Quarto project configuration. Use when Codex works on Quarto publishing tasks, especially academic writing, literature review documents, thesis/report formatting, book chapters, manuscript metadata, bibliography files, CSL styles, or render/preview troubleshooting.
---

# Quarto Publication

## Overview

Use this skill to work on Quarto documents as publication artifacts, not as generic Markdown. Preserve the author's content, verify exact Quarto syntax from official docs when uncertain, and make changes that render cleanly across the requested output formats.

## First Checks

1. Locate the concrete project root by finding `_quarto.yml`, `index.qmd`, `index.ipynb`, or a publication-specific folder.
2. Inspect existing `_quarto.yml`, YAML front matter, bibliography, CSL, template, style, and render output settings before editing.
3. Determine the publication type: single article/report, thesis, book, manuscript, website, slide deck, or mixed project.
4. Load the smallest relevant reference:
   - Read `references/publication-patterns.md` when writing or editing Quarto syntax, metadata, citations, cross-references, or project configuration.
   - Read `references/official-source-index.md` when source verification or more official links are needed.
5. If the user asks for exact current behavior, browse official Quarto docs under `https://quarto.org/docs/` before answering or editing.

## Authoring Rules

- Treat `.qmd` content as Pandoc-flavored Quarto Markdown with YAML metadata, executable code cells, and Quarto cross-reference syntax.
- Keep YAML indentation valid. Prefer `_quarto.yml` for project-wide metadata and per-document YAML for document-specific title, author, abstract, format, and citation metadata.
- Use bibliography metadata such as `bibliography: references.bib` and `csl: style.csl` only when corresponding files exist or are being created.
- Use citation keys from the bibliography exactly. Do not invent citation keys when editing literature text unless the user asks for placeholders.
- Use Quarto cross-reference labels with type prefixes such as `fig-`, `tbl-`, `eq-`, `sec-`, and `lst-`. Avoid underscores in labels because they can break LaTeX/PDF workflows.
- Prefer `quarto preview` for iterative work and `quarto render` for final validation.
- For publication projects with multiple formats, render the specific requested format first, then the whole project before final handoff if practical.

## Publication Workflows

### Create or Repair a Scholarly Document

1. Confirm the target format set: HTML, PDF, DOCX, Typst, EPUB, JATS, or another Quarto format.
2. Check front matter for title, subtitle, author entries, affiliation entries, date, abstract, keywords, bibliography, CSL, license, funding, and DOI/citation metadata as needed.
3. Ensure figures, tables, equations, appendices, and references use Quarto-supported syntax for the target formats.
4. Keep source text readable in plain Markdown; do not overuse raw LaTeX/HTML unless the target format requires it.
5. Run the narrowest render command that validates the changed path.

### Create or Repair a Book or Thesis

1. Treat the folder containing `_quarto.yml` as the book/thesis project root.
2. Keep chapter ordering in `book.chapters` explicit.
3. Keep bibliography and cross-reference settings project-wide unless a chapter has a justified local override.
4. Use `quarto preview` for authoring and `quarto render` before publication. A full render is required after global `_quarto.yml`, template, bibliography, or style changes.
5. Do not rename chapter files or move assets unless updating all references.

### Format Conversion or Output Configuration

1. Prefer Quarto format options over raw Pandoc command-line flags.
2. Keep format-specific settings under `format:` in YAML.
3. For PDF, identify the engine and template assumptions before introducing LaTeX-specific options.
4. For DOCX, use a reference document when house style matters.
5. For Typst, verify Typst-specific citation and layout behavior from official docs before changing citation processing.

## Validation

Use the smallest command that exercises the changed publication path:

```bash
quarto check
quarto preview
quarto render
quarto render path/to/file.qmd
quarto render --to pdf
quarto render --to html
quarto render --to docx
```

Report the exact command run and whether rendering succeeded. If validation is blocked, state the missing tool, missing file, unresolved citation, template error, or engine error.

## Official Sources

This skill is based on official Quarto documentation. Use `references/official-source-index.md` for the source map and `references/publication-patterns.md` for compact syntax and workflow guidance.
