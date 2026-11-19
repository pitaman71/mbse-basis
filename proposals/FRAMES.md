# Frames

Initiative: [INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework).

A frame holds what a scope binds: its symbols' objects, its variables' values, and its parameters' values, objects and
schemas. mbse-schemas implements a frame as a bespoke class today (`Transactions.Frame`, a mapping with its errors),
against [CAP-282: no model needs bespoke schema-aware code to read or write](../docs/capabilities/README.md#CAP-282). This proposal makes frames first-class schema data, with a clean
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

- **Nesting.** A sub-context hides a name of the context around it. Does a frame, or a context, link the one it
  extends, or does a procedure make a new frame that copies the outer bindings with its own added?
- **`References.OfValue` and `References.OfSchema`.** Neither exists. Is `OfSchema` a schema object's reference, which
  an `OfObject` whose path starts at the singleton `"."` writes today? Is `OfValue` a value of any schema held as a
  reference, and what does it hold? What does `OfSchema[Schemas.OfObject]`, a reference type with a schema argument,
  mean in mbse-schemas, which has no parametric schemas?
- **Binding and assignment.** The vocabulary says a parameter is assigned a value and bound to an object
  ([VOC-040: parameter assignment](../docs/VOCABULARY.md#VOC-040)). In the draft, a variable's and a parameter's `Binding` hold a value. Is "binding" the general word within a
  frame, or does a value need an assignment of its own?
- **A binding's name.** The draft gives a frame a property `Binding`. Is it a container of bindings keyed by name, as a
  frame maps names today?
- **Errors.** `Transactions.Frame` carries the errors annotated on it
  ([CAP-309: errors annotated on frames](../docs/capabilities/README.md#CAP-309)). Does a symbols frame, or a context, hold them?
- **What else a frame need not or must implement.** The draft says that a frame does not have to implement
  `Visitors.OfPattern`, and leaves a sentence unfinished after it: "There should be".
