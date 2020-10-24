from api.blueprints import api_blueprint
from api.blueprints.authentication import basic_auth, token_auth
from api.blueprints.base import base_response
from api.models import db


@api_blueprint.route("token", methods=["POST"])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()

    db.session.commit()

    return base_response(200, token)


@api_blueprint.route("token", methods=["DELETE"])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()

    db.session.commit()

    return base_response(204)
