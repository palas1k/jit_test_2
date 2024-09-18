
test:
	poetry run pytest

run:
	poetry run uvicorn main:app
