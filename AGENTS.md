# Research Report Workspace Router

This workspace stores shared research-report rules and reusable skills. `Report/` contains individual report projects. The workspace root is not a renderable Quarto project. These shared rules do not change explicit authorization already granted in a user's session.

## Route the work

| Request | Location | Guidance |
|---|---|---|
| Research report, explanation, Quarto slides, editable PPTX | A concrete project under `Report/` | [quarto-report](.agents/skills/quarto-report/SKILL.md); select the prose, Quarto, or PPTX branch |
| New or revised weekly research presentation | A concrete project under `Report/Weekly/` | [weekly-report](.agents/skills/weekly-report/SKILL.md) plus quarto-report and its weekly conventions |

Keep these two skills together under `.agents/skills/`. Select by report purpose, then load only the references needed for the requested output. Use available PDF, presentations, and browser tooling as supporting tools. Do not assume that tools available in the original author's environment are installed here. Formal manuscript publishing is outside this package.

## Locate the publication

1. Start from the user's named project; otherwise inspect `_quarto.yml`, `.qmd`, `.ipynb`, and nearby project documentation. Collection directories are not publication roots.
2. Read relevant source, metadata, bibliography, CSL, templates, styles, data, scripts, and outputs before editing. Preserve the existing project structure and scientific meaning.
3. Author, preview, inspect, and render from the individual report project. Use `quarto preview` for iteration and `quarto render` for delivery; rebuild the affected report after shared configuration changes.
4. Keep project-specific research notes, build scripts, data, assets, and deliverables in the publication. Keep reusable instructions centrally managed. Do not duplicate category-level agent rules or skill trees without a concrete need.

## Evidence and mathematical source

- Use the requested publication language; reports default to Chinese. Keep reusable agent instructions in clear English.
- Ground claims, data, equations, figures, and citations in supplied or actually generated evidence. Distinguish theory, observations, interpretations, hypotheses, and missing information. Do not invent results, references, author details, declarations, or priority claims.
- Preserve the user's argument order, terminology, notation, and meaning. Keep missing evidence visible as TODOs. Synthetic examples need user authorization and explicit test labels.
- Keep mathematical source editable. Read the bundled [Core convention](.agents/skills/quarto-report/references/notation-core.md) and apply it using [notation.md](.agents/skills/quarto-report/references/notation.md). Keep symbol roles, physical meanings, dimensions, and units consistent across the brief, slides, equations, and figures.
- Quarto renders LaTeX mathematics from `.qmd`. Direct PPTX uses the report skill's editable literal-LaTeX text convention unless the user specifies a different representation or the existing project uses one.
- Use supplied files and locations directly, and prefer verified local paper PDF/Markdown before online retrieval when available. Locate relevant materials from the project and workspace without requiring setup files. Ask only for genuinely missing material that blocks the task.
- Keep `.bib` and existing `.csl` resources near their publication. Use `_quarto.yml` for shared metadata and front matter for document-specific metadata. Use relative publication resource paths.
- Verify unfamiliar or potentially changed Quarto options against [official documentation](https://quarto.org/docs/).
- Preserve source materials, datasets, original figures, final outputs, and older report snapshots unless the user explicitly requests deletion.

## Validate and deliver

For slides, complete or update the detailed report brief before constructing the corresponding pages; keep full relevant derivations and traceable evidence there. Continue within the authorized request without a routine approval gate. Update the weekly content README with the finished project's actual topic and relative link.

Render requested outputs and inspect slide overviews and relevant full-size pages or PDF pages. Check mathematics, figures, tables, citations, cross-references, resource paths, clipping, and brief/output correspondence. Report actual commands, outputs, missing tools, and unresolved scientific requirements. Compilation success alone does not establish scientific validity or visual acceptance.

## Git boundaries and authorization

Report generation does not require Git setup. Detect the actual repository layout before any authorized staging or synchronization; do not initialize repositories or configure remotes merely because this template describes them.

- Before staging/committing, check status, existing staging, `git rev-parse --show-toplevel`, and `git remote -v` in the intended directory. Stage only task-related changes and preserve unrelated user work.
- Do not stage nested repositories as Git links in the workflow repository. Keep machine paths, secrets, caches, browser diagnostics, unrelated private notebook copies, and archives out of commits. The bundled Core file is an authorized part of this skill package.
- Batch a coherent revision after appropriate validation and diff review. A weekly report and its content README belong in the same checkpoint. Small isolated wording/formatting changes may wait for a substantive checkpoint.
- The original author's standing permission for automatic commit/push is not granted by distributing this template. Follow the recipient's actual session or repository authorization. If they authorize automatic checkpoints, commit/push meaningful completed revisions to their established current branch/remote without repeated confirmation.
- Verify commit and push results. On an ordinary recoverable failure, inspect and resolve the cause within scope; otherwise preserve local work and report the actual unsynced state. Never force-push or rewrite published history without explicit authorization.
