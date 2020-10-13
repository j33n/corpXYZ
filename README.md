CorporationXYZ: Notifications API
=================================

[![TravisCI](https://travis-ci.org/uber/Python-Sample-Application.svg?branch=master)](https://travis-ci.org/uber/Python-Sample-Application)
[![Coverage Status](https://coveralls.io/repos/uber/Python-Sample-Application/badge.png)](https://coveralls.io/r/uber/Python-Sample-Application)

Project Description
-------------------

A simple api application that allows companies to send and receive notifications to users via email or SMS

Up and Running Locally
------------------------

1. Fill in the relevant information in the `.flaskenv` file in the root folder
make sure the environment variables `FLASK_ENV`, `FLASK_APP`, `SECRET_KEY` and `DATABASE_URI` are present.
A Sample environment variable file can contain the following values
```
FLASK_ENV=development
FLASK_APP=corporationXYZ.app:create_app
SECRET_KEY=changeme
DATABASE_URI=postgresql://postgres@localhost:5432/corporationXYZ
```
2. make sure pipenv is installed on your local setup. If it's not present run `pip install pipenv`
3. Run `pipenv install` to install dependencies. Make sure you're in the root folder before running the command
4. Run `pipenv shell` to activate a Python virtual env
5. Run `corporationXYZ db upgrade` to run migrations
6. Run `corporationXYZ init` to populate our database with users
7. Run `corporationXYZ run` to run the project

Then navigate to http://127.0.0.1:5000/swagger-ui to view a Swagger UI to assist with api navigation
Or access http://127.0.0.1:5000/swagger.json to view the json documentation
