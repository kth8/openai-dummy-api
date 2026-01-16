FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY pyproject.toml ./
RUN uv pip install --system --frozen --no-dev

COPY . .

EXPOSE 7000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]
