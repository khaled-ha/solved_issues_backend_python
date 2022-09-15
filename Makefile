.PHONY: clean venv set_migrations

SHELL := /bin/zsh
ACTIVATE := source venv/bin/activate
clean:
	./delete_env_file.sh

venv:
	python -m venv venv
	$(ACTIVATE) && pip install -r requirements.txt
	$(ACTIVATE) venv/bin/activate && pip install -r requirements_test.txt

set_env:
	cp martial_art/martial_art/env.tpl martial_art/martial_art/.env

docker_clean:
	docker stop $(docker ps -aq)

set_migrations:
	alembic upgrade head
	docker-compose up -d --build db