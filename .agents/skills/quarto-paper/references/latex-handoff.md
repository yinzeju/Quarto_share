# Journal LaTeX Handoff

## Establish the target

Read the current official journal author guide and publisher's LaTeX instructions. Record URLs, access date, and verified requirements in the individual project. If a source is inaccessible, state the gap and proceed with verified publisher requirements for a technical test; do not invent journal-specific limits or certify full compliance.

Check article type, language, front matter, abstract and keyword limits, reference style, review/anonymity mode, figures/tables, separate submission items, and declarations. Never fill real-author declarations without evidence.

Prefer an appropriate maintained Quarto extension; record and vendor its exact revision and preserve license notices. Use project profiles for alternative outputs when useful. Check official documentation before adding unfamiliar options.

Authoritative references:

- https://quarto.org/docs/journals/
- https://quarto.org/docs/projects/profiles.html
- https://quarto.org/docs/output-formats/pdf-basics.html#latex-output
- https://quarto.org/docs/authoring/citations.html
- https://www.elsevier.com/researcher/author/policies-and-guidelines/latex-instructions

## Export and package

Quarto supports `latex` output. A journal PDF format with `keep-tex: true` also exports its actual journal `.tex`. Locate the actual file after rendering: with the tested Quarto 1.10.19 project, the PDF went to `_output/` while the retained `.tex` and bibliography intermediates stayed beside the `.qmd`. Preserve bibliography intermediates when needed using documented PDF options. Verify the template's bibliography backend: CSL/citeproc, natbib/BibTeX, and biblatex/Biber are not interchangeable.

Package the main `.tex`, local figures, bibliography, needed `.bbl`/`.bst`, and nonstandard class/style resources. Do not copy research datasets, private notes, or the entire working directory into a submission archive.

Check the target platform's current source-layout requirements. When it requires a flat LaTeX package, preserve the organized source tree and flatten only the exported bundle, rewriting file references and detecting basename collisions.

The helper `scripts/package_latex.py` handles conventional generated LaTeX with literal `includegraphics`, `input`, `include`, `bibliography`, and `bibliographystyle` references. It resolves local dependencies, collects bibliography styles via `kpsewhich` when needed, and accepts repeated `--resource` arguments for class/style files and generated `.bbl` files. Pass dynamic dependencies explicitly. This helper is not a general TeX parser and cannot certify arbitrary package closure.

Example from an individual paper directly below `Paper/`:

```powershell
quarto render manuscript.qmd --profile submission --to elsevier-pdf --no-execute
python ../../.agents/skills/quarto-paper/scripts/package_latex.py --tex manuscript.tex --root . --output _output/latex-source --resource _extensions/elsevier/elsarticle.cls
```

The output must be a new or empty directory. Choose a new name for later snapshots. The helper also creates a sibling ZIP and a file/hash manifest. Add supplementary files as explicit resources only after checking their content and required format.

## Test independent compilation

Extract the archive into a new directory outside the source project. Use the required engine and bibliography tool there. A typical natbib/BibTeX build is:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
bibtex manuscript
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error manuscript.tex
```

Inspect logs for missing files, unresolved citations/references, and material overfull boxes; visually review the PDF. Record the tested engine/distribution. A clean extracted-directory build proves independence from the original project, not independence from a standard TeX installation or compatibility with every editorial server.
