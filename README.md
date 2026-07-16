# secondbrain

## Installation

Clone the repository, then install the project and its dependencies:

```bash
uv sync
```

## Usage

Run through the CLI entrypoint:

```bash
uv run secondbrain
```

Use development environment settings explicitly:

```bash
uv run --env-file .env secondbrain
```

Or run it as a Python module:

```bash
uv run python -m secondbrain
```

## Environment Variables

`.env.example` is the tracked template. Copy it to `.env` for development.

`LOG_LEVEL` defaults to `INFO`; `.env` sets it to `DEBUG` for verbose console output.

`LOG_FILE` defaults to `app.log` and controls the log-file path.

`uv run --env-file .env` loads the development environment explicitly; environment files are not loaded automatically.

## Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Documentation

Preview the docs locally:

```bash
uv run python scripts/serve_docs.py
```

Build static documentation:

```bash
uv run mkdocs build
```
