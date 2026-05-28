# Document Permission API Draft

## Endpoints
- `POST /api/v1/documents/{document_id}/permissions`
  - Assign ACL entries to users/groups.
- `GET /api/v1/documents/{document_id}/permissions`
  - Retrieve ACL entries for a document.
- `DELETE /api/v1/documents/{document_id}/permissions/{permission_id}`
  - Remove ACL entry.
- `GET /api/v1/documents/{document_id}/permissions/effective`
  - Resolve effective permission for current user.

## ACL Entry Shape
```json
{
  "subject_type": "user|group",
  "subject_id": "string",
  "effect": "allow|deny",
  "action": "read|write|admin"
}
```

## Validation Rules
- `deny` entries are evaluated before `allow`.
- `admin` implies `read` and `write`.
- Only admins/editors with delegation rights can mutate ACL.
