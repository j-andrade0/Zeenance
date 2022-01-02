import service.usuario_service as service


def get_all():
    return service.get_all(), 200


def get_by_id(id):
    return service.get_by_id(id), 200


def post():
    return service.post(), 201


def put(id):
    return service.put(id), 200


def delete(id):
    return service.delete(id), 200
