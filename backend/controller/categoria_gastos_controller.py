from flask import jsonify
import service.categoria_gastos_service as service
from flask_jwt_extended import jwt_required


@jwt_required()
def get_all():
    return jsonify(service.get_all()), 200


@jwt_required()
def get_by_id(id):
    return jsonify(service.get_by_id(id)), 200


@jwt_required()
def post():
    return service.post(), 201


@jwt_required()
def put(id):
    return service.put(id), 200


@jwt_required()
def delete(id):
    return service.delete(id), 200
