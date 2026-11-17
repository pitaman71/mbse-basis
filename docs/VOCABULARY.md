<!-- nav -->
[← The mbse basis](README.md) · [Home](../README.md)

# Vocabulary

The terms every mbse repository uses alike, in code, docs and messages. Terms that are not modeling constructs are
defined here. A modeling construct is listed under the repository that defines it, in
[Modeling constructs](#modeling-constructs), below, with a link to its definition. A construct may also have a term
here, as the user decided: "A modeling construct is allowed to have a term in this doc. In that case the term
definition should be a simple sentence or paragraph that describes what the construct models and a link to the feature
if one is defined. Moving such entries to the mbse-schemas modeling constructs section is preferred." A line under
Modeling constructs that says what a construct models follows the same rule. A repository's documents cite these rather
than define them again.

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
- <a id="VOC-033"></a>**VOC-033: dialect** · adopted · **Dialect**: a language modeled as data, the kinds of term and
  statement of one expression or statement language, of a sublanguage its standard defines (type expressions, patterns,
  regular expressions, a preprocessor's directives), or of a published standard's or an ABI's datatypes; complete to its
  standard, and named `Expressions.<Family>.<Dialect>`, its family as its standard names it. Implemented by [CAP-098:
  dialects over one framework](capabilities/CAP-098.md) (the framework every dialect implements) and [CAP-226: complete
  expression dialects](capabilities/CAP-226.md); languages' dialects in [CAP-100: six languages' expression
  dialects](capabilities/CAP-100.md) and its languages' own, [CAP-227: the Python3 expression
  dialect](capabilities/CAP-227.md), [CAP-228: the TypeScript5 expression dialect](capabilities/CAP-228.md), [CAP-229:
  the C expression dialect](capabilities/CAP-229.md), [CAP-230: the C++ expression dialect](capabilities/CAP-230.md),
  [CAP-231: the SystemVerilog expression dialect, complete](capabilities/CAP-231.md); sublanguages in [CAP-276: Python's
  type expressions and match patterns as data](capabilities/CAP-276.md), [CAP-277: TypeScript's types and destructuring
  patterns as data](capabilities/CAP-277.md), [CAP-278: C's and C++'s type names and preprocessor directives as
  data](capabilities/CAP-278.md), [CAP-281: Python's, ECMAScript's and C++'s regular expressions as
  data](capabilities/CAP-281.md) and [CAP-294: POSIX's regular expressions as data](capabilities/CAP-294.md); standards' and ABIs' in [CAP-097: value domains
  of published standards](capabilities/CAP-097.md) and [CAP-267: C and C++ terms read under the ABI their holder
  names](capabilities/CAP-267.md); translated between by [CAP-101: translation between
  dialects](capabilities/CAP-101.md). The children of its terms and statements: [VOC-030: subterm](#VOC-030), [VOC-031:
  substatement](#VOC-031), [VOC-032: clause](#VOC-032).
- <a id="VOC-030"></a>**VOC-030: subterm** · adopted · **Subterm**: Expression and statement languages are part of what
  dialects ([VOC-033: dialect](#VOC-033)) model. A term that is a child of a term or a statement, held by one of its
  properties (`a` and `b` of `a + b`; a let's `value` and `body`; a cast's type). *Never*: "slot", "position". As the
  user decided: "I would refer to a child that is a statement as a "clause" and a child that is an
  expression term as a "subterm"", then "substatement" for the former.
- <a id="VOC-031"></a>**VOC-031: substatement** · adopted · **Substatement**: Expression and statement languages are
  part of what dialects ([VOC-033: dialect](#VOC-033)) model. A statement that is a child of a statement or a term (an
  `if` statement's branches, a loop's body, an arrow function's block), as ISO/IEC 14882 uses the word. As the user
  asked: "Is "substatement" cleaner than "clause"".
- <a id="VOC-032"></a>**VOC-032: clause** · adopted · **Clause**: Expression and statement languages are part of what
  dialects ([VOC-033: dialect](#VOC-033)) model. A part of a statement that its language's grammar allows only within
  that statement, and that holds statements: Python's `except` clause and `case`, owned by their `try` and `match`;
  mbse-programs' `Programs.Framework.Clause`, never a statement. As the user decided: "I don't much like
  treating a clause as a statement when it can only appear in that place", choosing `Clause` as its name, with this
  entry narrowed to it. Any child, subterm ([VOC-030: subterm](#VOC-030)) or substatement ([VOC-031:
  substatement](#VOC-031)), is a child. Qualified where it meets an mbse-transforms policy's clauses,
  mbse-schemas' `unique` clauses, or a grammar's own `…Clause` syntax nodes.
- <a id="VOC-034"></a>**VOC-034: closed constructor expression** · adopted · **Closed constructor expression**:
  Expression languages are part of what dialects ([VOC-033: dialect](#VOC-033)) model. A closed constructor expression
  is an expression that constructs a value from literals through the dialect's constructors and that refers to no free
  name. A literal is the simplest closed constructor expression. Displays and casts of literals are others, such as
  Python's `{1, 2}`, C's `(short)3` and `(int[]){1, 2}`, and SystemVerilog's `int'(5)`. Almost every value in a
  dialect's domains has a closed constructor expression in that dialect. Three kinds of value are the exceptions. A
  value that has identity (an object, a closure, a list that two places share) can be rebuilt only as an equal value,
  not as the same value. A value from outside the dialect, such as a host object or a data object, has no constructor
  in the dialect's language. A value in an intermediate state, such as a partly consumed generator, has no
  constructor for that state.
  *Never*: "a value that has no literal", where the text means a value that a closed constructor expression could
  construct.
- <a id="VOC-026"></a>**VOC-026: schema** · adopted · **Schema**: what describes a value, a property's, a symbol's, a branch's or a part's, and what
  a value of any schema is of. *Never*: "type", which "has no meaning in mbse-*", as the user decided; a host
  language's own type (Python's `int`, TypeScript's `BigInt`) is qualified as the host's.
- <a id="VOC-025"></a>**VOC-025: shape constraint** · adopted · **Shape constraint**: a bound on an index, a capacity or a tensor's shape, a constraint on the
  type of the property that keys a relation's entries, not part of the schema; a parameter bound into it gives a
  tensor's shape. Planned in mbse-schemas'
  meta-schemas overhaul ([CAP-108: relations as scalable containers](capabilities/CAP-108.md), containers), which removes
  the list's `extent`.
- <a id="VOC-027"></a>**VOC-027: second-order invention** · adopted · **Second-order invention**: a thing that can be modeled and invented
  elsewhere, such as a neutral expression language or datatypes. The project avoids them ([QUA-003: no second-order inventions](QUALITIES.md#QUA-003)), save as [PRI-022: second-order inventions by approval](PRINCIPLES.md#PRI-022)
  permits.
- <a id="VOC-028"></a>**VOC-028: human and agent** · adopted · **Human** and **agent**: sibling categories of who reads, writes and
  operates. A **user** is one persona of humans, beside engineering personas. *Never*: "user" as a synonym for humans.
- <a id="VOC-029"></a>**VOC-029: fungible** · adopted · **Fungible**: readily changeable to adapt to new situations;
  flexible. The third sense in [Merriam-Webster](https://www.merriam-webster.com/dictionary/fungible), which the
  project adopts uniformly, as the user decided. Its first two senses, interchangeable or replaceable by an
  equal part, are special cases of it.

VOC-006, VOC-010 to VOC-019 and VOC-021 became modeling constructs, listed below; VOC-020 and VOC-022 to VOC-024 were withdrawn.
Their IDs are not reused.

### Data and stores

The terms below name what code and documents in several repositories do with mbse-schemas' data and stores. The
constructs of mbse-schemas' data model and store, from reference objects to transactions and frames, are listed under
[mbse-schemas](#mbse-schemas), below.

- <a id="VOC-035"></a>**VOC-035: visitor** · adopted · **Visitor**: the protocol through which code reads and writes a
  value of one kind, `Visitors.OfX` for kind X ([PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004),
  [FEA-025: serialization behavior conventions in schema](features/FEA-025.md)). As the user decided: "Visitor is a
  protocol pure and simple. Proxy implements that protocol using dynamic classes. Codegen implements the protocol as
  generated `Builder` claseses." A proxy is mbse-schemas' implementation (under [mbse-schemas](#mbse-schemas), below),
  and a builder ([VOC-036: builder](#VOC-036)) is code generation's. An instance of a visitor of a store's data lives
  only within the transaction that made it
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).
- <a id="VOC-036"></a>**VOC-036: builder** · adopted · **Builder**: a class that code generation generates for a schema,
  which implements the visitor protocol ([VOC-035: visitor](#VOC-035)) for that schema's values
  ([FEA-022: code generation](features/README.md#FEA-022)). As the user decided, "Codegen implements the protocol as
  generated `Builder` claseses." [PRI-019: fluent builder syntax](PRINCIPLES.md#PRI-019) names the syntax in which code
  writes a model through the protocol, whether it writes through a generated `Builder` or through a proxy, whose
  dynamic classes include a `Builder` of their own ([PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004)).
- <a id="VOC-037"></a>**VOC-037: symbol binding** · adopted · **Symbol binding**: what a frame holds for each of its
  symbols, the object, or the parameter, that the symbol stands for in that result of a transaction
  ([FEA-027: mutations as queries](features/FEA-027.md),
  [the parametrics proposal](../proposals/PARAMETRICS.md#decided)). As the user decided, "Frames hold symbol bindings
  and property assignments, not proxies"
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)). A symbol binding is
  not a parameter binding ([VOC-038: parameter binding](#VOC-038)): as the user decided, "Parameter binding and symbol
  binding have different meanings and should be used as phrases, not just "binding"." *Never*: a bare "binding".
- <a id="VOC-038"></a>**VOC-038: parameter binding** · adopted · **Parameter binding**: what gives a parameter its value
  or its object within a scope ([FEA-033: model parameters](features/FEA-033.md)). A data object holds the parameter
  bindings for the parameters that its schema declares
  ([CAP-314: parameters bound by the data objects their schema governs](capabilities/README.md#CAP-314)). In
  mbse-expressions, an expression root holds parameter bindings for parameters that it declares, and an application
  holds them for the parameters of the definition that it applies
  ([CAP-163: parameters bound, applied and generated beyond mbse-schemas](capabilities/CAP-163.md),
  [the parametrics proposal](../proposals/PARAMETRICS.md#bound)). A parameter reference resolves through a parameter
  binding in its scope. A parameter binding is not a symbol binding ([VOC-037: symbol binding](#VOC-037)), as the user
  decided: "Parameter binding and symbol binding have different meanings and should be used as phrases, not just
  "binding"." *Never*: a bare "binding".
- <a id="VOC-039"></a>**VOC-039: journal** · adopted · **Journal**: a store's committed transactions, recorded as data in
  the order in which they were committed, from which the store's data is made again
  ([FEA-030: clean mutation-based transactional API](features/FEA-030.md)). "Journal" names two records, until their
  languages become one, as the user decided, choosing "(b)" of the options offered. In mbse-schemas, a journal is the
  list of transactions as they were submitted, replayed by executing each again
  ([CAP-129: journals replayed by execution](capabilities/CAP-129.md)). In mbse-journals, a journal records the changes
  that the transactions made ([CAP-271: the journal language](capabilities/README.md#CAP-271)): as the user put it,
  "journals store changes", and "journals store journal trransactions which store changes". The two records differ, as
  the user decided: "Mutation-transaction streams and change journals are not the same language - yet." A journal's
  elements are transactions, as the user decided: "Journals comprise transactions." *Never*: "journal entry".
## Modeling constructs

Links are relative to a polyrepo checkout, each repository beside mbse-basis, and read its `main` unless marked.
Repositories are at `https://github.com/pitaman71/<repository>`.

### mbse-schemas

For usage, read what its tests run, which cannot drift from the code, not its prose design documents, which give the
reasons: [its tutorials](https://github.com/pitaman71/mbse-schemas/blob/main/python3/tutorials/README.md), each step a case run in both languages, which
its [skill](https://github.com/pitaman71/mbse-schemas/blob/main/skills/mbse-schemas/SKILL.md) links practice by practice;
`Corpus.py` in mbse-schemas' conformance package, one program building every kind of schema and data,
whose output in [conformance/python3/](https://github.com/pitaman71/mbse-schemas/blob/main/conformance/python3) is the wire format, byte-identical in both languages;
and by topic, in [python3/tests/](https://github.com/pitaman71/mbse-schemas/blob/main/python3/tests) (TypeScript's notebooks have the same case IDs), `25_Builders`
(building in a store, the plain schemas of schemas, attributes such as `store.Schemas.OfInt`), `28_Extensions`
(`store.extend`), `27_Snapshots` (mutation logs, reading without a schema extension) and `22_Parametrics`.

Where a line below says what a construct models, it links the feature that the construct serves, then the capabilities
that define it.

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
- Reference object (an object schema marked `.ref(True)`): an object that stands on its own and that relations link,
  never held by a property or a container. A model makes a thing a reference object where several owners share it,
  where it is part of a cycle, or where something refers to it by identity. A reference object is a singleton, an
  owned object or a counted object, as its schema declares.
  [FEA-035: clean modeling separation between value objects and reference objects](features/FEA-035.md);
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects),
  [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md).
- Value object (an object schema not marked `.ref()`): an object without identity, held by one owner's property,
  directly or in a container, and copied and compared by value. Union values, intersection values and references are
  value objects.
  [FEA-035: clean modeling separation between value objects and reference objects](features/FEA-035.md);
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects).
- Relation (`OfRelation`): a kind of fact that links two or more reference objects, one by each of its named links, and
  that holds a value for each of its properties. Its `unique` clauses decide whether its entries are a set or a list.
  [FEA-035: clean modeling separation between value objects and reference objects](features/FEA-035.md);
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md),
  [CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md).
- Relation entry (`OfEntry`; its reference, `References.OfEntry`): one fact of a relation, with no identity beyond its
  relation, its links and its properties. An ownership entry, an entry through an adjacency marked `owner()`, places the
  object that it owns. A bare "entry" means a relation entry, as the user decided: ""entry" means relation entries.
  Journals comprise transactions." Any other sense of "entry" is qualified, and a journal's elements are transactions
  ([VOC-039: journal](#VOC-039)).
  [FEA-035: clean modeling separation between value objects and reference objects](features/FEA-035.md);
  [CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md),
  [CAP-130: references to objects, entries and frames](capabilities/CAP-130.md).
- Adjacency (`OfAdjacency`): an object schema's declaration that its objects fill one named link of a relation, by
  which an object reaches the entries that link it (`card.phones`). An adjacency marked `owner()` reaches the object's
  owner.
  [FEA-035: clean modeling separation between value objects and reference objects](features/FEA-035.md);
  [CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md),
  [CAP-205: anonymous adjacencies, a link filled without storage on the object](capabilities/CAP-205.md).
- Union (`OfUnion`): a value that holds exactly one of several named branches, each a schema of the same kind. A
  document that stands at a seam qualifies the term where it could be read as a C or C++ `union`.
  [FEA-025: serialization behavior conventions in schema](features/FEA-025.md);
  [CAP-153: unions and intersections of named branches and parts](capabilities/CAP-153.md).
- Schema extension (`store.extend`): the members, properties and adjacencies, that a transaction adds to the schemas
  that a store holds, meta-schemas included. A schema extension adds members, and it never changes or removes one. A
  module that extends the framework's schemas in its install, such as `Parametrics`, is an extending module, as the
  user decided: "A module that uses schema extension is an "extending module" not an "extension"." *Never*:
  "extension" for the module.
  [FEA-031: schemas as extensible data](features/FEA-031.md);
  [CAP-116: framework schemas extended, checked](capabilities/CAP-116.md),
  [CAP-171: parameters attached to every schema kind by extension](capabilities/CAP-171.md).
- Level (data, schema, plain schema of schemas, meta-schema):
  [Store overhaul, Levels](https://github.com/pitaman71/mbse-schemas/blob/main/docs/proposals/store-overhaul/README.md#levels). A *plain schema of schemas*
  (`Schemas.OfObject`, level 2) is what a schema extension extends; a *meta-schema* (level 3) is static code describing it.
- Module: [CAP-109: schemas as linked objects in modules](capabilities/CAP-109.md)
- Planned in the [Store overhaul](https://github.com/pitaman71/mbse-schemas/blob/main/docs/proposals/store-overhaul/README.md): object identity, `OfIdentity`, `as_instance` (step 4, [FEA-026: deterministic object identity](features/FEA-026.md));
  `Parameters.Bind` and `Parameters.Apply` ([CAP-114: parameter bindings are substituted and checked](capabilities/CAP-114.md)).
- Singleton (an object schema's `.singleton(name)`): a reference object identified by its global name. A store's data
  is what its singletons reach, and every schema object is reached from the root module, the singleton `"."`.
  [FEA-026: deterministic object identity](features/FEA-026.md);
  [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md),
  [CAP-161: isolated stores, with no global registry](capabilities/CAP-161.md).
- Owned object: a reference object identified by its owner's reference and its key in its owning relation. It lives as
  long as its owning entry, and removing that entry deletes it and, in cascade, everything that it owns.
  [FEA-026: deterministic object identity](features/FEA-026.md);
  [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md),
  [CAP-119: owned objects found by path](capabilities/CAP-119.md),
  [CAP-121: owned objects deleted in cascade](capabilities/CAP-121.md).
- Counted object: a reference object that is neither a singleton nor owned. It has no identity beyond the document
  that writes it, nothing finds it except through what links it, and it lives while anything holds it. A counted object
  has no reference, and a frame carries none. Counted objects are deprecated, as the user decided ("counted objects are
  now deprecated"); this line is rewritten when the capabilities of
  [INI-082: eliminate counted objects](../proposals/PRIORITIES.md#ini-082--eliminate-counted-objects) land.
  [FEA-026: deterministic object identity](features/FEA-026.md);
  [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md),
  [CAP-133: no durable references to counted objects](capabilities/CAP-133.md).
- Reference (`References.OfObject`, `.OfEntry`, `.OfFrame`, `.OfParameter`): a value object that designates something
  without holding it. An object reference designates a singleton, an owned object or a schema object; an entry
  reference, a relation entry; a frame reference, a frame; and a parameter reference, a parameter, by its name. A
  transaction resolves an object reference through a symbol that is given it, and a parameter binding
  ([VOC-038: parameter binding](#VOC-038)) in the reference's scope resolves a parameter reference. Paths are retired as
  a term, and documents speak of object references alone, as the user decided, choosing "(b)" of the options offered.
  *Never*: "path", where an object reference is meant.
  [FEA-026: deterministic object identity](features/FEA-026.md);
  [CAP-130: references to objects, entries and frames](capabilities/CAP-130.md),
  [CAP-311: references stabilized](capabilities/README.md#CAP-311),
  [CAP-312: a parameter reference in place of anything with a schema](capabilities/CAP-312.md).
- Extent (`store.extent(name)`): a store's extent of a schema, the objects of that schema, or of a schema that refines
  it, that the store holds. A store client finds an extent, as the user decided, "by introspecting schemas. Then closing
  ownership relations" ([the stacked stores proposal](../proposals/STACKED-STORES.md#decided)). "Extent" means a
  store's extent alone. The bounds of a list's or a container's index are its index domain, as the user put it: "For
  index types I refer to them as "index domains"". *Never*: "extent" for the bounds of an index.
  [FEA-028: one Store interface, lazy by default](features/FEA-028.md);
  [CAP-286: an extent through ownership](capabilities/README.md#CAP-286).
- Store (`Builders.Store`, which implements `Visitors.OfStore`): the root object of a body of data, which holds its own
  schemas and its data, isolated from every other store, and which may be stacked on a store below. A store outlives
  every transaction on it, as the user decided: "the store survives indefinitely." Each store holds its own schemas,
  built when it is made or through `store.extend`; no schema object is shared across stores (schema extension 23 in
  [CAP-116: framework schemas extended, checked](capabilities/CAP-116.md#decided)). There is one store type,
  `Builders.Store`, which registers a named schema by building it; `Stores.Combined` is deprecated (since 0.16.0).
  [FEA-028: one Store interface, lazy by default](features/FEA-028.md);
  [CAP-161: isolated stores, with no global registry](capabilities/CAP-161.md),
  [CAP-283: a store given a store below](capabilities/README.md#CAP-283),
  [CAP-308: stacking by mutation transactions, in one round trip](capabilities/README.md#CAP-308).
- Transaction (`Mutations.OfTransaction`; its imperative scope, `with store.transaction()`): a unit of work on a store,
  which commits all of its writes or none. Every write to a store's data happens within a transaction, and so does
  every read that no follow delivers. A transaction is a chain of terms over a stream of frames. Transactions do not
  nest.
  [FEA-030: clean mutation-based transactional API](features/FEA-030.md);
  [CAP-124: writes all-or-nothing in transactions](capabilities/CAP-124.md),
  [CAP-125: imperative transaction scope](capabilities/CAP-125.md),
  [CAP-138: mutation expressions over frame streams](capabilities/CAP-138.md),
  [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md).
- Install (a module-scope `install(txn)`; `store.install(...)`): a transaction that upserts the schemas that a module
  defines, so that installing it again writes nothing. A document that stands at a seam qualifies the term where it
  could be read as a package manager's install.
  [FEA-032: schema loading and wire alignment](features/FEA-032.md);
  [CAP-115: schemas defined by idempotent installs](capabilities/CAP-115.md).
- Upsert (`Mutations.OfUpsert`): a transaction's term that finds the object that its pattern designates before it
  creates one, and then writes its spec wherever the spec does not hold. Every install is an upsert.
  [FEA-027: mutations as queries](features/FEA-027.md);
  [CAP-139: upserts find before they create](capabilities/CAP-139.md).
- Frame (`Transactions.Frame`; its reference, `References.OfFrame`): one result of a transaction, which holds a symbol
  binding ([VOC-037: symbol binding](#VOC-037)) for each of its symbols and the property values that the transaction
  assigned. As the user decided, "Frames hold symbol bindings and property assignments, not proxies", and a frame
  carries no counted object (agreed: "fine"). A frame carries the errors annotated on it.
  [FEA-027: mutations as queries](features/FEA-027.md);
  [CAP-138: mutation expressions over frame streams](capabilities/CAP-138.md),
  [CAP-130: references to objects, entries and frames](capabilities/CAP-130.md),
  [CAP-309: errors annotated on frames](capabilities/CAP-309.md),
  [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided).
- Document (`Plain.ToPlain(store).OfObject` and `.Reachable`): one transaction that writes a graph sent without its
  store, in which its counted objects are numbered and the owned objects and singletons it links are referred to by
  reference. Of data, "document" names this construct alone, as the user decided, choosing "(b)" of the options
  offered; a written text, such as this one, is a document in the ordinary sense.
  *Never*: "an object's document", which names the answer of `Stores.Below.document`, code that
  [CAP-308: stacking by mutation transactions, in one round trip](capabilities/README.md#CAP-308) removes. A document
  is neither a frame nor a snapshot.
  [FEA-030: clean mutation-based transactional API](features/FEA-030.md);
  [CAP-128: graphs sent as one-transaction documents](capabilities/CAP-128.md).
- Follow: a subscription through which a store delivers to a follower the changes of each transaction that it
  commits, in the order of their commits. As the user decided, "Follows is the one legitimate alternative to
  transactions for read-only access", and "A follower reads what the follow delivers, and Follower subscriptions are
  layer-coupled as well."
  [FEA-030: clean mutation-based transactional API](features/FEA-030.md);
  [CAP-270: a transaction's changes observed at its commit](capabilities/README.md#CAP-270),
  [CAP-285: writes through, others' writes in](capabilities/README.md#CAP-285),
  [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided).
- Proxy (`Proxies.OfX`): mbse-schemas' implementation of the visitor protocol ([VOC-035: visitor](#VOC-035)) with
  dynamic classes, so that a program uses a schema without generated code. A proxy's data instances visit read-only,
  and its builders are writable.
  [FEA-025: serialization behavior conventions in schema](features/FEA-025.md);
  [PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004),
  [PRI-010: proxies and generated code read alike](PRINCIPLES.md#PRI-010),
  [CAP-107: one visitor protocol reads and writes data](capabilities/CAP-107.md).
- Parameter (`OfParameter`): a name only, a symbol standing for a schema (since 0.17.0); terms, applications and
  widths are mbse-expressions'. Bound by `Parameters.Bind`, planned: a reference object recording the substitution,
  which any operation taking the function interprets, applying it lazily or through `Parameters.Apply`
  ([CAP-114: parameter bindings are substituted and checked](capabilities/CAP-114.md)).
- Constraint: [CAP-166: constraints attached where they constrain](capabilities/CAP-166.md#open-questions). `requires` left mbse-schemas in 0.17.0, for
  mbse-patterns (schema extension 5 to 7 in [FEA-024: expressions as data](features/FEA-024.md#decided)), superseded there on 2026-11-05: a
  pattern's `requires` stays with mbse-schemas' `OfPattern`, evaluated by its executor.

### mbse-expressions

- Expression (`Expressions.Framework.Expression`), term (`Expressions.Framework.Term`: `literal`, `call`, `variable`,
  `let`, Basic's `quantifier`): [Terms and the core vocabulary](capabilities/CAP-095.md#terms-and-the-core-vocabulary)
- Dialect (`Terms.Dialect`), the construct that implements [VOC-033: dialect](#VOC-033): [The
  framework](capabilities/CAP-098.md#the-framework), [Dialects](capabilities/CAP-100.md#dialects)
- Translator: [Translators](capabilities/CAP-101.md#translators)
- Value domain: [Value domains](capabilities/CAP-097.md#value-domains)

### mbse-patterns

These name mbse-patterns 0.9.1. From 0.10.0 it keeps distributions, sampling, generators and characterizers, and its
predicates give way to mbse-schemas' `OfPattern` ([FEA-023: patterns over data](features/FEA-023.md)).

- Predicate (`OfPredicate`), symbol, match: [Predicates](capabilities/CAP-150.md#predicates)
- `Exists`, `Forall`, `Contains`: [The predicate algebra](capabilities/CAP-152.md#the-predicate-algebra)
- Application of a predicate: [Parameters and application](capabilities/CAP-150.md#parameters-and-application)
- Pattern, `Choices`, distributions of values: [Distributions](capabilities/CAP-072.md#distributions)

### mbse-programs

- Syntax node, kind, category: [Trees](capabilities/CAP-084.md#trees)
- Standard: [Standards](capabilities/CAP-085.md#standards)
- Language, entity, scope, program, transpiler, bridge: [Layers](capabilities/CAP-084.md#layers)

### mbse-transforms

- Transform, session, policy, trace: [The model](capabilities/CAP-074.md#the-model),
  [Data](capabilities/CAP-074.md#data), as built in its precursor, mbse-patterns 0.9.1's `Transforms`

### mbse-codegen-python

- The transforms of type generation (`Dataclass`, `Union`, `Alias`, ...), drop (`Codegen.Dropped`):
  [Transforms](capabilities/CAP-027.md#transforms)

## Earlier IDs

V-001 to V-026 are [VOC-001: specification](#VOC-001) to [VOC-026: schema](#VOC-026), the same numbers.

## Open items

The question below is one that the terms and the constructs of mbse-schemas' data model and store leave to the user.
The text above is written as the documents best support it until the user decides.

- **Reference.** "Reference" names a value of a `References` schema (Reference, under [mbse-schemas](#mbse-schemas)),
  which may be an object, entry, frame or parameter reference. It is also part of the name of a reference object
  (Reference object, under [mbse-schemas](#mbse-schemas)), which is an object rather than a reference, and it names a
  concrete or symbolic reference in code ([PRI-015: concrete references are programmatic](PRINCIPLES.md#PRI-015)). A
  parameter reference ([CAP-312: a parameter reference in place of anything with a schema](capabilities/CAP-312.md)) is
  resolved by a parameter binding ([VOC-038: parameter binding](#VOC-038)) in its scope, not by a store, unlike an
  object reference. The options are: (a) "reference" means a `References` value, always qualified by what it
  designates ("object reference", "parameter reference"), with "reference object" kept; (b) "reference object" renamed,
  so that "reference" names a `References` value alone; (c) a parameter reference given a name of its own, since
  nothing in a store resolves it.

---

<!-- nav -->
[← The mbse basis](README.md) · [Home](../README.md)
