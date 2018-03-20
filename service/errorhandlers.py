from flask import Blueprint, request, jsonify

error_handlers = Blueprint('error_handlers', __name__)

@error_handlers.app_errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@error_handlers.app_errorhandler(400)
def not_found(error=None):
    message = {
            'status': 400,
            'message': error.description,
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp
