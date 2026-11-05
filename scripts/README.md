<!-- nav -->
[← mbse-basis](../README.md)

# Tools for every mbse repository

Five tools live here, and every mbse repository runs them from here rather than keeping a copy:

- `polyrepo.py` keeps the repositories, which are separate git repositories checked out side by side,
  working as one project, and scaffolds a new one from the templates in `templates/repo/`.
- `update_doc_links.py` writes the navigation links at the top and bottom of each document.
- `update_item_titles.py` labels every link to an mbse-basis item with the item's ID and
  title.
- `update_link_forms.py` writes every link into another repository in the form its file calls
  for.
- `update_doc_titles.py` labels every link to a document with the document's title, never
  its path.

All five use only the standard library, so they run before anything is installed. Run them from inside the repository
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
| `new DIR --package AREA[.NAME] [--npm NAME]` | `git init` of a new repository, its files staged | run from mbse-basis: the starting set, from the templates, beside mbse-basis; refuses a `DIR` that exists |
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

### A new repository

A new mbse repository starts in the conventions rather than being reorganized into them later (the basis'
[PRI-041: a new repository starts in the conventions](../docs/PRINCIPLES.md#PRI-041)). Run from mbse-basis:

```sh
cd mbse-basis
python3 scripts/polyrepo.py new ../mbse-example --package Example     # mbse.Example and @mbse/example
python3 scripts/polyrepo.py new ../mbse-rest --package Services.Rest --npm @mbse/rest
```

It makes the directory, which must not exist, beside mbse-basis, and fills the templates in `templates/repo/`. Each is
named for the file it makes, its path included, with `.tmpl` added, so that no tool here reads a template as a
document or a source file. Names are filled in by string replacement of `{{REPO}}`, `{{PACKAGE}}` (`Services.Rest`),
`{{PACKAGE_PATH}}` (`Services/Rest`), `{{NPM}}` and `{{BASIS_COMMIT}}`; a placeholder it does not know stops it. The
starting set:

| Files | What they start as |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | what the repository is, to fill; the start-here table; the reading list, the hidden-memory rule and the `mbse:` resolution rule, word for word as every repository has them; the commands; `CLAUDE.md` is `@AGENTS.md` |
| `README.md`, `MBSE.md` | the README opening with why, to fill; `MBSE.md` pointing to mbse-basis', as mbse-diagrams has it |
| `siblings.json` | mbse-basis alone, pinned at its commit; a sibling the package uses is added, then pinned with `pin` |
| `python3/` | `pyproject.toml` for uv, `mbse/<Area>[/<Name>]/__init__.py`, `conftest.py`, `tests/` (PKG and SKL notebooks, the test plan) and `tutorials/README.md`, shaped as mbse-diagrams' |
| `typescript5/` | `package.json`, `tsconfig.json`, `.c8rc.json`, `deno.json`, `src/index.ts`, `tests/` (the same notebooks, `run-notebooks.ts`, `support.ts`, the test plan) and `tutorials/README.md` |
| `skills/<repo>/SKILL.md`, `skills/sync.sh` | the skill's one source, with a practice to fill that links PKG-01 in both languages and an opt-out on each section that teaches no how; `sync.sh` copies it into both packages, which the scaffold runs |
| `docs/EQUIVALENCE.md` | coverage, deliberate differences (none yet) and "Cases in one language only" (none yet), which SKL-03 reads |

Each passage a person writes is marked `TO FILL`. Then it writes the navigation lines with `update_doc_links.py`, runs
`git init` and stages every file, without committing, and prints the next steps: fill each `TO FILL`, install and run
both suites, add the siblings the package uses, run the link checks, and commit and push. The new repository passes
`update_link_forms.py`, `update_item_titles.py` and `update_doc_titles.py --check`, and both suites, as it is.

The templates are starting points, filled in once: the new repository owns its files from then on, and they are not
copies kept in sync with the templates, so no guidance is written twice (the basis'
[PRI-016: guidance written once](../docs/PRINCIPLES.md#PRI-016)). A template that a change to the conventions makes stale is updated here, for
the repositories still to come; `test_scaffold.py` fails when one no longer passes the link checks.

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

## update_item_titles.py

A link to an mbse-basis item is labeled with the item's ID and title, `[CAP-013: an in-memory store journaled to
DynamoDB](…)`, wherever it is: in a document or in a source comment, in any repository (the basis'
[The mbse basis](../docs/README.md), "A link is a link"). The title is written once, in the head of the item's
index entry (`**CAP-013: an in-memory store journaled to DynamoDB**`), and this tool copies it into every label and
into the heading of the item's detail file.

It relabels a link only when its label starts with an item's ID and its target resolves to that item, its anchor in an
index or its detail file, so a link that merely mentions an ID is left alone. The target may be written in any of the
three forms of a link (`update_link_forms.py`, below): a relative path, a GitHub URL into mbse-basis or the shorthand
`mbse:mbse-basis/...`. It does not turn a bare ID into a link:
where and how to cite is a writer's call. It reads only the files git tracks, so `git add` a new file before running it.

Run it after retitling an item, and check with `--check`, which writes nothing and exits 1 if any label is out of date:

```sh
cd mbse-rest
python3 ../mbse-basis/scripts/update_item_titles.py --check    # this repository: list what is out of date
python3 ../mbse-basis/scripts/update_item_titles.py ../mbse-react ../mbse-dynamodb   # relabel the ones named
```

## update_link_forms.py

A link that stays inside its repository is a relative path. A link into another repository takes the form its file
calls for (the basis' [The mbse basis](../docs/README.md), "A link is a link"):

| Where the link is | Its form |
|---|---|
| a markdown file, or a notebook's markdown cell | `https://github.com/pitaman71/<repo>/blob/main/<path>[#anchor]` |
| a skill (any file under `skills/` or a `skill/` directory), a source comment (`.py`, `.ts`, `.tsx`, `.js`, `.sh`), or a notebook's code cell | `mbse:<repo>/<path>[#anchor]`, resolved by the rule in every `AGENTS.md` |

The tool reads each file git tracks and rewrites each link into a sibling, `](../<repo>/...)` once normalized from the
file's directory, to its file's form; a GitHub URL or shorthand in the other form is rewritten too. It leaves alone
links inside the repository, URLs to other sites, and links in markdown's fenced code blocks and code spans, which are
examples; in a source file, it reads only comments and docstrings. In a notebook it edits only cell sources, and
rewrites the notebook only if one changed.

`--check` writes nothing. It lists the links in the wrong form, and every link into a sibling, in any form, whose file
is missing from the sibling's checkout beside the repository or whose anchor (a heading's slug, or an `id`) is not in
that file, and exits 1 if there are any:

```sh
cd mbse-rest
python3 ../mbse-basis/scripts/update_link_forms.py --check    # this repository: list what is wrong
python3 ../mbse-basis/scripts/update_link_forms.py ../mbse-react ../mbse-dynamodb   # rewrite the ones named
```

## update_doc_titles.py

A link's label is legible: an item's ID and title, or a document's title or a phrase naming it, never a path (the
basis' [The mbse basis](../docs/README.md), "A link is a link"). The tool finds each link labeled by a path or file
name, such as `[capabilities/README.md](README.md#CAP-108)` or ``[`MBSE.md`](MBSE.md)``, and when its target is a
document (a markdown file or a notebook, here or in a sibling, in any of the three forms of a link), replaces the label
with the document's title: its first `# ` heading, or a notebook's first in its markdown cells, without trailing
punctuation. The anchor is kept, so the first example becomes `[Capabilities](README.md#CAP-108)`. A link labeled by
an item's ID is left to `update_item_titles.py`. It reads only the markdown files and notebooks git tracks, edits only
a notebook's markdown cells, keeping the notebook's JSON format, and leaves alone fenced code blocks, code spans and
links to the placeholder `…`.

A path label it cannot fix needs a human: one to a file that is not a document (documents don't link source files),
to a file that does not exist, to a document without a title, or to another site. `--check` writes nothing, lists
every path label left by kind, and exits 1 if there are any:

```sh
cd mbse-rest
python3 ../mbse-basis/scripts/update_doc_titles.py --check    # this repository: list the path labels
python3 ../mbse-basis/scripts/update_doc_titles.py ../mbse-react ../mbse-dynamodb   # relabel the ones named
```

---

<!-- nav -->
[← mbse-basis](../README.md)
