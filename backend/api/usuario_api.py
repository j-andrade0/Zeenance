from flask import Blueprint
import controller.usuario_controller as controller


usuario_api = Blueprint('usuario_api', __name__)


@usuario_api.route('/usuario', methods=['GET'])
def get_all():
    return controller.get_all()


@usuario_api.route('/usuario/<id>', methods=['GET'])
def get_by_id(id):
    return controller.get_by_id(id)


@usuario_api.route('/usuario', methods=['POST'])
def post():
    return controller.post()


@usuario_api.route('/usuario/<id>', methods=['PUT'])
def put(id):
    return controller.put(id)


@usuario_api.route('/usuario/<id>', methods=['DELETE'])
def delete(id):
    return controller.delete(id)

# Login de usuario

@usuario_api.route('/login', methods=['POST'])
def login():
    return controller.login()

