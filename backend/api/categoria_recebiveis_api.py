from flask import Blueprint
import controller.categoria_recebiveis_controller as controller


categoria_recebiveis_api = Blueprint('categoria_recebiveis_api', __name__)


@categoria_recebiveis_api.route('/categoria_recebiveis', methods=['GET'])
def get_all():
    return controller.get_all()


@categoria_recebiveis_api.route('/categoria_recebiveis/<id>', methods=['GET'])
def get_by_id(id):
    return controller.get_by_id(id)


@categoria_recebiveis_api.route('/categoria_recebiveis', methods=['POST'])
def post():
    return controller.post()


@categoria_recebiveis_api.route('/categoria_recebiveis/<id>', methods=['PUT'])
def put(id):
    return controller.put(id)


@categoria_recebiveis_api.route('/categoria_recebiveis/<id>', methods=['DELETE'])
def delete(id):
    return controller.delete(id)