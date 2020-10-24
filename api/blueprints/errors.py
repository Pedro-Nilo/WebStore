from api.blueprints import api_blueprint
from api.blueprints.base import base_response
from api.models import db


@api_blueprint.errorhandler(404)
def not_found_error(error):
    return base_response(404, "%s" % error.description)


@api_blueprint.errorhandler(500)
def internal_error(error):
    db.session.rollback()

    return base_response(500,
                         "Sorry we have a problem, please try again later")
