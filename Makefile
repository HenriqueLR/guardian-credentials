#makefile

config: clean install migrate start

install:
	pip install -r requirements.txt

clean:
	@find . -name "*.pyc" | xargs rm -f

create_db:
	@if [ $(settings) ]; then \
		./app/manage.py syncdb --settings=conf.settings_production ;\
	else \
		./app/manage.py syncdb --settings=conf.settings ;\
	fi

start: clean
	@if [ $(settings) ]; then \
		./app/manage.py runserver 0.0.0.0:7000 --settings=conf.settings_production ;\
	else \
		./app/manage.py runserver 0.0.0.0:7000 --settings=conf.settings ;\
	fi

migrate:
	@if [ $(settings) ]; then \
		./app/manage.py makemigrations --settings=conf.settings_production ;\
		./app/manage.py migrate --settings=conf.settings_production ;\
	else \
		./app/manage.py makemigrations --settings=conf.settings ;\
		./app/manage.py migrate --settings=conf.settings ;\
	fi

clean_migrations:
	find ./app/guardian/migrations/ |grep '0'|xargs rm -f