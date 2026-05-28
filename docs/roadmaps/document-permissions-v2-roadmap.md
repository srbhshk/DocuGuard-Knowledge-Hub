# Document-Level Permissions v2 Roadmap

## Milestone 1: Schema and Policy Engine
- Add ACL tables (`document_permissions`, optional groups mapping).
- Implement effective policy resolver in backend service layer.

## Milestone 2: API and Admin UX
- Expose CRUD ACL APIs and effective-permission endpoint.
- Build admin-facing permission management UI.

## Milestone 3: Retrieval Enforcement
- Enforce ACL during retrieval candidate filtering.
- Add audit logs for authorization decisions.

## Milestone 4: Hardening
- Permission simulation endpoint for admins.
- Batch ACL operations and conflict resolution support.
