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
  user decided (2026-11-12): "I would refer to a child that is a statement as a "clause" and a child that is an
  expression term as a "subterm"", then "substatement" for the former.
- <a id="VOC-031"></a>**VOC-031: substatement** · adopted · **Substatement**: Expression and statement languages are
  part of what dialects ([VOC-033: dialect](#VOC-033)) model. A statement that is a child of a statement or a term (an
  `if` statement's branches, a loop's body, an arrow function's block), as ISO/IEC 14882 uses the word. As the user
  asked (2026-11-12): "Is "substatement" cleaner than "clause"".
- <a id="VOC-032"></a>**VOC-032: clause** · adopted · **Clause**: Expression and statement languages are part of what
  dialects ([VOC-033: dialect](#VOC-033)) model. A child that is a subterm ([VOC-030: subterm](#VOC-030)) or a
  substatement ([VOC-031: substatement](#VOC-031)), named by the property that holds it (`left`, `body`, `else`); not a
  helper (a value object that is neither, such as a declarator) nor a scalar property. As the user decided (2026-11-12):
  "Maybe "clause" can refer to the union of all children : substatements and subterms." Qualified where it meets an
  mbse-transforms policy's clauses, or a grammar's own `…Clause` syntax nodes.
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
  the list's extent.
- <a id="VOC-027"></a>**VOC-027: second-order invention** · adopted · **Second-order invention**: a thing that can be modeled and invented
  elsewhere, such as a neutral expression language or datatypes. The project avoids them ([QUA-003: no second-order inventions](QUALITIES.md#QUA-003)), save as [PRI-022: second-order inventions by approval](PRINCIPLES.md#PRI-022)
  permits.
- <a id="VOC-028"></a>**VOC-028: human and agent** · adopted · **Human** and **agent**: sibling categories of who reads, writes and
  operates. A **user** is one persona of humans, beside engineering personas. *Never*: "user" as a synonym for humans.
- <a id="VOC-029"></a>**VOC-029: fungible** · adopted · **Fungible**: readily changeable to adapt to new situations;
  flexible. The third sense in [Merriam-Webster](https://www.merriam-webster.com/dictionary/fungible), which the
  project adopts uniformly, as the user decided (2026-11-05). Its first two senses, interchangeable or replaceable by an
  equal part, are special cases of it.

VOC-006, VOC-010 to VOC-019 and VOC-021 became modeling constructs, listed below; VOC-020 and VOC-022 to VOC-024 were withdrawn.
Their IDs are not reused.

The terms below name the parts of mbse-schemas' data model and store, which every repository that keeps data in a store
uses. Each entry names mbse-schemas' own construct where one implements the term. The questions that these entries leave
open are listed under [Open items](#open-items), below.

### Objects and relations

- <a id="VOC-035"></a>**VOC-035: reference object** · proposed · **Reference object**: an object that stands on its own,
  has an identity where it is a singleton or owned, and is reached only through relations, never held by a property or a
  container. Its schema is a reference object schema, marked `.ref(True)` on mbse-schemas' `Schemas.OfObject` builder. A
  model makes a thing a reference object where several owners share it, where code navigates back from it, where it is
  part of a cycle, or where something refers to it by identity
  ([CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects)). A
  reference object is a singleton ([VOC-042: singleton](#VOC-042)), an owned object ([VOC-043: owned object](#VOC-043))
  or a counted object ([VOC-044: counted object](#VOC-044)), as its schema declares
  ([CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md)). A reference object is not a reference
  ([VOC-046: reference](#VOC-046)), though a reference may designate one.
- <a id="VOC-036"></a>**VOC-036: value object** · proposed · **Value object**: an object without identity, held by one
  owner's property, directly or in a container, copied by value, compared deeply and written nested in its owner. Its
  schema is an object schema not marked `.ref()`, and it has no adjacencies, since no entry links a value object
  ([CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects)). Union
  values, intersection values and references are value objects. A value object is not its visitor: as the user decided,
  "a value object and a visitor of that value object are not necessarily the same thing", so that the value outlives the
  transaction while the visitor that reads it does not
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).
- <a id="VOC-037"></a>**VOC-037: relation** · proposed · **Relation**: a schema, mbse-schemas' `Schemas.OfRelation`, of
  two or more named links and any number of properties, whose data is its entries ([VOC-038: entry](#VOC-038)). Each
  link is filled by a reference object, never by a value object, and values that belong to one owner are held in a
  container instead ([CAP-108: relations as scalable containers](capabilities/CAP-108.md)). A relation's `unique`
  clauses decide whether its entries are a set or a list, and what keys them from each end
  ([CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md)).
- <a id="VOC-038"></a>**VOC-038: entry** · proposed · **Entry**: a relation entry, one fact of a relation, which links
  one reference object by each of the relation's links and holds a value for each of its properties
  ([CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md)). An entry has
  no identity of its own. Its reference, `References.OfEntry`, designates it by its relation, its links and its
  properties, and entries compare by value
  ([CAP-130: references to objects, entries and frames](capabilities/CAP-130.md)). An ownership entry is an entry
  through an adjacency marked `owner()`, and it places the object it owns
  ([CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md)).
- <a id="VOC-039"></a>**VOC-039: adjacency** · proposed · **Adjacency**: an object schema's declaration, mbse-schemas'
  `Schemas.OfAdjacency`, that its objects fill one named link of a relation. An object reads and writes the entries that
  link it through its adjacency, by the adjacency's name (`card.phones`), and `Visitors.OfAdjacency` is its visitor
  ([CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md),
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md)). An adjacency marked `owner()` points back to
  the object's owner ([CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md)). An adjacency declared
  without a name lets an object fill the link with nothing held on the object
  ([CAP-205: anonymous adjacencies, a link filled without storage on the object](capabilities/CAP-205.md)).
- <a id="VOC-040"></a>**VOC-040: union** · proposed · **Union**: a schema, mbse-schemas' `Schemas.OfUnion`, of one or
  more named branches, each a schema of the same kind. A union value holds exactly one branch, by name, and writing one
  branch clears any other ([CAP-153: unions and intersections of named branches and parts](capabilities/CAP-153.md)). A
  union value is a value object. A document that stands at a seam qualifies the term where it could be read as a C or
  C++ `union` or as a union of classifiers
  ([CAP-034: schemas specialized by classifier intersection and union](capabilities/CAP-034.md)).
- <a id="VOC-041"></a>**VOC-041: schema extension** · proposed · **Schema extension**: the members, properties and
  adjacencies, that a transaction adds to a schema that the store was made holding, meta-schemas included. An extension
  may add members, but it may not change or remove any, and each store extends its own schemas
  ([CAP-116: framework schemas extended, checked](capabilities/CAP-116.md)). A module that extends the framework's
  schemas, such as `Parametrics`, does so in its install, run before use ([VOC-051: install](#VOC-051),
  [CAP-171: parameters attached to every schema kind by extension](capabilities/CAP-171.md)). A store that reads a
  snapshot made with an extension it lacks ignores, and lists, each member whose meaning needs that extension
  ([CAP-165: snapshots read by a store lacking their extensions](capabilities/CAP-165.md)).

### Identity and reference

- <a id="VOC-042"></a>**VOC-042: singleton** · proposed · **Singleton**: a reference object identified by its global
  name, which its schema declares by `.singleton(name)`. A singleton's path has no steps, and it is the root of every
  path to another reference object ([CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md)). A
  store's data is what its singletons reach
  ([CAP-161: isolated stores, with no global registry](capabilities/CAP-161.md)). The root module, the singleton `"."`,
  is where every schema object's path starts ([CAP-123: schema objects identified by path](capabilities/CAP-123.md)).
- <a id="VOC-043"></a>**VOC-043: owned object** · proposed · **Owned object**: a reference object identified by its
  path, the route from a singleton through the ownership entries that own it
  ([CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md),
  [CAP-119: owned objects found by path](capabilities/CAP-119.md)). An object is owned through an adjacency marked
  `owner()`, whose relation has two links, and an owned object lives as long as its owning entry. Its keys are generated
  from its owning relation's key patterns
  ([CAP-120: owned objects named and placed when built](capabilities/CAP-120.md)). Removing its owning entry deletes it,
  and in cascade everything it owns ([CAP-121: owned objects deleted in cascade](capabilities/CAP-121.md)).
- <a id="VOC-044"></a>**VOC-044: counted object** · proposed · **Counted object**: a reference object that is neither a
  singleton nor owned. It has no identity beyond the document that writes it, nothing finds it except through what links
  it, and it lives while anything holds it, as the host language decides
  ([CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md),
  [CAP-133: no durable references to counted objects](capabilities/CAP-133.md)). A counted object has no reference, and
  a frame refuses one ([CAP-130: references to objects, entries and frames](capabilities/CAP-130.md),
  [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md)). Counted objects are
  deprecated: as the user decided, "counted objects are now deprecated", and a reference object is to be a singleton or
  owned ([INI-082: eliminate counted objects](../proposals/PRIORITIES.md#ini-082--eliminate-counted-objects)).
- <a id="VOC-045"></a>**VOC-045: path** · proposed · **Path**: the identity of a singleton, an owned object or a schema
  object, written as a nested value object, mbse-schemas' `Paths.OfRoot`, never as a string. A path names the singleton
  it starts from, then each ownership entry it transits, by its adjacencies and its keys
  ([CAP-119: owned objects found by path](capabilities/CAP-119.md),
  [CAP-123: schema objects identified by path](capabilities/CAP-123.md)). A path is durable: as the user decided, "Paths
  on the other hand are durable"
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)). An object reference
  holds its object's path, in one canonical form ([CAP-311: references stabilized](capabilities/README.md#CAP-311)).
- <a id="VOC-046"></a>**VOC-046: reference** · proposed · **Reference**: a value object that designates something
  without holding it, written and read as any value is, of one of mbse-schemas' `References` schemas
  ([CAP-130: references to objects, entries and frames](capabilities/CAP-130.md),
  [CAP-311: references stabilized](capabilities/README.md#CAP-311)). An object reference, `References.OfObject`,
  designates a singleton, an owned object or a schema object by its path, and is written `{"path": P}`
  ([CAP-316: one written form for references](capabilities/CAP-316.md)). An entry reference, `References.OfEntry`,
  designates a relation entry, and a frame reference, `References.OfFrame`, a frame
  ([CAP-130: references to objects, entries and frames](capabilities/CAP-130.md)). A parameter reference,
  `References.OfParameter`, designates a parameter by its name
  ([CAP-312: a parameter reference in place of anything with a schema](capabilities/CAP-312.md)). A transaction resolves
  an object reference, through a symbol that is given it
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md)), and a binding in the
  reference's scope resolves a parameter reference
  ([the parametrics proposal](../proposals/PARAMETRICS.md#references-as-first-class-values)).
- <a id="VOC-047"></a>**VOC-047: extent** · proposed · **Extent**: a store's extent of a schema, the objects of that
  schema, or of a schema that refines it, that the store holds. mbse-schemas gives one by `store.extent(name)`, which is
  read within a transaction, as every read of a store's data is
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md)). As the user decided, a
  store client finds an extent "by introspecting schemas. Then closing ownership relations"
  ([CAP-286: an extent through ownership](capabilities/README.md#CAP-286),
  [the stacked stores proposal](../proposals/STACKED-STORES.md#decided)).

### Stores and transactions

- <a id="VOC-048"></a>**VOC-048: store** · proposed · **Store**: the root object of a body of data, through which code
  reaches schemas, builders and objects. A store holds its own schemas and its data, which is what its singletons reach,
  and it is isolated from every other store
  ([CAP-161: isolated stores, with no global registry](capabilities/CAP-161.md)). There is one Store interface, lazy by
  default, and a store may be stacked on a store below it
  ([FEA-028: one Store interface, lazy by default](features/FEA-028.md),
  [CAP-283: a store given a store below](capabilities/README.md#CAP-283),
  [CAP-308: stacking by mutation transactions, in one round trip](capabilities/README.md#CAP-308)). mbse-schemas' store
  is `Builders.Store`, which implements that interface, `Visitors.OfStore`
  ([CAP-149: data accessed through the store protocol](capabilities/CAP-149.md)). As the user decided, "the store
  survives indefinitely": a store outlives every transaction on it
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).
- <a id="VOC-049"></a>**VOC-049: transaction** · proposed · **Transaction**: a unit of work on a store, under an id the
  program gives, which commits all of its writes or none
  ([CAP-124: writes all-or-nothing in transactions](capabilities/CAP-124.md)). Every write to a store's data happens
  within a transaction, and so does every read that no follow delivers
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md)). A transaction is written as
  an expression, mbse-schemas' `Mutations.OfTransaction`, a chain of terms (map, upsert, update, reduce, partition),
  each of which consumes and produces a stream of frames
  ([CAP-138: mutation expressions over frame streams](capabilities/CAP-138.md)). A transaction's imperative scope, `with
  store.transaction()`, has no expression ([CAP-125: imperative transaction scope](capabilities/CAP-125.md)).
  Transactions do not nest.
- <a id="VOC-050"></a>**VOC-050: savepoint** · proposed · **Savepoint**: a write within an open transaction that commits
  or fails alone, all or nothing, without ending the transaction. A savepoint's writes become the transaction's writes
  when the savepoint commits. In mbse-schemas a savepoint is a set of proposals over the transaction's proposals
  (`Proposals.OfStore`), and a decoder that reads a document within an open transaction makes one
  ([CAP-128: graphs sent as one-transaction documents](capabilities/CAP-128.md),
  [CAP-124: writes all-or-nothing in transactions](capabilities/CAP-124.md)).
- <a id="VOC-051"></a>**VOC-051: install** · proposed · **Install**: a module-scope `install(txn)`, a transaction that
  upserts the schemas a module defines, so that installing it again writes nothing and installing more extends what it
  defined. The framework defines its own schemas by installs too
  ([CAP-115: schemas defined by idempotent installs](capabilities/CAP-115.md)). A store also runs an install given as
  plain data, by `store.install(...)`, which sends it to the store below first
  ([the stacked stores proposal](../proposals/STACKED-STORES.md#decided)). A document that stands at a seam qualifies
  the term where it could be read as a package manager's install.
- <a id="VOC-052"></a>**VOC-052: upsert** · proposed · **Upsert**: a transaction's term, mbse-schemas'
  `Mutations.OfUpsert`, that binds each of its symbols to the object its pattern's spec designates, finding the object
  before it creates one. An upsert creates an object only where it finds none, and then writes its spec wherever the
  spec does not hold ([CAP-139: upserts find before they create](capabilities/CAP-139.md),
  [CAP-138: mutation expressions over frame streams](capabilities/CAP-138.md)). An upsert finds an owned object by its
  owning entry and a schema object by its name ([CAP-139: upserts find before they create](capabilities/CAP-139.md)).
  Every install is an upsert.
- <a id="VOC-053"></a>**VOC-053: frame** · proposed · **Frame**: one result of a transaction's expression, which binds
  each symbol that its terms declare to one object, and each variable to a value. A transaction's terms consume and
  produce a stream of frames, and the transaction gives back the frames that its chain ends with
  ([CAP-138: mutation expressions over frame streams](capabilities/CAP-138.md)). A frame given back holds each object by
  its reference, not by a visitor: as the user decided, "Frames hold symbol bindings and property assignments, not
  proxies" ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).
  mbse-schemas' constructs are `Transactions.Frame`, which `store.transaction` gives back, and `References.OfFrame`, a
  frame's reference, which carries the frame to a client and up a stack of stores
  ([CAP-130: references to objects, entries and frames](capabilities/CAP-130.md),
  [CAP-308: stacking by mutation transactions, in one round trip](capabilities/README.md#CAP-308)). A frame carries the
  errors annotated on it ([CAP-309: errors annotated on frames](capabilities/CAP-309.md)), and it may witness the
  property values and relation entries it asserts
  ([CAP-131: frames witness values and entries](capabilities/CAP-131.md)).
- <a id="VOC-054"></a>**VOC-054: binding** · proposed · **Binding**: what associates a name with what it stands for. As
  the user decided, "bindings" names two different things
  ([the parametrics proposal](../proposals/PARAMETRICS.md#decided)). A frame binds each of its symbols to an object or
  to a parameter, and it assigns values to its variables ([VOC-053: frame](#VOC-053)). A data object binds parameters
  that its schema declares, through `Parametrics.BindsValue` and `Parametrics.BindsObject`
  ([CAP-314: parameters bound by the data objects their schema governs](capabilities/README.md#CAP-314)). In
  mbse-expressions, an expression root or an application binds the parameters of a definition
  ([CAP-163: parameters bound, applied and generated beyond mbse-schemas](capabilities/CAP-163.md)).
- <a id="VOC-055"></a>**VOC-055: journal** · proposed · **Journal**: a store's transactions, recorded as data in the
  order in which they were committed, from which the store's data is made again. As the user decided, a model is stored,
  communicated and analyzed in journal form ([the stacked stores proposal](../proposals/STACKED-STORES.md#decided),
  [FEA-056: fungible diagramming keeps agents and humans in the loop](features/FEA-056.md#decided)). In mbse-schemas, a
  journal is the list of transactions as they were submitted, replayed by executing each again
  ([CAP-129: journals replayed by execution](capabilities/CAP-129.md)). In mbse-journals, a journal entry is a
  transaction's effect, written in the journal language
  ([CAP-271: the journal language](capabilities/README.md#CAP-271)).
- <a id="VOC-056"></a>**VOC-056: snapshot** · proposed · **Snapshot**: a store's state written as two transactions, its
  schemas and then its data, which reading executes in order
  ([CAP-127: snapshots made of transactions](capabilities/CAP-127.md)). mbse-schemas writes one by
  `Plain.ToPlain(store).Snapshot()`. The framework is to make no snapshot except for checkpoints: as the user decided,
  "I'm really trying to avoid snapshotting at all in the framework - except for a rolling checkpoint/restore for
  reliability, possibly some for hot-scaling" ([the stacked stores proposal](../proposals/STACKED-STORES.md#decided)).
- <a id="VOC-057"></a>**VOC-057: follow** · proposed · **Follow**: a subscription through which a store gives a follower
  each transaction it commits, as that transaction's effect, in the order in which it commits them
  ([CAP-270: a transaction's changes observed at its commit](capabilities/README.md#CAP-270),
  [CAP-285: writes through, others' writes in](capabilities/README.md#CAP-285)). mbse-schemas' store gives one by
  `store.follow(follower)`. As the user decided, "Follows is the one legitimate alternative to transactions for
  read-only access", and "A follower reads what the follow delivers, and Follower subscriptions are layer-coupled as
  well" ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).

### Reading and writing

- <a id="VOC-058"></a>**VOC-058: visitor** · proposed · **Visitor**: an object through which code reads and writes a
  value of one kind, mbse-schemas' `Visitors.OfX`, the one protocol for kind X. An algorithm receives a visitor and
  pulls through it, and the visitor's mode decides whether a write takes effect
  ([PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004),
  [CAP-107: one visitor protocol reads and writes data](capabilities/CAP-107.md)). Serialization reads and writes
  through the visitor protocol ([PRI-026: serialization through the visitor protocol](PRINCIPLES.md#PRI-026)). A visitor
  of a store's data lives only within the transaction that made it: as the user decided, "any class that implements
  Visitor must be have a lifetime that is lexically scoped (such as `with store.transaction()`)"
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).
- <a id="VOC-059"></a>**VOC-059: proxy** · proposed · **Proxy**: mbse-schemas' dynamic implementation of the visitor
  protocol, `Proxies.OfX`, which lets a program use a schema without generated code. A proxy's data instance visits
  read-only, and its builder is writable ([PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004)). Within a
  transaction, a proxy is the visitor that wraps an object's durable copy: as the user decided, "_Proxy (the
  in-tranasaction visitor) can serve double as _Data (the durable, ideally more compact representation), but in the
  _Proxy case it needs to wrap the durable copy"
  ([CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)).
- <a id="VOC-060"></a>**VOC-060: builder** · proposed · **Builder**: a writable visitor that builds or changes a value
  in fluent syntax, one setter per property, finalized by `create`, `clone` or `update`, none of which validates
  ([PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004)). As the user decided, "The preferred form of models
  as data is fluent builder syntax" ([PRI-019: fluent builder syntax](PRINCIPLES.md#PRI-019)). mbse-schemas has data
  builders, `Proxies.OfX.Builder`, which `store.<Name>(...)` gives, and schema builders, `Schemas.OfX.Builder`, each a
  visitor of its kind's plain schema of schemas
  ([CAP-109: schemas as linked objects in modules](capabilities/CAP-109.md)).
- <a id="VOC-061"></a>**VOC-061: reader** · proposed · **Reader**: two constructs of mbse-schemas carry the name.
  `Readers.OfX` is the read-only view of a visitor protocol, a type that code which must not write takes, so that a type
  checker enforces it ([CAP-107: one visitor protocol reads and writes data](capabilities/CAP-107.md),
  [CAP-257: Python type checkers see an object's members as its schema types them](capabilities/CAP-257.md)). The reader
  of the wire format reads plain data, JSON or YAML into a store, `Plain.FromPlain`, tracking the schema that it expects
  as context ([PRI-026: serialization through the visitor protocol](PRINCIPLES.md#PRI-026),
  [CAP-158: values written as plain data, JSON and YAML](capabilities/CAP-158.md)).
- <a id="VOC-062"></a>**VOC-062: writer** · proposed · **Writer**: two constructs carry the name. In mbse-schemas, the
  writer of the wire format, `Plain.ToPlain`, writes a value as plain data, JSON or YAML, reading it through the visitor
  protocol ([PRI-026: serialization through the visitor protocol](PRINCIPLES.md#PRI-026),
  [CAP-158: values written as plain data, JSON and YAML](capabilities/CAP-158.md)). In mbse-expressions, a `Writer`
  writes an expression's terms through the builders, with methods, and evaluates nothing
  ([CAP-095: Basic terms as data](capabilities/CAP-095.md)).

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
- Value object, reference object, the constructs that implement [VOC-036: value object](#VOC-036) and
  [VOC-035: reference object](#VOC-035):
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects)
- Cardinality, `unique`: [CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md)
- Level (data, schema, plain schema of schemas, meta-schema):
  [Store overhaul, Levels](https://github.com/pitaman71/mbse-schemas/blob/main/docs/proposals/store-overhaul/README.md#levels). A *plain schema of schemas*
  (`Schemas.OfObject`, level 2) is what an extension extends; a *meta-schema* (level 3) is static code describing it.
- Module: [CAP-109: schemas as linked objects in modules](capabilities/CAP-109.md)
- Planned in the [Store overhaul](https://github.com/pitaman71/mbse-schemas/blob/main/docs/proposals/store-overhaul/README.md): object identity, `OfIdentity`, `as_instance` (step 4, [FEA-026: deterministic object identity](features/FEA-026.md));
  `Parameters.Bind` and `Parameters.Apply` ([CAP-114: parameter bindings are substituted and checked](capabilities/CAP-114.md)).
- Store, singleton, the constructs that implement [VOC-048: store](#VOC-048) and [VOC-042: singleton](#VOC-042):
  [CAP-161: isolated stores, with no global registry](capabilities/CAP-161.md).
  Each store holds its own schemas, built when it is made or through `store.extend`; no schema object is shared
  across stores (schema extension 23 in [CAP-116: framework schemas extended, checked](capabilities/CAP-116.md#decided)). There is one store type,
  `Builders.Store`, which registers a named schema by building it; `Stores.Combined` is deprecated (since 0.16.0).
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

Each item below is a question that the entries from [VOC-035: reference object](#VOC-035) to [VOC-062: writer](#VOC-062)
leave to the user. Each entry is written as the documents best support it until the user decides.

- **Terms or modeling constructs.** The preface above says that a modeling construct is only named here, with a link to
  its definition, while [VOC-035: reference object](#VOC-035) to [VOC-062: writer](#VOC-062) define mbse-schemas'
  constructs, as [VOC-033: dialect](#VOC-033) defines a dialect beside the construct `Terms.Dialect`. The options are:
  (a) keep the entries, each construct line under mbse-schemas linking its term, as the line for `Terms.Dialect` links
  [VOC-033: dialect](#VOC-033); (b) move the entries into the list of mbse-schemas' constructs, each a name and a link
  to the capability that defines it; (c) keep as terms only those that are not mbse-schemas' constructs, such as
  transaction, journal and binding.
- **Document, frame and snapshot.** The user has said that "document", as in "an object's document", is not canon, and
  that the canonical construct is the frame ([VOC-053: frame](#VOC-053)). "Document" names a built construct of
  mbse-schemas: [CAP-128: graphs sent as one-transaction documents](capabilities/CAP-128.md), which
  `Plain.ToPlain(store).OfObject` and `.Reachable` write, one transaction that holds an object and the counted objects
  it reaches. [CAP-108: relations as scalable containers](capabilities/CAP-108.md#value-objects-and-reference-objects)
  ("a document writes it once") and [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md) ("no
  identity beyond the document that writes it") use the word so, and so do [VOC-044: counted object](#VOC-044) and
  [VOC-050: savepoint](#VOC-050). "An object's document", the answer of `Stores.Below.document(path)`, is used in
  [the stacked stores proposal](../proposals/STACKED-STORES.md#decided-by-an-agent-for-review) (mbse-schemas 30,
  mbse-dynamodb 15, mbse-rest 19), in [CAP-304: a store below that answers later](capabilities/README.md#CAP-304) and
  [CAP-306: a public store-below interface](capabilities/README.md#CAP-306), both superseded by
  [CAP-308: stacking by mutation transactions, in one round trip](capabilities/README.md#CAP-308), and in
  [the journal storage proposal](../proposals/JOURNAL-STORAGE.md). A frame binds symbols to references, a document
  writes objects, and a snapshot ([VOC-056: snapshot](#VOC-056)) writes a whole store, so that the three are not
  synonyms. The options are: (a) no term for "document":
  [CAP-128: graphs sent as one-transaction documents](capabilities/CAP-128.md)'s construct is named anew, and "an
  object's document" gives way to the frames that a transaction streams back
  ([CAP-308: stacking by mutation transactions, in one round trip](capabilities/README.md#CAP-308)); (b) "document" kept
  for [CAP-128: graphs sent as one-transaction documents](capabilities/CAP-128.md)'s construct alone, with "an object's
  document" marked *Never*; (c) "document" adopted for any written form of objects, a snapshot among them.
- **Visitor and proxy.** [PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004) makes `Proxies.OfX` the
  implementation whose data instances and builders implement `Visitors.OfX`, and [VOC-059: proxy](#VOC-059) follows it.
  [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided) calls a proxy "the
  in-tranasaction visitor" that wraps the durable `_Data`, and says that frames hold no proxies, where its Design says
  that they hold no visitors. [CAP-284: objects loaded on demand](capabilities/README.md#CAP-284) calls an object of the
  store below not yet loaded "a proxy whose identity is kept by its reference", which
  [the parametrics proposal](../proposals/PARAMETRICS.md#references-as-first-class-values) turns into a
  `References.OfObject`. The options are: (a) "visitor" names the protocol and its role, and "proxy" names mbse-schemas'
  dynamic implementation, as drafted; (b) "proxy" names only the in-transaction wrapper of durable data, the `_Proxy`
  beside `_Data`; (c) "proxy" is not a term, and documents say "visitor" throughout.
- **Reader, writer and builder.** "Reader" names `Readers.OfX`, the read-only view of a visitor protocol, and also the
  wire format's reader, `Plain.FromPlain` ([PRI-026: serialization through the visitor protocol](PRINCIPLES.md#PRI-026),
  [CAP-069: wire format shorthand (scalars)](capabilities/CAP-069.md)). "Writer" names the wire format's writer,
  `Plain.ToPlain` ([PRI-026: serialization through the visitor protocol](PRINCIPLES.md#PRI-026),
  [CAP-108: relations as scalable containers](capabilities/CAP-108.md)), a stateful writer of snapshots
  ([CAP-164: subsequent snapshots sent as transactions](capabilities/CAP-164.md)), and mbse-expressions' `Writer`, which
  builds terms as a builder does ([CAP-095: Basic terms as data](capabilities/CAP-095.md)) and which
  [the principles' open items](PRINCIPLES.md#open-items) list as not yet following
  [PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004).
  [CAP-143: specs declarative, no read-modify-write](capabilities/CAP-143.md) proposes splitting `Visitor` into `Writer`
  and `Reader` classes. The options are: (a) both names kept, qualified by repository and construct, as drafted; (b)
  mbse-expressions' writers become builders, as [PRI-004: one visitor protocol per kind](PRINCIPLES.md#PRI-004)'s open
  item expects, so that "writer" means the wire format's alone; (c) the wire format's reader and writer are called
  decoder and encoder, as `Errors.DecodeError` already does
  ([CAP-159: error handling during deserialization is consistent across Python3 and Typescript5 bindings](capabilities/CAP-159.md)),
  so that "reader" means `Readers.OfX` alone.
- **Entry.** A bare "entry" means a relation entry in [VOC-038: entry](#VOC-038),
  [CAP-155: `unique` clauses on relation schemas govern relation cardinality](capabilities/CAP-155.md) and
  `References.OfEntry`. It also names a journal entry ([CAP-271: the journal language](capabilities/README.md#CAP-271)),
  a step of a path (`Paths.OfEntry`, [CAP-119: owned objects found by path](capabilities/CAP-119.md)), a container's
  entry-like elements ([CAP-108: relations as scalable containers](capabilities/CAP-108.md)), a callback's entry in a
  transaction's term list
  ([mbse-schemas' query guide](https://github.com/pitaman71/mbse-schemas/blob/main/skills/mbse-schemas/references/queries.md)),
  and an item's entry in an index ([the mbse basis](README.md#rules-for-writing-items)). The options are: (a) a bare
  "entry" means a relation entry, and every other use is qualified, as in "journal entry"; (b) "relation entry" is
  written in full everywhere; (c) the journal's entries, or the path's steps, are renamed.
- **Reference.** "Reference" names a value of a `References` schema ([VOC-046: reference](#VOC-046)), which may be an
  object, entry, frame or parameter reference. It is also part of the name of a reference object
  ([VOC-035: reference object](#VOC-035)), which is an object rather than a reference, and it names a concrete or
  symbolic reference in code ([PRI-015: concrete references are programmatic](PRINCIPLES.md#PRI-015)). A parameter
  reference ([CAP-312: a parameter reference in place of anything with a schema](capabilities/CAP-312.md)) is resolved
  by a binding in its scope, not by a store, unlike an object reference. The options are: (a) "reference" means a
  `References` value, always qualified by what it designates ("object reference", "parameter reference"), with
  "reference object" kept; (b) "reference object" renamed, so that "reference" names a `References` value alone; (c) a
  parameter reference given a name of its own, since nothing in a store resolves it.
- **Counted object, deprecated.**
  [INI-082: eliminate counted objects](../proposals/PRIORITIES.md#ini-082--eliminate-counted-objects) deprecates counted
  objects, while [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md),
  [CAP-133: no durable references to counted objects](capabilities/CAP-133.md) and
  [CAP-270: a transaction's changes observed at its commit](capabilities/README.md#CAP-270) still describe them as
  built, and [CAP-118: singletons, owned and counted objects](capabilities/CAP-118.md) still gives the counted mode to
  most objects other than singletons and definitions. The options are: (a) [VOC-044: counted object](#VOC-044) adopted
  now, and superseded when INI-082's capabilities land; (b) [VOC-044: counted object](#VOC-044) withdrawn, and the term
  marked deprecated in the entry for reference objects; (c) [VOC-044: counted object](#VOC-044) kept with *Never* for
  new models.
- **Binding and assignment.** As the user decided, "bindings" names two things ([VOC-054: binding](#VOC-054)): a frame
  binds symbols, and a data object, an expression root or an application binds parameters. A frame also assigns values
  to its variables ([the parametrics proposal](../proposals/PARAMETRICS.md#bound)), while
  [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided)'s "property
  assignments" and `Transactions.Frame.assigns` mean the property values that the transaction left on the objects its
  symbols bind. A frame's variables collide with [VOC-004: variable](#VOC-004), a variable that constraints bind. The
  options are: (a) one term, binding, qualified as "a frame's binding" or "a parameter binding", as drafted; (b) two
  terms, such as a frame "binding" its symbols and a data object "binding" its parameters under another name; (c) the
  frame's own vocabulary settled apart: its symbols bound, its variables valued, and its property assignments witnessed.
- **Journal: submitted or effects.** [CAP-129: journals replayed by execution](capabilities/CAP-129.md) defines a
  journal as the transactions as submitted, replayed by executing each again, while
  [CAP-271: the journal language](capabilities/README.md#CAP-271) defines a journal entry as a transaction's effect,
  applied idempotently. As the user decided, mutation-transaction streams and change journals "are not the same language
  - yet" ([CAP-271: the journal language](capabilities/README.md#CAP-271)). The options are: (a) "journal" means the
  record of effects, mbse-journals', and [CAP-129: journals replayed by execution](capabilities/CAP-129.md)'s list is
  named otherwise; (b) "journal" covers both, as drafted, until the two languages become one; (c)
  [CAP-129: journals replayed by execution](capabilities/CAP-129.md) is superseded by
  [CAP-271: the journal language](capabilities/README.md#CAP-271).
- **Extent.** [VOC-047: extent](#VOC-047) means a store's extent of a schema
  ([CAP-286: an extent through ownership](capabilities/README.md#CAP-286)). "Extent" also means the bounds of a list's
  or a container's index, in [VOC-025: shape constraint](#VOC-025) ("the list's extent"),
  [CAP-027: Python3 source generated from schemas](capabilities/CAP-027.md) and
  [CAP-107: one visitor protocol reads and writes data](capabilities/CAP-107.md). The options are: (a) "extent" means a
  store's extent of a schema alone, and the other sense is called a bound or a shape constraint
  ([VOC-025: shape constraint](#VOC-025)); (b) both senses are kept, each qualified.
- **Schema extension.** "Schema extension" names the construct ([VOC-041: schema extension](#VOC-041)), and also a
  series of decisions numbered in mbse-schemas' design ("schema extension 23" in
  [CAP-116: framework schemas extended, checked](capabilities/CAP-116.md#decided)), while "extension" also names a
  module installed to extend the framework, such as `Parametrics`. The options are: (a) the term as drafted, with the
  decision series cited by its document's name; (b) "extension" alone for the module, and "schema extension" for the
  members it adds.
- **Path and reference.** [CAP-132: paths retired for references](capabilities/CAP-132.md) plans to retire paths for
  references, while [CAP-311: references stabilized](capabilities/README.md#CAP-311) makes a path an object reference's
  identity and [CAP-315: every read within a transaction or through a follow](capabilities/CAP-315.md#decided) records
  that "Paths on the other hand are durable". The options are: (a) a path is kept as the identity that an object
  reference holds ([VOC-045: path](#VOC-045), as drafted), and
  [CAP-132: paths retired for references](capabilities/CAP-132.md) is restated or superseded; (b) paths are retired as a
  term, and documents speak of object references alone.

---

<!-- nav -->
[← The mbse basis](README.md) · [Home](../README.md)
