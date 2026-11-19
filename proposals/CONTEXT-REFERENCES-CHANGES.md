# Context + References + Changes cleanup

Initiative: [INI-014: context + references + changes cleanup](PRIORITIES.md#ini-014--context--references--changes-cleanup).
Related: [INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework), whose [parametrics](PARAMETRICS.md) the
contexts here serve.

The user wrote the sections below, from "Context as an MBSE data structure" to "Opens"; the sections after them record
the decisions taken on this proposal, what stacked stores need a frame to carry, and the questions still open.

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
hold the context used during procedures like validation,
traversal, transformation, interpretation, etc.

References.Frame is currently implemented as a bespoke class, contrary
to [PRI-018: no model needs code to read or write](../docs/PRINCIPLES.md#PRI-018).

```
VAL References.OfSchema
PROP References.OfSchema.object : References.OfObject
VAL References.OfObject (existing props here)
VAL References.OfEntry.links : Container[name, object]
VAL References.OfEntry.properties : Container[name, value]
VAL References.OfValue
VAL References.OfParameter
PROP References.OfParameter.value
```

## Frames as an MBSE data structure

Make Frames a first-class construct in value schemas with a clean 
stable seam with References.

## Changes as an MBSE data structure

## Opens

O-01. Does this proposal unintentionally displace boundary
between mbse-schemas and mbse-expressions  and mbse-programs?

O-02 Why was Frame formerly implementing Visitors.OfPattern?
Is there still a need and what is a proper representation?

## Decided

- **Frames take CAP-318's form**: "I prefer the CAP-318 form for frames." A frame carries symbol bindings, property
  assignments relative to a symbol binding, and relation entries relative to at least one symbol binding and to object
  references not otherwise bound to a symbol ([CAP-318: support for decoupled code](../docs/capabilities/README.md#CAP-318)).
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

## What a frame must carry

A frame given back by a transaction, or streamed by a layer of a stack, carries more than its bindings. As stacked
stores build it ([the stacked stores proposal](STACKED-STORES.md#a-cache-layer-and-the-layer-below)), a frame carries:

- its symbol bindings, each object by its reference;
- `assigns`, the values the transaction left in the properties its terms' specs name for a symbol;
- its errors, each a subterm, a kind and a message ([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309));
- `scope`, the id of the input frame or branch it descends from;
- `remainder`, where in the expression it halted, or none where it is complete;
- `journal`, the changes made in interpreting its input frame, a one-transaction `Changes.Journal` over the frame's own
  symbols.

A layer's stream also carries completion markers, `{"end": scope}`, which may carry a journal. Frames made schema data
must express every one of these, and the markers too, because a layer below that is another process, as mbse-rest's
and mbse-dynamodb's layers are, receives frames as they are written. The stacked stores' work holds those layers until
frames are schema data.

[CAP-318: support for decoupled code](../docs/capabilities/README.md#CAP-318), the user's capability, asks the same of frames that survive their
transaction: "Frames will need to be able to carry symbol bindings, property assignments (relative to a symbol binding),
and relation entries (relative to at least one symbol binding and object references not otherwise bound to a symbol)."
Its proposal, [mbse-schemas' decoupled code proposal](https://github.com/pitaman71/mbse-schemas/pull/59) (open), proposes that a frame carry its state as
a one-transaction `Changes.Journal`, replacing `References.OfFrame`'s `assigns` and `entries`.

The corpora of mbse-programs are frames written as `References.OfFrame` values, so that they are regenerated when
frames become schema data.

## Open questions

- **References' introduction.** The References section's first sentence repeats the Contexts section's: References
  "will create proper MBSE schemas that hold the context used during procedures". Is it meant to say what references
  hold?
- **The bespoke class.** The References section says "References.Frame is currently implemented as a bespoke class".
  The bespoke class is `Transactions.Frame`; `References.OfFrame` is schema data already, a frame's reference
  ([CAP-130: references to objects, entries and frames](../docs/capabilities/CAP-130.md)). Which is meant?
- **A parameter reference's value.** The draft gives `References.OfParameter` a `value`. A parameter reference holds its
  parameter's name and nothing else, as the user decided ([the parametrics proposal](PARAMETRICS.md#decided)), and a
  context's `Contexts.OfParameter` gives the parameter its value. Is `OfParameter.value` meant, and what does it hold?
- **A frame's form and its journal.** A frame in CAP-318's form, and a frame's `journal`, are each written as a
  `Changes.Transaction`. Is the frame's form its journal, as the decoupled code proposal's `state` would make it, or
  are the two kept apart: what the frame binds and witnesses, and what interpreting it changed? The Changes section is
  empty so far.
