from flask import request
from model.usuario_model import UsuarioModel as model


def get_all():
    return model.get_all()


def get_by_id(id):
    return model.get_by_id(id)


def post():
    dados = request.get_json()
    usuario = model(**dados)
    usuario.post()
    return {'msg':'Usuario criado'}


def put(id):
    dados = request.get_json()
    found = model.find_by_id(id)
    if found:
        model.put(id, **dados)
        return {'msg':'Dados alterados'}
    else:
        return {'msg':'Id not found'}


def delete(id):
    model.delete(id)
    return {'msg':'Usuario deletado'}

