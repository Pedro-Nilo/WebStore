from api.models import db
from config import Config
from flask import Flask
from flask_migrate import Migrate


migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from api.blueprints import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    return app
