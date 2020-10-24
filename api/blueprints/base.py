from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def base_response(status_code, response_data=None):
    payload = dict(result=HTTP_STATUS_CODES.get(status_code, "Unknown error"))

    if response_data:
        payload["data"] = response_data

    response = jsonify(payload)
    response.status_code = status_code

    return response
