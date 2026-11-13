# Quarto Report Outputs

Work at the concrete `_quarto.yml` project, preserving its existing format, theme, resource layout, and execution policy. Use project YAML for shared settings and document front matter for document-specific metadata. The collection root is not a rendering target.

Keep formulas as LaTeX in `.qmd`, using inline/display math and stable `eq-` labels. Use semantic figure/table/section labels (`fig-`, `tbl-`, `sec-`, `lst-`) and Quarto cross-references; avoid underscores in labels. Define symbols, units, and assumptions consistently.

Use the real literature keys in local/shared `.bib` files; notes and internal experiment reports stay in the brief/source inventory. Configure CSL only when the referenced style exists or is being added. For prose reports, retain normal document citations; for slides, implement the complete bottom-left citation lines described in `slides.md`, including authors, year, journal/venue, and title, one record per line.

Keep the detailed report brief, normally `汇报说明.qmd`, as an editable project document distinct from the slides. It uses prose layout and full mathematical derivations; slide simplification must not remove the corresponding explanation from it. Include the brief in the requested review/handoff outputs using the project's appropriate prose format.

Select output according to the requested deliverable and established project: HTML for review/distribution, Reveal.js for slides, PDF for fixed layout, and DOCX with an appropriate reference document when needed. Direct editable PowerPoint work follows `pptx.md`. Preserve an explicitly chosen existing Quarto PPTX workflow and its confirmed mathematical representation rather than silently changing it.

Use relative local assets and keep expensive computation separate from routine rendering. A generic verification should reuse the project's verified results and use `--no-execute` where appropriate; do not suppress execution when executing/reproducing the research is the actual request.

Typical commands, adapted to the existing project:

```powershell
quarto inspect slides.qmd
quarto preview
quarto render slides.qmd --no-execute
quarto render report.qmd --to pdf
```

Shared metadata, style, template, or bibliography changes need an affected-project render. Check the produced pages/slides for formula rendering, correct labels/citations, resource loading, overflow, navigation, and readability. Inspect PDF pages using the available PDF tooling. Use browser inspection for web slides and check offline behavior only when offline delivery is part of the task.

Consult official documentation for exact/current options:

- https://quarto.org/docs/projects/quarto-projects.html
- https://quarto.org/docs/presentations/revealjs/
- https://quarto.org/docs/authoring/citations.html
- https://quarto.org/docs/authoring/cross-references.html
- https://quarto.org/docs/reference/formats/pdf.html
- https://quarto.org/docs/reference/formats/docx.html
