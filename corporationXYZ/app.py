import os

from flask import Flask

from corporationXYZ import auth, api
from corporationXYZ.extensions import db, jwt, migrate, apispec, mail


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask("corporationXYZ")
    app.config.from_object("corporationXYZ.config")
    
    # MailTrap Email Settings
    app.config.update(
        MAIL_SERVER = os.getenv("MAILTRAP_SERVER"),
        MAIL_PORT = os.getenv("MAILTRAP_PORT"),
        MAIL_USERNAME = os.getenv("MAILTRAP_USERNAME"),
        MAIL_PASSWORD = os.getenv("MAILTRAP_PASSWORD"),
        MAIL_USE_TLS = True,
        TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID"),
        TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    )

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
    configure_apispec(app)
    register_blueprints(app)
    init_mailtrap(app)

    return app


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support
    """
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)


def init_mailtrap(app):
    """inititialise mailtrap and configs
    """
    mail.init_app(app)
