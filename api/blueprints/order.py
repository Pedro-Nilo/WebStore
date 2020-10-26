from api.blueprints import api_blueprint
from api.blueprints.base import base_response
from api.blueprints.authentication import token_auth
from api.services.order import OrderService
from flask import request


order_service = OrderService()


@api_blueprint.route("order", methods=["POST"])
@token_auth.login_required
def make_order():
    current_user = token_auth.current_user()

    result = order_service.add(current_user.id, request)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("order", methods=["GET"])
@token_auth.login_required
def get_orders():
    current_user = token_auth.current_user()

    if current_user.is_manager:
        result = order_service.get()
    else:
        result = order_service.get_by_client_id(current_user.id)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("order/<int:order_id>", methods=["GET"])
@token_auth.login_required
def get_order_by_id(order_id):
    current_user = token_auth.current_user()

    if current_user.is_manager:
        result = order_service.get_by_id(order_id)
    else:
        result = order_service.get_by_id(order_id, current_user.id)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("order/client/<int:client_id>", methods=["GET"])
@token_auth.login_required
def get_order_by_client_id(client_id):
    current_user = token_auth.current_user()

    if not current_user.is_manager and current_user.id != client_id:
        return base_response(401)

    result = order_service.get_by_client_id(client_id)

    return base_response(result["status_code"], result["message"])
