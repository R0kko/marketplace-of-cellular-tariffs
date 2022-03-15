#!/usr/bin/env bash

cd /code/ || exit 1
python manage.py migrate
python manage.py collectstatic --noinput
daphne -b 0.0.0.0 -p 8000 --access-log /var/log/code/daphne_access.log marketplace_of_ct.asgi:application