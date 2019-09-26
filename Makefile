admin:
	python manage.py createsuperuser --email admin@admin.com --username admin

check:
	python manage.py check

lint:
	pre-commit install && pre-commit run -a -v

migrations:
	python manage.py makemigrations
	python manage.py migrate

pyformat:
	black .

run:
	python manage.py runserver

shell:
	python manage.py shell_plus

test:
	pytest -sx



