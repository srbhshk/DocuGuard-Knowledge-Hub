# Testing Framework Usage and Guidelines

## Backend (Pytest)
- Place tests under `backend/tests`.
- Use focused unit tests and API integration tests.
- Run: `pytest backend/tests`.

## Frontend (Jest + Testing Library)
- Place tests near components in `frontend/src`.
- Prefer behavior-focused assertions over implementation details.
- Run: `npm test` in `frontend`.
