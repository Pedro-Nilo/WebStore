from api.blueprints import api_blueprint
from api.blueprints.base import base_response
from api.blueprints.authentication import token_auth
from api.services.product import ProductService
from flask import request


product_service = ProductService()


@api_blueprint.route("product", methods=["POST"])
@token_auth.login_required
def add_product():
    current_user = token_auth.current_user()

    if not current_user.is_manager:
        return base_response(401)

    result = product_service.add(request)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("product", methods=["GET"])
@token_auth.login_required
def get_products():
    result = product_service.get()

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("product/<string:product_name>", methods=["GET"])
@token_auth.login_required
def get_product_by_name(product_name):
    result = product_service.get_by_name(product_name)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("product/<int:product_id>", methods=["PUT"])
@token_auth.login_required
def update_product(product_id):
    current_user = token_auth.current_user()

    if not current_user.is_manager:
        return base_response(401)

    result = product_service.update(product_id, request)

    return base_response(result["status_code"], result["message"])


@api_blueprint.route("product/<int:product_id>", methods=["DELETE"])
@token_auth.login_required
def delete_product(product_id):
    current_user = token_auth.current_user()

    if not current_user.is_manager:
        return base_response(401)

    result = product_service.delete(product_id)

    return base_response(result["status_code"], result["message"])
