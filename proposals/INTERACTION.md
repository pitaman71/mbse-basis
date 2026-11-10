# Interaction

Initiative: [INI-040: diagrams framework](PRIORITIES.md#ini-040--diagrams-framework).

How a person edits a diagram that [the diagrams proposal](DIAGRAMS.md) lays out: the gestures, what each shows while it
is under way, and the one mutation it makes when it ends. Its capabilities:
[CAP-261: layout driven by any journal entry](../docs/capabilities/README.md#CAP-261), [CAP-243: a diagram displayed from its mutation stream](../docs/capabilities/README.md#CAP-243),
[CAP-262: a candidate mutation's layout previewed, never journalled](../docs/capabilities/README.md#CAP-262) and [CAP-263: touch-first gestures, each one mutation](../docs/capabilities/README.md#CAP-263).

## Decided

The user's decisions (2026-11-10):

- **Touch first, with CAD conventions for editing rules where needed**: "touch first augmented with CAD conventions
  for rule editing as needed". Structural edits (reordering, placing beside a sibling, moving into or out of a
  container) are direct manipulation, as on a touch screen; the rules behind the layout (adjacency specs, rotations)
  are shown and edited as a CAD tool shows and edits a sketch's constraints.
- **A drag shows its outcome while it is under way**: "Reordering for example can interactively shift siblings. Moving
  an object into or out of a container can visually highlight the destination, if necessary creating a "landing pad"
  that is a placeholder for the item still being dragged."
- **Gestures map onto a finite set of mutations, and the mapping is not trivial**: "Dragging an object might cause it
  to change position within the current container, or switch containers, or orientations relative to another sibling,
  etc."
- **A gesture inserts a mutation at the view's position in the journal**: "Gestures in this viewer cause mutations to
  be inserted at the current view position in the journal." Nothing is ever snapshotted: the model and its layouts
  are always stored, communicated and analyzed in journal form.
- **One shape at a time**, at first: a selection of several shapes is not dragged as one intent ("initially no").
- **CAP-243 split now** ("yes split now"): into the driver that takes any journal entry to the layout functions it
  implies (CAP-261), the renderer and its viewport (CAP-243), previews (CAP-262) and gestures (CAP-263).

## The journal is the timeline

The viewer shows the layout at a position in the journal, the engine's result for the mutations up to it. A gesture
inserts one mutation there; the mutations after it follow, through the same incremental engine, as any streamed
mutation does. So undo and redo are moves of the view's position, and editing the past is moving back and gesturing
there, as a parametric CAD tool's timeline is rolled back and a feature inserted.

## A drag

1. **Lift.** A press on a shape lifts it: the shape the finger holds becomes a ghost, drawn translucent, that follows
   the finger. The ghost is the view's alone: nothing is computed for it and nothing is mutated.
2. **Intent.** Where the finger is, and how long it stays, select one intent from a finite set, below. On a touch
   screen there is no hover, no modifier key and no Tab: an intent is chosen by drop zones large enough for a finger,
   with hysteresis so that it does not flicker at a zone's edge, and by dwell: resting over a container opens it, as a
   spring-loaded folder does, so that the shape can be dropped among its children. A label near the finger names the
   intent ("east of alu", "into io", "out to cpu").
3. **Preview.** The layout as the intent would leave it: siblings shift aside to open the slot; the destination
   container is highlighted; where the shape would land, a landing pad, a placeholder the dragged shape's size, takes
   its cell, and the container grows to hold it; where it came from, the gap closes.
4. **Drop or cancel.** Lifting the finger commits the intent: one mutation, inserted at the view's position. Dragging
   back to where the shape began, or off the diagram, cancels: nothing was mutated.

## Intents and their mutations

| Intent | Where the finger is | The mutation |
|---|---|---|
| Beside a sibling | an edge zone of a sibling | an adjacency spec to it, its rotation the side's, which a grid quantizes to a quarter turn |
| In a sibling's cell | the centre of a sibling | an adjacency spec that shares its cell |
| Back to its place | its own original slot | its specs removed, so that it reverts to its original insertion position |
| Reorder | between two siblings | open: below |
| Into, or out of, a container | a container's interior, after dwell; outside its container | open: below |
| Turned | a rotation handle | its vector's rotation, or its container's cell rotation |

## Previews, never journalled

A preview is the incremental engine's result for one candidate mutation, run and then undone; it is never written to
the journal. mbse-schemas holds a transaction's writes apart from the store until it commits, and drops them where it
is aborted, so the candidate and the container layout's adjustments to it run in a transaction that is aborted.
Physical placement holds its constraints outside the store, in its engine: each change of a candidate is undone
exactly, what it added removed and what it removed added again, and since every solution is unique, the engine returns
to the layout it had. A preview costs one incremental step and its undoing each time the intent changes, not each time
the finger moves.

## Editing rules, as CAD edits constraints

- Adjacency specs are drawn as glyphs between the shapes they relate, as a sketch's constraints are; a tap selects one,
  and deleting it removes the spec.
- An ignored rule is drawn in red, as an over-constrained sketch's are, and selecting it names the earlier rule it
  conflicts with.
- A shape's rotation, and a container's cell rotation, have handles.

## Open questions

1. **Reorder.** Whether dropping between siblings makes a new mutation that changes a child's insertion order, or an
   adjacency spec to the sibling it lands beside, and if a spec, to which sibling and by which side.
2. **Into or out of a container.** A child shape is owned, through `Logical.Owns`, by its container, and its path runs
   through it. Moving it to another container changes its owner, so its path, so its identity, and its points,
   vectors, specs and annotations go with the old one unless the mutation makes them again under the new. Whether
   containment and ownership should be separated, so that a move keeps a shape's identity, or a moved shape is a new
   object.
3. **Thresholds.** The sizes of the drop zones, the hysteresis, and how long a dwell opens a container.
