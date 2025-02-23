test-local:
	poetry run pytest

ruff-local:
	poetry run ruff check

test:
	docker build -t tester . && docker run --rm tester poetry run pytest

ruff:
	docker build -t linter . && docker run --rm linter poetry run ruff check

