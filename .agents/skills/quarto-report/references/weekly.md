# Weekly Reports

A weekly report is the user's periodic research presentation. Use [weekly-report](../../weekly-report/SKILL.md) for content planning and `quarto-report` for shared publication rules. This reference covers project location and the Weekly content README.

## Locate or create the project

- For an explicitly new weekly report, create a new concrete publication project. Use the requested meeting/report date, or the current date from the user's client context and timezone when no date is supplied. Format the date as `YYYYMMDD`; do not substitute the execution host's date. If no reliable date or timezone is available and it affects naming, resolve that information rather than assuming the original author's timezone.
- With no collision, use `Report/Weekly/YYYYMMDD/`. An existing date parent that only groups projects receives a separate descriptive project child. Confirm the concrete `_quarto.yml` or source location before rendering.
- A request to revise an existing weekly report reuses its project. A genuinely new report on the same date must preserve the earlier project. If the date path is already a concrete project, convert it to a date parent with distinct descriptive children, retaining the earlier project's content and updating affected relative references. Never overwrite or merge unrelated reports, or place a second Quarto project inside a renderable parent.
- Existing archive dates and project names remain stable during ordinary revisions. Do not rename a report merely because editing changes its filesystem modification time.

Keep source, `汇报说明.qmd` or its existing equivalent, bibliography, assets, project-specific scripts/data, and requested outputs within the concrete project. Reuse an appropriate established report style without copying generated caches or unrelated datasets.

## Maintain the Weekly README

After a new weekly report is finished, add its entry to `Report/Weekly/README.md`. After revising an existing report, update its entry if the topic, content, or path changed. Include a relative project link, a useful topic, and one or two concise sentences describing the actual final content.

Keep this README a reader-facing content directory. Do not add old/new path mappings, modification-time tables, migration logs, or build diagnostics. Preserve other reports' entries, avoid duplicates, and check that project links resolve. Identify an outline, excerpt, or unfinished experiment honestly when that affects what readers will find.

Commit the finished project and README update together when the shared Git policy calls for a meaningful-revision checkpoint. A weekly-report request does not itself schedule an automation.
