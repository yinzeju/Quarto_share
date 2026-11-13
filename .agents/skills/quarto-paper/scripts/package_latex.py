"""Flatten conventional Quarto LaTeX dependencies into a fresh source snapshot.

Dynamic TeX dependencies must be supplied with --resource. Standard TeX packages
remain dependencies of the recipient's TeX distribution.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import zipfile


REFERENCE = re.compile(
    r"\\(?P<command>includegraphics\*?|input|include|bibliography|bibliographystyle)"
    r"\s*(?:\[[^\]]*\]\s*)?\{(?P<value>[^{}\n]+)\}"
)


def package(tex, root, output, resources):
    tex, root, output = tex.resolve(), root.resolve(), output.resolve()
    archive = Path(str(output) + ".zip")
    if not tex.is_file():
        raise ValueError(f"Main TeX file does not exist: {tex}")
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError("Output must be a new or empty directory; use a new snapshot name.")
    if archive.exists():
        raise ValueError("The sibling ZIP already exists; use a new snapshot name.")
    files, names, rewritten = {}, {}, {}

    def add(path):
        path = path.resolve()
        if not path.is_file():
            raise ValueError(f"Resource does not exist: {path}")
        key = path.name.casefold()
        if key in names and names[key] != path:
            raise ValueError(f"Flat filename collision: {names[key]} and {path}")
        if key == "source-manifest.json":
            raise ValueError("Resource uses the reserved manifest filename.")
        names[key] = path
        if path in files:
            return
        files[path] = path.name
        if path.suffix.lower() == ".tex":
            text = path.read_text(encoding="utf-8-sig")
            # Preserve comments; inspect only active literal references.
            active = re.sub(r"(?<!\\)%[^\n]*", "", text)
            replacements = {}
            for match in REFERENCE.finditer(active):
                command, value = match["command"], match["value"]
                tokens = value.split(",") if command == "bibliography" else [value]
                new_tokens = []
                for token in tokens:
                    token = token.strip()
                    if "\\" in token or "#" in token:
                        raise ValueError(f"Dynamic file reference needs manual handling: {token}")
                    suffixes = {
                        "input": ["", ".tex"],
                        "include": ["", ".tex"],
                        "bibliography": ["", ".bib"],
                        "bibliographystyle": ["", ".bst"],
                    }.get(command, ["", ".pdf", ".png", ".jpg", ".jpeg", ".eps"])
                    dependency = None
                    for parent in (path.parent, root):
                        for suffix in suffixes:
                            candidate = (parent / (token + suffix)).resolve()
                            if candidate.is_file():
                                dependency = candidate
                                break
                        if dependency:
                            break
                    if dependency is None and command == "bibliographystyle":
                        kpsewhich = shutil.which("kpsewhich")
                        if kpsewhich:
                            result = subprocess.run(
                                [kpsewhich, token if token.endswith(".bst") else token + ".bst"],
                                capture_output=True, text=True, timeout=30, check=False,
                            )
                            candidate = Path(result.stdout.strip())
                            if result.returncode == 0 and candidate.is_file():
                                dependency = candidate
                    if dependency is None:
                        raise ValueError(f"Cannot resolve {command} resource {token!r} from {path.name}")
                    add(dependency)
                    new_tokens.append(dependency.stem if command == "bibliographystyle" else dependency.name)
                replacements[(command, value)] = ",".join(new_tokens)

            def replace(match):
                value = replacements.get((match["command"], match["value"]))
                if value is None:
                    return match.group(0)
                start, end = match.span("value")
                whole_start = match.start()
                return match.group(0)[:start - whole_start] + value + match.group(0)[end - whole_start:]

            rewritten[path] = REFERENCE.sub(replace, text)

    add(tex)
    for resource in resources:
        add(resource)
    for candidate in (tex.with_suffix(".bbl"), root / tex.with_suffix(".bbl").name):
        if candidate.is_file():
            add(candidate)
            break

    output.mkdir(parents=True, exist_ok=True)
    manifest = {"main_tex": tex.name, "scope": "Local source snapshot; standard TeX packages are required.", "files": []}
    for path, name in sorted(files.items(), key=lambda item: item[1].casefold()):
        target = output / name
        if path in rewritten:
            target.write_text(rewritten[path], encoding="utf-8", newline="\n")
        else:
            shutil.copyfile(path, target)
        origin = path.relative_to(root).as_posix() if path.is_relative_to(root) else "external-resource/" + path.name
        manifest["files"].append({"name": name, "source": origin, "sha256": hashlib.sha256(target.read_bytes()).hexdigest()})
    (output / "source-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as stream:
        for path in sorted(output.iterdir()):
            stream.write(path, arcname=path.name)
    print(json.dumps({"directory": str(output), "archive": str(archive), "files": len(files)}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tex", required=True, type=Path)
    parser.add_argument("--root", default=Path.cwd(), type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--resource", action="append", default=[], type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        package(root / args.tex, root, root / args.output, [root / value for value in args.resource])
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        parser.exit(1, f"Packaging failed: {error}\n")


if __name__ == "__main__":
    main()
