admin:
	python manage.py createsuperuser --email admin@admin.com --username admin

check:
	python manage.py check

lint:
	pre-commit install && pre-commit run -a -v

migrations:
	python manage.py makemigrations
	python manage.py migrate

nomigrations:
	python manage.py test --nomigrations

pyformat:
	black .

run:
	python manage.py runserver

test:
	python manage.py test



