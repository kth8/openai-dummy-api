FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY . .

RUN uv sync

EXPOSE 7000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]
