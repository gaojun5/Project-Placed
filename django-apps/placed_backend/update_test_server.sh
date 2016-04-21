#!/bin/bash
source /var/django-apps/virtualenvs/placed-ucl/bin/activate
python manage.py collectstatic
python manage.py migrate
python manage.py flush
python manage.py loaddata data/*.json
service apache2 restart