<!-- nav -->
[← Qualities](QUALITIES.md) · [Home](../README.md) · [Vocabulary →](VOCABULARY.md)

# The mbse basis

The mbse repositories keep promoting the same ideas into local special cases, each repository deciding again what
another already decided. This basis states those ideas once, as a small ontology every repository cites by ID, so that
a local document records only how it applies them and what differs. Each idea has one source of truth, its detailed
statement in one place; every other document links to it, introduced by bridge language that tells the reader enough
to keep reading without following the link (Rules for writing items, below).

Read this file, then the index of each kind below. Each index is one entry per item, kept short enough to read whole.

## Where documents live

| Location | Scope | May reference |
|---|---|---|
| `mbse-basis/docs/<NAME>.md` | the project: what every repository shares | definitions on the web |
| `mbse-<repo>/docs/<NAME>.md` | one repository | the project's documents, and definitions on the web |

`<NAME>` is a long name in capitals (`PRINCIPLES.md`, `EQUIVALENCE.md`).

## The design spec

The design spec organizes the project's architecture and plans in four tiers. Each tier relates to the one above it
many-to-many, not as a tree.

| Tier | Prefix | What it is | Index |
|---|---|---|---|
| 1. Quality | `QUA-` | How a persona, human or agent, instinctively assesses the product's value, against a rubric that seems natural to them: neither what the product does nor how | [Qualities](QUALITIES.md) |
| 2. Feature | `FEA-` | A cohesive, focused category of utility a persona values: what problems the product solves for that persona, not how. Its capabilities may or may not progress linearly within it. Confers qualities | [Features](features/README.md) |
| 3. Capability | `CAP-` | An increment of utility within a feature: how, in a coming release, the product solves a problem, circumscribing the part of the problem space it can solve. Implements features | [Capabilities](capabilities/README.md) |
| 4. Task | | A unit of work toward a capability | not enumerated |

**Every feature is external or internal.** An external feature serves a user persona; an internal feature serves an
engineering persona. Today's features are generally external, and today's tech debt generally internal.

**A feature's proven space should only grow.** Each capability that lands is an increment of it: each release, the
part of a feature's problem space its capabilities are proven to solve should be at least what it was.

**Scope is enumerated by capabilities and contained by features.** A capability is one increment, met or not, planned for
one release: it may have tasks, but no "met for this, not yet for that". Scope still to build, or found while
building, is a further capability, each its own increment, implementing the feature that contains it. A feature grows
by gaining capabilities; a capability never grows, and addressing the same capability in more than one release is
unplanned churn. Its **Current** says only whether it is met and where that was checked, or
that it is blocked or to assess.

**Tasks are not enumerated.** Their tracking is latent in git history; there is no need to surface them yet.

Three kinds of item sit outside the tiers:

| Kind | Prefix | What it is | Index |
|---|---|---|---|
| Principle | `PRI-` | A durable design or engineering decision that reinforces qualities when consistently applied across repositories, components, source code and the rest | [Principles](PRINCIPLES.md) |
| Vocabulary | `VOC-` | A borrowed, clarified or novel concept, and the one term that names it across code, documents, tutorials and skills, with a focus on the dimensions, domains, seams and gradients of the project's own engineering space | [Vocabulary](VOCABULARY.md) |
| Initiative | `INI-` | An investment of effort toward an external demo or product goal, in terms of the capabilities it must complete (or has), and the one plan category for what were once proposals and priorities; its proposals are its design documents | [Initiatives](../proposals/PRIORITIES.md) |

**Conventions are not a kind of their own.** A convention, how the work is done (equivalent implementations, notebook
tests, coverage, navigation), is either a principle, which serves a quality ([QUA-010: every repository works alike](QUALITIES.md#QUA-010) where it governs
the work), or a rule for documents (Rules for every document, below). A repository's `AGENTS.md` cites them rather than
stating them. A principle governs the product when a user could notice it broken, and the work when only a
contributor could.

## The doc spec

The doc spec organizes what humans and agents read and run, on four shelves.

| Shelf | What it is | Status |
|---|---|---|
| Tutorials | Executable documents, mostly Jupyter notebooks, that together are the user guide for humans and agents. Each doubles as a unit test | Fairly comprehensive across repositories, features and capabilities; keep their breadth, platform equivalence and level of detail, and add or refine one as each capability lands |
| Skills | Skill documents that together are a user guide optimized for agents: why, when and how, mostly language-independent, linking the items for what and the notebook cases for how | Fairly comprehensive across repositories, features and capabilities; keep their breadth, platform equivalence and level of detail, and add or refine one as each capability lands |
| Tests | Executable, platform-specific programs that unit-test mbse components | Fairly comprehensive across repositories, features and capabilities; keep their breadth, platform equivalence and level of detail, and add or refine one as each capability lands |
| References | Between vocabulary and tutorials: for an advanced human or agent with a specific goal in mind, organized around such goals, cross-linked with vocabulary, tutorials and capabilities | Not yet built, and not needed yet |

**What, why and how, each in one place.** The plan, the skills and the notebooks divide the labor, as the user decided
(2026-11-03):

- Jupyter notebooks contain anchors to cells that describe *how* to do "the thing" in a language.
- Skill files describe *why*, *when*, *how* to do "the thing" in a mostly language-independent manner.
- Plan items (FEA, CAP, etc.) enumerate "the things" the product can do in a specific user situation, to solve a
  problem, define and achieve the specific goal, realize and share value.

Each layer links the next: a skill links the items for *what*, and notebook anchors for *how*. A skill's *how* links its
notebook case in each language, as `mbse:` links with `#Tnn.k` anchors:
`[T01.2: checking data](mbse:<repo>/python3/tutorials/<file>.ipynb#T01.2)`, and the same in `typescript5/`. A tutorial
step's markdown cell starts with `<a id="Tnn.k"></a>`, where `nn.k` is the case ID of its `## nn.k · title` heading; a
test notebook's case cell starts with its own case ID, `<a id="PAT-03"></a>`; twins in the two languages carry
identical anchors. Notebooks stay one per tutorial; they are not split per case. **A gap is a bug**: a *how* that a skill
teaches without a notebook case is untested, as the user put it (2026-11-03): "a gap is a bug, per the new definition
because it means the examples are untested!" Surfacing such gaps, and writing the notebook cases that close them, is a
short-term goal.

How each shelf is kept is a principle: tutorials run as tests ([PRI-034: tutorials run as tests, committed with their outputs](PRINCIPLES.md#PRI-034)), tests are notebooks ([PRI-035: tests are notebooks: one suite each, the same case IDs in the same order in both languages](PRINCIPLES.md#PRI-035)),
the same cases, and every anchor a skill links, are in both languages ([PRI-038: the same cases in both languages](PRINCIPLES.md#PRI-038)), and guidance is written once
([PRI-016: guidance written once](PRINCIPLES.md#PRI-016)). A skill holds no programs of its own: its *how* is a notebook case, which those
principles run and check ([PRI-036: every program in a skill is complete and run; fragments are tagged as fragments](PRINCIPLES.md#PRI-036), superseded).

## Rules for every document

- **Navigation.** Each human-facing document of a repository (its README, `MBSE.md`, its tutorials, its `docs/`, its
  conformance README, and each package's README and test plan) is headed and ended by a `{previous, home, next}` line,
  in the repository's reading order. `scripts/update_doc_links.py` writes those lines; run it after adding, renaming or
  retitling a document. Agent-facing files (`AGENTS.md`, `CLAUDE.md`, skills) and test notebooks have none. Link text
  is human-readable, a document's title or a phrase naming it, never a path.
- **The README opens with why.** A repository's README says, in its first sentence or paragraph, TL;DR style, why the
  repository exists, in the terms of [why the mbse repositories exist](../MBSE.md); what it is comes after. Keep that opening true as the repository
  changes.
- **What an `AGENTS.md` holds.** What the repository is; a start-here table of what to read for each task, naming the
  repository's skill by path, its one source and the copy packaged in each language, which is how an agent finds it
  (no `.claude/skills` link); its commands;
  and its own mechanics (its checks, scripts, contracts and exceptions), stated nowhere else. Every repository's
  `AGENTS.md` gives the same reading list in the same priority. Must read before any work: [the mbse basis](README.md),
  [principles](PRINCIPLES.md), [features](features/README.md) and [capabilities](capabilities/README.md). Read
  selectively, on demand: [vocabulary](VOCABULARY.md) and [qualities](QUALITIES.md). It enumerates no items within
  them, as the user decided on 2026-11-01: "AGENTS.md instructs the agents on a consistent priority of files that must
  be read. Do not enumerate specific items within the documents that must be read." and "Agents *must* read these docs
  before doing any work: mbse-basis/docs/README.md, mbse-basis/docs/PRINCIPLES.md, mbse-basis/features/README.md,
  mbse-basis/capabilities/README.md. VOCAULBARY.md, PRIORITIES.md, QUALITIES.md may be read selectively or on
  demand." It carries two rules of its own, each word for word as here, so that a repository copies them verbatim:
  "Never write to `~/.claude/projects/*/memory/` or any hidden memory: what is worth keeping goes in the repository."
  and, for the shorthand a link out of a skill or a source comment takes (Rules for writing items, "A link is a link"):
  "Resolve a link written `mbse:<repo>/<path>`, as skills and source comments write a link into another mbse
  repository, to the first of these that exists: in a polyrepo checkout, `<repo root>/../<repo>/<path>`, where
  `<repo root>` is this repository's root; for a link into the installed package's own repository, `<path>` without its language directory (`python3/`
  or `typescript5/`), under the installed package's root (Python: the `site-packages` directory that holds `mbse/`;
  npm: the package's directory), where the package ships that file; otherwise
  `https://github.com/pitaman71/<repo>/blob/main/<path>`." A repository's `CLAUDE.md` is `@AGENTS.md` and nothing more.

## Other documents

**Initiatives.** An initiative is the one plan category for what were proposals, initiatives and priorities, as the user
decided (2026-11-12): "Proposals, initiatives, and priorities are already in use but they should be merged into a single
plan category." Each is an investment of effort toward an external demo or product goal, in terms of the capabilities it
must complete, enumerated as `INI-` in [Initiatives](../proposals/PRIORITIES.md). Its design documents are its
proposals, each headed by its initiative: a proposal proposes a cohesive group of changes, typically spanning
capabilities and sometimes features or qualities. It almost always adds capabilities, sometimes adds features,
occasionally refines a feature (a new ID, with links showing what it replaces), and very occasionally adds a quality. A
repository's design documents are proposals. A completed proposal is drained: its content moves into the items it adds
or refines, and into the shelves, and what remains cites them.

**Decisions, tech debt and TODOs are not kept as logs.** Each such log is drained and removed:

- A decision becomes a principle, a capability or, rarely, a feature or quality, and at the site where it applies, a
  source comment citing the principles and capabilities it applies.
- Pure tech debt becomes a capability of an internal feature. Tech debt that confers soft or unvalidated user value
  becomes a capability of an external feature.
- A TODO becomes a capability, or a task.

## Relations between items

| Relation | From | To | Meaning |
|---|---|---|---|
| *confers* | feature | quality | Meeting the feature advances the quality |
| *implements* | capability | feature | The capability is part of how the feature is met |
| *serves* | principle | quality | Applying the principle delivers the quality |
| *applies* | a source comment, or a repository's document | principle | This is the principle in one situation, plus a stated local delta |
| *replaces* | any item | an item of its kind | The item refines the other, which is superseded by it |
| *relates to* | any item | any item | A tension or overlap worth reading together |

Every feature confers at least one quality, every capability implements at least one feature, and every principle
serves at least one quality. An item that relates to nothing above it is a sign of a missing item, and is listed under
that index's open items rather than left dangling.

## Identifiers

An ID is a prefix of three capitals and a number, `XYZ-123`, relative to the document that defines it. Every document
that defines items lists them as definitions, each with an ID, a name, a title and a description, and each with an
anchor of its own, so that a link reaches the definition itself.

Items written before this scheme keep their IDs (`F-`, `P-`, `C-`, `V-`, and the prefixes of each repository's
documents) until they move into it. Moving an item records its old ID beside its new one, so that every citation still
resolves; where two documents gave the same ID to different items, or different IDs to the same item, the move
resolves the alias.

## Status

Every item has a status:

- **proposed**: drafted, not yet agreed.
- **adopted**: agreed; repositories cite it and follow it.
- **superseded by X**: replaced. The item keeps its ID and its entry, so that citations still resolve, and says what
  replaced it.

An item is adopted only as the user decides it: an agent proposes, and records an open item rather than resolve one
silently.

A feature is an objective, not a description of current behavior: an adopted feature may not be met yet. How far it is
met is what its capabilities' current status says. A capability's **Current** is checked, never guessed: it names where
it was checked (a branch, a version, a test), or says that it is blocked or to assess.

## Detail files

An item's detail file (`features/FEA-003.md`, `capabilities/CAP-013.md`) holds what its one-sentence entry cannot. Its
navigation line's "←" link goes back to the item's own entry in its index (`[← Capabilities](README.md#CAP-013)`). It holds
these sections, each only where it has something to hold:

- **As built**: how a repository built the item, and what it fixes where the item is silent. A repository's design
  document is drained into it once what it proposes is built.
- **Design**: how an item not yet met is to be built, until it is; then what was built is its As built.
- **Blocked**: a gap in another repository that keeps the item from being met, reported rather than worked around.
- **Open questions**: what stays undecided.
- **Decided**: the user's decisions, adopted, each recorded completely as the rule, every point and condition of it,
  quoted where the wording matters, never reduced to an example of what was built.
- **Decided by an agent, for review**: where the item was silent, the simplest default consistent with it and with the
  repositories it builds on, each *proposed* until reviewed, labeled with the repository and number it was decided
  under (`mbse-rest 12`).

An agent working in any repository records a decision it takes where an item is silent in that item's detail file,
under Decided by an agent, for review, in a pull request to mbse-basis beside its own; it records an open question
there too. That is the only edit to mbse-basis such work makes. Before deciding, it checks the item's Decided sections
and cites the entry rather than describe the decision again.

## Rules for writing items

- **IDs are permanent.** Never renumber or reuse one; supersede instead. Moving an item into the `XYZ-123` scheme keeps
  its old ID as an alias.
- **One entry per item in its index**: ID, status, one sentence, relations, and for a feature, external or internal.
  Rationale, examples and history go in an optional detail file, `features/FEA-005.md`, `principles/PRI-002.md`,
  linked from the entry and read only when needed.
- **Bridge, don't duplicate.** A statement has one source of truth. Every other mention links to it, introduced by
  bridge language: just enough to tie the current text to the target that a reader can keep reading without following
  the link. Sometimes the target's name or title is enough ("applies [PRI-019: fluent builder syntax](PRINCIPLES.md#PRI-019), fluent builder syntax"). Sometimes a
  phrase is enough, tying the target to the context. Sometimes it takes a sentence or two, restating a little of the
  target. Keep it as brief as that allows. A bridge never carries the target's full detail, and never diverges from
  it: a repository's document gives a principle's gist and its local change, not the principle's full statement. When
  a local decision turns out to be a general one, promote it here and replace the local text with a bridged citation.
- **A link is a link.** A citation of an item or a document is markdown link syntax, never a bare ID or file name
  that only looks like one, in documents and in source comments alike. A link that stays inside its repository is a
  relative path. A link that leaves it takes the form its file calls for. In a markdown file, including a notebook's
  markdown cells, it is a GitHub URL, `https://github.com/pitaman71/<repo>/blob/main/<path>[#anchor]`, which resolves
  wherever the document is read. In a skill (any file under a skill directory: `skills/`, `*/skill/`) and in a source
  comment (in `.py`, `.ts`, `.tsx`, `.js` and `.sh` files, and a notebook's code cells), it is the shorthand
  `mbse:<repo>/<path>[#anchor]`, `[CAP-013: an in-memory store journaled to DynamoDB](mbse:mbse-basis/docs/capabilities/CAP-013.md)`,
  which an agent resolves by the rule every `AGENTS.md` carries (Rules for every document): the sibling checkout
  first, then the installed package's own files, then GitHub. `scripts/update_link_forms.py` writes each link that
  leaves its repository in its file's form, and with `--check` lists those in the wrong form and those whose file or
  anchor is missing. Its label is legible: an item's ID and abbreviated title (`[CAP-013: an in-memory store journaled to
  DynamoDB](…)`), and a document's title or a phrase naming it, never a path (Rules for every document). A link to an
  item reaches its own anchor, or its detail file where it has one. An item's title is written once, in the head of its
  index entry; `scripts/update_item_titles.py` copies it into every label.
- **Documents don't link source files.** Links between documents and code point the other way: a source file names,
  in a comment, the items it addresses, and a commit message names the items it advances.
- **Edit, never append.** A statement that changes is edited, or its item superseded; contradicting statements never
  stand side by side.
- **Items may overlap.** The qualities and features are a specification, each a constraint on the project ([VOC-002: constraint](VOCABULARY.md#VOC-002)), and
  their conjunction is the objective. Overlapping items are not duplicates; never merge them to remove the overlap.
- **Keep each index short, about 10 KB**: a guideline, which is ranked well below keeping the documents
  organized.

---

<!-- nav -->
[← Qualities](QUALITIES.md) · [Home](../README.md) · [Vocabulary →](VOCABULARY.md)
