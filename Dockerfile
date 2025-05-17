FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /src

WORKDIR /src

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

RUN uv sync --frozen --no-cache

CMD ["/src/.venv/bin/fastapi", "run", "src/main.py", "--port", "8000", "--host", "0.0.0.0"]
