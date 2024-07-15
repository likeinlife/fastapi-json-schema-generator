DC = docker compose

ENV = --env-file sample.env

APP_FILE = docker-compose/app.yaml
STORAGES_FILE = docker-compose/storages.yaml

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} up --build -d

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up --build -d

.PHONY: down-app
down-app:
	${DC} -f ${APP_FILE} ${ENV} down

.PHONY: down-storages
down-storages:
	${DC} -f ${STORAGES_FILE} ${ENV} down

.PHONY: down-storages-v
down-storages-v:
	${DC} -f ${STORAGES_FILE} ${ENV} down -v

.PHONY: down-all
down-all:
	${MAKE} down-storages
	${MAKE} down-app

.PHONY: freeze
freeze:
	poetry export -o requirements.txt --without-hashes
