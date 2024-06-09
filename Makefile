runserver:
	python3 manage.py migrate --no-input
	gunicorn --config gunicorn_config.py config.wsgi:application

runserver-prod:
	python3 manage.py migrate --no-input
	python manage.py collectstatic --noinput
	gunicorn --config gunicorn_config.py config.wsgi:application

tests:
	docker-compose -f docker-compose.yml up --build -d
	docker-compose exec -T drf python3 manage.py test
	docker-compose exec -T drf flake8 habit/
	docker-compose exec -T drf flake8 users/
	docker-compose -f docker-compose.yml down --volumes

deploy-project:
	docker-compose -f docker-compose.prod.yml down
	docker-compose -f docker-compose.prod.yml up --build -d

check-containers:
	docker-compose -f docker-compose.prod.yml ps

celery-worker:
	celery -A config worker --loglevel=info

celery-beat:
	celery -A config beat --loglevel=info

bot-run:
	docker-compose -f docker-compose.prod.yml exec -T drf python3 manage.py bot

install-dependencies:
	ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --tags "install_dependencies"

deploy:
	ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --tags "deploy"
