---
name: weekly-report
description: Create or revise weekly research presentations with connected derivations, concise method overviews, literature synthesis, recent work, experiments, and next steps. Use quarto-report for shared publication and output rules.
---

# Weekly Research Reports

Organize periodic research presentations around a continuous scientific argument. The central rule for a detailed explanation is: **starting point → operations or derivation → useful result; the next page starts from that result.** Inputs and outputs can be equations, recorded data, estimated matrices, algorithms, or scientific conclusions.

Read [quarto-report](../quarto-report/SKILL.md) for shared evidence, notation, citations, output selection, rendering, and delivery rules. Use its [weekly project conventions](../quarto-report/references/weekly.md) for project location and the Weekly README. Those common rules remain in their existing sources; this skill governs content organization and explanation.

## 1. Establish the argument and choose the depth

Identify the research question, audience, main message, and the relationship between the literature and the user's recent work. Select the explanation depth before allocating slides.

| Mode | Use when | Intended understanding |
|---|---|---|
| Detailed explanation | A theory or computation is central to the report or supports the user's method | The audience can follow how the result is obtained from the stated inputs |
| Method overview | A paper supplies background, an alternative approach, or a comparison | The audience understands the core idea, tools, workflow, and output |

A useful default sequence is **detailed literature → method overviews → innovations and limitations → recent work → numerical experiments → next steps**. Adapt it to the materials, requested duration, and slide count. Not every paper needs detailed treatment, and a report need not contain every section. Explain a complete relevant calculation chain rather than attempting to reproduce an entire paper.

## 2. Develop the brief and page map

Follow the [detailed-brief contract](../quarto-report/references/report-brief.md) before producing slides. Preserve the full definitions, assumptions, derivations, and evidence there, then select the visible material according to the chosen explanation depth. A page plan can use this compact specification:

```text
Purpose and main point:
Starting point / input:
Known quantities, unknown quantities, and new symbols:
Operations or derivation:
Result / output:
Result used by the next page:
Evidence and planned visual material:
```

These fields guide authoring; they are not required on-screen labels. Check the page map for missing dependencies, unexplained matrices, and results whose subsequent use is unclear. Within a derivation, the next page's input should match the preceding output. At a chapter boundary, establish the new scientific problem rather than forcing an artificial algebraic link.

The brief can explain more than the projected page. In detailed mode, however, do not hide a requested derivation step only in the brief while jumping over it on the slides. During revision, keep affected pages and the overall page map aligned, respecting any explicit user instruction about which deliverables to update.

## 3. Build detailed explanations as connected stages

Make each page one logical stage with a useful intermediate result.

1. Start from the equation, data, or conclusion actually needed for this stage. Repeat the preceding result when necessary so the audience does not need to remember an off-screen expression. Introduce the physical problem before an abstract model when the audience needs that context.
2. Define new symbols near their first use. Give meanings and necessary dimensions, and distinguish measured data, known model quantities, unknown physical parameters, and data-based estimates. Apply the shared notation rules consistently within this report.
3. Show the operations in their actual order: substitution, expansion, elimination, decomposition, regression, or another supported calculation. Retain the intermediate expressions needed to follow a nontrivial transformation. State approximations and assumptions where they enter.
4. Give each newly constructed matrix or variable a clear origin and use. Explain how it is obtained and what it enables next. Use a short physical or computational interpretation when the equations alone do not make the step understandable.
5. Finish with the resulting equation, computable quantity, algorithm, or conclusion. The following page should use it directly instead of introducing a disconnected starting point.

For example, a data-based identification explanation may progress through recorded signals, a data equation, an estimated response operator, and physical coefficients. Each stage must show its own construction; naming a decomposition or optimization method alone does not supply the missing derivation.

### Long derivations and scrolling pages

Treat a slide as a logical stage, not necessarily a single screen of content. A long stage may use **whole-page vertical scrolling** with ordered equations and normal readable type. Preserve the requested logical page structure; do not collapse several requested stages into one page merely because scrolling is available.

Scroll the presentation page itself rather than placing the derivation inside a small nested panel. Split stages when that improves the reasoning, and avoid shrinking formulas to fit. When PDF is requested, verify that the export preserves the full scrolling content rather than only the initial viewport. The export may use a long page or a complete continuation layout appropriate to the requested delivery.

## 4. Present method overviews and synthesize the literature

An overview follows **research problem → core idea → tools → workflow → output**. Use a compact diagram or sequence to show what enters each major operation and what comes out. Explain why the tool matters, but omit derivations that are not needed at the selected depth. Avoid disconnected final formulas that require unexplained machinery.

After the literature sections, compare the papers using relevant shared dimensions:

- **Innovation:** the capability added, difficulty addressed, or procedure avoided relative to the stated comparison.
- **Assumptions:** required measurements, model structure, function families, or other conditions.
- **Limitations:** cases outside those assumptions, evidence, or practical computational reach.
- **Relevance:** the supported gap or idea that connects to the user's work.

Separate a theoretical restriction from a limit of the published experiments. Low-dimensional demonstrations alone do not establish that a method cannot handle high-dimensional systems; analyze the applicable data requirements, matrix sizes, identifiability, or computational cost. Do not invent a limitation to manufacture a motivation for the next section.

## 5. Explain the user's recent work with the same continuity

A useful chain is **available model and data → unresolved component → proposed representation or computation → learning objective → usable prediction model**. Adapt it to the actual work rather than imposing a particular residual model or algorithm.

Use the detailed-page rules: retain the preceding result, construct the next object, and show the resulting capability. For each loss term, identify the prediction, target or constraint, and source of supervision. Explain a regularizer through the property it enforces. Keep simplified explanatory formulas faithful to the method and retain necessary implementation details in the brief.

Distinguish training information from the inputs available during prediction. A final prediction procedure must not silently depend on future measured states or other training-only quantities. Separate completed work and observed results from hypotheses and proposed extensions.

## 6. Translate experiment reports into audience-facing evidence

Build this section around **experimental object → comparison and evaluation conditions → figures and numbers → supported conclusion**. Prefer an original setup schematic, quantitative table, and informative response curves over long descriptions.

- Replace internal task codes, run names, and dataset shorthand with simple scientific names such as "prior model" and "corrected model." Keep the mapping to original sources in the brief or existing source record, not in the projected text.
- Supply the context needed to interpret the evidence: physical object, relevant size, data split, prediction horizon, metric definition, units, and comparison conditions. Distinguish degrees of freedom, state dimensions, and groups of state variables when they differ.
- Show the requested meaningful comparisons; do not add every internal run found in the source report. Use comparable evaluation conditions and preserve the reported data and original figures. Reuse verified outputs unless new computation is requested.
- Name precisely what an aggregate covers. For an average, identify the quantities or groups, weighting, and evaluation set. Calculate derived summaries from unrounded values, then round for display. Changing an audience-facing name must not change the underlying metric.
- State the actual conclusion and any boundary that materially affects it. Do not turn finite-window accuracy into an unsupported claim of global validity, unique parameter recovery, or general applicability.

Simplify the presentation while keeping the definitions and evidence traceable. Do not expose local paths, production logs, or complex internal identifiers on the experiment slides.

## 7. End with concrete next steps

Connect each next step to an unresolved assumption, methodological gap, or experimental boundary. State the current gap, proposed action, and what the work should establish or test. Avoid vague lists of aspirations or presenting planned experiments as completed results.

## Keep projected text scientifically necessary

**Input/output continuity is an organizing rule, not a requirement to narrate the presentation on every page.** Let equations, diagrams, and results carry that structure.

- Remove presentation navigation, production commentary, and announcements of what will be explained.
- Remove prose that merely restates an equation or labels its left and right sides without adding necessary information. Use a concise symbol definition or local annotation when the distinction is needed.
- Do not add decorative subtitles, eyebrow lines, or strings of context tags by default. Each visible phrase should contribute independent scientific information.
- Use declarative titles and statements rather than questions. Put spoken transitions and extended explanations in the brief or speaker notes.
- Preserve necessary symbol definitions, assumptions, and reasons for nontrivial steps. Express them beside the relevant formula or in the shortest adequate notation; removing redundant prose must not remove a condition needed for correctness.

For every sentence, check whether deleting it would impair understanding of the scientific object, formula, reasoning, or result. If not, delete it.

## Check the completed report

Use the shared production checks, with particular attention to:

- Detailed pages form a complete calculation chain; each new object has a construction and a subsequent use.
- Overview pages communicate the core idea and tools; the synthesis accurately separates innovations, assumptions, and evidence limits.
- Symbols have consistent mathematical and physical meanings within the report and its deliverables.
- Experiment names are readable, values are traceable, and metric labels identify the actual quantities being compared or averaged.
- Whole-page scrolling works and requested exports contain every step; titles, references, and navigation do not obscure the derivation.
- The brief and requested final outputs correspond to the same version, with presentation commentary and repeated prose removed from the slides.
