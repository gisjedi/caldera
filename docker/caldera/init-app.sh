#!/bin/bash

psql -f docker/caldera/init-db.sql -U postgres -h postgis
python manage.py migrate
python manage.py erupt 1000 30