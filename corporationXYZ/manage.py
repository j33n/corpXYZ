import click
from flask.cli import FlaskGroup

from corporationXYZ.app import create_app


def create_corporationXYZ(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_corporationXYZ)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from corporationXYZ.extensions import db
    from corporationXYZ.models import User

    click.echo("create user")
    user = User(username="admin", email="admin@test.com", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
