"""Labels every link to a document with the document's title, never with its path.

A link's label is legible: an item's ID and title, or a document's title or a phrase naming it, never a path
(docs/README.md, "A link is a link"). This tool finds the links labeled by a path, `[capabilities/README.md](…)` or
`` [`MBSE.md`](…) ``: a label that, without the backticks around it, is a file name or a path with an optional
`#anchor`. When the link's target is a document, a markdown file or a notebook, in the repository or a sibling checked
out beside it, in any of the three forms of a link (a relative path, a GitHub URL or the shorthand `mbse:<repo>/...`),
the label becomes the document's title: its first `# ` heading (in a notebook, the first in its markdown cells),
without trailing punctuation. The anchor, a section's or an item's, is kept as it is. A link labeled by an item's ID is
not a path label, and is left to update_item_titles.py; a path label to an item's detail file takes the file's title,
which is the item's `ID: title`.

    python3 ../mbse-basis/scripts/update_doc_titles.py [--check] [repository ...]

The repositories are their roots; by default, the current directory. Only git-tracked markdown files and notebooks are
read; a notebook's markdown cells alone are edited, and it is rewritten, in the JSON format it had, only if one
changed. Links in fenced code blocks and code spans are examples, and left alone, as is a link whose target is the
placeholder `…`.

A path label this tool cannot fix needs a human: one whose target is not a document (documents don't link source
files), whose file does not exist, whose document has no title, or which goes to another site. With --check nothing
is written: every path label left is listed, by kind, and the exit status is 1 if there are any.

Like polyrepo.py, this is kept in mbse-basis and run for every mbse repository. Standard library only.
"""

from __future__ import annotations

import json
import posixpath
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

from update_link_forms import GITHUB, SCHEME, SHORT, masked

DOCUMENTS = {".md", ".ipynb"}
NAMES = "md|ipynb|py|pyi|ts|tsx|js|jsx|mjs|cjs|sh|json|toml|yaml|yml|txt|cfg|ini|lock|html|css|csv"
PATH_LABEL = re.compile(rf"[\w./-]+\.(?:{NAMES})(?:#[\w.-]*)?")
LINK = re.compile(r"(?<![!\\])\[([^\]\n]*)\]\(([^)\s]+)([^)\n]*)\)")
FRONT = re.compile(r"\A---\n.*?^---[ \t]*$", re.M | re.S)
TITLE = re.compile(r"^ {0,3}#[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
ID = re.compile(r"(?:QUA|FEA|CAP|PRI|VOC)-\d{3}\b")

KINDS = {
    "rewritable": "path label",
    "not a document": "path label, not a document",
    "missing": "path label, no such file",
    "untitled": "path label, document without a title",
    "elsewhere": "path label, link to another site",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    where: str      # a line, or a notebook's cell and line
    link: str
    kind: str       # a key of KINDS
    title: str = ""

    def __str__(self) -> str:
        return f"{self.path}:{self.where}: {self.link}" + (f" -> {self.title}" if self.title else "")


def path_label(label: str) -> bool:
    """Whether a link's label, without the backticks around it, is a path or a file name, rather than an item's ID."""
    bare = label.strip().strip("`").strip()
    return bool(PATH_LABEL.fullmatch(bare)) and not ID.match(bare)


def markdown_cells(path: Path) -> list[str]:
    return ["".join(c["source"]) for c in json.loads(path.read_text())["cells"] if c["cell_type"] == "markdown"]


def title(path: Path, cache: dict[Path, str]) -> str:
    """A document's title: its first `# ` heading outside code, plain text, without trailing punctuation; "" if none."""
    if path not in cache:
        texts = markdown_cells(path) if path.suffix == ".ipynb" else [path.read_text()]
        found = ""
        for text in texts:
            text = FRONT.sub(lambda m: "\n" * m[0].count("\n"), text)
            code = masked(text)
            heading = next((m for m in TITLE.finditer(text) if not any(a <= m.start() < b for a, b in code)), None)
            if heading:
                found = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading[1])
                found = re.sub(r"<[^>]+>", "", found).strip().rstrip(".:;,!?").strip()
                found = re.sub(r"([\[\]])", r"\\\1", found)
                break
        cache[path] = found
    return cache[path]


def target(link: str, here: Path, root: Path) -> Path | str:
    """The file a link's target designates, from the file `here` in the repository at `root`, or the kind of path label
    it leaves when it designates none in the mbse repositories."""
    for pattern in (GITHUB, SHORT):
        m = pattern.fullmatch(link)
        if m:
            base = root if m[1] == root.resolve().name else root.resolve().parent / m[1]
            return base / unquote(m[2])
    if SCHEME.match(link) or link.startswith("/"):
        return "elsewhere"
    path = unquote(link.partition("#")[0])
    return Path(posixpath.normpath((here.parent / path).as_posix())) if path else here


def relabel(text: str, here: Path, root: Path, cache: dict[Path, str]) -> tuple[str, list[tuple[int, str, str, str]]]:
    """Markdown `text`, from the file `here`, with each path label to a document replaced by the document's title, and
    each path label found: its offset, the link as written, its kind and the title it takes."""
    code = masked(text)
    found = []

    def link(m: re.Match) -> str:
        if any(a <= m.start() < b for a, b in code) or not path_label(m[1]) or "…" in m[2]:
            return m[0]
        file = target(m[2], here, root)
        if isinstance(file, str):
            kind, name = file, ""
        elif not file.exists():
            kind, name = "missing", ""
        elif not file.is_file() or file.suffix not in DOCUMENTS:
            kind, name = "not a document", ""
        else:
            name = title(file, cache)
            kind = "rewritable" if name else "untitled"
        found.append((m.start(), m[0], kind, name))
        return f"[{name}]({m[2]}{m[3]})" if name else m[0]

    return LINK.sub(link, text), found


def line(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def dump(notebook: dict, raw: str) -> str:
    """The notebook as JSON, in the format of `raw`, its text as read: the first that reproduces it, else nbformat's."""
    original = json.loads(raw)
    end = "\n" if raw.endswith("\n") else ""
    for indent in (1, 2, 4, None):
        for sort_keys in (True, False):
            for ensure_ascii in (False, True):
                options = {"indent": indent, "sort_keys": sort_keys, "ensure_ascii": ensure_ascii}
                if json.dumps(original, **options) + end == raw:
                    return json.dumps(notebook, **options) + end
    return json.dumps(notebook, indent=1, sort_keys=True, ensure_ascii=False) + end


def files(root: Path) -> list[str]:
    """The repository's tracked documents, relative to its root."""
    listed = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, text=True)
    names = (listed.stdout.split("\0") if listed.returncode == 0
             else [p.relative_to(root).as_posix() for p in root.rglob("*")])
    return [name for name in names if name and Path(name).suffix in DOCUMENTS and (root / name).is_file()
            and not (root / name).is_symlink()]


def update(roots: list[Path], check: bool = False) -> tuple[list[Finding], list[Path]]:
    """Relabels every path label to a document in the repositories; returns each path label found, and the files that
    were, or with check would be, changed."""
    findings, changed, cache = [], [], {}
    for root in roots:
        for name in files(root):
            path = root / name
            raw = path.read_text()
            if path.suffix == ".ipynb":
                notebook = json.loads(raw)
                texts, edited = [], False
                for i, cell in enumerate(notebook["cells"]):
                    if cell["cell_type"] != "markdown":
                        continue
                    source = cell["source"]
                    text = "".join(source)
                    new, found = relabel(text, path, root, cache)
                    texts.append((f"cell {i}, line ", text, found))
                    if new != text:
                        cell["source"] = new if isinstance(source, str) else new.splitlines(keepends=True)
                        edited = True
                new_raw = dump(notebook, raw) if edited else raw
            else:
                new_raw, found = relabel(raw, path, root, cache)
                texts = [("", raw, found)]
            for prefix, text, found in texts:
                for offset, link, kind, name in found:
                    findings.append(Finding(path, f"{prefix}{line(text, offset)}", link, kind, name))
            if new_raw != raw:
                changed.append(path)
                if not check:
                    path.write_text(new_raw)
    return findings, changed


def main(argv: list[str]) -> int:
    check = "--check" in argv
    roots = [Path(a) for a in argv if a != "--check"] or [Path.cwd()]
    findings, changed = update(roots, check=check)
    plural = lambda n, word: f"{n} {word}{'s' if n != 1 else ''}"  # noqa: E731
    left = [f for f in findings if check or f.kind != "rewritable"]
    for kind, heading in KINDS.items():
        for finding in (f for f in left if f.kind == kind):
            print(f"{heading if check or kind != 'rewritable' else 'relabeled'}: {finding}")
    counts = {kind: sum(f.kind == kind for f in findings) for kind in KINDS}
    rest = "; ".join(f"{counts[kind]} {KINDS[kind].removeprefix('path label, ')}" for kind in KINDS
                     if kind != "rewritable")
    if check:
        print(f"{plural(counts['rewritable'], 'path label')} to relabel, in {plural(len(changed), 'file')}; "
              f"left for a human: {rest}")
        return 1 if left else 0
    print(f"{plural(counts['rewritable'], 'path label')} relabeled, in {plural(len(changed), 'file')}; "
          f"left for a human: {rest}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
