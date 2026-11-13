# Test manuscript brief

This is a synthetic publishing-pipeline project, not a research submission.

- Question: Can Quarto preserve equations, a vector figure, an editable table, citations, and author metadata when exporting Elsevier-style LaTeX and PDF?
- Manuscript language: English.
- Target-format example: Computer Methods in Applied Mechanics and Engineering (CMAME), Elsevier.
- Scientific example: Standard one-dimensional linear finite elements with a manufactured diffusion solution. No novelty is claimed.
- Evidence: `scripts/generate-demo.py` produces `results/convergence.csv`, `results/convergence.json`, `results/convergence-table.qmd`, and `figures/verification.pdf`.
- Mathematical source: Integration by parts gives the weak form; differentiation verifies the analytical forcing.
- Literature: Two real background publications; neither establishes originality for this test.
- Identities: Author, institution, address, and email are explicitly fictional test metadata.
- Missing for a real paper: A research contribution, author-approved information/declarations, and a complete current CMAME compliance review.

## Claim-to-evidence map

| Claim | Evidence | Boundary |
|---|---|---|
| The exact field solves the boundary-value problem | Differentiation of the stated manufactured solution | One smooth one-dimensional problem |
| The solver shows approximately second-order L2 convergence | Generated CSV/JSON and results table | Observation, not a general proof |
| The manuscript exports to journal-style PDF and TeX | Commands/results in `validation.md` | Local toolchain only |
| The bundle builds independently of Quarto | Fresh extracted-directory build in `validation.md` | Requires a standard TeX distribution |
