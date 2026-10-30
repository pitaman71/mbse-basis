<!-- nav -->
[← mbse-basis](README.md) · [Principles →](docs/PRINCIPLES.md)

# Why the mbse repositories exist

The MBSE repositories are a major step towards reframing software, hardware, firmware, and cloud development through
executable specifications: closing the gap between human intent, docs, and component implementations in source
languages as diverse as TypeScript and SystemVerilog, C++ and Python. They also facilitate incremental formalization of
that intent throughout the development cycle. They support automated generation of production-level source code that is
both correct by construction and verified by tests. Every stage and every step of modeling, iterative formalization,
documentation and coding keeps humans and AI agents in the loop.

## How each repository contributes

| Repository | Its part of an executable specification |
|---|---|
| [mbse-basis](https://github.com/pitaman71/mbse-basis) | The shared ideas: features, principles, capabilities and vocabulary, stated once with permanent IDs that every other repository cites |
| [mbse-schemas](https://github.com/pitaman71/mbse-schemas) | The structure: objects, relationships whose entries carry properties, and their cardinalities, as one neutral schema that drives in-memory objects, JSON and YAML, validation, and generated bindings in each target language |
| [mbse-expressions](https://github.com/pitaman71/mbse-expressions) | The constraints: what a specification requires, written as expressions that every language checks alike and that translate into each implementation language, from Excel and MATLAB to C and SystemVerilog |
| [mbse-patterns](https://github.com/pitaman71/mbse-patterns) | Constraints over populations of data: named predicates that check implementations' data, find it, and generate realistic test data, so the specification is also the test oracle and the fixture |
| [mbse-programs](https://github.com/pitaman71/mbse-programs) | The code: target languages' complete syntax trees as data (C and C++, Python and TypeScript so far), so that generators build and rewrite real programs and print them as production source |
| [mbse-codegen-python](https://github.com/pitaman71/mbse-codegen-python) | The Python an implementation is written in: schemas rendered as dataclasses and read back, step by step with every decision recorded, so that code and specification cannot drift |

Each repository but mbse-basis has two equivalent implementations, in Python and TypeScript, that write
byte-identical JSON ([CAP-024: the same conformance corpora](docs/capabilities/README.md#CAP-024)), and an `AGENTS.md` for the AI agents that work in it. Each builds
on mbse-schemas, and lives beside the others as a sibling checkout.

## What a specification is made of

A specification ([V-001](docs/VOCABULARY.md)) is constraints (V-002) over variables (V-004), each held by a property
named `requires` on the part of a system it constrains; which parts those are is
[not decided yet](docs/capabilities/CAP-166.md#open-questions).

- **A constraint** is descriptive, not prescriptive (V-003): it bounds the space in which implementations operate
  correctly, and never says how. It binds variables, and is never executed. It is
  - **checked** (C-006), giving true, false or unknown, with a best effort to prove it true or false when its
    variables are restricted by other constraints but not determined;
  - **resolved** (C-020), in any direction: `total = sum(items)` determines `total` from `items`, and restricts
    `items` given `total`;
  - **generated from** (C-019): values chosen within its bounds.
- **Several constraints are one**: their conjunction.
- **A value is a constraint** that determines its variable (V-005), so checking an implementation adds its observed
  values to the constraints and checks the whole.
- **An expression** is how a constraint is written: a tree of terms (V-008). Its parts, such as `sum(items)`, are
  expressions, not constraints.
- **The specification is executable, nondeterministically** (V-001): each correct implementation is one choice of
  values consistent with every constraint, a program that is executed deterministically; generated test data is
  another.

---

<!-- nav -->
[← mbse-basis](README.md) · [Principles →](docs/PRINCIPLES.md)
