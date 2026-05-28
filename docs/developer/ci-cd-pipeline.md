# CI/CD Pipeline Setup and Usage

## Workflow Layers
- `ci.yml`: frontend/backend lint + tests.
- `docker-build.yml`: image build and push to GHCR on `main`.
- `docs.yml`: Sphinx docs build validation.

## Typical Flow
1. Open pull request -> CI validates lint/tests/docs.
2. Merge to `main` -> CI runs again and pushes container images.

## Troubleshooting
- Failing lint: run local linters before commit.
- Failing tests: run `pytest backend/tests` and `npm test` in `frontend`.
- Docker publish issues: verify `GITHUB_TOKEN` package permissions.
