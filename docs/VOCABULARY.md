<!-- nav -->
[← The mbse basis](README.md) · [Home](../README.md)

# Vocabulary

The terms every mbse repository uses alike, in code, docs and messages. Terms that are not modeling constructs are
defined here; a modeling construct is only named here, by the repository that defines it, with a link to its
definition. A repository's documents cite these rather than define them again.

Across this many languages, terms collide: an SVA `property`, a C++ template parameter, a SystemVerilog `constraint`
block. As the user put it: "Apparent collisions across this many languages are inevitable. Just be sure any
documentation and examples properly qualify a potentially colliding term along the seam." Wherever a document or
example stands at a seam between languages or frameworks, a term that collides across them is qualified with whose it
is: "a Verilog module", "an mbse module"; a host language's "type" beside an mbse "schema" ([VOC-026: schema](#VOC-026)).

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
  meta-schemas overhaul ([CAP-108: relations as scalable containers](capabilities/CAP-108.md), containers), which removes
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
  [CAP-109: schemas as linked objects in modules](capabilities/CAP-109.md#the-kinds)
- Basic scalar (`OfBool`, `OfInt`, `OfFloat`, `OfStr`, `OfBytes`): [CAP-156: the five basic scalars with boundless domains](capabilities/CAP-156.md).
  The only scalar schemas since 0.18.0: a store builds no other, and a scalar has no token; every finer scalar is a
  value domain (mbse-expressions).
- Branch, part, flat: [CAP-153: unions and intersections of named branches and parts](capabilities/CAP-153.md). A
  branch or part is an entry of `HasBranch` or `HasPart` (since 0.18.0), linking its type and carrying its name and
  description, not an object of its own.
- Container: [CAP-108: relations as scalable containers](capabilities/CAP-108.md)
- Value object, reference object:
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects)
- Cardinality, `unique`: [CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md)
- Level (data, schema, plain schema of schemas, meta-schema):
  [Store overhaul, Levels](../../mbse-schemas/docs/proposals/store-overhaul/README.md#levels). A *plain schema of schemas*
  (`Schemas.OfObject`, level 2) is what an extension extends; a *meta-schema* (level 3) is static code describing it.
- Module: [CAP-109: schemas as linked objects in modules](capabilities/CAP-109.md)
- Planned in the [Store overhaul](../../mbse-schemas/docs/proposals/store-overhaul/README.md): object identity, `OfIdentity`, `as_instance` (step 4, [FEA-026: deterministic object identity](features/FEA-026.md));
  `Parameters.Bind` and `Parameters.Apply` ([CAP-114: parameter bindings are substituted and checked](capabilities/CAP-114.md)).
- Store, singleton: [CAP-161: isolated stores, with no global registry](capabilities/CAP-161.md).
  Each store holds its own schemas, built when it is made or through `store.extend`; no schema object is shared
  across stores (schema extension 23 in [CAP-116: framework schemas extended, checked](capabilities/CAP-116.md#decided)). There is one store type,
  `Builders.Store`, which registers a named schema by building it; `Stores.Combined` is deprecated (since 0.16.0).
- Parameter (`OfParameter`): a name only, a symbol standing for a schema (since 0.17.0); terms, applications and
  widths are mbse-expressions'. Bound by `Parameters.Bind`, planned: a reference object recording the substitution,
  which any operation taking the function interprets, applying it lazily or through `Parameters.Apply`
  ([CAP-114: parameter bindings are substituted and checked](capabilities/CAP-114.md)).
- Constraint: [CAP-166: constraints attached where they constrain](capabilities/CAP-166.md#open-questions). `requires` left mbse-schemas in 0.17.0, for
  mbse-patterns (schema extension 5 to 7 in [FEA-024: expressions as data](features/FEA-024.md#decided)).

### mbse-expressions

- Expression (`Expressions.Framework.Expression`), term (`Expressions.Framework.Term`: `literal`, `call`, `variable`,
  `let`, Basic's `quantifier`): [Terms and the core vocabulary](capabilities/CAP-095.md#terms-and-the-core-vocabulary)
- Dialect (`Terms.Dialect`): [The framework](capabilities/CAP-098.md#the-framework),
  [Dialects](capabilities/CAP-100.md#dialects)
- Translator: [Translators](capabilities/CAP-101.md#translators)
- Value domain: [Value domains](capabilities/CAP-097.md#value-domains)

### mbse-patterns

- Predicate (`OfPredicate`), symbol, match: [Predicates](capabilities/CAP-150.md#predicates)
- `Exists`, `Forall`, `Contains`: [The predicate algebra](capabilities/CAP-152.md#the-predicate-algebra)
- Application of a predicate: [Parameters and application](capabilities/CAP-150.md#parameters-and-application)
- Pattern, `Choices`, distributions of values: [Distributions](capabilities/CAP-072.md#distributions)
- Transform, session, policy, trace: [The model](capabilities/CAP-074.md#the-model),
  [Data](capabilities/CAP-074.md#data)

### mbse-programs

- Syntax node, kind, category: [Trees](capabilities/CAP-084.md#trees)
- Standard: [Standards](capabilities/CAP-085.md#standards)
- Language, entity, scope, program, transpiler, bridge: [Layers](capabilities/CAP-084.md#layers)

### mbse-codegen-python

- The transforms of type generation (`Dataclass`, `Union`, `Alias`, ...), drop (`Codegen.Dropped`):
  [Transforms](capabilities/CAP-027.md#transforms)

## Earlier IDs

V-001 to V-026 are [VOC-001: specification](#VOC-001) to [VOC-026: schema](#VOC-026), the same numbers.

---

<!-- nav -->
[← The mbse basis](README.md) · [Home](../README.md)
