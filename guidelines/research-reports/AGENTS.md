# Research Report Project Rules

This reusable adaptation preserves the source workspace's report workflow without private paths. Merge it into your own report directory's AGENTS.md. Inherit workspace rules and follow explicit user requirements.

## Project and sources

- Use Quarto sources for new or restructured reports. Locate the concrete project root before editing.
- Inspect nearby configuration, sources, bibliographies, CSL files, templates, styles, assets, and existing output.
- Use the quarto-publication skill for scholarly writing, citations, cross-references, and output configuration.
- Preserve target formats and existing organization. A level-one heading does not necessarily mean one slide.
- Put shared metadata in _quarto.yml and document-specific metadata in document YAML.
- Do not impose legacy PPT masters or fixed layouts unless requested.
- Use relative resource paths; do not embed machine-specific paths in publication sources.

## Content and language

- Read all designated source material before structuring the report.
- Preserve meaning, argument order, terminology, notation, and emphasis unless the requested edit requires a change.
- Give each major section a central conclusion supported by relevant evidence.
- Do not invent facts, data, formulas, citations, results, or research directions.
- Mark missing material explicitly. Retain requested image references or placeholders.
- Distinguish theoretical results, observations, interpretations, and hypotheses.
- Default to Chinese for publication content, titles, captions, axes, and tables unless otherwise requested.
- Translate common terms consistently; retain necessary names, identifiers, and standard abbreviations.
- Use restrained, accurate, traceable scholarly language.
- Cite actual bibliography keys; use placeholders only when explicitly authorized.

## Mathematics

- Follow explicit user notation and available project notation guides. Private external notation files are not included here.
- Keep formulas as editable LaTeX in .qmd and render normally through Quarto/Pandoc.
- Use $...$ for inline math and $$...$$ for display math.
- Do not replace formulas with screenshots, bitmaps, outlined SVG, or manually drawn characters.
- Use stable eq- identifiers and Quarto references for numbered equations.
- Split or align long equations instead of making them unreadably small.
- Define variables, indices, spaces, units, and assumptions at first use; keep meanings consistent.
- Check numbering, references, scripts, brackets, escaping, and each required output format.

## Figures and evidence

- Prefer meaningful equations, tables, quantitative plots, matrices, networks, and dynamics diagrams.
- Do not add unrelated conceptual illustrations or decorative technical imagery.
- Use fig-, tbl-, eq-, sec-, and lst- cross-reference prefixes.
- Verify labels, units, legends, coordinates, and connector endpoints. Arrows express defined relationships.
- Keep terminology, variables, colors, and legends consistent.
- Trace data graphics to supplied data or code; label schematic illustrations clearly.

## Production and delivery

1. Locate the project and confirm target formats.
2. Read sources and extract arguments, equations, data, references, and assets.
3. Unify terminology, notation, headings, citation keys, and cross-reference identifiers.
4. Author semantic Quarto Markdown with native LaTeX and project-local resources.
5. Preview iteratively and render the smallest scope that exercises the change.
6. Render the full project after global configuration, template, bibliography, or style changes.
7. Inspect actual outputs for math, figures, references, navigation, pagination, code, and resource paths.
8. Report actual render commands and results. Retain requested assets and outputs; do not delete unrelated content.

Before handoff, verify source fidelity, consistent language, editable mathematics, valid citations, working assets, and format compatibility. Do not claim checks that were not performed.
