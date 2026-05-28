# Installation Guide (Docker Compose)

## Prerequisites
- Docker Engine + Docker Compose plugin.
- Available ports: 5173, 8000, 5432, 6333, 11434.

## Steps
1. Copy `.env.example` to `.env` and update secrets.
2. Start core services:
   - `docker compose -f infra/docker-compose.yml -f infra/docker-compose.dev.yml up --build`
3. Frontend: `http://localhost:5173`
4. Backend health: `http://localhost:8000/api/v1/health`

## Shutdown
- `docker compose -f infra/docker-compose.yml -f infra/docker-compose.dev.yml down`
