<!-- nav -->
[← mbse-basis](../README.md)

# Tools for every mbse repository

Two tools live here, and every mbse repository runs them from here rather than keeping a copy:

- [`polyrepo.py`](polyrepo.py) keeps the repositories, which are separate git repositories checked out side by side,
  working as one project.
- [`update_doc_links.py`](update_doc_links.py) writes the navigation links at the top and bottom of each document.

Both use only the standard library, so they run before anything is installed. Run them from inside the repository
they are for; the examples below assume its root, with mbse-basis beside it. Their tests are
`python3 -m unittest discover -s scripts`, run from mbse-basis.

## polyrepo.py

### Why it exists

The mbse repositories depend on each other: mbse-expressions on mbse-schemas, mbse-codegen-python on four others. They
remain in a temporary state of co-development during which a change in one should be seen at once by the others,
without publishing a package. Each repository is therefore checked out beside the others, in one parent folder, and
installs them by path:

```text
reboot2026/
  mbse-basis/            these tools, and what every repository shares
  mbse-schemas/
  mbse-expressions/      installs ../../mbse-schemas/python3 and file:../../mbse-schemas/typescript5
  mbse-patterns/
  mbse-programs/
  mbse-codegen-python/
```

Those siblings are the repositories a repository names in its `siblings.json`, with the version and the commit it was
last tested against:

```json
{
  "mbse-basis": {"repository": "git@github.com:pitaman71/mbse-basis.git", "commit": "84f47de..."},
  "mbse-schemas": {"repository": "git@github.com:pitaman71/mbse-schemas.git", "version": "0.10.0", "commit": "47c25d6..."}
}
```

The pin does what a submodule's recorded commit does, without the submodule: the checkouts stay ordinary repositories
that you edit, commit and branch as usual, side by side instead of nested. The lock files (`uv.lock`,
`package-lock.json`) record siblings by path, with no hash, so the pinned commit is what makes a checkout reproducible.
A repository has a Python package, a TypeScript one, or both, which carry its version alike. The version is the
compatibility contract: a sibling is compatible when it has the same major version (below 1.0, the same minor) and is no
older. Where both this repository and the sibling have Python packages, `python3/pyproject.toml` requires exactly that
range; a TypeScript `file:` dependency has no range, so `check` alone holds it to the contract. A release is the tag
`v<version>`. A sibling without packages, such as mbse-basis, has no version: it is pinned by commit alone and never
tagged.

### In git terms

| Command | Roughly | What it adds |
|---|---|---|
| `clone` | `git clone` each missing sibling, then `git checkout --detach <pin>` | skips siblings already there |
| `check [--strict]` | `git status` across the siblings | compatible versions, matching `pyproject.toml` ranges where there are Python packages; `--strict` requires each sibling clean at its pin |
| `pin` | `git add` of a submodule's new commit | records each sibling's version and `HEAD` in `siblings.json`, and the range in `pyproject.toml` if there is one; refuses a sibling with uncommitted changes |
| `workspace DIR --branch B [--edit S ...]` | `git worktree add` in every repository at once | worktrees side by side in `DIR`, so the relative paths hold; this repository and the `--edit` siblings on branch `B`, the others detached |
| `land DIR [--push]` | `git merge --ff-only` in each repository, then `git worktree remove` and `git branch -d` | dependencies first; tags each new version; refuses, before changing anything, anything that would not fast-forward cleanly |
| `push` | `git push` in each repository | dependencies first, with any new version tag; refuses, before pushing anything, a branch behind its upstream or a pin the sibling's branch does not contain |
| `remove DIR [--force]` | `git worktree remove` for a workspace | keeps the branches |
| `help` | | prints the full reference |

Each command acts for the repository it is run in and the siblings in its `siblings.json`. Run `push` or `workspace`
from the repository that depends on everything the change touches (mbse-codegen-python depends on all the others).

### Getting started

```sh
git clone git@github.com:pitaman71/mbse-basis.git
git clone git@github.com:pitaman71/mbse-patterns.git
cd mbse-patterns
python3 ../mbse-basis/scripts/polyrepo.py clone    # its siblings, beside it, at their pinned commits
python3 ../mbse-basis/scripts/polyrepo.py check
```

A cloned sibling is in detached HEAD at its pin. To change it, put it on a branch first, as with any detached checkout:
`git -C ../mbse-schemas switch main`.

### Everyday work, one person at a time

Work in the checkouts as in any repository: edit, test, commit. `check` reports a sibling that has moved past its pin;
that is expected while developing, and is not an error.

A change that spans repositories is committed in each, dependencies first. Then each dependent records what it was
tested against, and everything is pushed in order:

```sh
# changed mbse-schemas and mbse-expressions; both commits made
cd mbse-expressions
python3 ../mbse-basis/scripts/polyrepo.py pin       # siblings.json now names mbse-schemas' new commit
git commit -am "Pin mbse-schemas"
python3 ../mbse-basis/scripts/polyrepo.py push      # mbse-basis, mbse-schemas, then mbse-expressions
```

`push` checks everything first: if any repository is behind its upstream, or pins a commit its sibling's branch does
not have, nothing is pushed. Running it again is safe.

### Parallel work: workspaces

Two people or agents working at once in the same checkouts would see each other's half-finished changes, and git's own
worktree of one repository does not help: its siblings would not be beside it, so the relative paths break. A workspace
is a set of worktrees, one per repository, side by side:

```sh
cd mbse-patterns
python3 ../mbse-basis/scripts/polyrepo.py workspace ../worktrees/limits --branch limits --edit mbse-schemas
cd ../worktrees/limits/mbse-patterns
(cd python3 && uv sync --all-extras) && (cd typescript5 && npm install)
```

Here mbse-patterns and mbse-schemas are on the new branch `limits`, and the other siblings are detached at the commits
their checkouts are on. Work, commit and `pin` inside the workspace. When done, from the main checkout:

```sh
python3 ../mbse-basis/scripts/polyrepo.py land ../worktrees/limits --push
```

`land` fast-forwards each checkout's branch to its workspace branch, dependencies first. Where the version changed, it
tags `v<version>`. It then removes the worktrees and deletes the merged branches, and with `--push` pushes as `push`
does. It refuses, before changing anything, when a worktree has uncommitted changes, a checkout is not clean on a
branch, a branch would not fast-forward (merge the target branch into it, retest and re-pin), or a dependent pins an
edited sibling at anything other than that sibling's branch. To abandon a workspace instead:
`polyrepo.py remove ../worktrees/limits` (the branches are kept).

### Releases

A release is a version bump, made alike in `python3/pyproject.toml` and `typescript5/package.json` (whichever exist),
and the tag `v<version>`. `land` creates the tag; a bump committed directly on a branch is not tagged until you tag it
(`git tag -a v0.11.0 -m "Release 0.11.0"`), and `push` then pushes the tag with the branch. Below 1.0, a change that
dependents must adapt to bumps the minor version.

## update_doc_links.py

Each repository's human-facing documents form one reading order, like a book:

1. the README;
2. MBSE.md;
3. each language's tutorial and its notebooks;
4. the design documents;
5. the conformance corpus;
6. each package's README and test plan.

The tool writes a `previous · Home · next` line at the top and bottom of each, linking it to its neighbours. It leaves
agent-facing files (AGENTS.md, CLAUDE.md, skills) and test notebooks alone. Each line is marked by a hidden
`<!-- nav -->` comment, so running it again replaces the lines rather than adding more.

Run it after adding, renaming or retitling a document:

```sh
cd mbse-patterns
python3 ../mbse-basis/scripts/update_doc_links.py           # this repository
python3 ../mbse-basis/scripts/update_doc_links.py ../mbse-schemas ../mbse-programs   # or the ones named
```

Link text is each document's title, never a path. A document without a `# ` title is an error.

---

<!-- nav -->
[← mbse-basis](../README.md)
