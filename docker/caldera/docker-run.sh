#!/bin/bash

psql -f init-db.sql -U postgres -h postgis
python manage.py migrate
python manage.py erupt 1000 30