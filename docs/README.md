<!-- nav -->
[Home](README.md) · [Features →](FEATURES.md)

# The mbse basis

The mbse repositories keep promoting the same ideas into local special cases, each repository deciding again what
another already decided. This basis states those ideas once, as a small ontology every repository cites by ID, so that
a local document records only how it applies them and what differs. Each idea has one source of truth, its detailed
statement in one place; every other document links to it with a concise bridge statement rather than restating it.

Read this file, then the index of each kind below. Each index is one entry per item, kept short enough to read whole.

## Where documents live

| Location | Scope | May reference |
|---|---|---|
| `mbse-basis/docs/<NAME>.md` | the project: what every repository shares | definitions on the web |
| `mbse-<repo>/docs/<NAME>.md` | one repository | the project's documents, and definitions on the web |

`<NAME>` is a long name in capitals (`CAPABILITIES.md`, `OBJECT_IDENTITY.md`).

## The design spec

The design spec organizes the project's architecture and plans in four tiers. Each tier relates to the one above it
many-to-many, not as a tree.

| Tier | Prefix | What it is | Index |
|---|---|---|---|
| 1. Quality | `QUA-` | How a user instinctively assesses the product's value, against a rubric that seems natural to them: neither what the product does nor how | to scaffold |
| 2. Feature | `FEA-` | A cohesive, focused category of user-valued utility: what problems the product solves for its user, not how. Its capabilities may or may not progress linearly within it. Confers qualities | [FEATURES.md](FEATURES.md) |
| 3. Capability | `CAP-` | An increment of utility within a feature: how, in a coming release, the product solves a problem, circumscribing the part of the problem space it can solve. Implements features | [CAPABILITIES.md](CAPABILITIES.md) |
| 4. Task | | A unit of work toward a capability | not enumerated |

**Every feature is external or internal.** An external feature serves a user persona; an internal feature serves an
engineering persona. Today's features are generally external, and today's tech debt generally internal.

**A feature's proven space should only grow.** Each capability that lands is an increment of it: each release, the
part of a feature's problem space its capabilities are proven to solve should be at least what it was.

**Tasks are not enumerated.** Their tracking is latent in git history; there is no need to surface them yet.

Two kinds of item sit outside the tiers:

| Kind | Prefix | What it is | Index |
|---|---|---|---|
| Principle | `PRI-` | A design principle reapplied across repositories, interfaces and implementations: a durable decision that delivers quality as a repeatable engineering pattern | [PRINCIPLES.md](PRINCIPLES.md) |
| Vocabulary | `VOC-` | A borrowed, clarified or novel concept, and the one term that names it across code, documents, tutorials and skills, with a focus on the dimensions, domains, seams and gradients of the project's own engineering space | [VOCABULARY.md](VOCABULARY.md) |

**Conventions are not a kind of their own.** A convention, how the work is done (equivalent implementations, notebook
tests, coverage, navigation; today the shared invariants in each repository's `AGENTS.md`), is either a principle that
serves a quality an engineering persona values, or a rule of one of the doc spec's shelves. A repository's `AGENTS.md`
cites them rather than stating them. A principle governs the product when a user could notice it broken, and the work
when only a contributor could.

## The doc spec

The doc spec organizes what users and agents read and run, on four shelves.

| Shelf | What it is | Status |
|---|---|---|
| Tutorials | Executable documents, mostly Jupyter notebooks, that together are the user guide for humans and agents. Each doubles as a unit test | Fairly comprehensive across repositories, features and capabilities; keep their breadth, platform equivalence and level of detail, and add or refine one as each capability lands |
| Skills | Skill documents that together are a user guide optimized for agents | As tutorials |
| Tests | Executable, platform-specific programs that unit-test mbse components | As tutorials |
| References | Between vocabulary and tutorials: for an advanced user or agent with a specific goal in mind, organized around such goals, cross-linked with vocabulary, tutorials and capabilities | Not yet built, and not needed yet |

## Other documents

**Proposals.** A proposal is a document proposing a cohesive group of changes, typically spanning capabilities and
sometimes features or qualities. A proposal almost always adds capabilities, sometimes adds features, occasionally
refines a feature (a new ID, with links showing what it replaces), and very occasionally adds a quality. A
repository's design documents are proposals. A completed proposal is drained: its content moves into the items it
adds or refines, and into the shelves, and what remains cites them.

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

A feature is an objective, not a description of current behavior: an adopted feature may not be met yet. How far it is
met is what its capabilities' current status says.

## Rules for writing items

- **IDs are permanent.** Never renumber or reuse one; supersede instead. Moving an item into the `XYZ-123` scheme keeps
  its old ID as an alias.
- **One entry per item in its index**: ID, status, one sentence, relations, and for a feature, external or internal.
  Rationale, examples and history go in an optional detail file, `features/FEA-005.md`, `principles/PRI-002.md`,
  linked from the entry and read only when needed.
- **Cite, never restate.** A repository's document writes "applies PRI-007: ..." with only its local delta. When a
  local decision turns out to be a general one, promote it here and replace the local text with the citation.
- **Edit, never append.** A statement that changes is edited, or its item superseded; contradicting statements never
  stand side by side.
- **Items may overlap.** The qualities and features are a specification, each a constraint on the project (V-002), and
  their conjunction is the objective. Overlapping items are not duplicates; never merge them to remove the overlap.
- **Keep each index short, about 10 KB**: a guideline, which the user ranks well below keeping the documents
  organized.

---

<!-- nav -->
[Home](README.md) · [Features →](FEATURES.md)
