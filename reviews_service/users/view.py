# URI Mappings
import json
from flask import jsonify, request
from reviews_service.init import app
from reviews_service.exceptions import NotFoundError
from .controller import controller_ref
import http.client


@app.route('/api/users/', methods=['GET'])
def get_all():
    try:
        users_ = controller_ref.get_all()
        return json.dumps({'users': users_}), http.client.OK, {'Content-Type': 'application/json'}
    except Exception as e:
        return jsonify(message=str(e)), http.client.INTERNAL_SERVER_ERROR


@app.route('/api/users/<name>', methods=['GET'])
def get_by_name(name):
    try:
        user_ = controller_ref.get_by_name(name)
        return jsonify(user_), http.client.OK, {'Content-Type': 'application/json'}
    except NotFoundError as e:
        return jsonify(message=str(e)), http.client.NOT_FOUND
    except Exception as e:
        return jsonify(message=str(e)), http.client.INTERNAL_SERVER_ERROR


@app.route('/api/users/', methods=['POST'])
def add_user():
    try:
        user_data = request.json

        # content-type missed?
        if not user_data:
            return jsonify(message="invalid payload, check content-type, should be: Content-Type': 'application/json"),\
                   http.client.BAD_REQUEST

        user_ = controller_ref.add(user_data)
        return jsonify(user_), http.client.OK, {'Content-Type': 'application/json'}
    except NotFoundError as e:
        return jsonify(message=str(e)), http.client.NOT_FOUND
    except Exception as e:
        return jsonify(message=str(e)), http.client.INTERNAL_SERVER_ERROR


@app.route('/api/users/<name>', methods=['DELETE'])
def delete_by_name(name):
    try:
        controller_ref.delete_by_name(name)
        return jsonify({"status": "OK"}), http.client.OK, {'Content-Type': 'application/json'}
    except NotFoundError as e:
        return jsonify(message=str(e)), http.client.NOT_FOUND
    except Exception as e:
        return jsonify(message=str(e)), http.client.INTERNAL_SERVER_ERROR
