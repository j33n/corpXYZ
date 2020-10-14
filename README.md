CorporationXYZ: Notifications API
=================================

Project Description
-------------------

A simple api application that allows companies to send and receive notifications to users via email or SMS

Up and Running Locally
------------------------

1. Fill in the relevant information in the `.flaskenv` file in the root folder.
A valid environment variable file should contain the following values:
```
FLASK_ENV=development
FLASK_APP=corporationXYZ.app:create_app
SECRET_KEY=changeme
DATABASE_URL=postgresql://postgres@localhost:5432/corporationXYZ

MAILTRAP_SERVER=smtp.mailtrap.io
MAILTRAP_PORT=2525
MAILTRAP_USERNAME=59c7**********
MAILTRAP_PASSWORD=f6a8**********

TWILIO_ACCOUNT_SID=AC*****************************
TWILIO_AUTH_TOKEN=0d*****************************
TWILIO_PHONE_NBR=+1**********
```
2. make sure pipenv is installed on your local setup. If it's not present run `pip install pipenv`
3. Run `pipenv install` to install dependencies. Make sure you're in the root folder before running the command
4. Run `pipenv shell` to activate a Python virtual env
6. Run `corporationXYZ db migrate` to run migrations
5. Run `corporationXYZ db upgrade` to run any updated migrations
6. Run `corporationXYZ init` to populate our database with users
7. Run `corporationXYZ run` to run the project

Then navigate to http://127.0.0.1:5000/swagger-ui to view a Swagger UI to assist with api navigation
Or access http://127.0.0.1:5000/swagger.json to view the json documentation
