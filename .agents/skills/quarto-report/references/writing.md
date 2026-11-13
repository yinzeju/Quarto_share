# Report Writing

Read supplied research materials before outlining. Establish the audience, purpose, desired depth, and whether the result is a progress report, literature discussion, method explanation, or presentation. Infer details from existing projects rather than repeating questions already answered.

## Papers mentioned in supplied materials

Search the user's local MinerU library before looking online for a paper mentioned in notes, literature, experiment reports, or other supplied materials. This applies to report briefs, prose reports, slides, and weekly reports.

- Use the supplied paper files or local library directly. Otherwise inspect relevant material directories and project documentation for the matching PDF/Markdown or MinerU export; no library configuration is required. State when no usable local collection is available, then retrieve missing material from verified online sources as needed.
- Search filenames and paper directories first, then Markdown content as needed, using `rg --files` and `rg`. Match the title, DOI, or author/year against the candidate itself; MinerU folder names may truncate the title. Find both the corresponding PDF and Markdown, including nested files, rather than accepting a similarly named paper without checking identity.
- Prefer the local Markdown for text search and reading, and the paired PDF for original equations, figures, pagination, or extraction discrepancies. Preserve the original scientific meaning when checking OCR/Markdown errors. If only one representation exists, use it and obtain a missing counterpart only when the task needs it.
- Only after a local search finds no verified usable match, or the needed material is missing, search online. Prefer the publisher/DOI page, an official preprint repository, or the authors' institutional source. If the local library is inaccessible, state that accurately before using the online fallback; do not claim a completed local search.
- Record the paper identity and the material actually used in the brief/source inventory. Reuse available local files, keep publication asset links relative, and cite the paper's verified bibliographic record rather than the MinerU export or a local file path. The local library remains a source collection; a report task does not authorize reorganizing or overwriting it.

## Organize and explain

Build the argument around a research question, relevant evidence, the explanation it supports, and the remaining uncertainty. A progress report can emphasize completed work, observed problems, and the next decision; a paper presentation should explain the problem, method, assumptions, evidence, and limits without claiming new experiments.

Preserve argument order and terminology supplied by the user. Compress without changing scientific meaning. Each section/slide needs a clear point supported by the closest relevant mathematical statement, figure, table, or verified source. For presentations, first complete the detailed brief specified in `report-brief.md`, with whole-report explanation, chapters, materials, and per-slide derivations. Keep full relevant derivations in that document even when the projection omits them.

Use precise Chinese by default, including titles, captions, axes, legends, and tables. Retain searchable proper names and established technical identifiers, explaining specialist terms on first use. Avoid decorative English and promotional claims. Apply the bundled Core convention via `notation.md`; keep terms, units, and abbreviations consistent.

Trace figures and data to original sources or actually generated outputs. Label mathematical illustrations as illustrations. Preserve existing image links and requested placeholders; do not invent substitute experimental figures or numbers. Mark missing evidence visibly.

Experimental reporting should lead with quantitative tables and experiment figures, supported by concise protocol and interpretation. Keep notes and internal experiment reports in the source inventory, not the literature bibliography.

For prose reports, preserve the target document's heading and academic layout. For slides, use the 16:9 system and bottom-left, one-record-per-line literature references with authors, year, journal/venue, and title under `slides.md`. Formal manuscript authoring and journal submission are outside this report package; do not assume a separate manuscript skill is installed.
