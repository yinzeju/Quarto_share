# Direct Editable PowerPoint Output

Use this branch when creating or editing an editable PowerPoint deliverable. Use an available presentations skill and its required rendering workflow when present; otherwise select a suitable installed PPTX authoring/rendering tool and verify editability and layout. Report missing tools and unperformed checks accurately. Load `slides.md` for scientific style/citations; keep detailed implementation instructions in the tool workflow rather than copying them here.

## Existing formula-source contract

For direct PPTX authoring, preserve the former workspace convention: equations are editable text boxes containing literal LaTeX source. Use a monospaced font such as Consolas, preserve backslashes/subscripts/superscripts/braces, and put definitions nearby. Do not substitute equation screenshots, rendered image/SVG outlines, or manually drawn symbols for this contract. Split long expressions and adjust layout while retaining readability.

This convention belongs to the direct PPTX branch. Quarto HTML/PDF equations render normally from `.qmd`. If the user specifies an existing Quarto-to-PPTX workflow or a different mathematical representation, preserve that explicit requirement and validate the resulting editable content. Do not silently impose the raw-text convention on an established native-math project.

## Construction

- Preserve the requested page count/order and confirmed theme for edits. A new deck's sections and slides should follow the argument; mapping level-one source headings to slides is a starting convention only when consistent with the material and requested structure.
- Use editable text, shapes, tables, charts, and connectors. Preserve supplied image links/placeholders, using source figures rather than unrelated generated illustrations.
- In the inherited direct-PPTX workflow, a source-page image link reserves a blank image region for later manual insertion. Keep that link/placeholder and do not generate a replacement, unless the user requests a different image-handling workflow.
- For a new direct PPTX design, a useful starting hierarchy is 28-34 pt headings, 17-22 pt body text, and captions/footers at least 11 pt. Adapt the layout to the actual canvas and projection use; these point-size recommendations are not Quarto CSS rules.
- Use a stable page skeleton, restrained palette, aligned values, complete axes/legends, accurate connector endpoints, and labeled scientific relationships. Avoid dense text and decorative filler.

## Acceptance

Render and inspect every slide plus an overview. Check sequence, titles, margins, backgrounds, density, formulas and their literal source, data provenance, Chinese terminology, bibliography labels, and technical diagrams. Verify the PPTX opens, intended objects remain editable, and no text or objects clip/overlap or extend off-canvas. Re-render fixes before delivery and keep transient diagnostics separate from final deliverables.
