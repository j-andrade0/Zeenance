from flask import Blueprint
import controller.categoria_gastos_controller as controller


categoria_gastos_api = Blueprint('categoria_gastos_api', __name__)


@categoria_gastos_api.route('/categoria_gastos', methods=['GET'])
def get_all():
    return controller.get_all()


@categoria_gastos_api.route('/categoria_gastos/<id>', methods=['GET'])
def get_by_id(id):
    return controller.get_by_id(id)


@categoria_gastos_api.route('/categoria_gastos', methods=['POST'])
def post():
    return controller.post()


@categoria_gastos_api.route('/categoria_gastos/<id>', methods=['PUT'])
def put(id):
    return controller.put(id)


@categoria_gastos_api.route('/categoria_gastos/<id>', methods=['DELETE'])
def delete(id):
    return controller.delete(id)