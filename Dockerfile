FROM python:3.11-slim

ENV POETRY_VERSION=1.9.0

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /app
COPY pyproject.toml README.md ./
RUN poetry install --no-root

COPY . .

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
