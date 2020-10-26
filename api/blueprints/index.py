from api.blueprints import api_blueprint
from api.blueprints.base import base_response


@api_blueprint.route("/", methods=["GET"])
def index():
    return base_response(200, "WebStore API is running!")
