from flask import request
from flask_jwt_extended import get_jwt
from model.usuario_model import UsuarioModel as model
from model.usuario_model import Login, Logout


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
    usuario = model.find_by_id(id)
    usuario.delete()
    return {'msg':'Usuario deletado'}


# Login de usuario
def login():
    dados = request.get_json()

    if Login.dados_corretos(**dados):
        return Login.gerar_token(**dados)

# Logout de usuario
def logout():
    jwt_id = get_jwt()['jti'] # JWT Token Identifier
    return Logout.logout(jwt_id)

