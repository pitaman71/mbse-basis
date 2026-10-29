<!-- nav -->
[← Features](../features/README.md) · [Home](../README.md) · [Principles →](../PRINCIPLES.md)

# Capabilities

The third tier of the design spec: an increment of utility within a feature, how in a coming release the product
solves a problem, circumscribing the part of the problem space it can solve. A feature's capabilities enumerate, in
full, how it is met; a capability has no capabilities below it. A capability is planned for one release, and
may have tasks; what remains after its release is another capability, not the same one again ([the
basis](../README.md#the-design-spec), scope is enumerated by capabilities and contained by features). **Current** says whether each is met and where that was checked, so that build status lives here rather
than in each repository's design document.

## Index

### Equivalent implementations

- <a id="CAP-024"></a>**CAP-024: the same conformance corpora** · proposed · Every repository's Python and TypeScript implementations pass the same
  conformance corpora (CONF suites): the same names, errors and messages, and byte-identical JSON. *Implements*
  [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-030"></a>**CAP-030: the same cases in both languages** · proposed · Every repository's tests and tutorials hold the same cases in both
  languages. *Implements* [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-031"></a>**CAP-031: 100% coverage of both** · proposed · Every repository's tests cover 100% of both implementations. *Implements*
  [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.
- <a id="CAP-032"></a>**CAP-032: deliberate differences listed** · proposed · Each deliberate difference between a repository's implementations is
  listed in its `docs/EQUIVALENCE.md`. *Implements* [FEA-019: equivalent implementations](../features/README.md#FEA-019).
  - **Current**: as [CAP-024: the same conformance corpora](#CAP-024)'s: met in mbse-schemas, mbse-expressions, mbse-patterns and mbse-programs; to assess in
    mbse-codegen-python.

### Open-world models

- <a id="CAP-025"></a>**CAP-025: schemas open in content** · proposed · Schemas are open in content: nothing is mandatory but by constraint
  (checked as [CAP-029: three-valued constraint checking](#CAP-029) says). *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met in mbse-schemas 0.10.0; its dependents to assess.
- <a id="CAP-033"></a>**CAP-033: undeclared properties preserved** · proposed · Properties a schema does not declare are preserved when data is read,
  and written back as read. *Implements*: none (see Open items). *Applies* [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002).
  - **Current**: proposed in mbse-schemas' [`docs/OPEN_WORLD.md`](../../../mbse-schemas/docs/OPEN_WORLD.md) ([its part 2](../../../mbse-schemas/docs/OPEN_WORLD.md#2--undeclared-properties)), not built.
- <a id="CAP-034"></a>**CAP-034: extension of schemas a module does not own** · proposed · A module declares subtypes and extension properties of a schema it does
  not own. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: proposed in [`docs/OPEN_WORLD.md`](../../../mbse-schemas/docs/OPEN_WORLD.md) ([its part 1](../../../mbse-schemas/docs/OPEN_WORLD.md#1--intersections-as-subtyping)), not built.
- <a id="CAP-035"></a>**CAP-035: schema evolution** · proposed · A schema evolves so that data written for it stays valid. *Implements*
  [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: proposed in [`docs/OPEN_WORLD.md`](../../../mbse-schemas/docs/OPEN_WORLD.md) ([its part 3](../../../mbse-schemas/docs/OPEN_WORLD.md#3--evolution-that-keeps-data-valid)), not built.
- <a id="CAP-029"></a>**CAP-029: three-valued constraint checking** · proposed · Constraints are checked, three-valued. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met; where it was checked is to record.
- <a id="CAP-042"></a>**CAP-042: data generated from constraints** · proposed · Data is generated from constraints: sampled, and pseudorandom.
  *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: met; where it was checked is to record.
- <a id="CAP-043"></a>**CAP-043: constraints resolved in any direction** · proposed · Constraints are resolved in any direction. *Implements* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: to assess.

### Program models

- <a id="CAP-036"></a>**CAP-036: complete kinds for Python, TypeScript and C and C++** · proposed · Python's, TypeScript's and C
  and C++'s program models have complete kinds, built and printed. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-063"></a>**CAP-063: complete kinds for Verilog and SystemVerilog** · proposed · Verilog's and SystemVerilog's program models have complete kinds, built
  and printed. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: to assess.
- <a id="CAP-026"></a>**CAP-026: Python, TypeScript and C and C++ read as written** · adopted · Source code transpilers read
  Python, TypeScript and C and C++ source as written, semantically incorrect code included, through a pinned parser
  (tree-sitter, a practical choice at the time) whose gaps are corrected on the tree. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  *Applies* [PRI-002: preserve, don't lose](../PRINCIPLES.md#PRI-002).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-062"></a>**CAP-062: Verilog and SystemVerilog read as written** · proposed · Verilog and SystemVerilog source is read as written, semantically incorrect code included,
  through slang. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: to assess.
- <a id="CAP-044"></a>**CAP-044: Verilog and SystemVerilog read by slang** · proposed · Verilog and SystemVerilog source is read
  by its reference front end, slang, rather than tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met.
- <a id="CAP-066"></a>**CAP-066: Python read by CPython's ast** · proposed · Python source is read by its reference front end, CPython's `ast`, rather than
  tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: read through tree-sitter.
- <a id="CAP-067"></a>**CAP-067: TypeScript read by the TypeScript compiler API** · proposed · TypeScript and JavaScript source is read by their reference front end, the
  TypeScript compiler API, rather than tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: read through tree-sitter.
- <a id="CAP-068"></a>**CAP-068: C and C++ read by Clang** · proposed · C and C++ source is read by its reference front end, Clang, rather than tree-sitter. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: read through tree-sitter.
- <a id="CAP-037"></a>**CAP-037: Python and TypeScript trees as faithful as the reference front end's** · proposed · Python and
  TypeScript program models read source as faithfully as the language's reference front end reads correct code: their
  trees are checked against that front end's wherever it reads the code. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current** (main, v0.3.28): met on the conformance sources (PYPRS-01 against CPython's `ast`, TSPRS-01 against
    typescript-estree).
- <a id="CAP-064"></a>**CAP-064: C and C++ trees as faithful as the reference front end's** · proposed · C and C++ program models read source as faithfully as Clang reads correct
  code, their trees checked against its. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: C and C++ have no oracle yet.
- <a id="CAP-065"></a>**CAP-065: Verilog and SystemVerilog trees as faithful as the reference front end's** · proposed · Verilog and SystemVerilog program models read source as faithfully as
  slang reads correct code, their trees checked against its. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: to assess.
- <a id="CAP-038"></a>**CAP-038: every construct of the standards** · proposed · Program models read every construct of the language's standards, and
  locate an error where the text goes wrong. *Implements* [FEA-008: expressive program models](../features/README.md#FEA-008).
  - **Current**: not met: the tree-sitter grammars lag the standards (C++23 and C++26, Python 3.13 and
    later), and their errors are located where recovery starts.

### Code generation and the model trace

- <a id="CAP-027"></a>**[CAP-027: Python3 source generated from schemas](CAP-027.md)** · proposed · MBSE can generate Python3
  source code from schema models: their types, as dataclasses and type aliases. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md),
  [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  [PRI-015: concrete references are programmatic](../PRINCIPLES.md#PRI-015) depends on it: typed bindings are how code refers to model elements by reference.
  - **Current**: met (mbse-codegen-python's `Types`).
- <a id="CAP-045"></a>**CAP-045: TypeScript5 source generated from schemas** · proposed · MBSE can generate TypeScript5
  source code from schema models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-046"></a>**CAP-046: generated Python3 bound to its schemas** · proposed · Classes generated in Python3 are bound to their schemas (mbse-schemas' `Bindings`), so that they serialize,
  validate and are queried as a store's objects. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-047"></a>**CAP-047: parametric schemas as Python3 generics** · proposed · A parametric schema generates a Python3 generic: its value parameters as PEP 695 type parameters bounded by
  their types (`class Matrix[rows: int, cols: int]`), an application with `Literal` arguments. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-048"></a>**CAP-048: terms in generated Python3** · proposed · A width, an extent or an argument that is a term is written in generated Python3. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: terms are written by [CAP-051: Python3 source from expression models](#CAP-051).
- <a id="CAP-049"></a>**CAP-049: type parameters in Python3** · proposed · A schema's type parameters generate a generic Python3 class (`class Box[T]`). *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: mbse-schemas has no type parameters.
- <a id="CAP-051"></a>**CAP-051: Python3 source from expression models** · proposed · MBSE can generate Python3 source code from expression models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-052"></a>**CAP-052: Python3 source from pattern models** · proposed · MBSE can generate Python3 source code from pattern models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-053"></a>**CAP-053: C and C++ source from schema models** · proposed · MBSE can generate C and C++ source code from schema models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-054"></a>**CAP-054: Verilog and SystemVerilog source from schema models** · proposed · MBSE can generate Verilog and SystemVerilog source code from schema models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-055"></a>**CAP-055: generated TypeScript5 bound to its schemas** · proposed · Classes generated in TypeScript5 are bound to their schemas, so that they
  serialize, validate and are queried as a store's objects. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-056"></a>**CAP-056: parametric schemas as TypeScript5 generics** · proposed · A parametric schema generates a TypeScript5 generic, its parameters as type
  parameters and an application with literal type arguments. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-057"></a>**CAP-057: terms in generated TypeScript5** · proposed · A width, an extent or an argument that is a term is written in generated TypeScript5. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: terms are written by [CAP-060: TypeScript5 source from expression models](#CAP-060).
- <a id="CAP-058"></a>**CAP-058: type parameters in TypeScript5** · proposed · A schema's type parameters generate a generic TypeScript5 class (`class Box<T>`). *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: blocked: mbse-schemas has no type parameters.
- <a id="CAP-059"></a>**CAP-059: schemas round-trip through TypeScript5** · proposed · MBSE can round-trip schema models through TypeScript5 source: schemas to
  source and back give the same schemas, and source to schemas and back the same source, given the same decisions. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-060"></a>**CAP-060: TypeScript5 source from expression models** · proposed · MBSE can generate TypeScript5 source code from expression models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-061"></a>**CAP-061: TypeScript5 source from pattern models** · proposed · MBSE can generate TypeScript5 source code from pattern models. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md).
  - **Current**: not met.
- <a id="CAP-039"></a>**[CAP-039: schemas round-trip through Python3](CAP-039.md)** · proposed · MBSE can round-trip schema
  models through Python3 source: schemas to source and back give the same schemas, and source to schemas and back the
  same source, given the same decisions. *Implements* [FEA-022: code generation](../features/README.md#FEA-022), [FEA-017: AI in the loop via the model trace](../features/README.md#FEA-017), [FEA-018: humans in the loop via the model trace](../features/README.md#FEA-018).
  - **Current**: met for schemas' types (mbse-codegen-python's `Types`: the round trips are laws, tested both ways).
- <a id="CAP-040"></a>**CAP-040: every generation ambiguity a parameter** · superseded by [FEA-021: every generation ambiguity a parameter](../features/FEA-021.md) · Every
  ambiguity in generation is a parameter of the step that resolves it. It is a feature, not an increment of one.

### Wire format

- <a id="CAP-055"></a>**CAP-055: wire format shorthand (scalars)** · proposed · "in the scalar case of a `Schemas.OfAny` that represents a specific
  scalar (such as `Schemas.OfScalar` -> `Schemas.OfInt`) the wire format may omit the implied union wrapper(s) e.g.
  `1` instead of `{ "scalar": { "int": 1 } }` provided the written form unambiguously aligns with the schema (e.g.
  `scalar` -> `int`) and the reader must tolerate this optionality of representation": from `OfAny` through `OfScalar`
  to `OfInt`, up to two wrapper levels ("Yes, if you start with `OfAny` then go through `OfScalar` then `OfInt` you
  get up to 2 wrapper levels"). The unrestricted case is [CAP-057](#CAP-057). *Implements* [FEA-006: persistence](../features/README.md#FEA-006); applies
  [PRI-025: never guess the schema](../PRINCIPLES.md#PRI-025) and [PRI-026: serialization through the visitor protocol](../PRINCIPLES.md#PRI-026).
  - **Current**: not met in mbse-schemas: a restricted `OfAny` is written bare and read by the schema whose plain
    form fits, a guess, refused where several fit; no explicit wrapper is written.
- <a id="CAP-056"></a>**CAP-056: wire format shorthand (containers)** · proposed · "in the container case of a `Schemas.OfAny` that represents a
  specific container (e.g. `Schemas.OfContainer`) the wire format may omit the implied union wrapper
  `[ "dog", "cat", "mouse" ]` instead of `{ "container": [ "dog", "cat", "mouse" ] }` and the reader must tolerate this
  optionality of representation". *Implements* [FEA-006: persistence](../features/README.md#FEA-006); applies
  [PRI-025: never guess the schema](../PRINCIPLES.md#PRI-025) and [PRI-026: serialization through the visitor protocol](../PRINCIPLES.md#PRI-026).
  - **Current**: not met in mbse-schemas: a container value of an `OfAny` is tagged by its schema's name, or written
    bare where a restriction leaves one container schema.
- <a id="CAP-057"></a>**CAP-057: an unrestricted `OfAny` on the wire** · proposed · "in the unrestricted case of `Schemas.OfAny` the wire
  format is simply plain data". As the user put it, "a complex case that deserves its own CAPABILITY id and name. it
  seems to involve open world modeling that allows the wire format to be written unrestricted and read restricted
  which implies a schema change between writing and reading. I think that may be correct interpretation and possibly
  useful but I don't want to get stuck litigating it." Not designed: what a reader with no expected schema makes of
  plain data, and how a later, restricted reading of it applies [PRI-025: never guess the schema](../PRINCIPLES.md#PRI-025).
  *Implements* [FEA-006: persistence](../features/README.md#FEA-006); *relates to* [FEA-020: refinable models](../features/README.md#FEA-020).
  - **Current**: in mbse-schemas an unrestricted `OfAny`'s value is written tagged by one level, `{"int": 1}`, a value
    object by its schema's registered name, and read back as that schema's.

### Interaction models

- <a id="CAP-028"></a>**CAP-028: layered interaction models** · proposed · Interaction models layer functional behavior. *Implements* [FEA-009: layered interaction models](../features/README.md#FEA-009).
  - **Current**: not met.
- <a id="CAP-041"></a>**CAP-041: every kind of participant** · proposed · Interaction models cover each kind of participant (system, hardware,
  firmware, software, device, user, community, cloud resource, agent) and the interfaces between them. *Implements*
  [FEA-010: system behavior](../features/README.md#FEA-010) to [FEA-016: community behavior](../features/README.md#FEA-016).
  - **Current**: no kind covered.

### Schema-driven visualization and editing

Each capability's specification is in its own detail file, linked from the ID. **Current** for these is as recorded
before they moved here; each is to assess against mbse-rest, mbse-react, mbse-dynamodb and mbse-demo-apps.

- <a id="CAP-001"></a>**[CAP-001: no-code index view](CAP-001.md)** · adopted · Services and UI
  present a useful and usable index site driven exclusively by the schema. *Implements* [FEA-001: schema-driven UI](../features/FEA-001.md).
  - **Current**: to assess.
- <a id="CAP-002"></a>**[CAP-002: named schema list](CAP-002.md)** · adopted · An endpoint returns
  every named schema. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: met, by the store's schema snapshot, which holds every named schema ([As built](CAP-002.md#as-built)).
- <a id="CAP-003"></a>**[CAP-003: schema inspector](CAP-003.md)** · adopted · Given a schema's name,
  the UI obtains its full detail, unnamed schemas defined inline and named ones referenced. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: blocked: mbse-schemas cannot yet write one schema object as a document.
- <a id="CAP-004"></a>**[CAP-004: logical view templates](CAP-004.md)** · adopted · An endpoint
  returns, for every logical view kind, a mutation-query template whose symbols the UI gives each a schema or a
  reference. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-012"></a>**[CAP-012: logical view endpoints](CAP-012.md)** · adopted · One endpoint per
  logical view kind, taking a template with its symbols given and returning a stream of frames. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-005"></a>**[CAP-005: label and summary view](CAP-005.md)** · adopted · Logical view as label and summary: the
  minimum-sized view of an object or a relation entry. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-006"></a>**[CAP-006: chip view](CAP-006.md)** · adopted · Logical view as chip: a medium-sized,
  abbreviated view of an object or a relation entry. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-007"></a>**[CAP-007: detail view](CAP-007.md)** · adopted · Logical view of an object as detail: every
  schema-defined property and adjacency. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-008"></a>**[CAP-008: adjacency as a list of chips](CAP-008.md)** · adopted · Logical view of an adjacency as a list of
  chips: the immediate adjacencies of an object through one named adjacency. *Implements* [FEA-003: no-code logical views](../features/FEA-003.md).
  - **Current**: to assess.
- <a id="CAP-009"></a>**[CAP-009: schema browser](CAP-009.md)** · adopted · A section per named app
  schema, with a scrollable list of object chips. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-010"></a>**[CAP-010: object browser](CAP-010.md)** · adopted · A section per directory,
  with the chips of the objects its singleton holds. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-011"></a>**[CAP-011: relation browser](CAP-011.md)** · adopted · A section per relation
  entry, its properties' chip aside its linked objects' chips. *Implements* [FEA-004: index site browser views](../features/FEA-004.md).
  - **Current**: to assess.
- <a id="CAP-017"></a>**[CAP-017: object inspector](CAP-017.md)** · adopted · A shared panel showing
  the detail view of whatever object a gesture picks. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: complete (mbse-react, M3; editing added by [CAP-014: properties as markdown](CAP-014.md)).
- <a id="CAP-018"></a>**[CAP-018: adjacency inspector](CAP-018.md)** · adopted · Viewing and editing an
  entry and its outbound object, extant or proposed. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-019"></a>**[CAP-019: adjacencies at the end of a detail](CAP-019.md)** · adopted · Adjacencies at the end of a detail, each
  entry previewed as one chip. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-020"></a>**[CAP-020: provenance display](CAP-020.md)** · adopted · Who created an object,
  and when it was created and last modified. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-021"></a>**[CAP-021: lists ordered by creation](CAP-021.md)** · adopted · Adjacency lists ordered by creation where
  provenance is present. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-023"></a>**[CAP-023: relation inspector](CAP-023.md)** · adopted · The object inspector of
  one object among its siblings, stepping to the previous or next. *Implements* [FEA-005: inspector views](../features/FEA-005.md).
  - **Current**: to assess.
- <a id="CAP-013"></a>**[CAP-013: an in-memory store journaled to DynamoDB](CAP-013.md)** · adopted · An in-memory store journaled to DynamoDB,
  with occasional snapshots, replayed at startup. *Implements* [FEA-006: persistence](../features/FEA-006.md).
  - **Current**: to assess.
- <a id="CAP-014"></a>**[CAP-014: properties as markdown](CAP-014.md)** · adopted · Object properties as markdown, viewed and
  edited in the inspector. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-022"></a>**[CAP-022: booleans as checkboxes](CAP-022.md)** · adopted · Boolean properties as checkboxes.
  *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-015"></a>**[CAP-015: transaction provenance](CAP-015.md)** · adopted · Services keep a
  record of each transaction that writes, as mbse-schemas' `Provenance` module defines it. *Implements* [FEA-007: property kinds](../features/FEA-007.md).
  - **Current**: to assess.
- <a id="CAP-016"></a>**[CAP-016: comments](CAP-016.md)** · adopted · Comments, as data in an app's schema,
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
| C-002 | [CAP-025: schemas open in content](#CAP-025) | C-009 | [CAP-032: deliberate differences listed](#CAP-032) | C-016 | [CAP-039: schemas round-trip through Python3](CAP-039.md) |
| C-003 | [CAP-026: Python, TypeScript and C and C++ read as written](#CAP-026) | C-010 | [CAP-033: undeclared properties preserved](#CAP-033) | C-017 | [CAP-040: every generation ambiguity a parameter](#CAP-040) |
| C-004 | [CAP-027: Python3 source generated from schemas](CAP-027.md) | C-011 | [CAP-034: extension of schemas a module does not own](#CAP-034) | C-018 | [CAP-041: every kind of participant](#CAP-041) |
| C-005 | [CAP-028: layered interaction models](#CAP-028) | C-012 | [CAP-035: schema evolution](#CAP-035) | C-019 | [CAP-042: data generated from constraints](#CAP-042) |
| C-006 | [CAP-029: three-valued constraint checking](#CAP-029) | C-013 | [CAP-036: complete kinds for Python, TypeScript and C and C++](#CAP-036) | C-020 | [CAP-043: constraints resolved in any direction](#CAP-043) |
| C-007 | [CAP-030: the same cases in both languages](#CAP-030) | C-014 | [CAP-037: Python and TypeScript trees as faithful as the reference front end's](#CAP-037) | C-021 | [CAP-044: Verilog and SystemVerilog read by slang](#CAP-044) |

[CAP-001: no-code index view](CAP-001.md) to [CAP-023: relation inspector](CAP-023.md) kept the IDs they had in the workspace's former `VISUALIZATION.md`.

## Open items


- **Which parser for each language** (low priority). Tolerance and spec-awareness differ by language, as the editors'
  language services show. TypeScript's compiler, which tsserver is, parses any text to a full tree, type errors never
  affecting it. Python's semantic errors never affect a parse; CPython's `ast` fails only on syntax errors, without
  recovery, while Pyright's parser (Pylance's; MIT, written in TypeScript) and Ruff's recover from them. slang parses
  tolerantly and elaborates separately. C++ is the exception: its grammar depends on whether a name is a type, so a
  parser must resolve names, and Clang drops what it cannot resolve; EDG (Microsoft's C/C++ IntelliSense) copes but
  is commercial, so for Ccpp [CAP-068: C and C++ read by Clang](#CAP-068) conflicts with [CAP-026: Python, TypeScript and C and C++ read as written](#CAP-026). mbse-programs' [`docs/PROGRAMS.md`](../../../mbse-programs/docs/PROGRAMS.md) keeps Ccpp's front
  end under its Open questions until this is decided.
- The capabilities above are drafted from each repository's status sections; confirm them, then remove those sections
  and cite the capabilities instead. Schema capabilities land in mbse-schemas first, then in its dependents, each
  pinning the new release.
- **[CAP-033: undeclared properties preserved](#CAP-033) implements no feature.** It implemented F-005, now a quality ([QUA-002: open-world models](../QUALITIES.md#QUA-002)). Preserving undeclared data is not
  refinement ([FEA-020: refinable models](../features/README.md#FEA-020)); a feature for it is missing.
- **[CAP-015: transaction provenance](CAP-015.md) and [CAP-016: comments](CAP-016.md) sit under [FEA-007: property kinds](../features/FEA-007.md)** as they were first placed; provenance and comments
  may be features of their own.
- **Tech debt in the visualization capabilities.** Counted objects have no reference, so they are neither recorded nor
  transmitted ([FEA-003: no-code logical views](../features/FEA-003.md)), and browsers leave them out ([CAP-010: object browser](CAP-010.md), [CAP-011: relation browser](CAP-011.md)). It is to become a capability of a feature.

---

<!-- nav -->
[← Features](../features/README.md) · [Home](../README.md) · [Principles →](../PRINCIPLES.md)
