from flask import Blueprint
import controller.gastos_controller as controller


gastos_api = Blueprint('gastos_api', __name__)


@gastos_api.route('/gastos', methods=['GET'])
def get_all():
    return controller.get_all()


@gastos_api.route('/gastos/<id>', methods=['GET'])
def get_by_id(id):
    return controller.get_by_id(id)


@gastos_api.route('/gastos', methods=['POST'])
def post():
    return controller.post()


@gastos_api.route('/gastos/<id>', methods=['PUT'])
def put(id):
    return controller.put(id)


@gastos_api.route('/gastos/<id>', methods=['DELETE'])
def delete(id):
    return controller.delete(id)