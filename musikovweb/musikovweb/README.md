README.md
ssh -L 5432:localhost:5432 tom@astound.eu #psql
ssh -L 5672:localhost:5672 tom@astound.eu #rmq

python manage.py celery worker --loglevel=info


Reqs:
virtualenv setuptools python-software-properties
rabbitmq
postgresql
apache2
git
mod_wsgi
build-essential
graphviz
libgraphviz-dev
pkg-config
libpq-dev
python-dev



Services:
Gsqd
GA
Pusher


createuser -S -P -l -d
Enter name of role to add: lyricgraph
Enter password for new role: 
Enter it again: 
Shall the new role be allowed to create more new roles? (y/n) n

createdb -U lyricgraph -W lyricgraph