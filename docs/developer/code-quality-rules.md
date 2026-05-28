# Code Quality Rules and Enforcement

## Standards
- Frontend: ESLint + Prettier.
- Backend: Ruff + Black.
- Commit-time checks: pre-commit hooks.

## Enforcement Process
1. Run local lint/test before PR.
2. Pre-commit blocks obvious style/lint regressions.
3. CI is the final gate for lint and tests.
