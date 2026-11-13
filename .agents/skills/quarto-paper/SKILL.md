---
name: quarto-paper
description: Develop and publish research manuscripts under Paper, from research briefs and evidence-grounded drafts through revision, journal adaptation, bibliography, LaTeX source packaging, PDF export, and independent compilation. Use for formal papers and academic publication tasks; research reports and presentations belong to quarto-report.
---

# Research Paper Publishing

Support the full manuscript lifecycle with traceable claims and a reproducible publication source. Read the central workspace `AGENTS.md` for common rules and Git boundaries. Work inside the concrete paper under `Paper/`; keep reusable skills in the workflow repository.

## Locate the manuscript and phase

For a ready-to-render example, inspect [Paper/Template](../../../Paper/Template/README.md). It is copied from the author's actual synthetic CMAME pipeline test and includes the manuscript, figures, data, numerical script, journal extension and source-verification script. Copy it to a new project when requested; preserve its explicit synthetic/fictional labels until real evidence and author-approved metadata replace them. It is a publishing example, not a scientific contribution or a submission-ready manuscript.

Inspect source, `_quarto.yml`, author metadata, bibliography, evidence notes, figures, scripts, template/extension, and outputs. Establish the research question, paper type, language, available evidence, target journal if known, and current phase. Infer supplied facts; ask only about missing information that materially blocks the work. Preserve the existing scientific meaning and project conventions.

Load references only for the phase needed:

- [references/writing.md](references/writing.md): research brief, argument, first draft, revision, and evidence consistency.
- [references/quarto-output.md](references/quarto-output.md): manuscript metadata, citations, cross-references, and Quarto outputs.
- [references/journal-adaptation.md](references/journal-adaptation.md): official journal requirements, templates, references, author metadata, and submission items.
- [references/latex-handoff.md](references/latex-handoff.md): source packaging, the bundled helper, and independent compilation.
- [references/academic-formats.md](references/academic-formats.md): books, theses, and less frequent academic formats when explicitly requested.

## Develop and revise

Connect major claims to supplied/actually generated experiments, derivations, figures/tables, or verified literature. Choose an outline appropriate to the research, write where evidence is available, then reconcile the introduction, abstract, contributions, and conclusions. Keep unresolved scientific content visible rather than filling it with invented findings or references.

Use `assets/starter/` when starting a paper and no existing project fits. Replace scaffold TODOs with supported facts or retain them visibly. Keep a concise research brief, evidence provenance, and expensive research computation separate from routine rendering. Synthetic test manuscripts require explicit authorization and conspicuous test labels.

## Adapt and export

Keep `.qmd` canonical during drafting and `.bib` as the bibliography. Separate journal configuration from manuscript content. Verify current official journal/publisher requirements and record sources, dates, extension revisions, and unresolved requirements inside the paper. Match the actual bibliography backend, author/review mode, figures, and declarations; do not invent author-approved statements.

For LaTeX delivery, export the actual journal `.tex`, collect required local resources, and compile a fresh extracted package without Quarto. Preserve old submission snapshots. If the user requests subsequent manual LaTeX editing, identify a frozen handoff and its new source of truth.

## Validate and deliver

Check scientific claim/evidence correspondence, symbols, units, citation keys, cross-references, and abstract/result consistency. Render requested formats, inspect PDF pages when relevant, and verify the source package with the intended engine. Report actual commands, outputs, gaps, and environment/server limits. Compilation success does not establish scientific validation or complete journal compliance.

Provide links to the manuscript and requested deliverables. Apply the batched checkpoint policy and actual user authorization in the root AGENTS.md after meaningful completed revisions. Route changes to the actual repository, preserve unrelated work, and verify push results. The original author's standing permissions are not granted by sharing this package. Actual journal submission requires the user's explicit instruction.
