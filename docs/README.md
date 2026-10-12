<!-- nav -->
[Home](README.md) · [Features →](FEATURES.md)

# The mbse basis

The mbse repositories keep promoting the same ideas into local special cases, each repository deciding again what
another already decided. This basis states those ideas once, as a small ontology every repository cites by ID, so that
a local design document records only how it applies them and what differs.

Read this file, then the index of each kind below. Each index is one entry per item, kept short enough to read whole.

## Kinds of item

| Kind | Prefix | What it is | Index |
|---|---|---|---|
| Feature | `F-` | A qualitative objective that holds across the project and stays stable through its lifecycle: why | [FEATURES.md](FEATURES.md) |
| Principle | `P-` | A design principle reapplied locally across a class of related situations: how, in general | [PRINCIPLES.md](PRINCIPLES.md) |
| Capability | `C-` | A quantifiable objective that implements features; a feature's capabilities enumerate, in full, how it is met | [CAPABILITIES.md](CAPABILITIES.md) |
| Vocabulary | `V-` | A term every repository uses alike, with what it never means | [VOCABULARY.md](VOCABULARY.md) |

One kind is planned but not yet scaffolded: **conventions**, how the work is done (equivalent implementations, notebook
tests, coverage, navigation; today the shared invariants in each repository's `AGENTS.md`). Its prefix is still to
choose; `C-` is taken.

## Relations between items

| Relation | From | To | Meaning |
|---|---|---|---|
| *serves* | principle | feature | Applying the principle advances the feature |
| *implements* | capability | feature | The capability is part of how the feature is met |
| *applies* | a repository's decision | principle | The decision is the principle in one situation, plus a stated local delta |
| *relates to* | any item | any item | A tension or overlap worth reading together |

Every principle serves at least one feature, and every capability implements at least one. A principle or capability
that serves nothing is a sign of a missing feature, and is listed under that index's open items rather than left
dangling.

## Status

Every item has a status:

- **proposed**: drafted, not yet agreed.
- **adopted**: agreed; repositories cite it and follow it.
- **superseded by X**: replaced. The item keeps its ID and its entry, so that citations still resolve, and says what
  replaced it.

A feature is an objective, not a description of current behavior: an adopted feature may not be met yet. How far it is
met is what its capabilities' current status says.

## Rules for writing items

- **IDs are permanent.** Never renumber or reuse one; supersede instead.
- **One entry per item in its index**: ID, status, one sentence, relations. Rationale, examples and history go in an
  optional detail file, `features/F-005.md`, `principles/P-002.md`, linked from the entry and read only when needed.
- **Cite, never restate.** A repository's design document writes "applies P-007: ..." with only its local delta. When a
  local decision turns out to be a general one, promote it here and replace the local text with the citation.
- **Edit, never append.** A statement that changes is edited, or its item superseded; contradicting statements never
  stand side by side.
- **Features may overlap.** The features are a specification, each a constraint on the project (V-002), and their
  conjunction is the objective. Overlapping features are not duplicates; never merge them to remove the overlap.
- **Keep each index under 10 KB.**

---

<!-- nav -->
[Home](README.md) · [Features →](FEATURES.md)
