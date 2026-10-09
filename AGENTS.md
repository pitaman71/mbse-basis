# Guide for AI agents

mbse-basis states, once, what every mbse repository shares: features (F-), principles (P-), capabilities (C-) and
vocabulary (V-), each with a permanent ID. It holds no code. Other repositories are its siblings, checked out beside
it (`../mbse-schemas`, ...), and cite its items by ID.

## Start here

Read [docs/README.md](docs/README.md): the kinds of item, their relations, statuses and the rules for writing them.
Then read the index of whichever kind your task touches; each is short enough to read whole.

## Invariants

- **Only what spans repositories belongs here.** A decision that holds in one repository stays in that repository's
  design documents, citing the items it applies. When a local decision turns out to be general, promote it here and
  replace the local text with a citation.
- **Follow the rules in [docs/README.md](docs/README.md#rules-for-writing-items)**: IDs are permanent, one entry per
  item, cite never restate, edit never append, features may overlap, and each index stays under 10 KB.
- **A modeling construct is named, not defined.** [VOCABULARY.md](docs/VOCABULARY.md) defines terms that are not
  constructs, and lists each construct with a link to the repository that defines it.
- **Record what the user decides as the user decides it.** Adopted items are the user's; an agent proposes, and records
  open items rather than resolving them silently.
- **Current levels are checked, not guessed.** A capability's current level names where it was checked (a branch,
  a version, a test), or says it is to assess.
