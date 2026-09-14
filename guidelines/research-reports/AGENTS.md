# Research Report Project Rules

Merge these reusable rules into your report directory's AGENTS.md. Inherit workspace rules and follow explicit user requirements.

## Project and sources

- Use Quarto sources for new or restructured reports. Locate the concrete project root before editing.
- Inspect nearby configuration, sources, bibliographies, CSL files, templates, styles, assets, and existing output.
- Use the quarto-publication skill for scholarly writing, citations, cross-references, and output configuration.
- Preserve target formats and existing organization. A level-one heading does not necessarily mean one slide.
- Put shared metadata in _quarto.yml and document-specific metadata in document YAML.
- For Quarto scientific slides, follow the visual rules below, adapted from create-scientific-slides-cn. Do not carry over its PPTX construction, point sizes, or raw LaTeX text boxes; implement layouts using the target format's theme, styles, or template.
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

- Follow explicit user notation and available project notation guides.
- Keep formulas as editable LaTeX in .qmd and render normally through Quarto/Pandoc.
- Use $...$ for inline math and $$...$$ for display math.
- Do not replace formulas with screenshots, bitmaps, outlined SVG, or manually drawn characters.
- Use stable eq- identifiers and Quarto references for numbered equations.
- Split or align long equations instead of making them unreadably small.
- Define variables, indices, spaces, units, and assumptions at first use; keep meanings consistent.
- Check numbering, references, scripts, brackets, escaping, and each required output format.

## Scientific slide visual style

- Apply these rules to Quarto scientific slides, including Reveal.js and Beamer, rather than automatically to articles or other documents. Use them for new decks or requested restyling; keep local edits within the requested scope.
- Default to a 16:9 canvas with consistent safe margins and white or very pale blue-gray (#F7F9FB) backgrounds. Subtle grids and fine lines are acceptable. Avoid alternating light and dark backgrounds, large dark fills, and distracting textures.
- Use navy (#17324D) for headings and body text, blue (#2F6B9A) and teal (#168A8A) for primary emphasis, and cool gray (#B8C4CE) for rules. Reserve muted red (#B64B4B) for risks, errors, or counterexamples; warm gold (#A87316) may indicate secondary notes. Use at most two primary accent colors per slide and keep semantic colors consistent.
- Use Microsoft YaHei or a clear, reliable sans-serif Chinese font. Keep heading, body, caption, and footer hierarchies consistent. Adapt sizes to the canvas and target format for projection readability; do not keep shrinking text to fit excess content.
- Place concise, conclusion-led titles consistently at the top. Give each slide one central conclusion with necessary equations, data, or figures. Move detailed derivations or spoken explanations to notes or an appendix when appropriate.
- Prefer text beside a figure, a conclusion above evidence, a central equation with nearby definitions, or a full-width table or plot. Use whitespace, alignment, fine dividers, and heading hierarchy; avoid excessive rounded cards and mechanical three-column layouts.
- Render equations normally through Quarto. Keep definitions nearby and align multiline equations by equals signs or the left edge. Restrained pale fills or fine borders are acceptable; do not display raw LaTeX conversion boxes or use embossed effects.
- Use pale blue-gray table headers, white bodies, and optional subtle alternating rows. Avoid heavy grid borders, align numeric columns, standardize precision and units, and highlight only key values or changes.
- Give plots complete axes, units, and legends, with line styles and markers as well as color. Label network and flow nodes, tensor dimensions, or state variables as relevant. Keep connectors clear of text. Geometry, spectra, and operator diagrams must express defined mathematics.
- Prefer supplied experimental, apparatus, paper, and data figures. Avoid neon gradients, rainbow palettes, glow, space backgrounds, particles, robots, brain metaphors, and scientifically meaningless decoration.
- Keep titles, body areas, citations, and page numbers consistent. Reserve a bottom-left citation area that body text, equations, figures, and navigation cannot overlap.

## Scientific slide literature citations

- Put every literature citation at the bottom left of the slide where the source is used, left-aligned. Include literature sources for figures in this area. Do not scatter author-year or numbered citation markers in titles, body text, or beside figures.
- Use the exact display pattern Author(Year), such as 张三(2024) or Smith(2023), rather than [1], (Smith, 2023), or a full bibliography entry. The year is the verified publication year from the bibliography.
- For two authors, use 张三、李四(2024) or Smith & Jones(2023). For three or more, use 张三等(2024) or Smith et al.(2023). Disambiguate multiple works by the same author in the same year with bibliography-consistent suffixes such as 2024a and 2024b.
- List multiple sources in order of use, separated by semicolons; wrap within the citation area when necessary. Deduplicate sources within each slide. Reorganize or split a crowded slide instead of making citations unreadably small or overlapping content.
- Use consistent, readable text smaller and less prominent than the body, with adequate contrast and bottom clearance. Maintain citations per slide rather than repeating the entire deck's source list in a global footer.
- Retain complete, real bibliography entries in .bib files and trace every displayed citation to its key. Prefer citation processing and project styles to achieve the format. Verify missing author or year information; document unresolved gaps rather than inventing metadata.
- An optional appendix may contain full bibliography entries, but does not replace bottom-left citations on content slides. The short format and placement rules apply to content-slide citations; a full bibliography page uses a bibliography list layout.

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
   - For slides, plan each title, central conclusion, evidence, figures, equations, literature sources, and spoken transition before applying the visual rules.
4. Author semantic Quarto Markdown with native LaTeX and project-local resources.
5. Preview iteratively and render the smallest scope that exercises the change.
6. Render the full project after global configuration, template, bibliography, or style changes.
7. Inspect actual outputs for math, figures, references, navigation, pagination, code, and resource paths.
8. Report actual render commands and results. Retain requested assets and outputs; do not delete unrelated content.

Before handoff, verify source fidelity, consistent language, editable mathematics, valid citations, working assets, and format compatibility. For slides, inspect the whole deck for style consistency and every slide at presentation size for readable equations and figures, whitespace, overflow, and unobstructed bottom-left Author(Year) citations. Verify author and year metadata, fix layout issues, and render again. Do not claim checks that were not performed.
