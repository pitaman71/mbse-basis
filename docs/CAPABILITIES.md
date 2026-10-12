<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](README.md) · [Vocabulary →](VOCABULARY.md)

# Capabilities

Quantifiable objectives that hold across the project and implement features, often in a progression of increasing
qualitative value. Each entry lists its levels, L0 being none; **current** says which is met, so that build status
lives here rather than in each repository's design document.

## Index

- **C-001** · proposed · Equivalent implementations: every repository's Python and TypeScript implementations have the
  same names, errors and messages, and write byte-identical JSON. *Implements*: none yet (see Features, open items).
  - L1 conformance corpora compared (CONF suites); L2 tests and tutorials in the same cases in both languages; L3 100%
    coverage in both; L4 each deliberate difference listed in `docs/EQUIVALENCE.md`.
  - **Current**: L4 in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- **C-002** · proposed · Open-world schemas: a module extends a schema it does not own, and data written for the
  original stays valid. *Implements* F-005, F-006.
  - L1 open in content (nothing mandatory but by constraint; three-valued checking); L2 undeclared properties
    preserved (P-002); L3 independent extension: subtypes and extension properties declared by a module that does not
    own the schema; L4 evolution that keeps data valid. Each level lands in mbse-schemas first, then in its
    dependents, each pinning the new release.
  - **Current**: L1 landed (mbse-schemas 0.10.0). L2 to L4 proposed in mbse-schemas' `docs/OPEN_WORLD.md` (its parts
    2, 1 and 3), not built.
- **C-003** · adopted · Program models read source as written, semantically incorrect or syntactically incomplete,
  as faithfully as the language's reference front end reads correct code. *Implements* F-008. *Applies* P-002.
  - Per language: L1 complete kinds, built and printed; L2 read by a pinned parser, semantically incorrect code
    included, its gaps corrected on the tree; L3 its trees checked against the reference front end's wherever that
    front end reads the code; L4 every construct of the language's standards read, with errors located where the text
    goes wrong.
  - **Current** (main, v0.3.28): Python, TypeScript and Ccpp read through tree-sitter, a practical choice at the time;
    Python and TypeScript L3 on the conformance sources (PYPRS-01 against CPython's `ast`, TSPRS-01 against
    typescript-estree), Ccpp L2 with no oracle; Verilog and SystemVerilog read through slang, level to assess. None at
    L4: the tree-sitter grammars lag the standards (C++23 and C++26, Python 3.13 and later), and their errors are
    located where recovery starts.
- **C-004** · proposed · Code generation by language family, invertible and step by step. *Implements* F-001, F-002,
  F-008. P-015 depends on it: typed bindings are how code refers to model elements by reference.
  - Per family and per part (types, expressions, patterns): L1 generated; L2 read back, inverting generation; L3 every
    ambiguity a step's parameter.
  - **Current**: Python types L2, partly L3 (`frozen` and `slots` are parameters; other choices are fixed). Python
    expressions and patterns, and the C and C++, TypeScript and Verilog families, L0.
- **C-005** · proposed · Interaction models. *Implements* F-009 to F-016.
  - L1 layered functional behavior; then one level per participant kind covered (system, hardware, firmware,
    software, device, user, community, cloud resource, agent), and their interfaces.
  - **Current**: L0.
- **C-006** · proposed · Constraints used every way: checked, resolved and generated from. *Implements* F-005, F-006.
  - L1 checked, three-valued; L2 generated from (sampling and pseudorandom data); L3 resolved in any direction.
  - **Current**: L2; resolution is to assess.

## Open items

- **Which parser for each language** (low priority). Tolerance and spec-awareness differ by language, as the editors'
  language services show. TypeScript's compiler, which tsserver is, parses any text to a full tree, type errors never
  affecting it. Python's semantic errors never affect a parse; CPython's `ast` fails only on syntax errors, without
  recovery, while Pyright's parser (Pylance's; MIT, written in TypeScript) and Ruff's recover from them. slang parses
  tolerantly and elaborates separately. C++ is the exception: its grammar depends on whether a name is a type, so a
  parser must resolve names, and Clang drops what it cannot resolve; EDG (Microsoft's C/C++ IntelliSense) copes but
  is commercial, so tree-sitter stays defensible for Ccpp. mbse-programs' `docs/PROGRAMS.md` records the move to
  reference front ends as Resolved, and for Ccpp "fragments and code without its headers are out of scope"; both
  belong under its Open questions until this is decided.
- The levels above are drafted from each repository's status sections; confirm them, then remove those sections and
  cite the capability instead.
- C-004 L3 counts parameters, not coverage of ambiguities: it needs a measure, such as decisions fixed for every schema
  that should be parameters (mbse-codegen-python's `docs/BRIDGES.md` lists them).

---

<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](README.md) · [Vocabulary →](VOCABULARY.md)
