import click
from api.services.user import UserService


user_service = UserService()


def register(app):
    @app.cli.group()
    def webstore():
        """WebStore command line operations."""
        pass

    @webstore.command()
    @click.argument("username")
    @click.argument("email")
    @click.argument("password")
    def add_manager(username, email, password):
        """Add a manager user to WebStore.\n
           PARAMETERS:\n
            - username: Username for manager.\n
            - email: Email for manager.\n
            - password: Password for manager."""
        print(user_service.add_super(username, email, password))
