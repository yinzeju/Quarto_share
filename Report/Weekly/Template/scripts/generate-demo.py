"""Generate the explicitly synthetic oscillator data and scientific layout assets."""

from pathlib import Path
import csv
import hashlib
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parents[1]
INK, BLUE, TEAL, RED = "#17324D", "#2F6B9A", "#168A8A", "#B64B4B"


def save_plot(fig, name):
    for extension in ("png", "svg"):
        fig.savefig(ROOT / "assets" / f"{name}.{extension}", dpi=180, facecolor="white")
        if extension == "svg":
            path = ROOT / "assets" / f"{name}.{extension}"
            text = "\n".join(line.rstrip() for line in path.read_text(encoding="utf-8").splitlines()) + "\n"
            path.write_text(text, encoding="utf-8", newline="\n")
    plt.close(fig)


def fit_dmd(x, y, rank):
    u, singular, vh = np.linalg.svd(x, full_matrices=False)
    ur, vr = u[:, :rank], vh.conj().T[:, :rank]
    bridge = (y @ vr) / singular[:rank]
    reduced = ur.conj().T @ bridge
    values, vectors = np.linalg.eig(reduced)
    modes = bridge @ vectors
    operator = bridge @ ur.conj().T
    return operator, reduced, values, modes, singular


def forecast(operator, initial, steps):
    predicted = np.empty((initial.size, steps))
    state = initial.copy()
    for index in range(steps):
        state = operator @ state
        predicted[:, index] = state
    return predicted


def draw_system(displacement, time, font_path):
    frame = Image.new("RGB", (1000, 400), "#F7F9FB")
    draw = ImageDraw.Draw(frame)
    normal = ImageFont.truetype(font_path, 25)
    small = ImageFont.truetype(font_path, 21)
    title = ImageFont.truetype(font_path, 30)
    draw.text((35, 22), "教学合成算例：双自由度阻尼振子", font=title, fill=INK)
    draw.text((35, 69), f"无量纲时间 τ = {time:5.2f}", font=normal, fill=BLUE)
    centers = [340 + 66 * displacement[0], 660 + 66 * displacement[1]]
    y = 223
    for wall in (80, 920):
        draw.line((wall, 142, wall, 292), fill=INK, width=7)
    for reference in (340, 660):
        for top in range(138, 306, 16):
            draw.line((reference, top, reference, top + 7), fill="#B8C4CE", width=2)

    def spring(left, right):
        points = [(left, y), (left + 14, y)]
        for index, xx in enumerate(np.linspace(left + 20, right - 20, 17)):
            points.append((float(xx), y + (13 if index % 2 else -13)))
        points.extend([(right - 14, y), (right, y)])
        draw.line(points, fill=BLUE, width=4)

    spring(80, centers[0] - 48)
    spring(centers[0] + 48, centers[1] - 48)
    spring(centers[1] + 48, 920)
    for index, (center, color) in enumerate(zip(centers, (BLUE, TEAL)), start=1):
        draw.rounded_rectangle((center - 48, y - 41, center + 48, y + 41), radius=7, fill=color)
        draw.text((center - 25, y - 19), f"m{index}", font=normal, fill="white")
        draw.text((center - 56, y + 67), f"q{index} = {displacement[index-1]:+.2f}", font=small, fill=INK)
    draw.text((35, 348), "M = I，C = 0.08 I；三根弹簧的无量纲刚度均为 1", font=small, fill=INK)
    return frame


def main():
    for name in ("data", "assets", "sources"):
        (ROOT / name).mkdir(exist_ok=True)
    font_path = font_manager.findfont(font_manager.FontProperties(family=["Microsoft YaHei", "Noto Sans CJK SC", "DejaVu Sans"]))
    plt.rcParams.update({"font.family": font_manager.FontProperties(fname=font_path).get_name(),
                         "font.size": 12, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.unicode_minus": False, "svg.fonttype": "none"})
    dt, training_pairs, test_steps = 0.04, 150, 100
    stiffness = np.array([[2.0, -1.0], [-1.0, 2.0]])
    generator = np.block([[np.zeros((2, 2)), np.eye(2)], [-stiffness, -0.08 * np.eye(2)]])
    truth_operator = expm(dt * generator)
    states = np.empty((4, training_pairs + test_steps + 1))
    states[:, 0] = [0.9, -0.4, 0.0, 0.3]
    for index in range(states.shape[1] - 1):
        states[:, index + 1] = truth_operator @ states[:, index]
    time = np.arange(states.shape[1]) * dt
    x, y = states[:, :training_pairs], states[:, 1:training_pairs+1]
    actual = states[:, training_pairs+1:]
    outputs, rows = {}, []
    for rank in (2, 4):
        operator, reduced, eigenvalues, modes, singular = fit_dmd(x, y, rank)
        predicted = forecast(operator, states[:, training_pairs], test_steps)
        outputs[rank] = {"operator": operator, "reduced": reduced, "values": eigenvalues, "modes": modes, "prediction": predicted}
        rows.append({"rank": rank, "training_relative_frobenius": float(np.linalg.norm(y - operator @ x) / np.linalg.norm(y)),
                     "forecast_relative_frobenius": float(np.linalg.norm(actual - predicted) / np.linalg.norm(actual)),
                     "operator_relative_error": float(np.linalg.norm(operator - truth_operator) / np.linalg.norm(truth_operator))})
    full = outputs[4]
    amplitude = np.linalg.solve(full["modes"], states[:, training_pairs])
    modal = full["modes"] @ (amplitude[:, None] * full["values"][:, None] ** np.arange(1, test_steps + 1)[None, :])
    eigen_residual = np.linalg.norm(full["operator"] @ full["modes"] - full["modes"] * full["values"]) / np.linalg.norm(full["modes"])
    checks = {"full_state_rank": int(np.linalg.matrix_rank(x)), "full_rank_operator_error": rows[1]["operator_relative_error"],
              "mode_eigenrelation_relative_residual": float(eigen_residual),
              "modal_vs_recurrence_relative_error": float(np.linalg.norm(modal.real - full["prediction"]) / np.linalg.norm(full["prediction"]))}
    assert checks["full_state_rank"] == 4
    assert checks["full_rank_operator_error"] < 1e-10
    assert checks["mode_eigenrelation_relative_residual"] < 1e-10
    assert checks["modal_vs_recurrence_relative_error"] < 1e-10
    with (ROOT / "data/trajectory.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["m", "tau", "q1", "q2", "v1", "v2", "split"])
        for index, tau in enumerate(time):
            writer.writerow([index, float(tau), *map(float, states[:, index]), "fit" if index <= training_pairs else "forecast"])
    metadata = {"label": "Synthetic teaching example; not a real experiment", "dimensionless": True, "noise": "none",
                "dt": dt, "training_pairs": training_pairs, "forecast_steps": test_steps, "forecast_initial_index": training_pairs,
                "initial_state": states[:, 0].tolist(), "continuous_generator": generator.tolist(), "truth_operator": truth_operator.tolist(),
                "singular_values": singular.tolist(), "metrics": rows, "checks": checks}
    (ROOT / "data/results.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    table = ["| 保留秩 | 训练相对残差 | 未来 100 步相对误差 |", "|---:|---:|---:|"]
    for row in rows:
        table.append(f'| {row["rank"]} | {100*row["training_relative_frobenius"]:.3e}% | {100*row["forecast_relative_frobenius"]:.3e}% |')
    (ROOT / "data/metrics-table.qmd").write_text("\n".join(table) + "\n", encoding="utf-8", newline="\n")

    frames = [draw_system(states[:2, index], time[index], font_path) for index in range(0, states.shape[1], 3)]
    draw_system(np.zeros(2), 0.0, font_path).save(ROOT / "assets/system-static.png")
    frames[0].save(ROOT / "assets/oscillator.gif", save_all=True, append_images=frames[1:], duration=120, loop=0, optimize=True)

    fig, ax = plt.subplots(figsize=(8.6, 3.7), constrained_layout=True)
    for index, color in enumerate((BLUE, TEAL)):
        ax.plot(time, states[index], color=color, label=f"真值 q{index+1}")
        ax.plot(time[training_pairs+1:], full["prediction"][index], "--", color=color, linewidth=2.0, label=f"DMD q{index+1}")
    ax.axvline(time[training_pairs], color=RED, linestyle=":", label="预测起点")
    ax.set(xlabel="无量纲时间 τ", ylabel="无量纲位移", title="合成算例：从第 150 步初态向前预测")
    ax.legend(frameon=False, ncol=3, fontsize=10)
    ax.grid(alpha=0.18)
    save_plot(fig, "responses")

    fig, ax = plt.subplots(figsize=(5.5, 3.7), constrained_layout=True)
    ax.semilogy(np.arange(1, 5), singular, "o-", color=BLUE)
    ax.axvline(2.5, color=RED, linestyle="--", label="截断到 r = 2")
    ax.set(xlabel="奇异值序号", ylabel="奇异值", xticks=[1, 2, 3, 4], title="四个非零奇异值对应完整状态信息")
    ax.legend(frameon=False, fontsize=10)
    ax.grid(alpha=0.18)
    save_plot(fig, "singular-values")

    fig, ax = plt.subplots(figsize=(5.5, 3.7), constrained_layout=True)
    angle = np.linspace(-0.11, 0.11, 250)
    ax.plot(np.cos(angle), np.sin(angle), ":", color="#9AA9B5", label="单位圆局部")
    eigen_true = np.linalg.eigvals(truth_operator)
    ax.scatter(eigen_true.real, eigen_true.imag, s=125, facecolors="none", edgecolors=BLUE, label="真实离散算子")
    ax.scatter(full["values"].real, full["values"].imag, marker="x", s=65, color=TEAL, label="完整秩 DMD")
    ax.set(xlabel="Re λ", ylabel="Im λ", title="识别谱与真实离散谱重合", xlim=(0.991, 1.001), ylim=(-0.09, 0.09))
    ax.ticklabel_format(axis="x", style="plain", useOffset=False)
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    ax.grid(alpha=0.18)
    save_plot(fig, "spectrum")

    for index in (0, 1):
        fig, ax = plt.subplots(figsize=(5.4, 3.1), constrained_layout=True)
        ax.plot(time[training_pairs+1:], actual[index], color=INK, linewidth=2.6, label="真值")
        ax.plot(time[training_pairs+1:], full["prediction"][index], "--", color=TEAL, label="r = 4")
        ax.plot(time[training_pairs+1:], outputs[2]["prediction"][index], "-.", color=RED, label="r = 2")
        ax.set(xlabel="无量纲时间 τ", ylabel=f"q{index+1}", title=f"第 {index+1} 个位移分量：100 步预测")
        ax.legend(frameon=False, ncol=3, fontsize=9)
        ax.grid(alpha=0.18)
        save_plot(fig, f"q{index+1}-forecast")
    fig, ax = plt.subplots(figsize=(7.8, 2.5), constrained_layout=True)
    ax.plot(states[0, :training_pairs+1], states[2, :training_pairs+1], color=BLUE, label="拟合段")
    ax.plot(states[0, training_pairs:], states[2, training_pairs:], color=TEAL, label="后续真值")
    ax.set(xlabel="无量纲位移 q1", ylabel="无量纲速度 v1", title="衰减运动的相平面轨迹")
    ax.legend(frameon=False, ncol=2, fontsize=10)
    ax.grid(alpha=0.18)
    save_plot(fig, "phase")

    assets = []
    for path in sorted(path for path in (ROOT / "assets").rglob("*") if path.is_file()):
        assets.append({"path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    provenance = {"data": "Generated by scripts/generate-demo.py from the stated dimensionless linear oscillator; no real experimental data.",
                  "style_origin": "The author's 20261029 weekly report: formula-first pages, complete derivations, light 16:9 and bottom-left citations.",
                  "method": {"doi": "10.3934/jcd.2014.1.391", "preprint": "https://arxiv.org/abs/1312.0041", "scope": "Exact DMD; derivations are re-expressed using the bundled Core notation."},
                  "assets": assets}
    (ROOT / "sources/source-manifest.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"metrics": rows, "checks": checks, "gif_frames": len(frames)}, indent=2))


if __name__ == "__main__":
    main()
