# Interaction

Initiative: [INI-040: diagrams framework](PRIORITIES.md#ini-040--diagrams-framework).

How a person edits a diagram that [the diagrams proposal](DIAGRAMS.md) lays out: the gestures, what each shows while it
is under way, and the one mutation it makes when it ends. Its capabilities:
[CAP-264: containment separate from ownership](../docs/capabilities/README.md#CAP-264), [CAP-261: layout driven by any journal entry](../docs/capabilities/README.md#CAP-261), [CAP-243: a diagram displayed from its mutation stream](../docs/capabilities/README.md#CAP-243),
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
- **A reorder that splits an adjacency is an insertion; one that splits none is an adjacency**: "if the reordering
  splits any existing adjacency, then it is an insertion event. if no adjacencies are split, create an adjacency
  relative to the most recently inserted neighbor". A position is written by adjacency, never as an index: "adjacency
  does that". An insertion event inserts the dragged shape into the adjacency it splits: the spec from one neighbour to
  the other is replaced, in one mutation, by a spec from the first to the dragged shape and one from the dragged shape
  to the second, by the same rotation.
- **Containment is separated from ownership**: "yes containment should be separated from ownership", so that a shape
  moved into or out of a container keeps its identity ([CAP-264: containment separate from ownership](../docs/capabilities/README.md#CAP-264)).
- **Thresholds**: "yes propose defaults"; the defaults are below, for review.

## Decided by an agent, for review

Where the user's decisions leave a choice open, each *proposed* until reviewed:

- **Splitting an adjacency.** A drop between two siblings splits an adjacency where an adjacency spec holds the two
  next to each other, on the side the drop is between. Then the dragged shape is inserted into it, an insertion event,
  as decided above, and the container layout settles the two new specs as it settles any rule. Otherwise the spec made
  places the dragged shape beside whichever of the two neighbours was inserted more recently, on the side of it the
  drop was on.
- **The owner of a shape.** With containment apart from ownership, every shape is owned by its diagram, its name
  unique in the diagram, and its container is a role relation alone; its points, vectors and annotations are owned by
  the shape, as now, and so stay with it wherever it moves.
- **A shape's specs when it moves to another container.** An adjacency spec relates siblings, so the move removes, in
  the same mutation, the specs between the shape and its old siblings.
- **Thresholds**, in CSS pixels at a scale of 1:
  - a drag starts after a press held 300 ms, or a press that moves 6 px;
  - a sibling's edge zones are the outer quarter of its frame on each side, and at least 22 px deep, so that, with the
    gap and its neighbour's zone, a drop target is at least 44 px across, the size touch guidelines ask of a target;
    the rest of its frame is its centre zone;
  - an intent changes only once the finger is 8 px past the edge of its zone;
  - resting 600 ms over a container opens it;
  - a finger 12 px beyond a container's frame is out of it.

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
| Between two siblings | the gap between them, with their edge zones | where it splits an adjacency spec, that spec replaced by two, through the dragged shape; otherwise an adjacency spec beside the more recently inserted of the two |
| Beside a sibling | an outer edge zone of a sibling | an adjacency spec beside it, its rotation the side's, which a grid quantizes to a quarter turn |
| In a sibling's cell | the centre of a sibling | an adjacency spec that shares its cell |
| Back to its place | its own original slot | its specs removed, so that it reverts to its original insertion position |
| Into, or out of, a container | a container's interior, after dwell; outside its container | its container changed, keeping its identity, and its specs to its old siblings removed |
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
