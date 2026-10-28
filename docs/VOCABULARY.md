<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](README.md)

# Vocabulary

The terms every mbse repository uses alike, in code, docs and messages. Terms that are not modeling constructs are
defined here; a modeling construct is only named here, by the repository that defines it, with a link to its
definition. A repository's documents cite these rather than define them again.

Across this many languages, terms collide: an SVA `property`, a C++ template parameter, a SystemVerilog `constraint`
block. Wherever one of ours meets a language's own, in docs and examples, qualify the colliding term with whose it is.

## Terms

- <a id="VOC-001"></a>**VOC-001: specification** · adopted · **Specification**: constraints over variables, attached to the parts of a system they
  constrain. It is executable, nondeterministically: executing it chooses values consistent with every constraint.
  Each correct implementation is one such choice; generated test data is another.
- <a id="VOC-002"></a>**VOC-002: constraint** · adopted · **Constraint** is a modeling construct (see mbse-schemas, below). It is *checked*, *resolved*
  or *generated from*, never *executed*. *Never*: "rule".
- <a id="VOC-003"></a>**VOC-003: refinement** · adopted · **Refinement**: what a constraint does in formal logic. Adding a constraint refines a model,
  narrowing the values and implementations consistent with it. Each refinement is descriptive; a collection of them
  can amount to a prescription ([QUA-002: open-world models](QUALITIES.md#QUA-002), [PRI-021: refinement by constraint](PRINCIPLES.md#PRI-021)).
- <a id="VOC-004"></a>**VOC-004: variable** · adopted · **Variable**: what constraints bind; unrestricted, restricted or determined. A derived value is
  a variable determined by resolving a constraint, not a kind of its own.
- <a id="VOC-005"></a>**VOC-005: value** · adopted · **Value**: a constraint that determines its variable (`total = 5`). Given data, observed data
  and test fixtures are values, so checking an implementation adds its observed values to the constraints.
- <a id="VOC-007"></a>**VOC-007: property** · adopted · **Property**, never "field", which means only the host language's member that holds one.
- <a id="VOC-008"></a>**VOC-008: term** · adopted · **Term**: an element of an expression's tree. *Never*: a bare "node".
- <a id="VOC-009"></a>**VOC-009: syntax node** · adopted · **Syntax node**: an element of a program's tree. *Never*: a bare "node".
- <a id="VOC-026"></a>**VOC-026: schema** · adopted · **Schema**: what describes a value, a property's, a symbol's, a branch's or a part's, and what
  a value of any schema is of. *Never*: "type", which "has no meaning in mbse-*", as the user decided; a host
  language's own type (Python's `int`, TypeScript's `BigInt`) is qualified as the host's.
- <a id="VOC-025"></a>**VOC-025: shape constraint** · adopted · **Shape constraint**: a bound on an index, a capacity or a tensor's shape, a constraint on the
  type of the property that keys a relation's entries, not part of the schema; a parameter bound into it gives a
  tensor's shape. Planned in mbse-schemas'
  [Meta-schemas overhaul](../../mbse-schemas/docs/META_SCHEMAS.md), which removes
  the list's extent.
- <a id="VOC-027"></a>**VOC-027: second-order invention** · adopted · **Second-order invention**: a thing that can be modeled and invented
  elsewhere, such as a neutral expression language or datatypes. The project avoids them ([QUA-003: no second-order inventions](QUALITIES.md#QUA-003)), save as [PRI-022: second-order inventions by approval](PRINCIPLES.md#PRI-022)
  permits.
- <a id="VOC-028"></a>**VOC-028: human and agent** · adopted · **Human** and **agent**: sibling categories of who reads, writes and
  operates. A **user** is one persona of humans, beside engineering personas. *Never*: "user" as a synonym for humans.

VOC-006, VOC-010 to VOC-019 and VOC-021 became modeling constructs, listed below; VOC-020 and VOC-022 to VOC-024 were withdrawn.
Their IDs are not reused.

## Modeling constructs

Links are relative to a polyrepo checkout, each repository beside mbse-basis, and read its `main` unless marked.
Repositories are at `https://github.com/pitaman71/<repository>`.

### mbse-schemas

For usage, read what its tests run, which cannot drift from the code, not its prose design documents, which give the
reasons: the API on a page per language, [python.md](../../mbse-schemas/skills/mbse-schemas/references/python.md) and
[typescript.md](../../mbse-schemas/skills/mbse-schemas/references/typescript.md), each fenced program run by SKL-02;
[Corpus.py](../../mbse-schemas/python3/mbse/Schemas/Conformance/Corpus.py), one program building every kind of schema and data,
whose output in [conformance/python3/](../../mbse-schemas/conformance/python3) is the wire format, byte-identical in both languages;
and by topic, in [python3/tests/](../../mbse-schemas/python3/tests) (TypeScript's notebooks have the same case IDs), `25_Builders`
(building in a store, the plain schemas of schemas, paths such as `store.Schemas.OfInt`), `28_Extensions`
(`store.extend`), `27_Snapshots` (mutation logs, reading without an extension) and `22_Parametrics`.

- `OfAny`, `OfScalar`, `OfObject`, `OfProperty`, `OfRelation`, `OfAdjacency`, `OfEntry`, `OfUnion`,
  `OfIntersection`, `OfContainer`, `OfParameter`, `OfModule`:
  [Elements](../../mbse-schemas/docs/FRAMEWORK.md#elements)
- Basic scalar (`OfBool`, `OfInt`, `OfFloat`, `OfStr`, `OfBytes`): [Scalars](../../mbse-schemas/docs/FRAMEWORK.md#scalars).
  The only scalar schemas since 0.18.0: a store builds no other, and a scalar has no token; every finer scalar is a
  value domain (mbse-expressions).
- Branch, part, flat: [Unions and intersections by name](../../mbse-schemas/docs/FRAMEWORK.md#unions-and-intersections-by-name). A
  branch or part is an entry of `HasBranch` or `HasPart` (since 0.18.0), linking its type and carrying its name and
  description, not an object of its own.
- Container: [Lists](../../mbse-schemas/docs/FRAMEWORK.md#lists)
- Value object, reference object:
  [Value objects and reference objects](../../mbse-schemas/docs/FRAMEWORK.md#value-objects-and-reference-objects)
- Cardinality, `unique`: [Cardinality](../../mbse-schemas/docs/FRAMEWORK.md#cardinality)
- Level (data, schema, plain schema of schemas, meta-schema):
  [Store overhaul, Levels](../../mbse-schemas/docs/proposals/store-overhaul/README.md#levels). A *plain schema of schemas*
  (`Schemas.OfObject`, level 2) is what an extension extends; a *meta-schema* (level 3) is static code describing it.
- Module: [Meta-schemas](../../mbse-schemas/docs/FRAMEWORK.md#meta-schemas)
- Planned in the [Store overhaul](../../mbse-schemas/docs/proposals/store-overhaul/README.md): object identity, `OfIdentity`, `as_instance` (step 4, [Object identity](../../mbse-schemas/docs/OBJECT_IDENTITY.md));
  `Parameters.Bind` and `Parameters.Apply` ([Parametrics](../../mbse-schemas/docs/PARAMETRICS.md)).
- Store, singleton: [Stores](../../mbse-schemas/docs/FRAMEWORK.md#stores).
  Each store holds its own schemas, built when it is made or through `store.extend`; no schema object is shared
  across stores ([Schema extension](../../mbse-schemas/docs/SCHEMA_EXTENSION.md#decided), Decided, 23). There is one store type,
  `Builders.Store`, which registers a named schema by building it; `Stores.Combined` is deprecated (since 0.16.0).
- Parameter (`OfParameter`): a name only, a symbol standing for a schema (since 0.17.0); terms, applications and
  widths are mbse-expressions'. Bound by `Parameters.Bind`, planned: a reference object recording the substitution,
  which any operation taking the function interprets, applying it lazily or through `Parameters.Apply`
  ([Parametrics](../../mbse-schemas/docs/PARAMETRICS.md)).
- Constraint: [Where constraints attach](../../mbse-schemas/docs/FRAMEWORK.md#open-questions). `requires` left mbse-schemas in 0.17.0, for
  mbse-patterns ([Schema extension](../../mbse-schemas/docs/SCHEMA_EXTENSION.md#decided), Decided, 5 to 7).

### mbse-expressions

- Expression, `OfLiteral`, `OfOperation`, `OfVariable`, `OfLet`, `OfQuantifier`:
  [The Basic dialect](../../mbse-expressions/docs/EXPRESSIONS.md#the-basic-dialect)
- Dialect (`Terms.Dialect`): [The framework](../../mbse-expressions/docs/EXPRESSIONS.md#the-framework),
  [Dialects](../../mbse-expressions/docs/EXPRESSIONS.md#dialects)
- Translator: [Translators](../../mbse-expressions/docs/EXPRESSIONS.md#translators)
- Value domain: [Value domains](../../mbse-expressions/docs/EXPRESSIONS.md#value-domains)

### mbse-patterns

- Predicate (`OfPredicate`), symbol, match: [Predicates](../../mbse-patterns/docs/PATTERNS.md#predicates)
- `Exists`, `Forall`, `Contains`: [The predicate algebra](../../mbse-patterns/docs/PATTERNS.md#the-predicate-algebra)
- Application of a predicate: [Parameters and application](../../mbse-patterns/docs/PATTERNS.md#parameters-and-application)
- Pattern, `Choices`, distributions of values: [Distributions](../../mbse-patterns/docs/PATTERNS.md#distributions)
- Transform, session, policy, trace: [The model](../../mbse-patterns/docs/TRANSFORMS.md#the-model),
  [Data](../../mbse-patterns/docs/TRANSFORMS.md#data)

### mbse-programs

- Syntax node, kind, category: [Trees](../../mbse-programs/docs/PROGRAMS.md#trees)
- Standard: [Standards](../../mbse-programs/docs/PROGRAMS.md#standards)
- Language, entity, scope, program, transpiler, bridge: [Layers](../../mbse-programs/docs/PROGRAMS.md#layers)

### mbse-codegen-python

- The transforms of type generation (`Dataclass`, `Union`, `Alias`, ...), drop (`Codegen.Dropped`):
  [Transforms](capabilities/CAP-027.md#transforms)

## Open items

- **Retire the copies.** The vocabulary invariant in each repository's `AGENTS.md` restates [VOC-001: specification](#VOC-001) to [VOC-009: syntax node](#VOC-009); replace
  it with citations of this file.

## Earlier IDs

V-001 to V-026 are [VOC-001: specification](#VOC-001) to [VOC-026: schema](#VOC-026), the same numbers.

---

<!-- nav -->
[← Principles](PRINCIPLES.md) · [Home](README.md)
