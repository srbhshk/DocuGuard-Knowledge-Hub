# Connector Research and Design Summary

This document consolidates:
- API/auth research across Confluence, Notion, Google Drive, SharePoint.
- Connector architecture and ingestion data flow design.
- Prototype implementation notes from the Confluence API client.

## Prototype Outcome
- Implemented asynchronous Confluence client with list and get-page flows.
- Validated approach for source adapters using a thin HTTP wrapper with typed methods.

## Next Implementation Steps
1. Add OAuth token refresh abstraction and secure secret loading.
2. Create common normalized document DTO and adapter contracts.
3. Add incremental sync cursor persistence tables.
4. Wire connector output to the ingestion pipeline queue.
