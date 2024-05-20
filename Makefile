docker-compose-run:
	docker-compose up --build -d

check-db:
	docker-compose exec -T pgdb psql -U test -d postgres -c '\l' | grep tracker_db || exit 1

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