install:
	poetry install

update:
	poetry update

runserver:
	poetry run python3 manage.py runserver

migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

shell:
	poetry run python3 manage.py shell

.PHONY: page_loader page_loader test_page_loader tests
