"""Writes every link that leaves its repository in the form its file calls for.

A link within its repository is a relative path, and is left alone. A link into another mbse repository, a sibling
checked out beside it, takes one of two forms (docs/README.md, "A link is a link"):

- in a markdown file, and in a notebook's markdown cells, a GitHub URL,
  `https://github.com/pitaman71/<repo>/blob/main/<path>[#anchor]`;
- in a skill (any file under a `skills/` or `skill/` directory), in a source comment (a .py, .ts, .tsx, .js or .sh
  file) and in a notebook's code cells, the shorthand `mbse:<repo>/<path>[#anchor]`, which each repository's AGENTS.md
  says how to resolve.

    python3 ../mbse-basis/scripts/update_link_forms.py [--check] [repository ...]

The repositories are their roots; by default, the current directory. Each git-tracked file is read, and each markdown
link in it whose target is a relative path into a sibling (`../<repo>/...` once normalized from the file's directory,
against the repository's root), or a GitHub URL or shorthand in the other form, is rewritten to its file's form. Links
in fenced code blocks and code spans of markdown are examples, and left alone; so is every URL to another site, and a
GitHub URL or shorthand into the repository itself. In a source file, every link is taken for one in a comment. A
notebook's cell sources alone are edited, and it is rewritten only if one changed.

With --check nothing is written: the links in the wrong form are listed, and so are the links into a sibling, in any
form, whose file does not exist in the sibling's checkout beside the repository, or whose anchor (a heading's slug, or
an `id` or `name` attribute) the file lacks. The exit status is 1 if there are any.

Like polyrepo.py, this is kept in mbse-basis and run for every mbse repository. Standard library only.
"""

from __future__ import annotations

import io
import json
import posixpath
import re
import subprocess
import sys
import tokenize
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

OWNER = "pitaman71"
SOURCES = {".py", ".ts", ".tsx", ".js", ".sh"}
FIXTURES = {Path(__file__).resolve().parent / "test_update_link_forms.py"}  # wrong forms on purpose
LINK = re.compile(r"\]\(([^)\s]+)([^)\n]*)\)")
GITHUB = re.compile(rf"https://github\.com/{OWNER}/([\w.-]+)/blob/main/([^#?\s]*)(#\S*)?")
SHORT = re.compile(r"mbse:([\w.-]+)/([^#\s]*)(#\S*)?")
SCHEME = re.compile(r"[A-Za-z][\w+.-]*:")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?(?:^ {0,3}\1[`~]*[ \t]*$|\Z)", re.M | re.S)
SPAN = re.compile(r"(`+)[^\n]+?\1(?!`)")
HEADING = re.compile(r"^ {0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
ID_ATTR = re.compile(r"""\b(?:id|name)\s*=\s*["']([^"']+)["']""")


@dataclass(frozen=True)
class Finding:
    path: Path
    where: str      # a line, or a notebook's cell and line
    target: str
    detail: str     # the right form, or why the target is unresolved

    def __str__(self) -> str:
        return f"{self.path}:{self.where}: {self.target} {self.detail}"


def skill(rel: str) -> bool:
    parts = Path(rel).parts
    return parts[0] == "skills" or "skill" in parts[:-1]


def form(rel: str) -> str:
    """The form a file's links into siblings take: "mbse" or "github", or "notebook", whose cells say; "" for a file
    that holds none."""
    suffix = Path(rel).suffix
    if suffix == ".ipynb":
        return "notebook"
    if skill(rel):
        return "mbse"
    return {".md": "github"}.get(suffix, "mbse" if suffix in SOURCES else "")


def masked(text: str) -> list[tuple[int, int]]:
    """The spans of markdown `text` that are code: fenced blocks and code spans."""
    spans = [m.span() for m in FENCE.finditer(text)]
    rest = [m.span() for m in SPAN.finditer(text) if not any(a <= m.start() < b for a, b in spans)]
    return spans + rest


def python_comments(text: str) -> list[tuple[int, int]]:
    """The spans of Python `text` that are comments or docstrings (a string that is a statement of its own)."""
    starts = [0]
    for row in text.splitlines(keepends=True):
        starts.append(starts[-1] + len(row))
    offset = lambda at: starts[at[0] - 1] + at[1]  # noqa: E731
    spans, previous = [], tokenize.NEWLINE
    try:
        for token in tokenize.generate_tokens(io.StringIO(text).readline):
            if token.type == tokenize.COMMENT or (
                    token.type == tokenize.STRING and previous in (tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT)):
                spans.append((offset(token.start), offset(token.end)))
            if token.type not in (tokenize.COMMENT, tokenize.NL):
                previous = token.type
    except (tokenize.TokenError, SyntaxError):
        return [m.span() for m in re.finditer(r"#[^\n]*", text)]  # a notebook's magics, say
    return spans


def script_comments(text: str) -> list[tuple[int, int]]:
    """The spans of TypeScript or JavaScript `text` that are comments, skipping its strings (not its regex literals)."""
    spans, i, n = [], 0, len(text)
    while i < n:
        if text.startswith("//", i) or text.startswith("/*", i):
            end = text.find("\n" if text[i + 1] == "/" else "*/", i + 2)
            end = n if end < 0 else end + (0 if text[i + 1] == "/" else 2)
            spans.append((i, end))
            i = end
        elif text[i] in "'\"`":
            j = i + 1
            while j < n and text[j] != text[i] and (text[i] == "`" or text[j] != "\n"):
                j += 2 if text[j] == "\\" else 1
            i = j + 1
        else:
            i += 1
    return spans


def shell_comments(text: str) -> list[tuple[int, int]]:
    return [m.span() for m in re.finditer(r"(?:^|(?<=\s))#[^\n]*", text, re.M)]


def readable(text: str, syntax: str) -> list[tuple[int, int]]:
    """The spans of `text` whose links are links: in markdown, all but its code; in source, its comments."""
    if syntax == "markdown":
        bounds = sorted(masked(text))
        spans, start = [], 0
        for a, b in bounds:
            spans.append((start, a))
            start = max(start, b)
        return spans + [(start, len(text))]
    comments = {"python": python_comments, "script": script_comments, "shell": shell_comments}.get(syntax)
    return comments(text) if comments else [(0, len(text))]


SYNTAX = {".md": "markdown", ".py": "python", ".ts": "script", ".tsx": "script", ".js": "script", ".sh": "shell"}


def sibling(target: str, here: str, own: str) -> tuple[str, str, str] | None:
    """The sibling, path and anchor a link's target designates, or None for a link that stays in the repository, goes
    to another site, or is not a path. `here` is the linking file's directory, relative to the repository's root."""
    for pattern in (GITHUB, SHORT):
        m = pattern.fullmatch(target)
        if m:
            return None if m[1] == own else (m[1], m[2], m[3] or "")
    if SCHEME.match(target) or target.startswith(("#", "/")):
        return None
    path, _, anchor = target.partition("#")
    parts = posixpath.normpath(posixpath.join(here, path)).split("/")
    if parts[0] != ".." or len(parts) < 3:
        return None
    if parts[1] == "..":
        return ("..", "/".join(parts[1:]), f"#{anchor}" if anchor else "")
    if parts[1] == own:
        return None
    return parts[1], "/".join(parts[2:]), f"#{anchor}" if anchor else ""


def written(repo: str, path: str, anchor: str, kind: str) -> str:
    if kind == "github":
        return f"https://github.com/{OWNER}/{repo}/blob/main/{path}{anchor}"
    return f"mbse:{repo}/{path}{anchor}"


def slug(heading: str) -> str:
    """A heading's anchor, as GitHub writes it."""
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    return re.sub(r"[^\w\- ]", "", text).replace(" ", "-")


def anchors(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    """The anchors a markdown file or notebook defines: its headings' slugs, and its `id` and `name` attributes."""
    if path not in cache:
        if path.suffix == ".ipynb":
            cells = json.loads(path.read_text())["cells"]
            texts = ["".join(c["source"]) for c in cells if c["cell_type"] == "markdown"]
        else:
            texts = [path.read_text()]
        found, seen = set(), {}
        for text in texts:
            found |= set(ID_ATTR.findall(text))
            code = masked(text)
            for m in HEADING.finditer(text):
                if any(a <= m.start() < b for a, b in code):
                    continue
                base = slug(m[1])
                n = seen.get(base, 0)
                seen[base] = n + 1
                found.add(base if n == 0 else f"{base}-{n}")
        cache[path] = found
    return cache[path]


def unresolved(root: Path, repo: str, path: str, anchor: str, cache: dict[Path, set[str]]) -> str | None:
    """Why a link into a sibling does not resolve beside the repository, or None if it does."""
    if repo == "..":
        return "(leaves the folder of sibling checkouts)"
    target = root.resolve().parent / repo / unquote(path)
    if not target.exists():
        return f"(no file {repo}/{path})"
    name = unquote(anchor[1:])
    if name and target.is_file() and target.suffix in {".md", ".ipynb"}:
        if name not in anchors(target, cache) and name.lower() not in anchors(target, cache):
            return f"(no anchor {anchor} in {repo}/{path})"
    return None


def rewrite(text: str, here: str, own: str, kind: str, syntax: str) -> tuple[str, list[tuple[int, str, str, tuple]]]:
    """`text` with its links into siblings in the form `kind`, and each such link: its offset, its target as written,
    the form it should take ("" when it has that form already), and the sibling, path and anchor it designates."""
    spans = readable(text, syntax)
    links = []

    def link(m: re.Match) -> str:
        if not any(a <= m.start() < b for a, b in spans):
            return m[0]
        found = sibling(m[1], here, own)
        if found is None:
            return m[0]
        if found[0] == "..":
            links.append((m.start(), m[1], "", found))
            return m[0]
        right = written(*found, kind)
        links.append((m.start(), m[1], "" if right == m[1] else right, found))
        return m[0] if right == m[1] else f"]({right}{m[2]})"

    return LINK.sub(link, text), links


def line(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def files(root: Path) -> list[str]:
    """The repository's tracked files that can hold a link into a sibling, relative to its root."""
    listed = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, text=True)
    names = (listed.stdout.split("\0") if listed.returncode == 0
             else [p.relative_to(root).as_posix() for p in root.rglob("*")])
    return [name for name in names if name and form(name) and (root / name).is_file()
            and not (root / name).is_symlink() and (root / name).resolve() not in FIXTURES]


def update(roots: list[Path], check: bool = False) -> tuple[list[Finding], list[Finding], list[Path]]:
    """Rewrites the links into siblings in the repositories; returns the links in the wrong form, those that do not
    resolve (found only with check), and the files that were, or with check would be, changed."""
    wrong, missing, changed, cache = [], [], [], {}
    for root in roots:
        own = root.resolve().name
        for name in files(root):
            path, here, kind = root / name, posixpath.dirname(name), form(name)
            raw = path.read_text()
            if kind == "notebook":
                notebook = json.loads(raw)
                language = notebook.get("metadata", {}).get("kernelspec", {}).get("language", "python")
                texts = []
                for i, cell in enumerate(notebook["cells"]):
                    if cell["cell_type"] not in ("markdown", "code"):
                        continue
                    source = cell["source"]
                    text = "".join(source)
                    is_md = cell["cell_type"] == "markdown"
                    kind = "github" if is_md and not skill(name) else "mbse"
                    syntax = "markdown" if is_md else "python" if language == "python" else "script"
                    new, links = rewrite(text, here, own, kind, syntax)
                    texts.append((f"cell {i}, line ", text, links))
                    if new != text:
                        cell["source"] = new if isinstance(source, str) else new.splitlines(keepends=True)
                new_raw = raw
                if any(right for _, _, links in texts for _, _, right, _ in links):
                    new_raw = json.dumps(notebook, indent=1, sort_keys=True, ensure_ascii=False)
                    new_raw += "\n" if raw.endswith("\n") else ""
            else:
                new_raw, links = rewrite(raw, here, own, kind, SYNTAX.get(path.suffix, ""))
                texts = [("", raw, links)]
            for prefix, text, links in texts:
                for offset, target, right, found in links:
                    where = f"{prefix}{line(text, offset)}"
                    if right:
                        wrong.append(Finding(path, where, target, f"-> {right}"))
                    if check:
                        why = unresolved(root, *found, cache)
                        if why:
                            missing.append(Finding(path, where, target, why))
            if new_raw != raw:
                changed.append(path)
                if not check:
                    path.write_text(new_raw)
    return wrong, missing, changed


def main(argv: list[str]) -> int:
    check = "--check" in argv
    roots = [Path(a) for a in argv if a != "--check"] or [Path.cwd()]
    wrong, missing, changed = update(roots, check=check)
    for finding in wrong:
        print(f"{'wrong form' if check else 'rewrote'}: {finding}")
    for finding in missing:
        print(f"unresolved: {finding}")
    plural = lambda n, word: f"{n} {word}{'s' if n != 1 else ''}"  # noqa: E731
    if check:
        print(f"{plural(len(wrong), 'link')} in the wrong form, in {plural(len(changed), 'file')}; "
              f"{plural(len(missing), 'link')} unresolved")
        return 1 if wrong or missing else 0
    print(f"{plural(len(wrong), 'link')} rewritten, in {plural(len(changed), 'file')}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
