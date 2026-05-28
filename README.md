# DocuGuard Knowledge Hub

DocuGuard Knowledge Hub is a self-hosted enterprise knowledge platform for secure internal document search and question answering, designed around a custom RAG pipeline, role-based access controls, and enterprise deployment requirements.

This is the **Day 0 milestone**: repository initialization from a FLOWiGANTT plan, including base monorepo scaffolding and foundational implementation artifacts. FLOWiGANTT plan: [Shared build plan](https://flowigantt.com/shared/z2enWKZ7eLTZBdVSiQKP-QjrpKY1r48q).

## Current Implementation Status

- Monorepo foundations created for `backend/`, `frontend/`, `infra/`, `tests/`, and `.github/workflows/`.
- Backend initialized with FastAPI app shell, health and query endpoints, SQLAlchemy models, and Alembic baseline migrations.
- Frontend initialized with React + TypeScript + Chakra UI plus Jest and ESLint/Prettier setup.
- Docker and CI/CD foundations implemented (`ci`, `docker-build`, and `docs` workflows).
- Initial custom RAG skeleton added (chunking, embedding placeholder, retrieval placeholder, generation, and pipeline orchestration).
- Documentation system scaffolded (Sphinx base, install/testing/migration/quality docs, contribution guide).

## Project Documentation

- Architecture: [`docs/architecture-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md`](docs/architecture-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md)
- PRD: [`docs/prd-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md`](docs/prd-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md)
- Features: [`docs/features-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md`](docs/features-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md)
- Stories: [`docs/stories-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md`](docs/stories-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md)
- Tasks: [`docs/tasks-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md`](docs/tasks-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md)
- Evaluation: [`docs/evaluation-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md`](docs/evaluation-6ed935c4-df4d-49ef-a9de-5cd1c25f46c2.md)

## Repository Structure

- `backend/`: FastAPI application, database models, migrations.
- `frontend/`: React + TypeScript + Chakra UI app.
- `infra/`: Docker Compose files for local and production-like setup.
- `docs/`: architecture, planning, and implementation guides.

## Quick Start

Prerequisites:

- Python 3.11+ (required for backend dependencies)
- Docker Desktop / Docker daemon running

1. Backend dependencies: `pip install -r backend/requirements.txt`
2. Frontend dependencies: `cd frontend && npm install`
3. Run locally via Compose:
   - `docker compose -f infra/docker-compose.yml -f infra/docker-compose.dev.yml up --build`
   - This command uses `build` overrides from `infra/docker-compose.dev.yml` for local images.

## Quality Commands

- Backend lint: `ruff check backend && black --check backend`
- Backend test: `pytest backend/tests`
- Frontend lint: `cd frontend && npm run lint`
- Frontend test: `cd frontend && npm test`

## What's next (Day 1+)

- Complete integration of persistent vector retrieval by wiring embeddings and query retrieval to Qdrant, replacing current placeholder behavior in the initial RAG skeleton.
- Expand document ingestion and connector execution from research/prototype into production-ready sync flows for Confluence, Notion, Google Drive, and SharePoint.
- Implement document-level permissions end-to-end (schema, APIs, policy enforcement, and retrieval-time filtering) per roadmap and design documents.
- Harden enterprise auth and governance by advancing SSO integration paths (SAML/OIDC), audit logging coverage, and admin-facing permission observability.
- Move from scaffolded docs to operational docs by extending Sphinx/user/developer guides with environment-specific deployment, troubleshooting, and runbook content.
- Increase test depth beyond foundation checks with fuller backend integration tests, frontend feature tests, and CI validation for migration and environment workflows.
