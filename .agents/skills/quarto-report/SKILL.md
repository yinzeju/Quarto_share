---
name: quarto-report
description: Create or revise research reports and scientific presentations under Report, including shared production rules used by weekly-report. Develop a detailed mathematical report brief before producing Quarto slides or editable PPTX. Use for reports and talks; formal manuscript publishing is outside this package.
---

# Research Reports

Turn research materials into a faithful, readable report or presentation. Use the central workspace `AGENTS.md` for shared scientific rules and Git boundaries; work in the concrete publication under `Report/`.

## Establish the deliverable

Inspect the supplied notes, literature, experiment reports, existing source, `_quarto.yml`, styles, bibliography, assets, scripts, and final outputs. Determine whether the request concerns a prose report, Quarto slide deck, or PowerPoint file, and preserve an established format unless the user asks to change it. Reports default to Chinese.

Use the supplied files and locations directly; no source-location configuration is required. When the user refers to notes, literature, or experiment reports without filenames, search the current project and relevant workspace materials first, including for weekly reports. Search filenames with `rg --files`, then relevant content with `rg`, using the requested topic, title, or experiment keywords. Use existing project documentation to locate materials, read verified matches, and record what was actually used in the brief/source inventory. Do not scan unrelated private directories. Report an inaccessible location or a missing necessary source accurately; ask only for the material that actually blocks the requested work.

When supplied materials mention a paper, first locate its PDF and Markdown in the user's local MinerU library before searching online. Read the local-first retrieval rules in [references/writing.md](references/writing.md); use online sources only after the local lookup fails to provide the needed paper/material.

For every report, read the bundled [Core notation](references/notation-core.md) before mathematical authoring and apply it using [references/notation.md](references/notation.md). Within each report, keep symbols' mathematical roles and physical meanings consistent across sections, the brief, slides, formulas, and figures; explicitly distinguish necessary reuse.

For weekly reports, also use [weekly-report](../weekly-report/SKILL.md) for content planning and [references/weekly.md](references/weekly.md) for project location and the content directory README. The common production rules remain here.

Choose one output branch and load only its relevant references:

- Read [references/writing.md](references/writing.md) for evidence selection, report structure, and prose revision.
- For a new presentation or substantive slide revision, read [references/report-brief.md](references/report-brief.md). Complete or update the detailed report brief before making the corresponding slides.
- For Quarto source, metadata, references, or rendering, read [references/quarto-output.md](references/quarto-output.md).
- For new/redesigned slides or per-slide citation work, read [references/slides.md](references/slides.md).
- For direct editable PPTX authoring, read [references/pptx.md](references/pptx.md) and use a suitable available presentations workflow. Its formula-source convention applies to this branch. Report a missing authoring or rendering tool rather than claiming an unperformed check.
- For translation-heavy material, consult [references/chinese-terminology.md](references/chinese-terminology.md) when needed.

Prose reports use document-level academic layout and literature references. Slides use the 16:9 visual system and a bottom-left literature citation area: each record occupies its own line and identifies authors, year, journal/venue, and title. Notes and internal experiment reports are evidence inputs, not literature citations. Quarto mathematics renders normally from `.qmd`; direct PPTX authoring preserves the established editable LaTeX-text convention.

## Author and revise

Read the specified material, establish the central argument, and map important statements to formulas, data, original figures, or verified literature. Preserve the user's scientific meaning and sequence. Keep missing evidence visible, and separate observed results, theory, interpretation, and illustrative examples.

For slides, first save a detailed report brief, normally `汇报说明.qmd`, covering the whole report, chapter plan, reference materials, and every slide's content with complete relevant mathematical derivations. It is a core production basis alongside the supplied evidence and user instructions. Select the projection content from it; derivations and explanation may remain off-slide without being omitted from the brief. Keep both synchronized when revising. Continue to slides within the authorized task without adding a routine approval gate.

For prose, choose a coherent section structure and explanatory depth. For experimental sections, prioritize verified data tables and experiment figures, with only necessary protocol, interpretation, and limitations. Retain user-specified image sources or placeholders.

Keep source files, project-specific scripts/data, notes, and deliverables in the report project. Shared skills remain in the workflow repository. Reuse existing verified experiment outputs unless recomputation is part of the request.

## Validate and hand off

Run the selected output branch's build and checks. Inspect slide overviews and relevant full-size pages; check mathematics, figure/table readability, citations, broken resources, clipping, and consistency. Re-render after a material fix. Use the available PDF skill for PDF layout review and browser tools for rendered Quarto slides when appropriate.

Check the brief/slide correspondence, notation compliance, literature-only citation lines, and experiment evidence. For weekly reports, update `Report/Weekly/README.md` with the final topic, a brief content summary, and a valid project link.

Report the actual commands, deliverables, and remaining content/environment issues. Preserve original assets and final outputs. Follow the recipient's actual Git authorization and the batched checkpoint policy in the root `AGENTS.md`; automatic commit/push requires their standing or session authorization. Defer isolated trivial edits when appropriate. Route work products and shared skill changes to the repositories actually configured for them.
