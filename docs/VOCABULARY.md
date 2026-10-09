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
- **V-020** · adopted · **Datatype**: a type characterized by its values and properties, apart from how they are
  represented, as ISO/IEC 11404 defines it.
- **V-022** · adopted · **Plain value** and **undeclared property**: a value whose type is unrefined, or refined only by
  a dialect not loaded, is held as its wire value and written back as read; so is a property no schema declares,
  after the declared ones, in the order read. Checking reports both as unknown (P-002).
- **V-023** · adopted · **Shape constraint**: a bound on an index, a capacity or a tensor's shape, a constraint on the
  type of the property that keys a relation's entries, not part of the schema.
- **V-024** · adopted · **Subsumption**: a type that must be of another is one wherever the other is expected, and
  reads its properties as its own (`car.mass`); composition (`car.Vehicle.mass`) is not a policy.

V-006, V-010 to V-019 and V-021 became modeling constructs, listed below; their IDs are not reused.

## Modeling constructs

Links are to `main` unless marked. Repositories are at `https://github.com/pitaman71/<repository>`.

### mbse-schemas

- `OfObject`, `OfProperty`, `OfRelation`, `OfAdjacency`, `OfEntry`, `OfParameter`, `OfApply`:
  [Elements](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#elements)
- Value object, reference object:
  [Value objects and reference objects](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#value-objects-and-reference-objects)
- Cardinality, `unique`: [Cardinality](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#cardinality)
- Meta-schema, module: [Meta-schemas](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#meta-schemas)
- Store, singleton: [Stores](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md#stores)
- Constraint, `requires`: [What a specification is made of](https://github.com/pitaman71/mbse-schemas/blob/main/MBSE.md#what-a-specification-is-made-of)
- On the `scalars` branch, not yet pushed: `OfName`, `Intersects`, `Unions`, variant, meta-relation, `uses`, open and
  one-link relations: [Schema vocabulary](https://github.com/pitaman71/mbse-schemas/blob/scalars/docs/VOCABULARY.md).
  Retiring there: `OfAny`, `OfNative`, `OfUnion`, `OfIntersection`, `OfIndexed`, and a list's extent (a store's
  extent stays).

### mbse-expressions

- Expression, `OfLiteral`, `OfOperation`, `OfVariable`, `OfLet`, `OfQuantifier`:
  [The Basic dialect](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#the-basic-dialect),
  being removed with Basic (F-004)
- Dialect (`Terms.Dialect`): [The framework](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#the-framework),
  [Dialects](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#dialects)
- Translator: [Translators](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#translators)
- Value domain: [Value domains](https://github.com/pitaman71/mbse-expressions/blob/main/docs/EXPRESSIONS.md#value-domains),
  giving way to the ISO/IEC 11404 dialect's datatypes (V-020)

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

- **Retire the copies.** The vocabulary invariant in each repository's `AGENTS.md` and "What a specification is made
  of" in each `MBSE.md` restate V-001 to V-009; replace them with citations of this file.
- **Links into the `scalars` branch** resolve once it is pushed, and move to `main` when it lands.

---

<!-- nav -->
[← Capabilities](CAPABILITIES.md) · [Home](README.md)
