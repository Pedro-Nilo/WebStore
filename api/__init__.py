import logging
import os

from api.models import db
from config import Config
from flask import Flask
from flask_migrate import Migrate
from logging.handlers import RotatingFileHandler


migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from api.blueprints import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    if not app.debug:
        if not os.path.exists("logs"):
            os.mkdir("logs")

        file_handler = RotatingFileHandler("logs/webstore.log", maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s"
                + " [in %(pathname)s:%(lineno)d]"))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('Webstore startup')

    return app
