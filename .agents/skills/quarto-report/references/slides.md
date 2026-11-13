# Scientific Slide Style and Citations

Use for new designs, requested visual unification, or slide-specific citation work. First write or update the detailed brief under `report-brief.md`; it contains the complete explanations and derivations from which visible slide content is selected. Preserve an established design for narrow edits. Read `pptx.md` for the PowerPoint formula representation; Quarto slides render mathematics normally.

## Layout and scientific figures

- Default to 16:9 with white or very light gray-blue (`#F7F9FB`) backgrounds, stable margins, and fixed title/footer/page-number positions. Avoid alternating light/dark backgrounds and decorative gradients/textures.
- Use navy (`#17324D`) text, blue (`#2F6B9A`) and teal (`#168A8A`) emphasis, cool gray (`#B8C4CE`) rules, restrained red (`#B64B4B`) for errors/counterexamples, and warm gold (`#A87316`) for secondary notes. Use at most two dominant accents per slide and consistent semantic colors.
- Use Microsoft YaHei or another clear Chinese sans-serif. Keep a stable hierarchy readable in projection. Split or simplify crowded slides instead of repeatedly shrinking text.
- Put a concise conclusion-oriented title above the evidence. Prefer left-text/right-figure, top-conclusion/bottom-evidence, central-formula, or full-width table/curve layouts. Use whitespace, alignment, and thin rules rather than repeated rounded cards.
- Prefer formulas, quantitative tables/curves, coordinates, matrices/operators, networks, geometry, and dynamics/control diagrams. Give every visual a scientific purpose, accurate labels, variables, dimensions, and directions.
- Curves need axes, units, and legends; combine line styles/markers with color. Tables need aligned values, consistent decimals/units, minimal rules, and selective emphasis. Light blue-gray headers and restrained alternating fills are appropriate.
- Build connectors after their nodes, attach them to the intended boundaries, and avoid crossing unrelated labels. Feedback paths should be distinguishable and labeled. Use three-dimensional perspective only when it explains a spatial relation.
- Prefer original apparatus, experimental, paper, and data figures. Avoid decorative technology imagery, rainbow/neon effects, particles, robots, brains, or scientifically meaningless graphics.
- Keep symbol definitions near equations; split/align long expressions. Apply the bundled Core convention through `notation.md` to all symbols, including figures and table labels. Quarto equations remain editable LaTeX in `.qmd` and render normally; PPTX representation follows its own branch.
- Experimental slides prioritize data tables and experiment figures. Add only the task/protocol context, supported interpretation, and material limitations needed to understand them; avoid prose that repeats the displayed values.

## Citations on content slides

- Reserve a dedicated bottom-left, left-aligned citation area on every slide that uses literature, including figure sources. Keep body content, mathematics, and navigation clear of it.
- Every citation identifies **authors, year, journal/venue, and paper title**, for example the field order `Author(s) (Year). Journal/Venue. Title.` Use verified author names, year suffixes when needed, and bibliographic titles. A verified journal abbreviation and normal author abbreviation such as `et al.` may improve fit.
- Give each literature record its own visual line. Stack multiple references vertically in order of use, deduplicate within the slide, and never join different records with semicolons. Reserve sufficient footer width and height, and adjust the page content or layout to keep complete records readable without overlap or arbitrary title truncation.
- Cite literature only. Do not cite personal notes, internal experiment reports, local paths, or production logs in the footer or fabricate bibliography entries for them. Their provenance remains in the report brief/source manifest. Cite a genuine published paper underlying a dataset/method when relevant.
- Keep complete verified `.bib` records and a reliable mapping to footer text. Use the actual conference, preprint repository, or publisher for non-journal literature rather than inventing a journal. Resolve missing metadata from sources; keep unresolved items visible in the brief before treating the citation as ready.
- Avoid scattered numeric markers and inline author-year labels next to titles, body, or graphics. An optional full-reference appendix does not replace the complete per-slide citation lines.

## Visual acceptance

Inspect the whole-deck overview for rhythm, hierarchy, density, background, and color consistency, then every page and relevant full-size details. Verify titles, page order, equations, tables, legends, references, and resource loading. Fix clipping, overlaps, unreadable text, low contrast, malformed labels, and citation-area conflicts; re-render after changes.
