README.md
ssh -L 5432:localhost:5432 tom@astound.eu #psql
ssh -L 5672:localhost:5672 tom@astound.eu #rmq

python manage.py celery worker --loglevel=info

