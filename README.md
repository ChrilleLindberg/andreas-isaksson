# PABLIQ produktmatchning

Bootstrap of the matcher service. Requires Python 3.11 and Poetry 1.9.

## Development

```bash
# start all services
$ docker compose up -d

# run the API locally
$ poetry run uvicorn api.main:app --reload
```

### Database

The Postgres service already contains the `pgvector` extension. If you need to
create it manually in a fresh database:

```bash
psql $DATABASE_URL -c 'CREATE EXTENSION IF NOT EXISTS pgvector;'
```

### Configuration

Create a `.env` file in the project root and place your tokens here:

```
PABLIQ_TOKEN=your-token
OPENAI_API_KEY=your-api-key
```

The application automatically loads variables from `.env` on startup.

## Tests

```bash
$ docker compose up -d
$ poetry run pytest
```
