#
# Makefile: Automation for local building and testing.
#

SHELL := /bin/zsh
ACTIVATE := source venv/bin/activate

DB_IMAGE := db
REQS := (requirements.txt|requirements_test.txt)

SOURCE_VENV := source venv/bin/activate

# Python definitions. Support Python 3.9 and 3.10 on GH workflow
PYTHON_INTERPRETER := python3.9
PIP := $(PYTHON_INTERPRETER) -m pip
VENV_DIR = venv

DOCKER_SERVER_IMAGE_TAG := server
DOCKER_IMAGE_VERSION := latest
DOCKER_EXPOSE_PORT := 8000
DATABASE_URL := localhost
POSTGRES_USER :=
POSTGRES_PASSWORD :=
POSTGRES_DB :=

.PHONY: clean venv set_migrations run docker_stop docker_build tests unit_tests serve

lint:
	scripts/lint.sh

clean:
	./delete_env_file.sh

migrate:
	docker-compose up -d $(DB_IMAGE)
	alembic upgrade head

venv:
	$(PYTHON_INTERPRETER) -m venv $(VENV_DIR)
	$(SOURCE_VENV) && $(PIP) install --upgrade pip
	$(SOURCE_VENV) && $(PIP) install -r requirements_test.txt
	$(SOURCE_VENV) && $(PIP) install -r requirements.txt
#for req in $(REQS); do pip install -r $$req ; done

docker_stop:
	docker stop $(docker ps -aq)

# set_migrations:
# 	docker-compose down -v
# 	docker-compose up -d db
# 	alembic revision --autogenerate
# 	alembic upgrade head
# 	docker-compose up -d --build server

docker_build:
	docker build -t $(DOCKER_SERVER_IMAGE_TAG):$(DOCKER_IMAGE_VERSION) -f Dockerfile .

docker_clean:
	docker-compose --project-name $(DOCKER_SERVER_IMAGE_TAG) rm --stop --force
	docker volume rm $(DOCKER_SERVER_IMAGE_TAG)_database-data

# Test the code in the virtual environment
tests: venv docker_build
	docker-compose --project-name $(DOCKER_SERVER_IMAGE_TAG) up -d --force-recreate --no-deps
	$(SOURCE_VENV) && alembic downgrade base && alembic upgrade head
#docker cp ./seeds/seed.sql $(DOCKER_SERVER_IMAGE_TAG)_db_1:/seed.sql
#docker exec ${DOCKER_SERVER_IMAGE_TAG}_db_1 psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -f /seed.sql

unit_tests: venv
	docker-compose --project-name $(DOCKER_SERVER_IMAGE_TAG) up -d --force-recreate --no-deps auth_db
	sleep 3 # need to find a way to do this with some readiness probe
	$(SOURCE_VENV) && alembic downgrade base && alembic upgrade head
	docker cp ./seeds/seed-for-ut.sql $(DOCKER_SERVER_IMAGE_TAG)_db_1:/seed.sql
	docker exec ${DOCKER_SERVER_IMAGE_TAG}_db_1 psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -f /seed.sql
	set -o pipefail && $(SOURCE_VENV) && pytest -s --cov=data_service --cov-report=term | tee pytest-coverage.txt

# Runs the containerized app with docker compose
serve:
	docker-compose --project-name $(DOCKER_SERVER_IMAGE_TAG) up -d

run:
	docker-compose up -d
