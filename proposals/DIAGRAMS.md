# Diagrams

Initiative: [INI-040: diagrams framework](PRIORITIES.md#ini-040--diagrams-framework).

`mbse-diagrams` will be a framework for rendering diagrams 
representing schema-governed data. 

`Framework.Logical` defines MBSE schemas for modeling a "logical layout"
of a diagram in terms of points, vectors, segments, shapes and layout 
relationships between shapes. Logical layout does not track coordinates
or any relative/absolute placement information. 

**Orientation.** Every entity has one orientation, an angle relative to the root view, which is "up". An entity
inherits its orientation along its path to the root, and only a vector changes it:

- **A vector** carries a rotation. Its end point's orientation is its start point's plus that rotation. A shape's
  border and extent points are reached from its origin by vectors, so they take those vectors' rotations.
- **A cell** inherits its container's orientation. Whether its displacement within the container also rotates it is
  defined by the container type: a grid's cells keep the container's "up", while a radial container might turn each
  cell to face outward.
- **A shape** in a container reaches its cell along its adjacency, which acts as a vector: a direction from the
  "from" shape, relative to the container's orientation, selects the cell. A shape added without an adjacency goes to
  the next cell in the container's insertion order. Either way, the shape and its origin take that cell's orientation.
- **A container** takes the orientation of its parent shape. The root container, the diagram's own, is "up".

Physical layout resolves orientations to absolute directions in the diagram.

A logical layout point becomes a point in the physical layout.

A vector is a start point, an end point, a rotation, and a `length : float` in terms of
diagram units. Remember, in logical layout points are
just names, not coordinates. It is the responsibility of physical layout
to assign point coordinates.

Every shape has an origin point which for simple geometric shapes must 
coincide with the geometric center of the shape.

Every shape may have a collection of border points. Each border point
is connected to the shape's origin via a vector. Border 
points are usually connected to one another in adjacent
pairs via vectors.

A segment is attached to two points and has no stated length: unlike a
vector, it places neither point, and physical layout draws it between
wherever its points are placed.

Shapes have relationships:
- containment : container/parent shape, contained/child shape
- adjacency : within a container, from shape, to shape, via a direction
  relative to the container's orientation, acting as a vector

An adjacency is a logical layout spec, it is not a connector.

Containers are implicit constructs that contain shapes and participate
in deciding how those shapes are arranged with respect to one another.
The diagram is a rectangular root object which has an implied container
for top-level shapes in the diagram. Every shape may have an implied
container and must have a container if it has any children
(the "children" of a shape are always delegated to its implied
container).

A container is a collection of cells that dynamically expand
based on the children and their relationships. The shape and layout 
of the cells are determined by the type of container. 
The layout may permit or forbid elasticity along axes that make
sense to that container shape. Adding children without adjacency
spec results in each successive child being added to 
its own cell according to a sequence that is predictable based
on the container's shape. Adding an adjacency spec to an existing
child that can be achieved with a simple change in insertion order
causes the insertion order to change. Removing an adjacency spec
from an existing child causes it to revert to its original insertion
order position. 

Adding adjacency specs with the same "from" shape and same rotation
causes the cell along that rotation to receive multiple children.
The cell is itself a container that will expand if necessary.

Each container type says whether its cells take a rotation from their
displacement within it.

Grid layout with rows and columns must 
be a container type that is supported; a grid's cells keep the container's
orientation. Others may be added as needed.

Every shape has a collection of extent points. Each extent point
is connected to the shape's origin via a vector. Extent points
are used during physical layout to determine how to distribute resizing 
moves such that every child fits in its container cell.

`Framework.Container` defines MBSE schemas for tracking container
layouts as:
- container/cell containment structure
- extent of cells along each axis within a container
- set of child shape(s) in each cell

`Framework.Physical` defines MBSE schemas for modeling physical layout
(as point coordinates, primarily) which annotate a logical layout
to which it is connected by annotation relations.

Physical layout is computed in terms of floating point "diagram units",
and tracks placements as relative and absolute coordinates for
points, directions, shapes, etc. in those units.
Every shape, container, cell in the diagram gets its own `unit_length : float`
computed from its container (and from its container all the way up
to the diagram). `scaling_factor` is applied in this process
between container and its children.

The diagram exposes properties that tune physical layout:

- `unit_length : float` how long a "unit length" vector is at the top level of
  the diagram (1.0 is typical)
- `scaling_factor : float` how "unit length" scales from container to child
  at each level of containment
- `margin : float` number of units of collapsing margin between cells and
  between a container and its parent. Margin is passed from parent to
  child container without scaling.

The diagram itself is dynamically sized, expanding as necessary when
cells are added and shrinking when cells are removed from its implied
container. A UI component should have a fixed-size viewport, and should
auto-scale to accommodate diagram resizing specifically when one of the
viewport boundaries are crossed by the resizing.

The layout algorithm (container and physical together) is fundamentally 
*incremental*. Basically that means it processes mutations rather than 
the model itself. The purpose is to keep humans and AI "in the loop" 
by permitting fine-grained edits to the logical layout at any point in 
the process. Also by completely avoiding any "bulk recompute" layout
algorithm we can guarantee the final layout is a deterministic function 
of the mutation sequence.

The layout algorithm does *not* process a logical layout directly.
Instead, when a UI wishes to display a logical layout, that logical
layout model is first snapshotted as mutations. Then the mutations 
are streamed to the layout engine. Each mutation is processed individually. 
At each mutation, the layout algorithm will:

- consider how objects, relation entries, and properties will change
- anticipate the effect those mutations have on the previous layout 
  state (which is inductively assumed to comply with all layout rules) 
- apply the mutation to its cumulative model of the logical layout,
  temporarily allowing violation of layout rules
- make incremental adjustments to cell assignments and cell extents
- make incremental adjustments to point placements that will 
  restore consistency of the point positions with the layout rules after 
  the mutation has been replayed

User error can create unsolvable scenarios. When used as stated in this doc 
no such conflicts should exist. Incremental layout should detect trivial cases and ignore the later of two definitely incompatible rules.
Conflicts beyond trivial cases result in unspecified but deterministic
behavior.

A mutation may lift condition(s) that caused previous rule 
applications to be ignored. These rule applications must be queued,
and checked. If the mutation lifts a restriction they should be
applied in queued order. This is an intentional refinement of the
deterministic replay rule.

## Rules

- adding(removing) a shape to(from) the diagram or a child to(from) a shape
  causes its container to add(remove) cells if necessary
- adding(removing) cells to(from) a container causes the container to
  expand(shrink) its physical size
- expanding(shrinking) a container causes its parent (which may be a cell)
  to expand(shrink) accordingly just enough to contain it
- shape context (orientation, `unit_length`) is computed recursively starting
  from the diagram
- border points must be spaced from their shape's origin correctly
- minimum shape size (maximum extent along any axis) is configurable
  and enforced by physical layout

## Division of Labor

- `mbse-diagrams` will provide container-level layout components in
  python3 and typescript5, equivalent per [PRI-028: both implementations change together](../docs/PRINCIPLES.md#PRI-028). Container
  layout is only concerned with container extents (as number of cells
  along each axis), cell contents, and has no knowledge of coordinates of 
  any kind.
- `mbse-diagrams` will provide physical layout components in
  python3 and typescript5, equivalent per [PRI-028: both implementations change together](../docs/PRINCIPLES.md#PRI-028), by an incremental
  constraint solver, Kiwi, in each (decided 2026-11-09; first planned in typescript5 only)
