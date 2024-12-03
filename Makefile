.PHONY: lint
lint:
	mypy --disable-error-code=attr-defined .
	ruff check --fix .

.PHONY: check-problems
check-problems:
	python tools/helpers.py $(or $(year),2024)
