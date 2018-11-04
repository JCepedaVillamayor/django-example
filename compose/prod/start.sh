#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py makemigrations
python manage.py migrate
gunicorn config.wsgi -w 2 -b 0.0.0.0:8000