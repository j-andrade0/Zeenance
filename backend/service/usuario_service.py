from flask import request
from model.usuario_model import UsuarioModel as model


def get_all():
    model.get_all()


def get_by_id(id):
    model.get_by_id(id)


def post():
    dados = request.get_json()
    usuario = model(**dados)
    usuario.post()


def put(id):
    dados = request.get_json()
    usuario = model(**dados)
    usuario.update(id)
