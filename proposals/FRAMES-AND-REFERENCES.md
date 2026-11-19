# Frames + References cleanup

Initiative: [INI-014: frames + references cleanup](PRIORITIES.md#ini-014--frames--references-cleanup). Related:
[INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework), whose [parametrics](PARAMETRICS.md) the contexts
here serve.

A frame holds what a scope binds: its symbols' objects, its variables' values, and its parameters' values, objects and
schemas. mbse-schemas implements a frame as a bespoke class today (`Transactions.Frame`, a mapping with its errors),
contrary to [PRI-018: no model needs code to read or write](../docs/PRINCIPLES.md#PRI-018). This proposal makes frames first-class schema data, with a clean
and stable seam with `References`, as references were made first-class ([CAP-311: references stabilized](../docs/capabilities/README.md#CAP-311)). The
contexts that validation and simplification take are frames of this kind
([CAP-313: parameter references valid where their parameters are assigned or bound](../docs/capabilities/CAP-313.md),
[the parametrics proposal](PARAMETRICS.md)).

## The user's draft

The user wrote these schemas, in the user's notation (`OBJ` an object schema, `PROP` a property):

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

- **A sub-context is copied** ("copied", the second of the options offered). Where a procedure meets a statement that
  assigns or binds names, it makes a new frame that copies the outer frame's bindings and adds or replaces the
  statement's own. Nothing links the new frame to the outer one, so that every frame is complete in itself, and is sent
  as a value with nothing to follow.
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

- **Three kinds of frame, and a context of them.** A variables frame gives each variable a value of a schema. A symbols
  frame gives each symbol an object of an object schema. A parameters frame gives each parameter a value, an object or
  a schema; a parameter given a schema is a type parameter
  ([CAP-298: simplification over type parameters](../docs/capabilities/README.md#CAP-298)). A context holds one frame of each kind.
- **Frames are value objects.** `OBJ`, not a reference object: a frame has no identity of its own in a store. It is
  written, read and compared as any value is, and a transaction gives frames back as values, holding references and
  values, not proxies ([CAP-315: every read within a transaction or through a follow](../docs/capabilities/CAP-315.md#decided)).
- **The seam with `References`.** Each binding holds references only: a schema by `References.OfSchema`, an object by
  `References.OfObject`, and a value by `References.OfValue`.
- **Who uses a context.** Validation takes a context as its argument
  ([CAP-313: parameter references valid where their parameters are assigned or bound](../docs/capabilities/CAP-313.md#decided)). A dialect's simplifier takes one as its scope, and makes a sub-context where it
  meets one of the dialect's own statements that assign or bind a name. A transaction gives back symbols frames.

## Open questions

- **A symbol binding's path.** The updated schema writes a symbol binding's properties as `Symbols.Binding.binding.name`,
  with a `binding` step that a variable assignment's and a parameter binding's properties lack. Is the step meant?
- **Frames and contexts.** The updated schema gives the assignments and bindings, not the frames. Do
  `Variables.Frame`, `Symbols.Frame`, `Parameters.Frame` and `Contexts.Frame` remain, each holding its kind's
  assignments or bindings?
- **A parameter assigned a value.** The vocabulary says a parameter is assigned a value and bound to an object
  ([VOC-040: parameter assignment](../docs/VOCABULARY.md#VOC-040)). `Parameters.Binding` holds a `value`. Is a parameter given a value through a binding, or through an
  assignment of its own, as a variable is?
- **The journal and the bindings.** A frame's `journal`, and the decoupled code proposal's `state`, are each a
  one-transaction `Changes.Journal` over the frame's symbols, which holds symbol bindings, property assignments and
  relation entries as changes. Are a frame's bindings and assignments this proposal's value objects, its journal's
  changes, or both, and where does a relation entry relative to a symbol go?
- **Errors.** `Transactions.Frame` carries the errors annotated on it
  ([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309)). Does a symbols frame, or a context, hold them?
- **What else a frame need not or must implement.** The draft says that a frame does not have to implement
  `Visitors.OfPattern`, and leaves a sentence unfinished after it: "There should be".
