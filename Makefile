.PHONY: test cov run clean

test:
	uv run pytest -vv

cov:
	uv run pytest --cov=reports --cov-report=term-missing

run:
	uv run reports --files employees1.csv employees2.csv --report performance
