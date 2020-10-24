from flask import Blueprint


api_blueprint = Blueprint("api_blueprint", __name__)


from api.blueprints import customer, errors, index
