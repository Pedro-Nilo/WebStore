from api.blueprints.base import base_response
from api.models.user import User
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth


basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@token_auth.verify_token
def verify_token(token):
    return User.check_token(token) if token else None


@basic_auth.error_handler
def basic_auth_error(status):
    return base_response(status)


@token_auth.error_handler
def token_auth_error(status):
    return base_response(status)
