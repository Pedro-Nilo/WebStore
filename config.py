import os
from dotenv import load_dotenv


base_directory = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(base_directory, ".flaskenv"))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "Tm92ZW1icm80OSE="

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(base_directory, "webstore.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
