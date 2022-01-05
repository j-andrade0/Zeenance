from flask import request
from model.categoria_gastos_model import CategoriaGastosModel as model


def get_all():
    return model.get_all()


def get_by_id(id):
    return model.get_by_id(id)


def post():
    dados = request.get_json()
    usuario = model(**dados)
    usuario.post()
    return {'msg':'Categoria criada'}


def put(id):
    dados = request.get_json()
    found = model.find_by_id(id)
    if found:
        model.put(id, **dados)
        return {'msg':'Dados alterados'}
    else:
        return {'msg':'Id nao encontrado'}


def delete(id):
    usuario = model.find_by_id(id)
    usuario.delete()
    return {'msg':'Categoria deletada'}

