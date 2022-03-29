from flask import request
from model.categoria_gastos_model import CategoriaGastosModel as model


def get_all():
    return model.get_all()


def get_by_id(id):
    return model.get_by_id(id)


def post():
    dados = request.get_json()
    categoria = model(**dados)
    categoria.post()
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
    categoria = model.find_by_id(id)
    categoria.delete()
    return {'msg':'Categoria deletada'}

