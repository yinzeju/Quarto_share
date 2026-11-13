# Other Academic Publication Formats

Load only for a requested thesis, book, or other formal academic publication. Establish its concrete project, required format, and institutional/publisher constraints; preserve existing chapter order and local templates. Routine journal papers do not need this reference.

For books/theses, keep explicit chapter ordering in `book.chapters`, shared bibliography and cross-reference settings at project scope, and document-specific metadata in the relevant chapters. Prefer Quarto metadata/options to scattered raw Pandoc flags. Verify current syntax with official documentation before introducing unfamiliar settings.

Preview during authoring. Render the full book after global `_quarto.yml`, templates, bibliography, or style changes and before release, because a preview may not refresh all global state. Check chapter/appendix ordering, numbering, references, and all requested output formats.

For PDF, identify the engine and template assumptions. For DOCX, use an appropriate reference document when house style matters. For Typst, verify its current citation/layout options. For EPUB, verify cover and chapter metadata. Select only the formats actually requested and keep format-specific options in their YAML branches.

Use verified citation/document metadata when making a publication citable; do not fabricate a DOI, ORCID, license, funding statement, or reference record. Consult the relevant current appendix guidance for the chosen output instead of applying an unrelated format's conventions.

- https://quarto.org/docs/books/
- https://quarto.org/docs/books/book-structure.html
- https://quarto.org/docs/books/book-crossrefs.html
- https://quarto.org/docs/reference/formats/docx.html
- https://quarto.org/docs/reference/formats/typst.html
- https://quarto.org/docs/reference/formats/epub.html
- https://quarto.org/docs/authoring/appendices.html
