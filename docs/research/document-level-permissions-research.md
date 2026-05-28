# Document-Level Permissions Research

## Model Recommendation
Use hybrid RBAC + ACL:
- RBAC gates collection access at coarse level.
- ACL grants/denies per-document access to users/groups.

## Best Practices
- Default deny at document layer when ACL is enabled.
- Keep inherited collection access explicit for explainability.
- Include audit fields (`granted_by`, `granted_at`, `reason`).
- Support effective-permission resolution endpoint for debugging.

## Policy Evaluation Order
1. Authentication validity.
2. Tenant/workspace boundary.
3. Collection-level RBAC permission.
4. Document-level deny rules.
5. Document-level allow rules.
6. Emergency/admin override logging.
