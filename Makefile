#makefile

config: clean install migrate start

install:
	pip install -r requirements.txt

clean:
	@find . -name "*.pyc" | xargs rm -f

create_db:
	./app/manage.py syncdb --settings=conf.settings ;\

start: clean
	./app/manage.py runserver 0.0.0.0:7000 --settings=conf.settings ;\

migrate:
	./app/manage.py makemigrations --settings=conf.settings ;\
	./app/manage.py migrate --settings=conf.settings ;\

clean_migrations:
	find ./app/guardian/migrations/ |grep '0'|xargs rm -f