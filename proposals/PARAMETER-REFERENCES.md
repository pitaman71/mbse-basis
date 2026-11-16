# Parameter references, and references as first-class values

Initiative: [INI-010: schemas framework](PRIORITIES.md#ini-010--schemas-framework).

A parameter reference is a value object that stands in a model's data in place of anything that has a schema. Its
binding, in an enclosing scope, gives what it stands for. This proposal makes mbse-schemas' `References` module the
one seam through which any reference stands in place of a value: a parameter reference, which a binding resolves, and
an object reference, which a store resolves. With that one seam, a parameter reaches every dialect, kind and property
without any of them opting in. The same seam serves the stacked stores, whose objects not yet loaded are references
too ([the stacked stores proposal](STACKED-STORES.md)).

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
- **A parameter is a named reference**: the user chose that a parameter, in an expression, is written as a name, and
  that simplification takes a parameter's value from the scope first, and from the bindings stored in a model later.

## The design

### References, the one seam

mbse-schemas' `References` module defines the value objects that designate something: `References.OfObject` (an object,
by its path), `OfEntry`, `OfProperties` and `OfFrame`. This proposal adds `References.OfParameter`, a parameter by its
name. Every reference is a value object, so a store holds it, compares it and writes it as it does any value.

### One rule: a reference in place of any value

Wherever a value of a schema S is expected, a reference may stand in its place. The reference is valid where it
resolves to something of S, and it is invalid where it resolves to something else. The rule is one predicate, which
every place that checks a value against its schema calls. In mbse-schemas those places are, in each language: the
proxies' check that a written value is of its declared schema, together with the write paths of scalars and
containers; the proxies' check of what a link accepts, where a reference already stands in for an object; validation
of a value; validation of an entry; and the plain form's encoder and decoder. Links already accept a reference to an
object; the rule extends the same acceptance to every value.

### Resolution never loads

A parameter reference resolves through a binding in an enclosing scope. In mbse-schemas the enclosing scope is the
definition that declares the parameter (`Parametrics.HasParameters`) and binds it (`Parametrics.BindsValue`,
`Parametrics.BindsObject`). In mbse-expressions' simplification, the enclosing scope is also the scope that the caller
gives. An object reference resolves through a store, against what the store holds or what a transaction brought back.
Resolution never fetches from a store below on its own, because a transaction goes down a stack of stores whole and
comes back up in one round trip. That resolution is added beside the existing one, which loads an object from a store
below when a link to it is read; the existing resolution stays as it is until the stacked stores' revised design
replaces it, because mbse-schemas' store-below cases (BLW-01 to BLW-20) and the suites of mbse-rest and mbse-dynamodb
depend on it. A resolution that finds nothing gives the schema that the reference implies, and the
caller decides what an unresolved reference means: validation reports it, and simplification leaves it in the
residual.

### Identity

An object reference's identity is its path, written in one canonical form, so that two equal paths give one identity
whatever the order of their keys. A link's key, and so the key of every relation entry, is built from that identity.

### The wire form

A reference is written in the plain form as any value object is. Where the schema that the reader expects at a node
already says that the node holds a reference, the reference is written bare. Where the reader could take the node for
a value of the expected schema, the reference carries a marker that names its schema. The plain form uses one written
form for references, in place of the forms it uses today (`{"reference": ...}` in effects, `{"ref": ...}` in documents'
specs, and `$ref` in the nested expression form). The written form keeps a reference to a schema object, whose path
starts at the singleton `"."`, apart from a reference to data, because the two resolve differently: a schema path
through the store's schemas, and a data path through its objects. Changing the written form changes the conformance
corpora of mbse-schemas and mbse-rest, which the same change regenerates in both languages.

### Simplification and code generation

In mbse-expressions, a parameter reference is a leaf of an expression. The simplifier substitutes the value of a bound
parameter, and it leaves an unbound one in the residual, where an ancestor may still fold it away (`false && p`). Code
generators write a parameter as the target language's own construct: a C++ template parameter, a C macro, a
SystemVerilog `parameter`, or a Python generic.

## Capabilities

Each capability is one increment of [FEA-033: model parameters](../docs/features/FEA-033.md) or of
[FEA-028: one Store interface, lazy by default](../docs/features/FEA-028.md), in the order of work:

1. [CAP-311: references stabilized](../docs/capabilities/README.md#CAP-311), in mbse-schemas: `References.OfParameter`;
   an object reference's canonical identity; a resolution that never loads, and a public function for the schema a
   reference implies; and one wire form for references. It changes no behavior that a caller sees but the written
   form of a reference, and it lands first, so that the stacked stores' work continues on a stable `References`.
2. [CAP-312: a reference in place of any value](../docs/capabilities/README.md#CAP-312), in mbse-schemas: the one rule,
   in each place that checks a value against its schema, in both languages.
3. [CAP-313: parameter references bound and validated](../docs/capabilities/README.md#CAP-313), in mbse-schemas: a
   parameter reference is valid where an enclosing definition binds it to a value of the right schema, and invalid
   otherwise. It supersedes [CAP-181: parameters wherever literals may appear](../docs/capabilities/CAP-181.md), which
   asked for the same of literals alone.
4. [CAP-296: simplification over literals, variables and parameters](../docs/capabilities/README.md#CAP-296) and
   [CAP-298: simplification over type parameters](../docs/capabilities/README.md#CAP-298), in mbse-expressions: the
   simplifier's rule for a parameter reference, and the scope's bindings.
5. [CAP-163: parameters bound, applied and generated beyond mbse-schemas](../docs/capabilities/CAP-163.md), in the
   code generators and mbse-programs.

## Open questions

- **The marker.** Which marker names a reference's schema where the reader could not tell it from a value. The plain
  form marks a refinement of a value object with `$schema`, and a reserved key, such as `$schema` naming
  `References.OfParameter`, would serve. The choice is the user's.
- **The stacked stores' placeholder.** Whether mbse-schemas' private placeholder for an object of the store below
  (`Proxies._Unresolved`) becomes a `References.OfObject`. The stacked stores' design is under revision, so this
  question waits for it.
- **A parameter reference's fields.** Whether a parameter reference holds its parameter's name alone, or also the path
  of the definition that declares the parameter.
