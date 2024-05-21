runserver:
	python3 manage.py runserver

docker-compose-run:
	docker-compose up --build -d

tests:
	docker-compose exec -T drf python3 manage.py test

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