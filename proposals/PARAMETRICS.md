# Parametrics

Initiative: [INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework).

A model takes parameters ([FEA-033: model parameters](../docs/features/FEA-033.md)). This proposal states how a
parameter is declared, bound, referenced, validated, substituted, simplified and generated, from one end to the other.
Its central idea is the parameter reference: a value object that stands in a model's data in place of anything that has
a schema, and that a parameter binding in an enclosing scope resolves. mbse-schemas' `References` module is the one seam
through which any reference stands in place of a value, so that a parameter reaches every dialect, kind and property
without any of them opting in. The same seam serves the stacked stores, whose objects not yet loaded are references too
([the stacked stores proposal](STACKED-STORES.md)). The capabilities' detail files keep the decisions already taken
about parameters, and this proposal links them rather than restating them.

## Decided

The user decided these rules:

- **Parameters are universal**: "a parameter reference, as a value object, may appear in any data structure in place
  of anything that has a schema."
- **Validation**: "at validation time that parameter reference must be bound in an enclosing scope/context to the right
  kind of schema, or the reference is invalid."
- **Simplification**: "at simplification time a reference to an unbound parameter are left in the residual, allowing
  ancestors to potentially simplify that out if possible."
- **Code generation**: "at codegen time, parameters should be encoded in constructs idiomatic to the langauge (such as
  C++ `template`s, C `define`, SV `parameter` or `define`, Python generics, etc.)"
- **Capabilities quantify the feature**: "At the feature level support for parameter references anywhere is a work in
  progress quantified by capabilities that once fully fulfilled make it universal."
- **Simpler, not more complicated**: "I would also like us to exploit this ground-level design to make implementation
  much simpler rather than more complicated."
- **`References` as the point of entry**: "can we use Refeences.py/ts as a designated point of entry to avoid a broader
  overhaul? Perhaps we can minimize ripple effects to other repositories by ensuring referenes are first-class citizens
  of the framework."
- **The wire format**: "wire format should serialize a data reference with a schema reference if the schema is in any
  way ambiguous given the current data node and the schema expected by the parser at that node. If the schema can be
  unambiguously determined then the data reference needs not carry the schema reference with it." This is
  [PRI-025: never guess the schema](../docs/PRINCIPLES.md#PRI-025) and
  [PRI-026: serialization through the visitor protocol](../docs/PRINCIPLES.md#PRI-026), applied to references.
- **Stacked stores in parallel**: "We should plan the work to stabilize references so that the stacked stores work can
  resume in paralell asap."
- **Parameter bindings and symbol bindings**: "Parameter binding and symbol binding have different meanings and should
  be used as phrases, not just "binding"." A frame holds a symbol binding for each of its symbols, to an object or to a
  parameter, and it assigns values to variables; frames stay in mbse-schemas. An expression root that declares
  parameters may also hold parameter bindings for one or more of them; those parameter bindings go in mbse-expressions.
- **A schema declares, its data binds**: "Schemas may hold parameter declarations. Parameter bindings should be held by
  the data object governed by that schema."
- **Parameter bindings link the data object**: `Parametrics.BindsValue` and `BindsObject` link the data object that
  binds a parameter, not its schema, as the user decided.
- **A parameter is a named reference**: the user chose that a parameter, in an expression, is written as a name, and
  that simplification takes a parameter's value from the scope first, and from the parameter bindings stored in a model
  later. A parameter reference holds its parameter's name and nothing else.

The capabilities' detail files hold the user's earlier decisions about parameters, which this proposal builds on:
[CAP-112: parameters modeled as schema data](../docs/capabilities/CAP-112.md#decided) (a parameter is for a value or for
an object, exactly one; parameters are names only; parameters that denote domains belong to mbse-expressions),
[CAP-113: parameters bound at their definitions](../docs/capabilities/CAP-113.md#decided) (`BindsValue`'s `value` is
an entry property and `BindsObject`'s object a third link), and
[CAP-114: parameter bindings are substituted and checked](../docs/capabilities/CAP-114.md#decided) (a type parameter's
constraint starts at level 0, with level 2 planned).

## A parameter's life

### Declared

A definition, a schema of any kind, declares its parameters, as mbse-schemas' `Parametrics` module builds them
([CAP-112: parameters modeled as schema data](../docs/capabilities/CAP-112.md), met). A parameter is a
`Schemas.OfParameter`, with a name. It is for a value of one schema (`Parametrics.ForValue`) or for an object of one
object schema (`Parametrics.ForObject`), exactly one. A definition holds its parameters through
`Parametrics.HasParameters`, as one `Parametrics.OfParameters`.

### Bound

Parameter bindings exist in two repositories, and symbol bindings in one
([VOC-037: symbol binding](../docs/VOCABULARY.md#VOC-037), [VOC-038: parameter binding](../docs/VOCABULARY.md#VOC-038)).
In mbse-schemas, a data object may hold parameter bindings for the parameters that its schema declares, and a frame
holds a symbol binding for each of its symbols, to an object or to a parameter, and assigns values to its variables. In
mbse-expressions, an expression root that declares parameters may hold parameter bindings for one or more of them, and
an application holds parameter bindings for the parameters of the definition it applies, by name, and partially where it
binds some parameters alone. A parameter given no argument stays unbound. The scope in which a parameter reference is
resolved is the chain of data objects, frames, expression roots and applications that enclose the reference, innermost
first; a data object encloses its own values. In mbse-expressions' simplification, the scope that the caller gives is
also such a scope. A data object binds a parameter through `Parametrics.BindsValue`, its value an entry property, or
`Parametrics.BindsObject`, its object a third link, each linking the data object and the parameter. A data object's
parameter bindings are
[CAP-314: parameters bound by the data objects their schema governs](../docs/capabilities/README.md#CAP-314)'s.

### Referenced

A parameter reference, `References.OfParameter`, designates a parameter by its name, and holds nothing else. It is a value object, beside
mbse-schemas' other references: `References.OfObject`, `OfEntry`, `OfProperties` and `OfFrame`. One rule makes it
universal. Wherever a value of a schema S is expected, a reference may stand in its place, valid where it resolves to
something of S, and invalid where it resolves to something else. The rule is one predicate, which every place that
checks a value against its schema calls. In mbse-schemas those places are, in each language: the proxies' check that a
written value is of its declared schema, together with the write paths of scalars and containers; the proxies' check
of what a link accepts, where a reference already stands in for an object; validation of a value; validation of an
entry; and the plain form's encoder and decoder.

### Validated

A parameter reference is valid where an enclosing definition or application declares and binds its parameter, and binds
it to a value of the schema that the reference stands for. Validation reports an unbound parameter reference, and a
parameter reference bound to a value of another schema, as invalid. A parameter binding's value is checked against its
parameter's `ForValue` schema, or its object against its `ForObject` schema. Data whose schema depends on a parameter
that its scope leaves unbound is neither valid nor invalid there: validation reports it as unknown.

### Substituted

Applying a definition substitutes each of its parameter bindings for the parameter references that designate the bound
parameter ([CAP-114: parameter bindings are substituted and checked](../docs/capabilities/CAP-114.md)). Substitution
writes new data and changes none, as simplification does. An expression parameter, which CAP-114 leaves to be designed,
is a parameter reference in an expression's term, and substituting it is the same operation.

### Simplified

In mbse-expressions, a parameter reference is a leaf of an expression. The simplifier substitutes the value of a bound
parameter, and it leaves an unbound one in the residual, where an ancestor may still fold it away (`false && p`). A
type parameter is a parameter reference where a type is expected, and the simplifier substitutes it as it substitutes
any parameter ([CAP-296: simplification over literals, variables and parameters](../docs/capabilities/README.md#CAP-296),
[CAP-298: simplification over type parameters](../docs/capabilities/README.md#CAP-298)).

### Generated

A code generator writes a parameter as the target language's own construct: a C++ template parameter, a C macro, a
SystemVerilog `parameter`, or a Python generic. A parameter stays a parameter in generated code, and is not replaced by
a value before generating ([CAP-163: parameters bound, applied and generated beyond mbse-schemas](../docs/capabilities/CAP-163.md)).

## References as first-class values

### Identity

An object reference's identity is its path, written in one canonical form, so that two equal paths give one identity
whatever the order of their keys. A link's key, and so the key of every relation entry, is built from that identity.

### Resolution

A parameter reference resolves through a parameter binding in its scope. An object reference resolves within a
transaction, as every read does: a symbol given the reference binds what it designates
([CAP-315: every read within a transaction or through a follow](../docs/capabilities/CAP-315.md)). Each layer of a stack
resolves it with its own transaction interpreter, through hooks the layer provides, and no function resolves a reference
over the Store interface from outside a layer ([the stacked stores proposal](STACKED-STORES.md#decided)). A layer that
does not hold the object forwards the transaction down the stack whole, so that resolution never fetches one object at a
time; frames come back up the stack as `References.OfFrame`, each object by its reference. mbse-schemas' private
placeholder for an object of the store below, `Proxies._Unresolved`, therefore becomes a `References.OfObject`
([CAP-308: stacking by mutation transactions, in one round trip](../docs/capabilities/README.md#CAP-308)). A reference
that a transaction does not resolve has the schema that its path implies, which the interpreter's hooks give through the
layer's schemas alone, and the caller decides what an unresolved reference means: validation reports it, and
simplification leaves it in the residual.

### The wire form

A reference is written in the plain form as any value object is. Where the schema that the reader expects at a node
already says that the node holds a reference, the reference is written bare. Where the reader could take the node for
a value of the expected schema, the reference carries a reference to its schema, as the user's wire rule requires. The plain form uses one written
form for references, in place of the forms it uses today (`{"reference": ...}` in effects, `{"ref": ...}` in documents'
specs, and `$ref` in the nested expression form). The written form keeps a reference to a schema object, whose path
starts at the singleton `"."`, apart from a reference to data, because the two resolve differently: a schema path
through the store's schemas, and a data path through its objects. Changing the written form changes the conformance
corpora of mbse-schemas, mbse-rest, mbse-expressions and mbse-programs, the only data written in the forms it
replaces, which are regenerated ([CAP-316: one written form for references](../docs/capabilities/CAP-316.md)).

## Capabilities

Each capability is one increment of [FEA-033: model parameters](../docs/features/FEA-033.md) or of
[FEA-028: one Store interface, lazy by default](../docs/features/FEA-028.md), in the order of work:

1. [CAP-311: references stabilized](../docs/capabilities/README.md#CAP-311), in mbse-schemas: `References.OfParameter`
   and an object reference's canonical identity. It landed first, so that the stacked stores' work continues on a
   stable `References`.
2. [CAP-316: one written form for references](../docs/capabilities/README.md#CAP-316), in mbse-schemas: the plain form
   writes every reference in one form. It changes no behavior that a caller sees but the written form of a reference.
3. [CAP-312: a parameter reference in place of anything with a schema](../docs/capabilities/README.md#CAP-312), in mbse-schemas: the one rule,
   in each place that checks a value against its schema, in both languages.
4. [CAP-314: parameters bound by the data objects their schema governs](../docs/capabilities/README.md#CAP-314), in mbse-schemas: a data object may bind
   the parameters that its schema declares. It supersedes [CAP-113: parameters bound at their
   definitions](../docs/capabilities/CAP-113.md), which bound a parameter at its schema.
5. [CAP-313: parameter references bound and validated](../docs/capabilities/README.md#CAP-313), in mbse-schemas: a
   parameter reference is valid where its scope binds it to a value of the right schema, and invalid otherwise. It
   supersedes [CAP-181: parameters wherever literals may appear](../docs/capabilities/CAP-181.md), which asked for the
   same of literals alone.
6. [CAP-114: parameter bindings are substituted and checked](../docs/capabilities/CAP-114.md): applying a definition
   substitutes its parameter bindings, and checks each parameter binding against its parameter's schema.
7. [CAP-296: simplification over literals, variables and parameters](../docs/capabilities/README.md#CAP-296) and
   [CAP-298: simplification over type parameters](../docs/capabilities/README.md#CAP-298), in mbse-expressions: the
   simplifier's rule for a parameter reference, and the scope's parameter bindings. These two need only CAP-311 and
   CAP-312, because the caller's scope binds the parameters, so they may proceed beside steps 4 to 6.
8. [CAP-163: parameters bound, applied and generated beyond mbse-schemas](../docs/capabilities/CAP-163.md), in the
   code generators and mbse-programs.

## Open questions

- **Shapes bound to parameters.** How is a parameter bound into a constraint on the shape of a relation's key, to give a
  tensor's shape ([CAP-114: parameter bindings are substituted and
  checked](../docs/capabilities/CAP-114.md#open-questions))?
- **Equal applications.** Are two applications that substitute alike, such as `Matrix(n, n)` and `Square(n)`, equal
  ([CAP-163: parameters bound, applied and generated beyond
  mbse-schemas](../docs/capabilities/CAP-163.md#open-questions))?
