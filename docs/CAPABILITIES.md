<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](README.md) · [Vocabulary →](VOCABULARY.md)

# Capabilities

Quantifiable objectives that hold across the project and implement features. A feature's capabilities enumerate, in
full, how it is met; a capability has no parts or levels below it. **Current** says where each is met and where that
was checked, so that build status lives here rather than in each repository's design document.

## Index

- **C-001** · proposed · Every repository's Python and TypeScript implementations pass the same conformance corpora
  (CONF suites): the same names, errors and messages, and byte-identical JSON. *Implements*: none yet (see Features,
  open items).
  - **Current**: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- **C-007** · proposed · Every repository's tests and tutorials hold the same cases in both languages. *Implements*:
  as C-001.
  - **Current**: as C-001.
- **C-008** · proposed · Every repository's tests cover 100% of both implementations. *Implements*: as C-001.
  - **Current**: as C-001.
- **C-009** · proposed · Each deliberate difference between a repository's implementations is listed in its
  `docs/EQUIVALENCE.md`. *Implements*: as C-001.
  - **Current**: as C-001.
- **C-002** · proposed · Schemas are open in content: nothing is mandatory but by constraint (checked as C-006 says).
  *Implements* F-005, F-006.
  - **Current**: met in mbse-schemas 0.10.0; its dependents to assess.
- **C-010** · proposed · Properties a schema does not declare are preserved when data is read, and written back as
  read. *Implements* F-005. *Applies* P-002.
  - **Current**: proposed in mbse-schemas' `docs/OPEN_WORLD.md` (its part 2), not built.
- **C-011** · proposed · A module declares subtypes and extension properties of a schema it does not own.
  *Implements* F-005, F-006.
  - **Current**: proposed in `docs/OPEN_WORLD.md` (its part 1), not built.
- **C-012** · proposed · A schema evolves so that data written for it stays valid. *Implements* F-006.
  - **Current**: proposed in `docs/OPEN_WORLD.md` (its part 3), not built.
- **C-013** · proposed · Each language's program model has complete kinds, built and printed. *Implements* F-008.
  - **Current** (main, v0.3.28): met for Python, TypeScript and Ccpp; Verilog and SystemVerilog to assess.
- **C-003** · adopted · Source code transpilers read source as written, semantically incorrect code included, through
  a pinned parser whose gaps are corrected on the tree. *Implements* F-008. *Applies* P-002.
  - **Current** (main, v0.3.28): met for Python, TypeScript and Ccpp through tree-sitter, a practical choice at the
    time; Verilog and SystemVerilog read through slang, to assess.
- **C-021** · proposed · Each language family's source is read by its reference front end rather than tree-sitter:
  Python by CPython's `ast`, TypeScript and JavaScript by the TypeScript compiler API, C and C++ by Clang, Verilog
  and SystemVerilog by slang. *Implements* F-008.
  - **Current** (main, v0.3.28): met for Verilog and SystemVerilog (slang); not for Python, TypeScript and Ccpp,
    which read through tree-sitter.
- **C-014** · proposed · Program models read source as faithfully as the language's reference front end reads correct
  code: their trees are checked against that front end's wherever it reads the code. *Implements* F-008.
  - **Current** (main, v0.3.28): met for Python and TypeScript on the conformance sources (PYPRS-01 against CPython's
    `ast`, TSPRS-01 against typescript-estree); not for Ccpp, which has no oracle; Verilog and SystemVerilog to
    assess.
- **C-015** · proposed · Program models read every construct of the language's standards, and locate an error where
  the text goes wrong. *Implements* F-008.
  - **Current**: met for no language: the tree-sitter grammars lag the standards (C++23 and C++26, Python 3.13 and
    later), and their errors are located where recovery starts.
- **C-004** · proposed · Code is generated from models for each language family, for types, expressions and
  patterns. *Implements* F-001, F-002, F-008. P-015 depends on it: typed bindings are how code refers to model
  elements by reference.
  - **Current**: met for Python types; not for Python expressions and patterns, nor the C and C++, TypeScript and
    Verilog families.
- **C-016** · proposed · Generated code is read back into the model, inverting generation. *Implements* F-001, F-002.
  - **Current**: as C-004.
- **C-017** · proposed · Every ambiguity in generation is a parameter of the step that resolves it. *Implements*
  F-001, F-002.
  - **Current**: partly met for Python types (`frozen` and `slots` are parameters; other choices are fixed); not met
    elsewhere.
- **C-005** · proposed · Interaction models layer functional behavior. *Implements* F-009.
  - **Current**: not met.
- **C-018** · proposed · Interaction models cover each kind of participant (system, hardware, firmware, software,
  device, user, community, cloud resource, agent) and the interfaces between them. *Implements* F-010 to F-016.
  - **Current**: no kind covered.
- **C-006** · proposed · Constraints are checked, three-valued. *Implements* F-005, F-006.
  - **Current**: met; where it was checked is to record.
- **C-019** · proposed · Data is generated from constraints: sampled, and pseudorandom. *Implements* F-005, F-006.
  - **Current**: met; where it was checked is to record.
- **C-020** · proposed · Constraints are resolved in any direction. *Implements* F-005, F-006.
  - **Current**: to assess.

## Open items

- **Which parser for each language** (low priority). Tolerance and spec-awareness differ by language, as the editors'
  language services show. TypeScript's compiler, which tsserver is, parses any text to a full tree, type errors never
  affecting it. Python's semantic errors never affect a parse; CPython's `ast` fails only on syntax errors, without
  recovery, while Pyright's parser (Pylance's; MIT, written in TypeScript) and Ruff's recover from them. slang parses
  tolerantly and elaborates separately. C++ is the exception: its grammar depends on whether a name is a type, so a
  parser must resolve names, and Clang drops what it cannot resolve; EDG (Microsoft's C/C++ IntelliSense) copes but
  is commercial, so for Ccpp C-021 conflicts with C-003. mbse-programs' `docs/PROGRAMS.md` keeps Ccpp's front end
  under its Open questions until this is decided.
- The capabilities above are drafted from each repository's status sections; confirm them, then remove those sections
  and cite the capabilities instead. Schema capabilities land in mbse-schemas first, then in its dependents, each
  pinning the new release.
- C-017 counts parameters, not coverage of ambiguities: it needs a measure, such as decisions fixed for every schema
  that should be parameters (mbse-codegen-python's `docs/BRIDGES.md` lists them).

---

<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](README.md) · [Vocabulary →](VOCABULARY.md)
