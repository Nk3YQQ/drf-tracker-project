runserver:
	python3 manage.py runserver

coverage:
	coverage run --source='.' manage.py test
	coverage report

celery-worker:
	celery -A config worker --loglevel=info

celery-beat:
	celery -A config beat --loglevel=info

bot-run:
	python3 manage.py bot