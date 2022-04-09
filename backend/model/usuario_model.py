from util.db import db
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token
from blocklist import BLOCKLIST
from model.gastos_model import GastosModel



class UsuarioModel(db.Model):
    __tablename__ = 'tb_usuario'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique = True, nullable=False)
    senha = db.Column(db.String(32), nullable=False)
    gastos = db.relationship('GastosModel')


    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


 # API Methods:


    def get_all():
        if UsuarioModel.find_all() == []:
            return {}
        return UsuarioModel.find_all()


    def get_by_id(id):
        found = UsuarioModel.find_by_id(id)
        if found:
            return found.json()
        return {}


    def post(self):
        UsuarioModel.add(self)


    def put(id, **dados):
        UsuarioModel.update(id, **dados)


    def delete(self):
        UsuarioModel.remove(self)


# Class methods:


    @classmethod
    def find_all(cls):
        return [found.json() for found in cls.query.all()]


    @classmethod
    def find_by_id(cls, id):
        return UsuarioModel.query.filter_by(id=id).first()


    @classmethod
    def find_by_email(cls, email):
        return UsuarioModel.query.filter_by(email=email).first()


    def add(self):
        db.session.add(self)
        db.session.commit()


    def remove(self):
        db.session.delete(self)
        db.session.commit()


    def update(id, **dados):
      UsuarioModel.query.filter_by(id=id).update(dict(**dados))
      db.session.commit()


    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'gastos': [gasto.json() for gasto in self.gastos]

        }


    def __repr__(self):
        return '<Usuario %r>' % self.id


class Login():
    def dados_corretos(**dados):

        user = UsuarioModel.find_by_email(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            return True

    def gerar_token(**dados):
        user = UsuarioModel.find_by_email(dados['login'])

        token_de_acesso = create_access_token(identity=user.id)
        return {'access_token': token_de_acesso}


class Logout():

    def logout(jwt_id):
        BLOCKLIST.add(jwt_id)
        return {'message': 'Deslogado com sucesso!'}
