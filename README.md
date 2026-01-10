# Context Data Schemas

This repo contains shared data contracts and database migrations.

## Setup

1. Copy environment file and update values:
   ```bash
   cp .env.example .env
   ```
2. Install dependencies:
   ```bash
   poetry install
   ```

## Run migrations

- Ensure `DATABASE_URL` is set (local `.env` or environment).
- Run:
  ```bash
  alembic upgrade head
  ```

## Local tunnel (example)

If your database is only reachable via a tunnel, establish it first, then run migrations.
