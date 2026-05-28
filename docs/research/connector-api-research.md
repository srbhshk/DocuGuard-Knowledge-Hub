# Connector API Research

## Sources Evaluated
- Confluence Cloud REST API: basic auth with email + API token, CQL search, page content retrieval.
- Notion API: OAuth 2.0, scoped integrations, block/page database retrieval.
- Google Drive API: OAuth 2.0, service-account flows for enterprise, file metadata + export endpoints.
- SharePoint (Microsoft Graph): OAuth 2.0 via Azure AD app registration, drives/sites/items endpoints.

## Authentication Summary
- Confluence: personal/API token for PoC, OAuth 2.0 for production.
- Notion: internal integration token for dev, OAuth for distributed app.
- Google Drive: service-account for backend jobs, delegated scopes for user-specific access.
- SharePoint: client credentials for app-only access where allowed, delegated for user-context retrieval.

## Connector Design Constraints
- Normalize metadata across sources (`external_id`, `source`, `owner`, `modified_at`, `permissions`).
- Support incremental sync using source-specific cursors/timestamps.
- Preserve source permission metadata for downstream authorization.
- Store source raw payload for audit/debug only when policy allows.
