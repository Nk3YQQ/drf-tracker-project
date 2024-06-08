runserver:
	python3 manage.py migrate --no-input
	python manage.py collectstatic --noinput
	gunicorn --config gunicorn_config.py config.wsgi:application

build-and-run:
	docker-compose up --build -d

tests:
	docker-compose exec -T drf python3 manage.py test

linters:
	docker-compose exec -T app flake8 blogapp/
	docker-compose exec -T app flake8 shopapp/
	docker-compose exec -T app flake8 users/

stop:
	docker-compose down

clean-up:
	docker-compose down --volumes

coverage:
	coverage run --source='.' manage.py test
	coverage report

celery-worker:
	celery -A config worker --loglevel=info

celery-beat:
	celery -A config beat --loglevel=info

bot-run:
	python3 manage.py bot