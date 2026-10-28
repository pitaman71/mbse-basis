<!-- nav -->
[← Features](../features/README.md) · [Home](../README.md) · [Principles →](../PRINCIPLES.md)

# Capabilities

The third tier of the design spec: an increment of utility within a feature, how in a coming release the product
solves a problem, circumscribing the part of the problem space it can solve. A feature's capabilities enumerate, in
full, how it is met; a capability has no parts or levels below it. **Current** says where each is met and where that
was checked, so that build status lives here rather than in each repository's design document.

## Index

### Equivalent implementations

- <a id="CAP-024"></a>**CAP-024** · proposed · Every repository's Python and TypeScript implementations pass the same
  conformance corpora (CONF suites): the same names, errors and messages, and byte-identical JSON. *Implements*
  [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-030"></a>**CAP-030** · proposed · Every repository's tests and tutorials hold the same cases in both
  languages. *Implements* [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-031"></a>**CAP-031** · proposed · Every repository's tests cover 100% of both implementations. *Implements*
  [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-032"></a>**CAP-032** · proposed · Each deliberate difference between a repository's implementations is
  listed in its `docs/EQUIVALENCE.md`. *Implements* [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.

### Open-world models

- <a id="CAP-025"></a>**CAP-025** · proposed · Schemas are open in content: nothing is mandatory but by constraint
  (checked as [CAP-029: three-valued constraint checking](#CAP-029) says). *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met in mbse-schemas 0.10.0; its dependents to assess.
- <a id="CAP-033"></a>**CAP-033** · proposed · Properties a schema does not declare are preserved when data is read,
  and written back as read. *Implements*: none (see Open items). *Applies* [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002).
  - **Current**: proposed in mbse-schemas' [`docs/OPEN_WORLD.md`](../../../mbse-schemas/docs/OPEN_WORLD.md) ([its part 2](../../../mbse-schemas/docs/OPEN_WORLD.md#2--undeclared-properties)), not built.
- <a id="CAP-034"></a>**CAP-034** · proposed · A module declares subtypes and extension properties of a schema it does
  not own. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: proposed in [`docs/OPEN_WORLD.md`](../../../mbse-schemas/docs/OPEN_WORLD.md) ([its part 1](../../../mbse-schemas/docs/OPEN_WORLD.md#1--intersections-as-subtyping)), not built.
- <a id="CAP-035"></a>**CAP-035** · proposed · A schema evolves so that data written for it stays valid. *Implements*
  [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: proposed in [`docs/OPEN_WORLD.md`](../../../mbse-schemas/docs/OPEN_WORLD.md) ([its part 3](../../../mbse-schemas/docs/OPEN_WORLD.md#3--evolution-that-keeps-data-valid)), not built.
- <a id="CAP-029"></a>**CAP-029** · proposed · Constraints are checked, three-valued. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met; where it was checked is to record.
- <a id="CAP-042"></a>**CAP-042** · proposed · Data is generated from constraints: sampled, and pseudorandom.
  *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met; where it was checked is to record.
- <a id="CAP-043"></a>**CAP-043** · proposed · Constraints are resolved in any direction. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: to assess.

### Program models

- <a id="CAP-036"></a>**CAP-036** · proposed · Each language's program model has complete kinds, built and printed.
  *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met for Python, TypeScript and Ccpp; Verilog and SystemVerilog to assess.
- <a id="CAP-026"></a>**CAP-026** · adopted · Source code transpilers read source as written, semantically incorrect
  code included, through a pinned parser whose gaps are corrected on the tree. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008). *Applies* [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002).
  - **Current** (main, v0.3.28): met for Python, TypeScript and Ccpp through tree-sitter, a practical choice at the
    time; Verilog and SystemVerilog read through slang, to assess.
- <a id="CAP-044"></a>**CAP-044** · proposed · Each language family's source is read by its reference front end rather
  than tree-sitter: Python by CPython's `ast`, TypeScript and JavaScript by the TypeScript compiler API, C and C++ by
  Clang, Verilog and SystemVerilog by slang. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met for Verilog and SystemVerilog (slang); not for Python, TypeScript and Ccpp,
    which read through tree-sitter.
- <a id="CAP-037"></a>**CAP-037** · proposed · Program models read source as faithfully as the language's reference
  front end reads correct code: their trees are checked against that front end's wherever it reads the code.
  *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met for Python and TypeScript on the conformance sources (PYPRS-01 against CPython's
    `ast`, TSPRS-01 against typescript-estree); not for Ccpp, which has no oracle; Verilog and SystemVerilog to
    assess.
- <a id="CAP-038"></a>**CAP-038** · proposed · Program models read every construct of the language's standards, and
  locate an error where the text goes wrong. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: met for no language: the tree-sitter grammars lag the standards (C++23 and C++26, Python 3.13 and
    later), and their errors are located where recovery starts.

### Code generation and the model trace

- <a id="CAP-027"></a>**CAP-027** · proposed · Code is generated from models for each language family, for types,
  expressions and patterns. *Implements* [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018), [FEA-008: expressive program models](../features/README.md#FEA-008). [PRI-015: concrete references are programmatic](../PRINCIPLES.md#PRI-015) depends on it: typed bindings are how
  code refers to model elements by reference.
  - **Current**: met for Python types; not for Python expressions and patterns, nor the C and C++, TypeScript and
    Verilog families.
- <a id="CAP-039"></a>**CAP-039** · proposed · Generated code is read back into the model, inverting generation.
  *Implements* [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: as [CAP-027: code generated from models](#CAP-027)'s: met for Python types; not for Python expressions and patterns, nor the C and C++, TypeScript and
    Verilog families.
- <a id="CAP-040"></a>**CAP-040** · proposed · Every ambiguity in generation is a parameter of the step that resolves
  it. *Implements* [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: partly met for Python types (`frozen` and `slots` are parameters; other choices are fixed); not met
    elsewhere.

### Interaction models

- <a id="CAP-028"></a>**CAP-028** · proposed · Interaction models layer functional behavior. *Implements* [FEA-009: layered interaction models](../features/README.md#FEA-009).
  - **Current**: not met.
- <a id="CAP-041"></a>**CAP-041** · proposed · Interaction models cover each kind of participant (system, hardware,
  firmware, software, device, user, community, cloud resource, agent) and the interfaces between them. *Implements*
  [FEA-010: system behavior](../features/README.md#FEA-010) to [FEA-016: community behavior](../features/README.md#FEA-016).
  - **Current**: no kind covered.

### Schema-driven visualization and editing

Each capability's specification is in its own detail file, linked from the ID. **Current** for these is as the
workspace's `VISUALIZATION.md` left it; each is to assess against mbse-rest, mbse-react, mbse-dynamodb and
mbse-demo-apps.

- <a id="CAP-001"></a>**[CAP-001](CAP-001.md)** · adopted · No-code index view: services and UI
  present a useful and usable index site driven exclusively by the schema. *Implements* [FEA-001: schema-driven UI](../features/FEA-001.md).
  - **Current**: to assess.
- <a id="CAP-002"></a>**[CAP-002](CAP-002.md)** · adopted · Named schema list: an endpoint returns
  every named schema. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: returns the store's whole schema snapshot instead, while [CAP-003: schema inspector](CAP-003.md) is blocked.
- <a id="CAP-003"></a>**[CAP-003](CAP-003.md)** · adopted · Schema inspector: given a schema's name,
  the UI obtains its full detail, unnamed schemas defined inline and named ones referenced. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: blocked: mbse-schemas cannot yet write one schema object as a document.
- <a id="CAP-004"></a>**[CAP-004](CAP-004.md)** · adopted · Logical view templates: an endpoint
  returns, for every logical view kind, a mutation-query template whose symbols the UI gives each a schema or a
  reference. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-012"></a>**[CAP-012](CAP-012.md)** · adopted · Logical view endpoints: one endpoint per
  logical view kind, taking a template with its symbols given and returning a stream of frames. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-005"></a>**[CAP-005](CAP-005.md)** · adopted · Logical view as label and summary: the
  minimum-sized view of an object or a relation entry. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-006"></a>**[CAP-006](CAP-006.md)** · adopted · Logical view as chip: a medium-sized,
  abbreviated view of an object or a relation entry. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-007"></a>**[CAP-007](CAP-007.md)** · adopted · Logical view of an object as detail: every
  schema-defined property and adjacency. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-008"></a>**[CAP-008](CAP-008.md)** · adopted · Logical view of an adjacency as a list of
  chips: the immediate adjacencies of an object through one named adjacency. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-009"></a>**[CAP-009](CAP-009.md)** · adopted · Schema browser: a section per named app
  schema, with a scrollable list of object chips. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-010"></a>**[CAP-010](CAP-010.md)** · adopted · Object browser: a section per directory,
  with the chips of the objects its singleton holds. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-011"></a>**[CAP-011](CAP-011.md)** · adopted · Relation browser: a section per relation
  entry, its properties' chip aside its linked objects' chips. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-017"></a>**[CAP-017](CAP-017.md)** · adopted · Object inspector: a shared panel showing
  the detail view of whatever object a gesture picks. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: complete (mbse-react, M3; editing added by [CAP-014: properties as markdown](CAP-014.md)).
- <a id="CAP-018"></a>**[CAP-018](CAP-018.md)** · adopted · Adjacency inspector: viewing and editing an
  entry and its outbound object, extant or proposed. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-019"></a>**[CAP-019](CAP-019.md)** · adopted · Adjacencies at the end of a detail, each
  entry previewed as one chip. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-020"></a>**[CAP-020](CAP-020.md)** · adopted · Provenance display: who created an object,
  and when it was created and last modified. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-021"></a>**[CAP-021](CAP-021.md)** · adopted · Adjacency lists ordered by creation where
  provenance is present. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-023"></a>**[CAP-023](CAP-023.md)** · adopted · Relation inspector: the object inspector of
  one object among its siblings, stepping to the previous or next. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-013"></a>**[CAP-013](CAP-013.md)** · adopted · An in-memory store journaled to DynamoDB,
  with occasional snapshots, replayed at startup. *Implements* [FEA-006: persistence](../features/FEA-006.md).
  - **Current**: to assess.
- <a id="CAP-014"></a>**[CAP-014](CAP-014.md)** · adopted · Object properties as markdown, viewed and
  edited in the inspector. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-022"></a>**[CAP-022](CAP-022.md)** · adopted · Boolean properties as checkboxes.
  *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-015"></a>**[CAP-015](CAP-015.md)** · adopted · Transaction provenance: services keep a
  record of each transaction that writes, as mbse-schemas' `Provenance` module defines it. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-016"></a>**[CAP-016](CAP-016.md)** · adopted · Comments, as data in an app's schema,
  shown and posted through general, schema-driven capabilities. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.

## Not yet planned

Capabilities without an ID are not in plan yet. Each planned feature's are at the end of its detail file in `../features/`: low-code
custom views ([FEA-001: schema-driven UI](../features/FEA-001.md)); detail with closures, closure as a list of chips ([FEA-003: no-code logical views](../features/FEA-003.md)); store over DynamoDB ([FEA-006: persistence](../features/FEA-006.md));
object links in markdown, shared property handling by the UI, properties as text and dates, and as financial,
scientific and engineering values ([FEA-007: property kinds](../features/FEA-007.md)). Those of unplanned features are in
[features/UNPLANNED.md](../features/UNPLANNED.md).

## Earlier IDs

| Earlier | Now | Earlier | Now | Earlier | Now |
|---|---|---|---|---|---|
| C-001 | [CAP-024: the same conformance corpora](#CAP-024) | C-008 | [CAP-031: 100% coverage of both](#CAP-031) | C-015 | [CAP-038: every construct of the standards](#CAP-038) |
| C-002 | [CAP-025: schemas open in content](#CAP-025) | C-009 | [CAP-032: deliberate differences listed](#CAP-032) | C-016 | [CAP-039: generated code read back](#CAP-039) |
| C-003 | [CAP-026: source read as written](#CAP-026) | C-010 | [CAP-033: undeclared properties preserved](#CAP-033) | C-017 | [CAP-040: every generation ambiguity a parameter](#CAP-040) |
| C-004 | [CAP-027: code generated from models](#CAP-027) | C-011 | [CAP-034: extension of schemas a module does not own](#CAP-034) | C-018 | [CAP-041: every kind of participant](#CAP-041) |
| C-005 | [CAP-028: layered interaction models](#CAP-028) | C-012 | [CAP-035: schema evolution](#CAP-035) | C-019 | [CAP-042: data generated from constraints](#CAP-042) |
| C-006 | [CAP-029: three-valued constraint checking](#CAP-029) | C-013 | [CAP-036: complete kinds](#CAP-036) | C-020 | [CAP-043: constraints resolved in any direction](#CAP-043) |
| C-007 | [CAP-030: the same cases in both languages](#CAP-030) | C-014 | [CAP-037: trees as faithful as the reference front end's](#CAP-037) | C-021 | [CAP-044: reference front ends](#CAP-044) |

[CAP-001: no-code index view](CAP-001.md) to [CAP-023: relation inspector](CAP-023.md) kept the IDs they had in the workspace's `VISUALIZATION.md`.

## Open items

- **Which parser for each language** (low priority). Tolerance and spec-awareness differ by language, as the editors'
  language services show. TypeScript's compiler, which tsserver is, parses any text to a full tree, type errors never
  affecting it. Python's semantic errors never affect a parse; CPython's `ast` fails only on syntax errors, without
  recovery, while Pyright's parser (Pylance's; MIT, written in TypeScript) and Ruff's recover from them. slang parses
  tolerantly and elaborates separately. C++ is the exception: its grammar depends on whether a name is a type, so a
  parser must resolve names, and Clang drops what it cannot resolve; EDG (Microsoft's C/C++ IntelliSense) copes but
  is commercial, so for Ccpp [CAP-044: reference front ends](#CAP-044) conflicts with [CAP-026: source read as written](#CAP-026). mbse-programs' [`docs/PROGRAMS.md`](../../../mbse-programs/docs/PROGRAMS.md) keeps Ccpp's front
  end under its Open questions until this is decided.
- The capabilities above are drafted from each repository's status sections; confirm them, then remove those sections
  and cite the capabilities instead. Schema capabilities land in mbse-schemas first, then in its dependents, each
  pinning the new release.
- [CAP-040: every generation ambiguity a parameter](#CAP-040) counts parameters, not coverage of ambiguities: it needs a measure, such as decisions fixed for every schema
  that should be parameters (mbse-codegen-python's [`docs/BRIDGES.md`](../../../mbse-codegen-python/docs/BRIDGES.md) lists them).
- **[CAP-033](#CAP-033) implements no feature.** It implemented F-005, now a quality ([QUA-002: open-world models](../QUALITIES.md#QUA-002)). Preserving undeclared data is not
  refinement ([FEA-020: refinable models](../features/README.md#FEA-020)); a feature for it is missing.
- **[CAP-015](CAP-015.md) and [CAP-016: comments](CAP-016.md) sit under [FEA-007: property kinds](../features/FEA-007.md)** (property kinds) as `VISUALIZATION.md` placed them; provenance and comments
  may be features of their own.
- **Tech debt in the visualization capabilities.** Counted objects have no reference, so they are neither recorded nor
  transmitted ([FEA-003: no-code logical views](../features/FEA-003.md)), and browsers leave them out ([CAP-010: object browser](CAP-010.md), [CAP-011: relation browser](CAP-011.md)). It is to become a capability of a feature.

---

<!-- nav -->
[← Features](../features/README.md) · [Home](../README.md) · [Principles →](../PRINCIPLES.md)
