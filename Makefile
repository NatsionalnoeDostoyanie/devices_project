.PHONY: install-base install-full lint format-code run migrations migrate migrations-migrate _set-test-superuser-password create-test-superuser run-container docker-compose-build docker-compose-up

install-base:
	poetry install --no-dev

install-full:
	poetry install

lint:
	poetry run mypy .

format-code:
	poetry run autoflake . && poetry run isort . && poetry run black .

run:
	cd src && poetry run python manage.py runserver 0.0.0.0:8000

migrations:
	cd src && poetry run python manage.py makemigrations

migrate:
	cd src && poetry run python manage.py migrate

migrations-migrate:
	make migrations && make migrate

_set-test-superuser-password:
	cd src && poetry run python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='$$SUPERUSER_NAME'); user.set_password('$$SUPERUSER_PASSWORD'); user.save()"

create-test-superuser:
	cd src && poetry run python manage.py createsuperuser \
		--username $(SUPERUSER_NAME) \
		--email $(SUPERUSER_EMAIL) \
		--noinput
	make _set-test-superuser-password

first-run-container:
	make install-full && make migrations-migrate && make create-test-superuser && make run

docker-compose-build-and-up:
	docker-compose build && docker-compose up

