from api.blueprints import api_blueprint
from api.blueprints.base import base_response
from api.blueprints.authentication import token_auth
from api.services.user import UserService
from flask import request


user_service = UserService()


@api_blueprint.route("user", methods=["POST"])
def add_user():
    result = user_service.add(request)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("user", methods=["GET"])
@token_auth.login_required
def get_users():
    current_user = token_auth.current_user()

    if current_user.is_manager:
        result = user_service.get()
    else:
        result = user_service.get_by_id(current_user.id)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("user/<int:user_id>", methods=["GET"])
@token_auth.login_required
def get_user_by_id(user_id):
    current_user = token_auth.current_user()

    if current_user.is_manager or current_user.id == user_id:
        result = user_service.get_by_id(user_id)
    else:
        return base_response(401)

    return base_response(result["status_code"], result["message"])
