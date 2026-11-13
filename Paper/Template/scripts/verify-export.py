"""Compile a flat source ZIP outside the Quarto project and retain build evidence."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=Path("_output/latex-source.zip"))
    parser.add_argument("--output", type=Path, default=Path("_output/independent-build"))
    args = parser.parse_args()
    archive = ROOT / args.archive
    destination = ROOT / args.output
    work = Path(tempfile.mkdtemp(prefix="quarto-cmame-standalone-"))
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as stream:
        names = stream.namelist()
        if any("/" in name or "\\" in name or name in (".", "..") for name in names):
            raise RuntimeError("Source archive is not flat.")
        stream.extractall(work)
    manifest = json.loads((work / "source-manifest.json").read_text(encoding="utf-8"))
    for record in manifest["files"]:
        if hashlib.sha256((work / record["name"]).read_bytes()).hexdigest() != record["sha256"]:
            raise RuntimeError(f"Resource integrity check failed: {record['name']}")
    main_tex = manifest["main_tex"]
    job = Path(main_tex).stem
    engine, bibliography = shutil.which("pdflatex"), shutil.which("bibtex")
    if not engine or not bibliography:
        raise RuntimeError("pdflatex and bibtex must be available on PATH.")
    latex = [engine, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-recorder", main_tex]
    commands = [latex, [bibliography, job], latex, latex]
    environment = os.environ.copy()
    for key in ("TEXINPUTS", "BIBINPUTS", "BSTINPUTS"):
        environment.pop(key, None)
    command_results = []
    for index, command in enumerate(commands, start=1):
        result = subprocess.run(command, cwd=work, env=environment, capture_output=True, text=True, errors="replace", timeout=180)
        log_name = f"pass-{index}.txt"
        (destination / log_name).write_text(result.stdout + result.stderr, encoding="utf-8")
        command_results.append({"command": [Path(command[0]).name, *command[1:]], "exit_code": result.returncode, "log": log_name})
        if result.returncode:
            raise RuntimeError(f"Independent build failed; inspect {log_name}")
    log = (work / f"{job}.log").read_text(encoding="utf-8", errors="replace")
    fatal_markers = ("There were undefined references", "undefined citations", "multiply defined", "Overfull \\hbox", "Overfull \\vbox")
    if any(marker in log for marker in fatal_markers):
        raise RuntimeError("Final LaTeX log contains unresolved references or material overflow.")
    recorder = (work / f"{job}.fls").read_text(encoding="utf-8", errors="replace")
    if str(ROOT).replace("\\", "/").casefold() in recorder.replace("\\", "/").casefold():
        raise RuntimeError("The independent build accessed the original project.")
    for suffix in (".pdf", ".log", ".bbl", ".blg", ".fls"):
        shutil.copyfile(work / (job + suffix), destination / (job + suffix))
    report = {
        "success": True,
        "flat_archive": True,
        "manifest_hashes_verified": True,
        "build_outside_project": True,
        "original_project_accessed": False,
        "quarto_invoked": False,
        "commands": command_results,
        "nonfatal_notes": [line.strip() for line in log.splitlines() if "Warning:" in line or "Underfull" in line],
        "engine": subprocess.run([engine, "--version"], capture_output=True, text=True, errors="replace").stdout.splitlines()[0],
    }
    (destination / "verification.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
