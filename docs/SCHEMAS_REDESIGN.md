<!-- nav -->
[← Vocabulary](VOCABULARY.md) · [Home](README.md)

# Schemas redesign

How the framework's modules are to be reorganized around the schema vocabulary's kinds: `Schemas`, `Visitors` and
`Proxies` mirroring one another kind by kind, a store and a module as the roots of data and of schemas, and a property's
value visited as a value of a name, plain or a variant. 

This is a design under review: nothing in it is built. 

What the user decided is quoted; the rest is proposed, and what is undecided is listed under Open questions. 

It concerns mbse-schemas, on its `scalars` branch, and builds on its
[Schema vocabulary](https://github.com/pitaman71/mbse-schemas/blob/main/docs/VOCABULARY.md) refactoring (slices 1 to
4 built, 5 next) and on its framework design's Resolved entry "Datatypes' operations are modeled, not coded; scalars
are plain, typed by `Schemas`' own names"
([framework design](https://github.com/pitaman71/mbse-schemas/blob/main/docs/FRAMEWORK.md)).

## Three modules that mirror one another

As the user put it: "Proxies should be a Visitors implementation and all three should mirror one another", and,
for each kind X of the vocabulary:

| Name | Is |
|---|---|
| `Schemas.OfX` | the kind's schema: `Spec`, `Builder` and `Data`, as now |
| `Visitors.OfX` | "defines the reverse visitor protocol": how data of the kind writes itself into a visitor (`accept`) |
| `Proxies.OfX` | "defines Spec, Builder, Data" of the kind's data |
| `Proxies.OfX.Data` | in-program representation of schema-defined data that may be built, mutated, frozen, serialized, traversed, analyzed, and introspected programmatically |
| `Proxies.OfX.Spec` | acceptable argument that may contain an instance of this kind or a callback expecting and returning a builder of this kind |
| `Proxies.OfX.Builder` | "must implement Visitors.OfX" |

The prefix follows the vocabulary: "Of is for Schemas only", so `Of` names a kind of the schema vocabulary, in each module that mirrors it, and nothing outside it.


## Fluent Builder/Visitor/Spec pattern

All data stored by the framework is governed by schemas, and anything governed by schemas must follow a design pattern comprising these three constructs:

| Name | Is |
|---|---|
| `OfX.Schema` | In-memory classes that capture the data organization and representation as a Python/Typescript DSL following the MBSE principles of iterative refinement. Schemas are data. Even the schemas themselves have a meta-schema. |
| `OfX.Visitors` | Inverse visitor interface - as a fluent API - that enables source code in any language to be written with or without schema awareness, effectively treating type introspection as a traversal problem. |
| `OfX.Builder` | In-memory classes that wrap schema-defined data elements, implementing the `OfX.Visitors` fluent api as well as providing type-specific read and write accessors. Every builder has a specific target - which may be new, putative, or pre-existing. Builder fluent api always ends with a call to `clone()` `copy()` or `update()` |

"Even the schemas themselves have a meta-schema." - `Schemas.OfX.Schema` is a bespoke class that defines how schema models are stored, visited, serialized, deserialized, compared, etc.

## Schema Kinds

| Name | Is |
|---|---|
| `OfModule` | registry of defined schemas. potentially nestable |
| `OfStore` | a view of schema-defined data. potentially remote, in transit, sharded, etc. must have a `root` module. |
| `OfName` | a name for any type labeled by the schema |
| `OfObject` | a type with values that can be decomposed as properties. singletons can be named and must exist in the store. |
| `OfRelation` | a type with values that represent entries that associate one or more reference objects to each other (by named link symbls). Entries may optionally contain properties which act as keys. Cardinality can be restricted via the 'union' property of the relation. |
| `OfAdjacency` | denotes that a particular object type may participate in an entry of a specific relation and via a specific named link symbol. the set of legal values for a relation link is inferreed from adjacencies. Adjacencies may be named, in which case they appear as container properties on proxy and generated data classes. Adjancencies may also be anonymous, in which case the denote legal association with the relation and link symbol but no container property will be inferred on the object. |

## The roots: a store of data, a module of schemas

"OfStore is the root of schema-governed data and OfModule is a root of schemas." The user specified the store's
protocol:

```python fragment
Visitors.OfStore                     # a view of schema-defined data
Visitors.OfStore.root -> Schemas.OfModule                                   # root of schema definitions,
                                                                            # assuming modules become hierarchical
Visitors.OfStore.stream(pattern: PatternT, order: Order[PatternT]) -> Iterable[Match[PatternT]]
```

`Proxies.OfStore` implements it. Where it meets today's `Stores.Store` protocol, proposed and to confirm:

| Today (`Stores.Store`) | Under `Visitors.OfStore` |
|---|---|
| `schema(name)`, `registered(name)`, `name_of(schema)`, `names()` | navigating `root`: a name resolves through the modules it nests in (`crm.Contact` is `Contact` in `crm`) |
| `register(schema)` | defining a schema in a module under `root` |
| `extent(name)` | `stream` with a pattern "objects of type `name`", in first-reference order |
| `singleton(name)` | `stream` with a pattern for that singleton, or kept |
| `builder(name, instance)` | `Proxies.OfObject.Builder` of the type |
| `member(instance, name)` | reading the property through `Visitors.OfObject` |

## A property's value

The user decided:

- "Visitors.OfAny goes away."
- Every property's value is visited through `Visitors.OfName` ("all of them do"), an entry property's too, whatever
  the kind of the property's type: a property typed by an object schema holds a value of that type or of one that
  specializes it.
- `Visitors.OfName` "gets two methods": `.as_variant(variant)` and `.as_plain(plain)`, each taking a callable that
  receives a builder and returns it.
- A variant "must be a variant (specializes) the current OfName or the callback is not called and None is returned".
  The property's own type counts ("yes"): a `Phone` held by `home: Phone` goes through `as_variant` too.
- The variant's type is chosen inside the callable, given as itself (a "slight preference" for this over passing it
  to `as_variant`): `v.as_variant(lambda b: b.of(Email, lambda e: e.address("a@b")))`.
- "we will need Visitors.OfPlain, Proxies.OfPlain": `as_plain`'s callable receives a `Visitors.OfPlain`, which replaces
  `Visitors.OfNative` (`has`, `get`, `set`, `clear`), and proxies implement it as `Proxies.OfPlain.Builder`.
- "Visitor methods of the form as_*() should always take a callback and return the callback's return value or None if
  the callback is not invoked." Every other visitor method that is not a query keeps returning `self`.

So, proposed:

| Today | Under the redesign |
|---|---|
| `p.value(lambda a: a.as_native(lambda n: n.set(3)))` | `p.value(lambda v: v.as_plain(lambda n: n.set(3)))` |
| `p.value(lambda a: a.as_object(lambda o: ...))` | `p.value(lambda v: v.as_variant(lambda b: b.of(Phone, lambda o: ...)))` |
| `Visitors.OfAny`, `Visitors.OfNative` | `Visitors.OfName`, `Visitors.OfPlain` |

A visitor that reads (a writer, a validator, a comparison) runs the callback for the kind of value actually there; a
visitor that builds runs the one the caller chose.

## Scalars

Decided, and recorded in the framework design's Resolved: mbse-schemas holds no dialect's code; a scalar value is held
as plain data, written as read, compared and keyed by wire value; a dialect's qualities (`Equatable`) are `OfName`s its
types specialize ("by specializes, at least for now"), and its operations are relations, each modeled externally, by
reference code or in a formal logic. mbse-schemas defines the plain scalars `Schemas.Text`, `Number`, `Integer`
(specializing `Number`) and `Boolean` ("fine for this iteration"), which type the meta-schemas' names, widths and
flags. A qualitative basis for types (cardinality, order and exactness as theories) is set aside for now.

The ordering of plain scalars was agreed "pending how you plan to model it". Proposed: a rule of the wire format, as
sorting entries by key is, stated in EQUALITY.md and implemented alike in both languages; numbers by exact value (a
`Plain.Number` compared as an exact decimal, never through a float), text by code point, false before true; values
numerically equal but written differently (`1`, `1.0`) neither equal nor ordered; other values equal or incomparable.
The alternative is a quality, `Schemas.Ordered`, that `Text`, `Number` and `Boolean` specialize, with a relation naming
the operation, modeled by reference code (the two implementations).

## Where today's proxies go

Asked "Why did we ever start collecting storage under Proxies.Of* other than Proxies.OfStore - the only place they
belong": the names came from mirroring `Schemas`' and `Visitors`' naming in the package's first version, from value
objects (`OfObject.Record`, 0.1), and from the user's "Adjacencies, as specified" (`Proxies.OfEntry.Data`, 0.9.1), not
from a decision about where data belongs. Under the redesign:

| Kind | `Proxies.OfX.Builder` (implements `Visitors.OfX`), today | `Proxies.OfX.Data`, today |
|---|---|---|
| `OfObject` | `_ObjectBuilder` (reference objects), `_RecordBuilder` (value objects) | `OfObject.Data`, `OfObject.Record` |
| `OfName` | `_AnySlot` | (open) |
| `OfPlain` | `_NativeSlot` | (open) |
| `OfProperty` | `_PropertySlot` | (open) |
| `OfAdjacency` | `_AdjacencySlot` | `OfAdjacency.Data`, the entries' tuple |
| `OfEntry` | `_EntryBuilder` | `OfEntry.Data` |
| `OfLink` | `_LinkSlot` | (open) |
| `OfStore` | (the store) | the data its root reaches |

## Open questions

- **`OfObject.Record`** is outside Spec, Builder and Data: are reference objects and value objects one
  `Proxies.OfObject.Data`, told apart by their schema (`.ref()`), with one builder?
- **`Data` of a kind that stores nothing of its own** (a plain value held as itself, a name's value, a property's, a
  link's target): a type alias naming what is held, or none?
- **`PatternT`, `Order` and `Match`**: mbse-schemas cannot depend on mbse-patterns. Generic protocols here, with
  mbse-patterns supplying patterns, or a minimal pattern here (objects of a type, entries of a relation) that
  mbse-patterns extends? A match is presumably a binding of the pattern's symbols to objects and entries.
- **Nested modules**: "assuming modules become hierarchical", how a module defines modules, and how names resolve
  through them.
- **How far mirroring goes**: whether every column is filled (`Visitors.OfModule`, `Schemas.OfPlain`,
  `Schemas.OfEntry`, `Schemas.OfLink`), or only where a kind has values to visit; and whether the other implementations
  of the visitor protocols (`Plain`'s writers, `Validators`, `Reachable`) take `OfX` names as `Comparison`'s do.
- **The ordering of plain scalars**: a rule of the wire format, or a modeled quality (above).
- **Sequencing**: this changes every visitor in both languages and every dependent's use of the protocols. Proposed:
  slice 5 removes `OfNative` with the plain scalars and the property-value protocol (`Visitors.OfName`, `OfPlain`,
  `as_*` returning the callback's result); `Visitors.OfStore` with `root` and `stream`, and `Proxies.OfX` as Spec,
  Builder and Data, follow as a slice of their own.

---

<!-- nav -->
[← Vocabulary](VOCABULARY.md) · [Home](README.md)
