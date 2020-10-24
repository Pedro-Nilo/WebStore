from api.blueprints import api_blueprint
from api.models import db
from flask import jsonify


@api_blueprint.errorhandler(404)
def not_found_error(error):
    return jsonify(dict(status=404, message=error))


@api_blueprint.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify(dict(status=404, message=error))
