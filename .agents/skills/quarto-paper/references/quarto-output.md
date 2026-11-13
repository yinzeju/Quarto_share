# Quarto Manuscript Outputs

Identify the concrete project before editing/rendering. Keep shared settings in `_quarto.yml`, document metadata in front matter, the body in `.qmd`, and bibliography in `.bib`; preserve existing shared resources and house style. Use relative paths and local static submission figures.

Use structured author/affiliation metadata only from verified information. Check title, abstract, keywords, language, author correspondence, bibliography, and any required declarations. Do not add example ORCIDs, funding assertions, or approvals to a real manuscript merely to complete metadata.

Use real citation keys with Pandoc syntax such as `[@key]`. Match the target's citation backend: citeproc/CSL, natbib/BibTeX, and biblatex/Biber serve different workflows. Referenced `.bib`, `.csl`, and class/style files must exist. Journal-specific requirements belong to the manuscript, not to the global skill.

Preserve semantic headings and stable unique `fig-`, `tbl-`, `eq-`, `sec-`, and `lst-` labels, avoiding underscores. Render editable LaTeX math normally from `.qmd`; define notation and check all cross-references. Prefer editable tables and static local figures in the submission path. Raw LaTeX should be limited to necessary format-specific content because it may not carry into HTML/DOCX.

Use HTML for review when useful, journal PDF for layout, and `.tex` for source handoff. A `latex` format exports TeX; a journal PDF format with `keep-tex: true` retains the actual journal source. Locate the retained file after rendering rather than assuming that the project output directory contains it. See `latex-handoff.md` for the tested source-packaging procedure.

Typical commands, adapted to the paper's existing configuration:

```powershell
quarto inspect manuscript.qmd
quarto render manuscript.qmd --to html --no-execute
quarto render manuscript.qmd --profile submission --to elsevier-pdf --no-execute
```

The Elsevier example applies only when that local extension/profile is present. Use the actual target format/engine. Preserve the project's execution policy; use `--no-execute` for a formatting test with verified outputs, not when research execution is requested. Inspect PDF pages after rendering. Run an affected-project render after shared template/metadata/bibliography changes.

Official references for exact/current behavior:

- https://quarto.org/docs/authoring/front-matter.html
- https://quarto.org/docs/authoring/citations.html
- https://quarto.org/docs/authoring/cross-references.html
- https://quarto.org/docs/output-formats/pdf-basics.html
- https://quarto.org/docs/manuscripts/
