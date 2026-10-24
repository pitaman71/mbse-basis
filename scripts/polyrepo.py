"""The mbse repositories each one depends on, which live beside it as sibling checkouts.

This module lives in mbse-basis, its one copy. Run it from anywhere in a repository's checkout, which is the repository
it runs for ("this repository" below):

    python3 ../mbse-basis/scripts/polyrepo.py COMMAND

`siblings.json`, at this repository's root, names each sibling with the version and the commit this repository was
tested with:

    {"mbse-schemas": {"repository": "git@github.com:pitaman71/mbse-schemas.git", "version": "0.1.0",
                      "commit": "bbd2c1c..."}}

Development uses the siblings as they are, so that a change in one is seen at once by the others: Python installs
`../../<sibling>/python3` (`tool.uv.sources`) and TypeScript `file:../../<sibling>/typescript5`, which their lock files
record by path, without a hash. The commit makes a checkout reproducible: `clone` checks it out, and `check --strict`
requires it. A repository has a Python package (`python3/pyproject.toml`), a TypeScript one (`typescript5/package.json`)
or both, and both carry its version alike. The version is the contract: a sibling is compatible when it has the same
major version (the same minor below 1.0) and is no older. Where this repository has a Python package and the sibling
has one too, `python3/pyproject.toml` requires exactly that range, so uv refuses an incompatible sibling too; a
TypeScript `file:` dependency carries no range, so only `check` holds TypeScript to the contract. A release of a sibling
is the tag `v<version>`. A sibling without packages, such as mbse-basis, has no version: it is pinned by commit alone,
and never tagged.

    check [--strict]          siblings present, compatible, and required alike by pyproject.toml where both have
                              Python packages; --strict also requires each clean at its pinned commit
    clone                     clones each missing sibling at its pinned commit (fresh clones, CI)
    pin                       records each sibling's version and commit (here, and the version's range in
                              pyproject.toml, if there is one); a sibling with uncommitted changes cannot be pinned
    workspace DIR [--branch NAME] [--edit SIBLING ...]
                              a workspace for parallel work: git worktrees of this repository and of its siblings,
                              side by side in DIR, so that the relative paths to the siblings hold; this repository on
                              the new branch NAME (detached without it), the siblings named by --edit on NAME too, and
                              the others detached at their checkouts' commits
    land DIR [--push]         lands a workspace's change: each worktree on a branch is fast-forwarded into its
                              repository's checkout, siblings before their dependents; each new version is tagged
                              v<version>; then the workspace and its merged branches are removed. It refuses, before
                              changing anything, a worktree with changes, a checkout that is not clean on a branch, a
                              branch that does not fast-forward it, or a pin of an edited sibling that is not that
                              sibling's branch. --push then pushes every repository in the workspace, as push does
    push                      pushes this repository and its siblings, siblings first: each one's branch, if it is
                              ahead of the remote, and its version's tag, if the remote lacks it. It refuses, before
                              pushing anything, a checkout not on a branch, a branch behind its upstream, or a pin of a
                              commit that the sibling's branch does not contain. Rerunning it is safe
    remove DIR [--force]      removes a workspace's worktrees, refusing one with uncommitted changes unless --force;
                              branches are kept

Standard library only, so that it runs before anything is installed.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path()  # the dependent this runs for, and its files; set by main
CONFIG = ROOT / "siblings.json"
PYPROJECT = ROOT / "python3" / "pyproject.toml"
COMMAND = "python3 ../mbse-basis/scripts/polyrepo.py"


def parse(version: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if match is None:
        raise SystemExit(f"not a version: {version!r}")
    major, minor, patch = (int(g) for g in match.groups())
    return major, minor, patch


def bound(version: str) -> str:
    """The first version that is no longer compatible with `version`."""
    major, minor, _ = parse(version)
    return f"{major + 1}.0" if major > 0 else f"0.{minor + 1}"


def requirement(version: str) -> str:
    return f">={version},<{bound(version)}"


def compatible(pinned: str, actual: str) -> bool:
    p, a = parse(pinned), parse(actual)
    same = p[0] == a[0] and (p[0] > 0 or p[1] == a[1])
    return same and a >= p


def has_python(sibling: Path) -> bool:
    return (sibling / "python3" / "pyproject.toml").is_file()


def version_of(sibling: Path) -> str | None:
    """The sibling's version, which its Python and TypeScript packages, whichever it has, agree on; None without."""
    versions = []
    if has_python(sibling):
        python = re.search(r'^version = "([^"]+)"', (sibling / "python3" / "pyproject.toml").read_text(), re.M)
        versions.append(python and python.group(1))
    if (sibling / "typescript5" / "package.json").is_file():
        versions.append(json.loads((sibling / "typescript5" / "package.json").read_text()).get("version"))
    if None in versions or len(set(versions)) > 1:
        raise SystemExit(f"{sibling.name}: its packages must each have the version, alike; they have {versions}")
    return versions[0] if versions else None


def git(sibling: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(sibling), *args], capture_output=True, text=True).stdout.strip()


def required(name: str) -> list[str]:
    """The version ranges pyproject.toml requires of `name`, with or without extras."""
    return re.findall(rf'"{re.escape(name)}(?:\[[^\]]*\])?([^"]*)"', PYPROJECT.read_text())


def check(strict: bool) -> int:
    failures = 0
    for name, entry in json.loads(CONFIG.read_text()).items():
        sibling, pinned = ROOT.parent / name, entry.get("version")
        if not sibling.is_dir():
            print(f"{name}: missing at {sibling}; run {COMMAND} clone")
            failures += 1
            continue
        actual = version_of(sibling)
        ranges = required(name) if PYPROJECT.is_file() and has_python(sibling) else None
        if (pinned is None) != (actual is None):
            print(f"{name}: pinned {'without' if pinned is None else 'with'} a version, but "
                  f"{'has one' if actual else 'has none'}; run pin")
            failures += 1
            continue
        if pinned is not None and not compatible(pinned, actual):
            print(f"{name}: {actual} is not compatible with the pinned {pinned}")
            failures += 1
        if pinned is not None and ranges is not None and (not ranges or any(r != requirement(pinned) for r in ranges)):
            print(f"{name}: pyproject.toml must require {name}{requirement(pinned)}, not {ranges}; run pin")
            failures += 1
        commit = entry.get("commit")
        at_pin = commit is not None and git(sibling, "rev-parse", "HEAD") == commit
        clean = not git(sibling, "status", "--porcelain")
        if not (at_pin and clean):
            where = "has changes" if at_pin else "has no pinned commit; run pin" if commit is None else (
                f"is not at its pinned commit {commit[:7]}")
            if strict:
                print(f"{name}: {where}; reproducing a checkout needs each sibling clean at its pinned commit")
                failures += 1
            else:
                print(f"{name}: {actual or 'unversioned'}, {where} (developing against the sibling as it is)")
        else:
            print(f"{name}: {actual or 'unversioned'}, at its pinned commit {commit[:7]}")
    return 1 if failures else 0


def clone() -> int:
    for name, entry in json.loads(CONFIG.read_text()).items():
        sibling = ROOT.parent / name
        if sibling.is_dir():
            print(f"{name}: present")
            continue
        subprocess.run(["git", "clone", "--quiet", entry["repository"], str(sibling)], check=True)
        target = entry.get("commit") or f"v{entry['version']}"
        subprocess.run(["git", "-C", str(sibling), "checkout", "--quiet", "--detach", target], check=True)
        print(f"{name}: cloned at {target[:7] if entry.get('commit') else target}")
    return 0


def pin() -> int:
    config = json.loads(CONFIG.read_text())
    text = PYPROJECT.read_text() if PYPROJECT.is_file() else None
    dirty = [name for name in config if git(ROOT.parent / name, "status", "--porcelain")]
    if dirty:
        raise SystemExit(f"uncommitted changes in {dirty}: a pin is a commit, so commit them first")
    for name, entry in config.items():
        sibling = ROOT.parent / name
        version = version_of(sibling)
        entry.pop("version", None)
        if version is not None:
            entry["version"] = version
        if version is not None and text is not None and has_python(sibling):
            text = re.sub(rf'"({re.escape(name)}(?:\[[^\]]*\])?)[^"]*"', rf'"\g<1>{requirement(version)}"', text)
        entry["commit"] = git(sibling, "rev-parse", "HEAD")
        print(f"{name}: pinned {version or 'by commit'} at {entry['commit'][:7]}")
        if not git(sibling, "branch", "--remotes", "--contains", entry["commit"]):
            print(f"{name}: {entry['commit'][:7]} is not pushed yet; clone needs it pushed")
    CONFIG.write_text(json.dumps(config, indent=2) + "\n")
    if text is not None:
        PYPROJECT.write_text(text)
    return 0


def worktree(source: Path, target: Path, branch: str | None) -> None:
    """A worktree of `source` at `target`: on `branch` (made from the checkout's commit if new), or detached."""
    if git(source, "status", "--porcelain", "--untracked-files=no"):
        print(f"{source.name}: has uncommitted changes, which the worktree does not get")
    if branch is None:
        args = ["--detach", str(target), "HEAD"]
    elif git(source, "rev-parse", "--verify", "--quiet", f"refs/heads/{branch}"):
        args = [str(target), branch]
    else:
        args = ["-b", branch, str(target), "HEAD"]
    subprocess.run(["git", "-C", str(source), "worktree", "add", "--quiet", *args], check=True)
    where = f"on {branch}" if branch else f"detached at {git(target, 'rev-parse', '--short', 'HEAD')}"
    print(f"{target}: {where}")


def workspace(directory: Path, branch: str | None, edit: list[str]) -> int:
    siblings = json.loads(CONFIG.read_text())
    unknown = [name for name in edit if name not in siblings]
    if unknown or (edit and branch is None):
        raise SystemExit(f"--edit takes siblings ({', '.join(siblings)}) and needs --branch; got {edit}")
    missing = [name for name in siblings if not (ROOT.parent / name).is_dir()]
    if missing:
        raise SystemExit(f"missing siblings {missing}; run {COMMAND} clone")
    for name in [ROOT.name, *siblings]:
        if (directory / name).exists():
            raise SystemExit(f"{directory / name} already exists")
    directory.mkdir(parents=True, exist_ok=True)
    worktree(ROOT, directory / ROOT.name, branch)
    for name in siblings:
        worktree(ROOT.parent / name, directory / name, branch if name in edit else None)
    installs = [f"({cmd})" for package, cmd in (("python3/pyproject.toml", "cd python3 && uv sync --all-extras"),
                                                 ("typescript5/package.json", "cd typescript5 && npm install"))
                if (ROOT / package).is_file()]
    print(f"next: cd {directory / ROOT.name}" + (f", then install: {' and '.join(installs)}" if installs else ""))
    return 0


def remove(directory: Path, force: bool) -> int:
    trees = sorted(p for p in directory.iterdir() if (p / ".git").is_file()) if directory.is_dir() else []
    if not trees:
        raise SystemExit(f"{directory}: no worktrees here")
    dirty = [t.name for t in trees if git(t, "status", "--porcelain")]
    if dirty and not force:
        raise SystemExit(f"uncommitted changes in {dirty}; commit them, or pass --force to discard them")
    for tree in trees:
        common = Path(git(tree, "rev-parse", "--path-format=absolute", "--git-common-dir"))
        subprocess.run(["git", "-C", str(common.parent), "worktree", "remove", *(["--force"] if force else []),
                        str(tree)], check=True)
        print(f"{tree}: removed")
    if not any(directory.iterdir()):
        directory.rmdir()
    return 0


def checkout_of(tree: Path) -> Path:
    """The repository checkout a worktree belongs to."""
    return Path(git(tree, "rev-parse", "--path-format=absolute", "--git-common-dir")).parent


def pins(tree: Path) -> dict[str, dict[str, str]]:
    config = tree / "siblings.json"
    return json.loads(config.read_text()) if config.is_file() else {}


def dependency_order(trees: dict[str, Path]) -> list[str]:
    """The workspace's repositories, each after the siblings it pins (by name; ties by name)."""
    order: list[str] = []
    visiting: set[str] = set()

    def visit(name: str) -> None:
        if name in order:
            return
        if name in visiting:
            raise SystemExit(f"{name}: its siblings pin it in a cycle")
        visiting.add(name)
        for sibling in sorted(pins(trees[name])):
            if sibling in trees:
                visit(sibling)
        visiting.discard(name)
        order.append(name)

    for name in sorted(trees):
        visit(name)
    return order


def land(directory: Path, push: bool) -> int:
    trees = {p.name: p for p in sorted(directory.iterdir()) if (p / ".git").is_file()} if directory.is_dir() else {}
    if not trees:
        raise SystemExit(f"{directory}: no worktrees here")
    branches = {name: git(tree, "symbolic-ref", "--quiet", "--short", "HEAD") for name, tree in trees.items()}
    landing = [name for name in dependency_order(trees) if branches[name]]
    checkouts = {name: checkout_of(tree) for name, tree in trees.items()}
    problems = [f"{name}: has uncommitted changes" for name, tree in trees.items()
                if git(tree, "status", "--porcelain")]
    if not landing:
        problems.append("no worktree is on a branch: nothing to land")
    targets: dict[str, tuple[Path, str]] = {}
    for name in landing:
        tree, checkout = trees[name], checkout_of(trees[name])
        target = git(checkout, "symbolic-ref", "--quiet", "--short", "HEAD")
        targets[name] = checkout, target
        if not target:
            problems.append(f"{name}: the checkout {checkout} is not on a branch")
            continue
        if git(checkout, "status", "--porcelain", "--untracked-files=no"):
            problems.append(f"{name}: the checkout {checkout} has uncommitted changes")
        head = git(tree, "rev-parse", "HEAD")
        for base in (target, git(checkout, "rev-parse", "--abbrev-ref", "--quiet", f"{target}@{{upstream}}")):
            ancestor = ["git", "-C", str(checkout), "merge-base", "--is-ancestor", base, head]
            if base and subprocess.run(ancestor).returncode:
                problems.append(f"{name}: {branches[name]} does not fast-forward {base}; merge {base} into it, retest"
                                " and re-pin")
        for sibling, entry in pins(tree).items():
            if sibling in landing and entry.get("commit") != git(trees[sibling], "rev-parse", "HEAD"):
                problems.append(f"{name}: pins {sibling} at {str(entry.get('commit'))[:7]}, not at its branch "
                                f"{branches[sibling]}; run pin and commit")
    if problems:
        raise SystemExit("nothing landed:\n" + "\n".join(f"  {p}" for p in problems))
    for name in landing:
        checkout, target = targets[name]
        subprocess.run(["git", "-C", str(checkout), "merge", "--quiet", "--ff-only", branches[name]], check=True)
        version, at = version_of(trees[name]), git(checkout, "rev-parse", "--short", "HEAD")
        tag = f"v{version}"
        if version is None:
            print(f"{name}: {target} at {at}; unversioned, so no release")
        elif git(checkout, "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"):
            print(f"{name}: {target} at {at}; {tag} exists, so no release")
        else:
            subprocess.run(["git", "-C", str(checkout), "tag", "--annotate", tag, "--message", f"Release {tag[1:]}"],
                           check=True)
            print(f"{name}: {target} at {at}, tagged {tag}")
    remove(directory, False)
    for name in landing:  # merged, so deleting them loses nothing
        subprocess.run(["git", "-C", str(targets[name][0]), "branch", "--quiet", "--delete", branches[name]],
                       check=True)
        print(f"{name}: deleted the branch {branches[name]}")
    if not push:
        print(f"next: {COMMAND} push")
        return 0
    return publish(checkouts)  # the detached siblings too, whose commits the landed pins may name


def publish(checkouts: dict[str, Path]) -> int:
    """Pushes each checkout's branch and its version's tag, siblings first, after checking that every push can land."""
    order = dependency_order(checkouts)
    problems, plans = [], []
    for name in order:
        checkout = checkouts[name]
        branch = git(checkout, "symbolic-ref", "--quiet", "--short", "HEAD")
        if not branch:
            problems.append(f"{name}: the checkout {checkout} is not on a branch")
            continue
        upstream = git(checkout, "rev-parse", "--abbrev-ref", "--quiet", f"{branch}@{{upstream}}")
        behind = upstream and git(checkout, "rev-list", "--count", f"{branch}..{upstream}") != "0"
        if behind:
            problems.append(f"{name}: {branch} is behind {upstream}; pull, retest and re-pin")
        for sibling, entry in pins(checkout).items():
            commit = entry.get("commit")
            if sibling not in checkouts:
                continue
            contains = ["git", "-C", str(checkouts[sibling]), "merge-base", "--is-ancestor", str(commit), "HEAD"]
            if commit is None or subprocess.run(contains, capture_output=True).returncode:
                problems.append(f"{name}: pins {sibling} at {str(commit)[:7]}, which {sibling}'s branch does not "
                                "contain; run pin and commit")
        ahead = not upstream or git(checkout, "rev-list", "--count", f"{upstream}..{branch}") != "0"
        version = version_of(checkout)
        tag = f"v{version}"
        tagged = version is not None and git(checkout, "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}")
        released = git(checkout, "ls-remote", "--tags", "origin", f"refs/tags/{tag}")
        plans.append((name, checkout, [branch] if ahead else [], [tag] if tagged and not released else []))
    if problems:
        raise SystemExit("nothing pushed:\n" + "\n".join(f"  {p}" for p in problems))
    for name, checkout, branch, tag in plans:  # siblings first, so that what a dependent pins is there before it
        if not branch + tag:
            print(f"{name}: up to date")
            continue
        subprocess.run(["git", "-C", str(checkout), "push", "--quiet", *(["--set-upstream"] if branch else []),
                        "origin", *branch, *tag], check=True)
        print(f"{name}: pushed {' '.join(branch + tag)}")
    return 0


def push() -> int:
    return publish({**{name: ROOT.parent / name for name in json.loads(CONFIG.read_text())}, ROOT.name: ROOT})


def option(argv: list[str], name: str) -> list[str]:
    """The values that follow `name` on the command line, up to the next option."""
    args = argv[1:]
    if name not in args:
        return []
    values = []
    for arg in args[args.index(name) + 1:]:
        if arg.startswith("--"):
            break
        values.append(arg)
    return values


def main(root: Path, argv: list[str]) -> int:
    """Runs the command `argv` (without the program's name) for the dependent at `root`."""
    global ROOT, CONFIG, PYPROJECT
    ROOT, CONFIG, PYPROJECT = root, root / "siblings.json", root / "python3" / "pyproject.toml"
    command = argv[0] if argv else "check"
    if command == "check":
        return check("--strict" in argv[1:])
    if command in ("clone", "pin", "push"):
        return {"clone": clone, "pin": pin, "push": push}[command]()
    if command in ("workspace", "remove", "land") and len(argv) > 1 and not argv[1].startswith("--"):
        directory = Path(argv[1]).resolve()
        if command == "remove":
            return remove(directory, "--force" in argv[2:])
        if command == "land":
            return land(directory, "--push" in argv[2:])
        branch = option(argv, "--branch")
        return workspace(directory, branch[0] if branch else None, option(argv, "--edit"))
    raise SystemExit(__doc__)


def root_of(directory: Path) -> Path:
    """The checkout, or worktree, that `directory` is in."""
    top = git(directory, "rev-parse", "--show-toplevel")
    if not top:
        raise SystemExit(f"{directory} is not in a git checkout; run this from the repository it is for")
    return Path(top)


if __name__ == "__main__":
    sys.exit(main(root_of(Path.cwd()), sys.argv[1:]))
