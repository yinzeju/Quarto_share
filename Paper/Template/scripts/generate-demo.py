"""Generate reproducible toy finite-element evidence for the pipeline test."""
from pathlib import Path
import csv
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def solve(elements):
    nodes = np.linspace(0.0, 1.0, elements + 1)
    h = 1.0 / elements
    stiffness = np.zeros((elements + 1, elements + 1))
    load = np.zeros(elements + 1)
    points, weights = np.polynomial.legendre.leggauss(4)
    shape = np.column_stack(((1 - points) / 2, (1 + points) / 2))
    local_stiffness = np.array([[1.0, -1.0], [-1.0, 1.0]]) / h
    for element in range(elements):
        indices = [element, element + 1]
        x = nodes[element] + (points + 1) * h / 2
        force = np.pi**2 * np.sin(np.pi * x)
        stiffness[np.ix_(indices, indices)] += local_stiffness
        load[indices] += shape.T @ (weights * force) * h / 2
    values = np.zeros_like(nodes)
    values[1:-1] = np.linalg.solve(stiffness[1:-1, 1:-1], load[1:-1])
    points, weights = np.polynomial.legendre.leggauss(8)
    e0_squared = e1_squared = 0.0
    for element in range(elements):
        x = nodes[element] + (points + 1) * h / 2
        approximation = values[element] * (1 - points) / 2 + values[element + 1] * (1 + points) / 2
        gradient = (values[element + 1] - values[element]) / h
        e0_squared += np.dot(weights, (np.sin(np.pi * x) - approximation)**2) * h / 2
        e1_squared += np.dot(weights, (np.pi * np.cos(np.pi * x) - gradient)**2) * h / 2
    return nodes, values, float(np.sqrt(e0_squared)), float(np.sqrt(e1_squared))


def main():
    results, figures = ROOT / "results", ROOT / "figures"
    results.mkdir(exist_ok=True)
    figures.mkdir(exist_ok=True)
    rows = []
    for elements in (8, 16, 32, 64):
        _, _, e0, e1 = solve(elements)
        order = None if not rows else float(np.log2(rows[-1]["l2_error"] / e0))
        rows.append({"elements": elements, "h": 1 / elements, "l2_error": e0, "h1_seminorm_error": e1, "l2_order": order})
    with (results / "convergence.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    (results / "convergence.json").write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
    table = ["| Elements | $L^2$ error | $H^1$ seminorm error | $L^2$ order |", "|---:|---:|---:|---:|"]
    for row in rows:
        order = "-" if row["l2_order"] is None else f'{row["l2_order"]:.3f}'
        table.append(f'| {row["elements"]} | {row["l2_error"]:.6e} | {row["h1_seminorm_error"]:.6e} | {order} |')
    table.extend(["", ": Errors for the manufactured-solution test, computed by the local solver. {#tbl-convergence}", ""])
    (results / "convergence-table.qmd").write_text("\n".join(table), encoding="utf-8")

    plt.rcParams.update({"font.family": "serif", "font.size": 10, "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42})
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0), constrained_layout=True)
    x = np.linspace(0, 1, 300)
    nodes, values, _, _ = solve(8)
    axes[0].plot(x, np.sin(np.pi * x), color="#172f4f", label="Exact solution")
    axes[0].plot(nodes, values, "o--", color="#c66828", markersize=4, label="Linear FEM, N = 8")
    axes[0].set(xlabel="Coordinate x", ylabel="Scalar field u", title="(a) Manufactured solution")
    axes[0].legend(frameon=False, fontsize=8, loc="lower center")
    h = np.array([row["h"] for row in rows])
    e0 = np.array([row["l2_error"] for row in rows])
    e1 = np.array([row["h1_seminorm_error"] for row in rows])
    axes[1].loglog(h, e0, "o-", color="#172f4f", label=r"$L^2$ error")
    axes[1].loglog(h, e1, "s-", color="#c66828", label=r"$H^1$ seminorm error")
    axes[1].loglog(h, e0[0] * (h / h[0])**2 * 0.55, ":", color="#172f4f", label=r"$O(h^2)$ guide")
    axes[1].loglog(h, e1[0] * (h / h[0]) * 1.6, ":", color="#c66828", label=r"$O(h)$ guide")
    axes[1].set(xlabel="Mesh size h", ylabel="Error", title="(b) Mesh refinement")
    axes[1].set_xticks(h[::-1])
    axes[1].set_xticklabels([r"$1/64$", r"$1/32$", r"$1/16$", r"$1/8$"])
    axes[1].xaxis.set_minor_formatter(NullFormatter())
    fig.legend(*axes[1].get_legend_handles_labels(), loc="outside lower center", ncol=4, frameon=False, fontsize=8)
    axes[1].grid(alpha=0.2)
    fig.savefig(figures / "verification.pdf", metadata={"Title": "Manufactured-solution pipeline test"})
    fig.savefig(figures / "verification.png", dpi=220)
    plt.close(fig)
    print(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
