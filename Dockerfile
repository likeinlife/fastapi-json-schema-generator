FROM python:3.12.4-alpine3.19

WORKDIR /opt/app

RUN apk add curl

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.lock pyproject.toml README.md ./

RUN pip install --no-cache-dir --upgrade -r requirements.lock

COPY src src

RUN chmod +x ./src/rest_json_schema/docker-entrypoint.sh

ENTRYPOINT cd ./src/rest_json_schema/ && sh ./docker-entrypoint.sh