# Priorities

The order in which the schema-driven visualization ([FEA-001: schema-driven UI](../docs/features/FEA-001.md) and the features beside it)
is built. Each section is a step, in order; Later lists what comes after,
unordered.

## clean mutation-based transactional API

`mbse-rest` must define a clean transactional API using mutations as the
primary if not exclusive query and response encoding and serialization.

## single-user demo with schema driven index site for any MBSE app

- demo app: work tracking (mbse-demo-apps' [`docs/WORK_TRACKER.md`](../../mbse-demo-apps/docs/WORK_TRACKER.md))
- persistence: [CAP-013: an in-memory store journaled to DynamoDB](../docs/capabilities/CAP-013.md)
- Python + FastAPI + DynamoDB
- React + Typescript + CSS-in-TS
- db initialization by schema
- local tenancy (for demos)
- in-browser search-sort-filter
- Views are fully responsive balancing window resize, proportionate
  initial allocation of major display sections, value abbreviation,
  and font scaling
- auto scrolling on all views

## object properties as markdown ([FEA-007: property kinds](../docs/features/FEA-007.md), [CAP-014: properties as markdown](../docs/capabilities/CAP-014.md))

## comments ([CAP-016: comments](../docs/capabilities/CAP-016.md), with [CAP-015: transaction provenance](../docs/capabilities/CAP-015.md), [CAP-018: adjacency inspector](../docs/capabilities/CAP-018.md) to [CAP-022: booleans as checkboxes](../docs/capabilities/CAP-022.md))

## relation inspector ([CAP-023: relation inspector](../docs/capabilities/CAP-023.md))

## add diagram views

## add search-sort-filter

## finish out property editing

## add relation editing

## Later

- object properties as text/date ([FEA-007: property kinds](../docs/features/FEA-007.md))
- object properties as financial/scientific/engineering ([FEA-007: property kinds](../docs/features/FEA-007.md))
- Views prefer device-native gestures (esp. pinch/scroll/pan/zoom)
- full stack view paging : list
- Responsive UI can be configured by css-in-ts
- private tenancy
- multi-tenancy
- MCP integration
- AI chat session integration : chatGPT
- AI chat session integration : model selection
- schema extension
- low-code custom views
- UI in React Native
- persistence in mySQL and noSQL
- schema migration
- services in Typescript
- UI in ios native
- UI in Android native
- UI in Angular, Vue
