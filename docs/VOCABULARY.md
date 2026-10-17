<!-- nav -->
[← Capabilities](CAPABILITIES.md) · [Home](README.md)

# Vocabulary

The terms every mbse repository uses alike, in code, docs and messages. Terms that are not modeling constructs are
defined here; a modeling construct is only named here, by the repository that defines it, with a link to its
definition. A repository's documents cite these rather than define them again.

Across this many languages, terms collide: an SVA `property`, a C++ template parameter, a SystemVerilog `constraint`
block. Wherever one of ours meets a language's own, in docs and examples, qualify the colliding term with whose it is.

## Terms

- **V-001** · adopted · **Specification**: constraints over variables, attached to the parts of a system they
  constrain. It is executable, nondeterministically: executing it chooses values consistent with every constraint.
  Each correct implementation is one such choice; generated test data is another.
- **V-002** · adopted · **Constraint** is a modeling construct (see mbse-schemas, below). It is *checked*, *resolved*
  or *generated from*, never *executed*. *Never*: "rule".
- **V-003** · adopted · **Refinement**: what a constraint does in formal logic. Adding a constraint refines a model,
  narrowing the values and implementations consistent with it. Each refinement is descriptive; a collection of them
  can amount to a prescription (F-007).
- **V-004** · adopted · **Variable**: what constraints bind; unrestricted, restricted or determined. A derived value is
  a variable determined by resolving a constraint, not a kind of its own.
- **V-005** · adopted · **Value**: a constraint that determines its variable (`total = 5`). Given data, observed data
  and test fixtures are values, so checking an implementation adds its observed values to the constraints.
- **V-007** · adopted · **Property**, never "field", which means only the host language's member that holds one.
- **V-008** · adopted · **Term**: an element of an expression's tree. *Never*: a bare "node".
- **V-009** · adopted · **Syntax node**: an element of a program's tree. *Never*: a bare "node".
- **V-026** · adopted · **Schema**: what describes a value, a property's, a symbol's, a branch's or a part's, and what
  a value of any schema is of. *Never*: "type", which "has no meaning in mbse-*", as the user decided; a host
  language's own type (Python's `int`, TypeScript's `BigInt`) is qualified as the host's.
- **V-025** · adopted · **Shape constraint**: a bound on an index, a capacity or a tensor's shape, a constraint on the
  type of the property that keys a relation's entries, not part of the schema; a parameter bound into it gives a
  tensor's shape. Planned in mbse-schemas'
  [Meta-schemas overhaul](https://github.com/pitaman71/mbse-schemas/blob/main/docs/META_SCHEMAS.md), which removes
  the list's extent.

V-006, V-010 to V-019 and V-021 became modeling constructs, listed below; V-020 and V-022 to V-024 were withdrawn.
Their IDs are not reused.

## Modeling constructs

Links are to `main` unless marked. Repositories are at `https://github.com/pitaman71/<repository>`.

### mbse-schemas

For usage, read what its tests run, which cannot drift from the code, not its prose design documents, which give the
reasons: the API on a page per language, [python.md](https://github.com/pitaman71/mbse-schemas/blob/main/skills/mbse-schemas/references/python.md) and
[typescript.md](https://github.com/pitaman71/mbse-schemas/blob/main/skills/mbse-schemas/references/typescript.md), each fenced program run by SKL-02;
[Corpus.py](https://github.com/pitaman71/mbse-schemas/blob/main/python3/mbse/Schemas/Conformance/Corpus.py), one program building every kind of schema and data,
whose output in [conformance/python3/](https://github.com/pitaman71/mbse-schemas/blob/main/conformance/python3) is the wire format, byte-identical in both languages;
and by topic, in [python3/tests/](https://github.com/pitaman71/mbse-schemas/blob/main/python3/tests) (TypeScript's notebooks have the same case IDs), `25_Builders`
(building in a store, the plain schemas of schemas, paths such as `store.Schemas.OfInt`), `28_Extensions`
(`store.extend`), `27_Snapshots` (mutation logs, reading without an extension) and `22_Parametrics`.

- `OfAny`, `OfScalar`, `OfObject`, `OfProperty`, `OfRelation`, `OfAdjacency`, `OfEntry`, `OfUnion`,
  `OfIntersection`, `OfContainer`, `OfParameter`, `OfModule`:
  [Elements](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#elements)
- Basic scalar (`OfBool`, `OfInt`, `OfFloat`, `OfStr`, `OfBytes`): [Scalar types](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#scalar-types).
  The only scalar schemas since 0.18.0: a store builds no other, and a scalar has no token; every finer scalar is a
  value domain (mbse-expressions).
- Branch, part, flat: [Unions and intersections by name](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#unions-and-intersections-by-name). A
  branch or part is an entry of `HasBranch` or `HasPart` (since 0.18.0), linking its type and carrying its name and
  description, not an object of its own.
- Container: [Lists](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#lists)
- Value object, reference object:
  [Value objects and reference objects](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#value-objects-and-reference-objects)
- Cardinality, `unique`: [Cardinality](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#cardinality)
- Level (data, schema, plain schema of schemas, meta-schema):
  [Store overhaul, Levels](https://github.com/pitaman71/mbse-schemas/blob/main/docs/proposals/store-overhaul/README.md#levels). A *plain schema of schemas*
  (`Schemas.OfObject`, level 2) is what an extension extends; a *meta-schema* (level 3) is static code describing it.
- Module: [Meta-schemas](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#meta-schemas)
- Planned in the [Store overhaul](https://github.com/pitaman71/mbse-schemas/blob/main/docs/proposals/store-overhaul/README.md): object identity, `OfIdentity`, `as_instance` (step 4, [Object identity](https://github.com/pitaman71/mbse-schemas/blob/main/docs/OBJECT_IDENTITY.md));
  `Parameters.Bind` and `Parameters.Apply` ([Parametrics](https://github.com/pitaman71/mbse-schemas/blob/main/docs/PARAMETRICS.md)).
- Store, singleton: [Stores](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#stores).
  Each store holds its own schemas, built when it is made or through `store.extend`; no schema object is shared
  across stores ([Schema extension](https://github.com/pitaman71/mbse-schemas/blob/main/docs/SCHEMA_EXTENSION.md#decided), Decided, 23). There is one store type,
  `Builders.Store`, which registers a named schema by building it; `Stores.Combined` is deprecated (since 0.16.0).
- Parameter (`OfParameter`): a name only, a symbol standing for a schema (since 0.17.0); terms, applications and
  widths are mbse-expressions'. Bound by `Parameters.Bind`, planned: a reference object recording the substitution,
  which any operation taking the function interprets, applying it lazily or through `Parameters.Apply`
  ([Parametrics](https://github.com/pitaman71/mbse-schemas/blob/main/docs/PARAMETRICS.md)).
- Constraint: [Where constraints attach](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#open-questions). `requires` left mbse-schemas in 0.17.0, for
  mbse-patterns ([Schema extension](https://github.com/pitaman71/mbse-schemas/blob/main/docs/SCHEMA_EXTENSION.md#decided), Decided, 5 to 7).

### mbse-expressions

- Expression, `OfLiteral`, `OfOperation`, `OfVariable`, `OfLet`, `OfQuantifier`:
  [The Basic dialect](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#the-basic-dialect)
- Dialect (`Terms.Dialect`): [The framework](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#the-framework),
  [Dialects](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#dialects)
- Translator: [Translators](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#translators)
- Value domain: [Value domains](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#value-domains)

### mbse-patterns

- Predicate (`OfPredicate`), symbol, match: [Predicates](https://github.com/pitaman71/mbse-patterns/blob/main/docs/PATTERNS.md#predicates)
- `Exists`, `Forall`, `Contains`: [The predicate algebra](https://github.com/pitaman71/mbse-patterns/blob/main/docs/PATTERNS.md#the-predicate-algebra)
- Application of a predicate: [Parameters and application](https://github.com/pitaman71/mbse-patterns/blob/main/docs/PATTERNS.md#parameters-and-application)
- Pattern, `Choices`, distributions of values: [Distributions](https://github.com/pitaman71/mbse-patterns/blob/main/docs/PATTERNS.md#distributions)
- Transform, session, policy, trace: [The model](https://github.com/pitaman71/mbse-patterns/blob/main/docs/TRANSFORMS.md#the-model),
  [Data](https://github.com/pitaman71/mbse-patterns/blob/main/docs/TRANSFORMS.md#data)

### mbse-programs

- Syntax node, kind, category: [Trees](https://github.com/pitaman71/mbse-programs/blob/main/docs/PROGRAMS.md#trees)
- Standard: [Standards](https://github.com/pitaman71/mbse-programs/blob/main/docs/PROGRAMS.md#standards)
- Language, entity, scope, program, transpiler, bridge: [Layers](https://github.com/pitaman71/mbse-programs/blob/main/docs/PROGRAMS.md#layers)

### mbse-codegen-python

- The transforms of type generation (`Dataclass`, `Union`, `Alias`, ...), drop (`Codegen.Dropped`):
  [Transforms](https://github.com/pitaman71/mbse-codegen-python/blob/main/docs/CODEGEN.md#transforms)

## Open items

- **Retire the copies.** The vocabulary invariant in each repository's `AGENTS.md` restates V-001 to V-009; replace
  it with citations of this file.

---

<!-- nav -->
[← Capabilities](CAPABILITIES.md) · [Home](README.md)
