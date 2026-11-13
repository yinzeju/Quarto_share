# Detailed Report Brief

Use the user's notes, literature, experiment reports, and other supplied evidence to write a detailed report brief before creating slides. Reuse the existing equivalent document when it meets this contract; otherwise prefer `汇报说明.qmd` in the concrete project. A title-only outline or speaker notes alone are insufficient. Use the user's report language, normally Chinese.

For papers mentioned in these materials, follow the MinerU-first lookup in `writing.md`: find and read the local PDF/Markdown before searching online for missing material.

The brief is one of the core production bases, together with the user's instructions and the actual source materials. Resolve discrepancies against that evidence rather than treating an earlier brief as unquestionable authority. If the user requests only a brief, deliver that stage; otherwise continue to the requested slides without requiring an extra approval.

## Whole-report explanation

Start with these elements, before the page-by-page specification:

- Main content: research question, scope, intended audience, central argument, main messages, and the distinction between literature results, existing experiments, interpretations, and proposals.
- Chapter plan: the role and logical order of each section, its planned slides, and how it connects to the report's argument. Respect a requested slide count and reporting duration.
- Reference materials: identify the supplied notes, papers, experiment reports, datasets, figures, and relevant locations/sections. State which material supports which chapter and what remains missing. Keep this source inventory distinct from the literature bibliography.
- Notation basis: use the bundled Core convention, record its content version and any necessary mapping from a paper's notation to the report's notation, following `notation.md`.

## Per-slide specification

For each planned slide, provide enough detail to make and check it without guessing the underlying mathematics:

1. **Purpose and main point:** slide number, title, role in its chapter, and the specific message supported by the evidence.
2. **Planned visible content:** the selected text, equations, tables, and figures, including the intended layout and which detailed material stays in the brief or speaker notes.
3. **Full content explanation and mathematical derivation:** definitions and assumptions; symbol types, dimensions, and units; intermediate transformations; required identities and justifications; and the final expression or algorithm. Explain approximations, truncation, statistical estimates, and boundary/validity conditions. Derive the nontrivial mathematics needed for the slide rather than merely restating its final formula. Do not fill missing derivations with invented results.
4. **Evidence and assets:** exact source sections, local figure/data paths, table values, experiment configuration, and any pending evidence. Preserve the supplied values and distinguish actual results from illustrations or planned work.
5. **Literature citation lines:** verified authors, year, journal/venue, and title for literature used on the slide, following `slides.md`. Notes and internal experiment reports belong in the evidence inventory, never in this footer list.
6. **Spoken explanation and transition:** the necessary explanation, likely conceptual difficulty, and connection to the next slide.

The brief may be substantially longer than the slides. Preserve the detailed mathematical chain there while selecting a readable subset for projection. Retain editable LaTeX and consistent equation references; follow the selected output branch for slide mathematics.

## Experimental sections

Use a compact task/protocol description, then quantitative tables and experiment figures. Include the baseline names, metrics/units, horizons, data split, and comparison conditions needed to interpret them. State a supported conclusion and any limitation that changes its meaning. Avoid repeated scene-setting, generic claims of improvement, and long prose that duplicates the table or curve. Detailed mathematics still belongs in the brief when it is needed to understand the method or metric.

## Revision and validation

For a narrow revision, update the affected brief sections and slides together rather than rebuilding unrelated chapters. Reconcile the overall page map after structural changes. Check that visible claims and numeric values are supported, every planned slide has its detailed explanation, and all omitted derivation steps remain available in the brief. A brief may document an unresolved issue, but its presence does not turn an unsupported claim into a finished slide.
