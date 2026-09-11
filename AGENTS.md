# AGENTS.md

This file gives project-level instructions for Codex and other coding agents working in this repository.

Treat this repository as a Quarto publishing workspace. It may contain multiple concrete publication projects such as theses, reports, books, manuscript drafts, websites, and slide decks.

## Required Workflow

1. Identify the concrete Quarto project folder before editing. A child folder may be a category folder rather than the project root.
2. For scholarly writing, thesis, article, book, bibliography, citation, cross-reference, output-format, or publication tasks, use `.codex/skills/quarto-publication/SKILL.md`.
3. Prefer official Quarto documentation for exact syntax and current option names. When an option may have changed, verify it from `https://quarto.org/docs/` before changing files.
4. Inspect nearby `_quarto.yml`, `.qmd`, `.ipynb`, `.bib`, `.csl`, template, and style files before editing. Preserve the local publication style unless the user asks for a redesign.
5. Keep generated text in the user's requested language for publication content. Keep internal skill and agent instructions in clear English for reuse by agents.
6. Do not hard-code machine-specific absolute paths inside Quarto projects unless the user explicitly asks.
7. Do not delete rendered outputs, large assets, data folders, or thesis/report files unless explicitly asked.

## Quarto Workspace Conventions

- Put reusable Quarto project instructions in project-local `AGENTS.md` files when a child project needs stricter rules.
- Keep bibliographies as `.bib` files and citation styles as `.csl` files near the concrete project unless the existing project uses a shared bibliography.
- Prefer `_quarto.yml` for shared metadata across a project and document YAML front matter for document-specific metadata.
- Use `quarto preview` for iterative authoring and `quarto render` before publication or handoff.
- For books, render the full project before release because preview may not fully refresh global configuration changes.

