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

- **`OfSchema[Schemas.OfObject]`.** What does a reference type with a schema argument mean in mbse-schemas, which has no
  parametric schemas: a constraint on the kind of schema referenced, which validation checks, or schemas that take
  arguments?
- **Binding and assignment.** The vocabulary says a parameter is assigned a value and bound to an object
  ([VOC-040: parameter assignment](../docs/VOCABULARY.md#VOC-040)). In the draft, a variable's and a parameter's `Binding` hold a value. Is "binding" the general word within a
  frame, or does a value need an assignment of its own?
- **A binding's name.** The draft gives a frame a property `Binding`. Is it a container of bindings keyed by name, as a
  frame maps names today?
- **Errors.** `Transactions.Frame` carries the errors annotated on it
  ([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309)). Does a symbols frame, or a context, hold them?
- **What else a frame need not or must implement.** The draft says that a frame does not have to implement
  `Visitors.OfPattern`, and leaves a sentence unfinished after it: "There should be".
