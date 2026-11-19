# Frames + References cleanup

Initiative: [INI-014: frames + references cleanup](PRIORITIES.md#ini-014--frames--references-cleanup). Related:
[INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework), whose [parametrics](PARAMETRICS.md) the contexts
here serve.

A frame is what a transaction gives back: its symbols' objects, the property values and relation entries it
witnesses, and what stacked stores carry with it. mbse-schemas implements a frame as a bespoke class today
(`Transactions.Frame`, a mapping with its errors), contrary to [PRI-018: no model needs code to read or write](../docs/PRINCIPLES.md#PRI-018). This proposal makes
frames first-class schema data, with a clean and stable seam with `References`, as references were made first-class
([CAP-311: references stabilized](../docs/capabilities/README.md#CAP-311)). It also makes contexts, a different thing, a standardized argument for procedures: the
names in effect where a procedure runs, as validation and simplification take them
([CAP-313: parameter references valid where their parameters are assigned or bound](../docs/capabilities/CAP-313.md),
[the parametrics proposal](PARAMETRICS.md)).

## The user's first draft

The user first wrote these schemas, in the user's notation (`OBJ` an object schema, `PROP` a property):

```text
OBJ Variables.Frame
PROP Variables.Frame.Binding
PROP Variables.Frame.Binding.schema: References.OfSchema[Schemas.OfAny]
PROP Variables.Frame.Binding.value : References.OfValue

OBJ Symbols.Frame
PROP Symbols.Frame.Binding
PROP Symbols.Frame.Binding.schema: References.OfSchema[Schemas.OfObject]
PROP Symbols.Frame.Binding.object : References.OfObject

OBJ Parameters.Frame
PROP Parameters.Frame.Binding
PROP Parameters.Frame.Binding.schema : References.OfSchema
PROP Parameters.Frame.Binding.object : References.OfObject
PROP Parameters.Frame.Binding.value : References.OfValue

OBJ Contexts.Frame
PROP Contexts.Frame.parameters : Parameters.Frame
PROP Contexts.Frame.symbols : Symbols.Frame
PROP Contexts.Frame.variables : Variables.Frame
```

And: "A Frame does not have to implement Visitors.OfPattern."

## The user's updated schema

The user then recommended these value objects (`VAL` a value object schema), in place of the draft's bindings:

```text
VAL Variables.Assignment
PROP Variables.Assignment.name
PROP Variables.Assignment.schema: References.OfSchema[Schemas.OfAny]
PROP Variables.Assignment.value : References.OfValue

VAL Symbols.Binding
PROP Symbols.Binding.binding.name
PROP Symbols.Binding.binding.schema: References.OfSchema[Schemas.OfObject]
PROP Symbols.Binding.binding.object : References.OfObject

VAL Parameters.Binding
PROP Parameters.Binding.name
PROP Parameters.Binding.schema : References.OfSchema
PROP Parameters.Binding.object : References.OfObject
PROP Parameters.Binding.value : References.OfValue
```

A variable is assigned a value, and a symbol is bound to an object. A parameter binding holds a value, an object or a
schema, so that one kind of entry serves a parameter of each kind.

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

## Design

- **Frames.** A frame is what a transaction gives back, or what a layer of a stack streams: a value object, with no
  identity of its own in a store, holding references and values, not visitors
  ([CAP-315: every read within a transaction or through a follow](../docs/capabilities/CAP-315.md#decided)). It takes CAP-318's form, which `Changes.Transaction` already writes: its
  symbols, each bound to an object by its reference (`Changes.Symbol`); its property assignments, each relative to a
  symbol (`Changes.OfProperty`); and its relation entries, each holder a symbol and each link a symbol or an object
  reference (`Changes.OfEntry`). It also carries what stacked stores need, below: its errors, `scope`, `remainder` and
  `journal`.
- **Contexts.** A context is the standardized argument of a procedure, coupled or decoupled: validation, a dialect's
  simplifier, comparison, and code that runs over frames. It holds the names in effect where the procedure runs: each
  variable's assignment, each symbol's binding and each parameter's binding, the updated schema's
  `Variables.Assignment`, `Symbols.Binding` and `Parameters.Binding`. A parameter given a schema is a type parameter
  ([CAP-298: simplification over type parameters](../docs/capabilities/README.md#CAP-298)). Validation takes one
  ([CAP-313: parameter references valid where their parameters are assigned or bound](../docs/capabilities/CAP-313.md#decided)), and a dialect's simplifier takes one as its scope.
- **The seam with `References`.** An assignment or a binding holds references only: a schema by `References.OfSchema`,
  an object by `References.OfObject`, and a value by `References.OfValue`.

## Open questions

- **A symbol binding's path.** The updated schema writes a symbol binding's properties as `Symbols.Binding.binding.name`,
  with a `binding` step that a variable assignment's and a parameter binding's properties lack. Is the step meant?
- **Where contexts live.** A context is not a reference, and `References` may not cover it. Is it a module of its own,
  such as `Contexts`, holding the context schema and its assignments and bindings, or does it belong elsewhere?
- **A parameter assigned a value.** The vocabulary says a parameter is assigned a value and bound to an object
  ([VOC-040: parameter assignment](../docs/VOCABULARY.md#VOC-040)). `Parameters.Binding` holds a `value`. Is a parameter given a value through a binding, or through an
  assignment of its own, as a variable is?
- **A frame's form and its journal.** A frame in CAP-318's form, and a frame's `journal`, are each written as a
  `Changes.Transaction`. Is the frame's form its journal, as the decoupled code proposal's `state` would make it, or
  are the two kept apart: what the frame binds and witnesses, and what interpreting it changed?
- **Errors.** `Transactions.Frame` carries the errors annotated on it
  ([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309)). Does a symbols frame, or a context, hold them?
- **What else a frame need not or must implement.** The draft says that a frame does not have to implement
  `Visitors.OfPattern`, and leaves a sentence unfinished after it: "There should be".
