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

    # Only the manager has the right to see the list of users
    if current_user.is_manager:
        result = user_service.get()
    else:
        # If you are a customer, this will only return your own information
        result = user_service.get_by_id(current_user.id)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("user/<int:user_id>", methods=["GET"])
@token_auth.login_required
def get_user_by_id(user_id):
    current_user = token_auth.current_user()

    if not current_user.is_manager and current_user.id != user_id:
        return base_response(401)

    result = user_service.get_by_id(user_id)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("user/<int:user_id>", methods=["PUT"])
@token_auth.login_required
def update_user(user_id):
    current_user = token_auth.current_user()

    # Only the user himself can edit his data
    if current_user.id != user_id:
        return base_response(401)

    result = user_service.update(user_id, request)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("user/<int:user_id>", methods=["DELETE"])
@token_auth.login_required
def delete_user(user_id):
    current_user = token_auth.current_user()

    # Manager and the user himself can delete his data
    if not current_user.is_manager and current_user.id != user_id:
        return base_response(401)

    result = user_service.delete(user_id)

    return base_response(result["status_code"], result["message"])
