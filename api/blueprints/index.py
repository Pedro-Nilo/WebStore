from flask import jsonify
from api.blueprints import api_blueprint


@api_blueprint.route("/", methods=["GET"])
def index():
    return jsonify(dict(message="WebStore API is running!"))
