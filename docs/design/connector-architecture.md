# Connector Architecture and Data Flow

## Components
- `connector_registry`: maps source type to client implementation.
- `connector_clients`: source-specific API wrappers.
- `sync_orchestrator`: schedules and tracks sync jobs.
- `normalizer`: converts source payload to canonical document model.
- `ingestion_bridge`: forwards normalized documents into RAG ingestion pipeline.

## Data Flow
1. Sync request created for source + scope.
2. Client fetches changed items using cursor/time filter.
3. Normalizer maps metadata/content into canonical format.
4. Permission metadata extracted and attached.
5. Documents pushed to ingestion queue.
6. Sync checkpoints persisted for incremental runs.

## Error Handling
- Retry transient failures (HTTP 429/5xx) with backoff.
- Mark hard failures with source-specific diagnostic context.
- Persist per-item ingestion errors for partial sync reconciliation.
