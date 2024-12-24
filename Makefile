dev-sync:
	uv sync --all-extras --cache-dir .uv-cache

prod-sync:
	uv sync --no-dev --cache-dir .uv-cache

lint:
	uv run ruff format
	uv run ruff check --fix
	uv run mypy --install-types --non-interactive --package strava_client
