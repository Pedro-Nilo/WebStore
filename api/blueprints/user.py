from flask import jsonify
from api.blueprints import api_blueprint


users = [
    {
        "name": "John",
        "email": "john@example.com"
    },
    {
        "name": "Susan",
        "email": "susan@example.com"
    }
]


@api_blueprint.route("user", methods=["GET"])
def get_all_users():
    return jsonify(users)
