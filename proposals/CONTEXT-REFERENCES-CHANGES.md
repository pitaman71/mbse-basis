# Context + References + Changes cleanup

Initiative: [INI-014: context + references + changes cleanup](PRIORITIES.md#ini-014--context--references--changes-cleanup).
Related: [INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework), whose [parametrics](PARAMETRICS.md) the
contexts here serve.

The user wrote the sections below, from "Context as an MBSE data structure" to "Opens"; the sections after them list
the bespoke data structures this proposal replaces and record the decisions taken on it.

## Context as an MBSE data structure

`mbse-schemas.Contexts` will create proper MBSE schemas that
hold the context used during procedures like validation,
traversal, transformation, interpretation, etc.

```
VAL Contexts.OfVariable
PROP Contexts.OfVariable.name
PROP Contexts.OfVariable.schema: References.OfSchema[Schemas.OfAny]
PROP Contexts.OfVariable.value : References.OfValue

VAL Contexts.OfSymbol
PROP Contexts.OfSymbol.name
PROP Contexts.OfSymbol.schema: References.OfSchema[Schemas.OfObject]
PROP Contexts.OfSymbol.object : References.OfObject

VAL Contexts.OfParameter
PROP Contexts.OfParameter.name
PROP Contexts.OfParameter.schema : References.OfSchema
PROP Contexts.OfParameter.object : References.OfObject
PROP Contexts.OfParameter.value : References.OfValue
```

## References as an MBSE data structure

`mbse-schemas.References` will create proper MBSE schemas that
designate what data refers to: objects, schemas, relation entries,
values and parameters, each a value that outlives the transaction
that made it.

```
VAL References.OfSchema
PROP References.OfSchema.object : References.OfObject
VAL References.OfObject (existing props here)
VAL References.OfEntry.links : Container[name, object]
VAL References.OfEntry.properties : Container[name, value]
VAL References.OfValue
VAL References.OfParameter
PROP References.OfParameter.name
```

## Changes as an MBSE data structure

## Opens

O-01. Does this proposal unintentionally displace boundary
between mbse-schemas and mbse-expressions  and mbse-programs?

O-02 Why was Frame formerly implementing Visitors.OfPattern?
Is there still a need and what is a proper representation?

## Targets

The bespoke data structures in the three modules, Contexts, References and Changes, that MBSE schemas are to replace.
`Transactions` is not among them, as the user decided: "I am trying to hunt down and eliminate bespoke data structures
in favor of MBSE schemas in three specific modules. `Transactions` does not need to be included."

- **Contexts.** The module does not exist yet. Validation takes its context as a plain mapping (`Mapping[str, Any]` in
  Python, `ReadonlyMap<string, unknown>` in TypeScript) ([CAP-313: parameter references valid where their parameters are assigned or bound](../docs/capabilities/CAP-313.md)).
  `Contexts.OfVariable`, `OfSymbol` and `OfParameter` replace it. mbse-expressions' simplifier scope,
  `Symbolics.Variables`, is another such mapping, outside mbse-schemas.
- **References.** None. Every reference is schema data already: `References.OfObject`, `OfFrame`, `OfProperties`,
  `OfEntry`, `OfError` and `OfParameter`. `References.OfSchema` and `OfValue` are new schemas, not replacements.
- **Changes.** `_Gathered`, a Python dataclass and a TypeScript interface, holds what a transaction changed before it
  commits: its symbols, each a reference or a schema; its entries removed or inserted, as tuples of the holder symbol,
  the adjacency, the verb, the other links' symbols and the properties; and its properties changed, as tuples. It
  becomes a `Changes.Transaction` once the transaction commits, whose `Changes.Symbol`, `Changes.OfEntry` and
  `Changes.OfProperty` hold the same, so that the changes can be gathered as a `Changes.Transaction` directly. The
  module's `_At` classes (`_Symbols`, `_Links`, `_Object`, `_Adjacency`, `_EntryProperties`, `_Value`, `_Members`)
  hold no model data: they tell `Plain` the schema each part of a change is read by, so that they are code, not data
  structures.

## Decided

- **A frame is not a context**: "Contrary to what I said in the proposal today, a frame is not a context. But we do need
  contexts as a standardized argument for procedures (whether coupled or decoupled) and I'm not sure References covers
  it." A context is the argument that a procedure, coupled or decoupled, takes; a frame is what a transaction gives back.
- **A sub-context is copied** ("copied", the second of the options offered). Where a procedure meets a statement that
  assigns or binds names, it makes a new context that copies the outer context's assignments and bindings and adds or
  replaces the statement's own. Nothing links the new context to the outer one, so that every context is complete in
  itself, and is sent as a value with nothing to follow.
- **`References.OfSchema` is new**: "Reference.OfSchema is new and it is perfectly acceptable to implement it using
  OfObject as a base class or coding pattern with the '.' prefix convention formalized". A schema reference's path
  starts at the singleton `"."`, as a schema object's path does today; `OfSchema` makes that convention a schema of its
  own, which may refine `References.OfObject` or follow its pattern.
- **`References.OfValue` is data that holds a value of any schema** (agreed to the reading offered, "your reading is
  correct"). It is a data object, and `Schemas.OfAny` is the schema that admits a value of any schema: "References.OfValue
  is the data object whereas Schemas.OfAny is the schema".
- **A schema argument is a constraint, for now** ("the first is okay for now"). In `References.OfSchema[Schemas.OfObject]`,
  the bracket constrains the kind of schema that the reference may designate, here an object schema, and validation
  checks it. mbse-schemas has no schemas that take arguments, and the bracket adds none.
