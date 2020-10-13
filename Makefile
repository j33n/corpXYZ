.PHONY: init init-migration build run db-migrate test tox

init:  build run
	docker-compose exec web corporationXYZ db upgrade
	docker-compose exec web corporationXYZ init
	@echo "Init done, containers running"

build:
	docker-compose build

run:
	docker-compose up -d

db-migrate:
	docker-compose exec web corporationXYZ db migrate

db-upgrade:
	docker-compose exec web corporationXYZ db upgrade

test:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e test

tox:
	docker-compose run -v $(PWD)/tests:/code/tests:ro web tox -e py38

lint:
	docker-compose run web tox -e lint