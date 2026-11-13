"""Check and ZIP publishing skills and runnable templates from an explicit allowlist."""

from pathlib import Path
from urllib.parse import unquote
import argparse
import ast
import hashlib
import json
import re
import sys
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("quarto-report", "weekly-report", "quarto-paper")
ENTRIES = (
    "README.md", "AGENTS.md", ".gitignore", ".gitattributes",
    *(f".agents/skills/{name}" for name in SKILLS),
    "docs", "scripts",
    "Paper/README.md", "Report/README.md", "Report/Weekly/README.md",
    "Report/Weekly/Template",
    *(f"Paper/Template/{name}" for name in (
        "README.md", ".gitignore", "_quarto.yml", "_quarto-submission.yml",
        "manuscript.qmd", "references.bib", "highlights.txt", "math-header.html", "math-tex.lua",
        "notes", "scripts", "figures", "results", "_extensions", "assets",
    )),
)
TEXT_SUFFIXES = {".md", ".qmd", ".yml", ".yaml", ".py", ".bib", ".css", ".scss", ".js", ".html", ".lua", ".tex", ".cls", ".bst", ".csl", ".csv", ".json", ".txt", ".svg"}
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".woff", ".woff2", ".ttf"}
SKIP_DIRS = {"__pycache__", ".quarto", "_output", "tmp", "output", ".playwright-cli", "node_modules"}
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
MACHINE_PATH = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"
    r"|/(?:Users|home)/[^\s/]+/"
    r"|\\\\[A-Za-z0-9_.-]+\\[A-Za-z0-9_.-]+\\"
)
SECRET = re.compile(
    r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"
    r"|\bgh[pousr]_[A-Za-z0-9]{20,}"
    r"|\bgithub_pat_[A-Za-z0-9_]{20,}"
    r"|\bsk-[A-Za-z0-9_-]{24,}"
)


def collect():
    files = []
    for entry in ENTRIES:
        base = ROOT / entry
        if not base.exists():
            raise ValueError(f"Required entry is missing: {entry}")
        candidates = [base] if base.is_file() else [base, *base.rglob("*")]
        for path in candidates:
            rel = path.relative_to(ROOT)
            if any(part in SKIP_DIRS or part.endswith("_files") for part in rel.parts) or path.suffix in {".pyc", ".pyo"}:
                continue
            if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
                raise ValueError(f"Linked or external content is not allowed: {rel.as_posix()}")
            if path.is_file():
                if path.name not in {".gitignore", ".gitattributes", "LICENSE"} and path.suffix not in TEXT_SUFFIXES | BINARY_SUFFIXES:
                    raise ValueError(f"Unexpected file type; review before sharing: {rel.as_posix()}")
                files.append(path)
    return sorted(set(files), key=lambda path: path.relative_to(ROOT).as_posix())


def check(files):
    errors = []
    allowed = set(files)
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix in BINARY_SUFFIXES:
            continue
        content = path.read_text(encoding="utf-8-sig")
        # LaTeX map type annotations can resemble drive paths.
        path_text = content
        if path.suffix in {".md", ".qmd"}:
            path_text = re.sub(r"(?s)\$\$.*?\$\$", "", path_text)
            path_text = re.sub(r"\$[^$\n]+\$", "", path_text)
        if MACHINE_PATH.search(path_text):
            errors.append(f"{rel}: machine-specific path found")
        if SECRET.search(content):
            errors.append(f"{rel}: possible credential found")
        if path.suffix == ".py":
            try:
                ast.parse(content, filename=rel)
            except SyntaxError as error:
                errors.append(f"{rel}: {error.msg}, line {error.lineno}")
        if path.suffix not in {".md", ".qmd"}:
            continue
        # Code fences may contain illustrative Markdown, not document links.
        prose = re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$", "", content)
        for match in LINK.finditer(prose):
            target = match.group(1).strip()
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / target).resolve()
            # Quarto selects PNG/PDF for extensionless image paths by output format.
            if resolved.is_relative_to(ROOT) and not resolved.exists() and not resolved.suffix:
                alternatives = [resolved.with_suffix(suffix) for suffix in (".png", ".pdf", ".svg", ".jpg") if resolved.with_suffix(suffix).is_file()]
                if alternatives:
                    if any(candidate not in allowed for candidate in alternatives):
                        errors.append(f"{rel}: image variant will not be packaged: {target}")
                    continue
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{rel}: broken or external local link: {target}")
            elif resolved.is_file() and resolved not in allowed:
                errors.append(f"{rel}: link target will not be packaged: {target}")
        if path.name == "SKILL.md":
            front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
            if not front:
                errors.append(f"{rel}: missing skill front matter")
            elif not re.search(rf"(?m)^name: {re.escape(path.parent.name)}$", front[1]):
                errors.append(f"{rel}: skill name does not match its directory")
            elif not re.search(r"(?m)^description: \S", front[1]):
                errors.append(f"{rel}: missing skill description")
    for name in SKILLS:
        for entry in ("SKILL.md", "agents/openai.yaml"):
            if ROOT / ".agents/skills" / name / entry not in allowed:
                errors.append(f"Missing required skill resource: {name}/{entry}")
    if errors:
        raise ValueError("\n".join(errors))


def build(files):
    manifest = {
        "scope": "Paper/report/weekly skills, Core notation, and runnable paper and scientific presentation templates.",
        "files": [
            {"path": path.relative_to(ROOT).as_posix(),
             "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
             "bytes": path.stat().st_size}
            for path in files
        ],
    }
    output = ROOT / "dist" / "quarto-share.zip"
    if output.parent.is_symlink() or output.is_symlink():
        raise ValueError("Archive output must not be a symbolic link.")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Stable metadata gives an identical archive for identical source bytes.
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            info = zipfile.ZipInfo("quarto-share/" + path.relative_to(ROOT).as_posix())
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo("quarto-share/share-manifest.json")
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(info, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed.")
    print(f"Built dist/quarto-share.zip: {len(files)} files plus SHA-256 manifest")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate without writing a ZIP.")
    args = parser.parse_args()
    try:
        files = collect()
        check(files)
        print(f"Checked {len(files)} files: links, skill entries, Python syntax, and path/secret patterns")
        if not args.check:
            build(files)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Share build failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
