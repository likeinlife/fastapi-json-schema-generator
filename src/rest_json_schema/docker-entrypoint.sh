#!/bin/sh

alembic upgrade head

if [ "$APP_DEBUG" = "True" ]; then
    echo "DEBUG MODE"
    uvicorn presentation.api.main:default_app --host 0.0.0.0 --port 8000 --reload --factory
else
    echo "RELEASE MODE"
    gunicorn presentation.api.main:default_app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --factory
fi