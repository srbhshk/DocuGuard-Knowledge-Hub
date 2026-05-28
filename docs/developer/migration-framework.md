# Migration Framework Usage and Best Practices

Alembic is selected as the migration framework for PostgreSQL schema evolution.

## Common Commands
- Create migration: `alembic revision -m \"message\"`
- Apply latest: `alembic upgrade head`
- Roll back one: `alembic downgrade -1`

## Best Practices
- Keep migrations atomic and reversible.
- Include schema/index changes in the same migration when tightly coupled.
- Always review generated SQL for destructive changes.
