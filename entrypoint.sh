#!/bin/sh
while !</dev/tcp/db/5432; do sleep 1

uvicorn app.main:app --host ${APP_HOST} --port ${APP_PORT} --reload

exec "$@"