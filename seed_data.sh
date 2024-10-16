#!/bin/bash

rm -rf tractice/migrations
rm db.sqlite3
python manage.py makemigrations tracticeapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata artists
python manage.py loaddata shows
python manage.py loaddata songs
python manage.py loaddata showsongs
python manage.py loaddata practicesessions