"""Keeps every link to an mbse-basis item labeled with the item's ID and title.

An item's title is the one its index entry gives, in the entry's head: `**CAP-013: an in-memory store journaled to
DynamoDB**`, in docs/QUALITIES.md, docs/features/README.md, docs/capabilities/README.md, docs/PRINCIPLES.md or
docs/VOCABULARY.md. A link to an item, in any repository's documents or source comments, is labeled `ID: title`
(docs/README.md, "A link is a link"), and an item's detail file is headed `# ID: title`. Run this after changing a
title, or to check that no label has drifted:

    python3 ../mbse-basis/scripts/update_item_titles.py [--check] [repository ...]

The repositories are their roots; by default, the current directory. A link counts as one to an item when its label
starts with the item's ID and its path resolves to that item: its anchor in an index, or its detail file. Other links
are left alone. With --check nothing is written: the files whose labels are out of date are listed, and the exit status
is 1 if there are any.

Like polyrepo.py, this is kept in mbse-basis and run for every mbse repository.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASIS = Path(__file__).resolve().parent.parent
INDEXES = ["QUALITIES.md", "features/README.md", "capabilities/README.md", "PRINCIPLES.md", "VOCABULARY.md"]
DETAILED = ["features", "capabilities"]
SUFFIXES = {".md", ".py", ".ts", ".tsx", ".js", ".json", ".toml", ".ipynb"}
FIXTURES = Path(__file__).resolve().parent / "test_update_item_titles.py"  # stale labels on purpose
ID = r"(?:QUA|FEA|CAP|PRI|VOC)-\d{3}"
HEAD = re.compile(rf'^- <a id="({ID})"></a>\*\*\[?\1: (.+?)(?:\]\([^)]*\))?\*\*', re.M)
LINK = re.compile(rf"\[({ID})(?::[^\]\n]*)?\]\(([^)\s#]*)(#[^)\s]*)?\)")


def titles(docs: Path) -> dict[str, str]:
    """Each item's title, from the heads of the index entries."""
    found = {}
    for index in INDEXES:
        path = docs / index
        if path.exists():
            found.update(HEAD.findall(path.read_text()))
    return found


def item(docs: Path, target: Path, anchor: str) -> str | None:
    """The item a link's target designates: an anchor in an index, or a detail file."""
    try:
        rel = target.resolve().relative_to(docs.resolve()).as_posix()
    except ValueError:
        return None
    if rel in INDEXES and re.fullmatch(ID, anchor):
        return anchor
    folder, _, name = rel.rpartition("/")
    stem = name.removesuffix(".md")
    if folder in DETAILED and name.endswith(".md") and re.fullmatch(ID, stem):
        return stem
    return None


def relabel(text: str, here: Path, docs: Path, known: dict[str, str]) -> str:
    """`text`, from the file `here`, with each link to an item labeled `ID: title`, and a detail file's heading too."""
    def link(m: re.Match) -> str:
        label, path, anchor = m[1], m[2], (m[3] or "")[1:]
        target = (here.parent / path) if path else here
        if item(docs, target, anchor) != label or label not in known:
            return m[0]
        return f"[{label}: {known[label]}]({path}{m[3] or ''})"
    text = LINK.sub(link, text)
    own = item(docs, here, "")
    if own in known:
        text = re.sub(rf"^# {own}(?::| ·) .*$", f"# {own}: {known[own]}", text, count=1, flags=re.M)
    return text


def files(root: Path) -> list[Path]:
    """The repository's tracked text files that can hold a link."""
    listed = subprocess.run(["git", "-C", str(root), "ls-files"], capture_output=True, text=True)
    names = listed.stdout.split() if listed.returncode == 0 else [p.relative_to(root).as_posix() for p in root.rglob("*")]
    return [root / name for name in names if Path(name).suffix in SUFFIXES and (root / name).is_file()
            and (root / name).resolve() != FIXTURES]


def update(roots: list[Path], basis: Path = BASIS, check: bool = False) -> list[Path]:
    """Relabels every link to an item in the repositories; returns the files that were, or with check would be, changed."""
    docs = basis / "docs"
    known = titles(docs)
    changed = []
    for root in roots:
        for path in files(root):
            text = path.read_text()
            new = relabel(text, path, docs, known)
            if new != text:
                changed.append(path)
                if not check:
                    path.write_text(new)
    return changed


def main(argv: list[str]) -> int:
    check = "--check" in argv
    roots = [Path(a) for a in argv if a != "--check"] or [Path.cwd()]
    changed = update(roots, check=check)
    for path in changed:
        print(f"{'out of date' if check else 'relabeled'}: {path}")
    print(f"{len(changed)} file{'s' if len(changed) != 1 else ''} {'out of date' if check else 'relabeled'}")
    return 1 if check and changed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
