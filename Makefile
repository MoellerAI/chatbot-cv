.PHONY: install run test shell

# Make sure to adjust the path to your FastAPI application and other configurations if needed.

install:
	@echo "Installing dependencies..."
	@cd apps/backend && poetry install

run:
	@echo "Starting FastAPI application..."
	@cd apps/backend && poetry run uvicorn main:app --reload

test:
	@echo "Running tests..."
	cd apps/backend && poetry run pytest

lint:
	@echo "Linting code with pylint"
	cd apps/backend && poetry run pylint -d line-too-long -d missing-module-docstring -d broad-except -d missing-final-newline -d ungrouped-imports -d duplicate-code -d trailing-newlines -d trailing-whitespace --fail-under=.0 --recursive=y .

format:
	@echo "Formatting code with black..."
	cd apps/backend && poetry run black .

coverage:
	@echo "Generating test coverage report..."
	cd apps/backend && poetry run pytest --cov=. --cov-report=term-missing --cov-fail-under=100
