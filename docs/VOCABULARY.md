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

- `OfAny`, `OfNative`, `OfObject`, `OfProperty`, `OfRelation`, `OfAdjacency`, `OfEntry`, `OfUnion`,
  `OfIntersection`, `OfIndexed`, `OfParameter`, `OfApply`:
  [Elements](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#elements)
- Native type, token: [Native types](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#native-types)
- Branch, part, flat: [Unions and intersections by name](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#unions-and-intersections-by-name)
- List, keyed list, extent: [Lists](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#lists)
- Value object, reference object:
  [Value objects and reference objects](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#value-objects-and-reference-objects)
- Cardinality, `unique`: [Cardinality](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#cardinality)
- Meta-schema, module: [Meta-schemas](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#meta-schemas)
- Planned in the [Meta-schemas overhaul](https://github.com/pitaman71/mbse-schemas/blob/main/docs/META_SCHEMAS.md):
  one-link and open relations, `OfModule`, `Defines`, meta-relation, anonymous adjacency. Retiring there: `OfAny`,
  `OfIndexed`, and a list's extent (a store's extent stays).
- Store, singleton: [Stores](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#stores)
- Constraint, `requires`: [Where constraints attach](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#open-questions)

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
