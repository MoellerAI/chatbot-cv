.PHONY: install run test shell

# Make sure to adjust the path to your FastAPI application and other configurations if needed.

install:
	@echo "Installing dependencies..."
	@cd backend && poetry install

run:
	@echo "Starting FastAPI application..."
	@cd backend && poetry run uvicorn main:app --reload

test:
	@echo "Running tests..."
	cd backend && poetry run pytest

lint:
	@echo "Linting code with pylint"
	cd backend && poetry run pylint -d line-too-long -d missing-module-docstring -d broad-except -d missing-final-newline -d ungrouped-imports -d duplicate-code -d trailing-newlines -d trailing-whitespace --fail-under=4.0 --recursive=y .

format:
	@echo "Formatting code with black..."
	cd backend && poetry run black .
