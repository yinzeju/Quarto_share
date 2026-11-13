# CMAME test-format requirements and source provenance

Verification date: 2026-10-28.

## Primary sources

1. CMAME Guide for Authors: https://www.sciencedirect.com/journal/computer-methods-in-applied-mechanics-and-engineering/publish/guide-for-authors
   - The page returned HTTP 403 in this session, including a direct local HTTP request. Current detailed requirements could not be fully verified.
   - Third-party claims about mandatory graphical abstracts, precise abstract/keyword limits, or review mode are not treated as verified requirements.
2. Elsevier LaTeX instructions: https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions
   - Verified: elsarticle is supported.
   - Verified: requested archives include manuscript source, bibliography, figures, and nonstandard local class/style dependencies.
   - Verified: Editorial Manager requires all LaTeX submission files at the same folder level.
3. CMAME publisher page: https://shop.elsevier.com/journals/computer-methods-in-applied-mechanics-and-engineering/0045-7825
   - Computational-method developments in applied mechanics/engineering are in scope; this publishing test does not establish a contribution to that scope.
4. Quarto Elsevier extension: https://github.com/quarto-journals/elsevier
   - Version: 0.4.5; vendored revision: b766702f8a0b625eefa78c23c5137c37ff84a43c.
   - Provides elsarticle output, natbib, numbered citations, and publisher front matter.
5. Quarto documentation:
   - https://quarto.org/docs/journals/
   - https://quarto.org/docs/output-formats/pdf-basics.html#latex-output

## Choices for this technical test

- Elsevier preprint mode; no production-layout claim.
- English, concise abstract, five keywords, author/affiliation/corresponding-author fields, and numbered references.
- natbib/BibTeX with `elsarticle-num.bst`.
- Static vector PDF figure and editable Markdown table.
- Declaration sections exercise layout while avoiding real-author assertions.
- Separate highlights are an additional artifact, not certification of the current portal's requirements.

## Open requirements before a real submission

Reopen the official CMAME guide and verify article type, abstract/keyword limits, separate items (including highlights and any graphical abstract), reference details, review/anonymity mode, declaration requirements, and portal TeX compatibility. This project validates only local authoring/export/compilation.
