from util.db import db


class CategoriaRecebiveisModel(db.Model):
    __tablename__ = 'tb_categoria_recebiveis'


    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(45))
    descricao = db.Column(db.String(70), nullable=True)


    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao


 # API Methods:


    def get_all():
        if CategoriaRecebiveisModel.find_all() == []:
            return {}
        return CategoriaRecebiveisModel.find_all()


    def get_by_id(id):
        found = CategoriaRecebiveisModel.find_by_id(id)
        if found:
            return found.json()
        return {}


    def post(self):
        CategoriaRecebiveisModel.add(self)


    def put(id, **dados):
        CategoriaRecebiveisModel.update(id, **dados)


    def delete(self):
        CategoriaRecebiveisModel.remove(self)


# Class methods:


    @classmethod
    def find_all(cls):
        return [found.json() for found in cls.query.all()]


    @classmethod
    def find_by_id(cls, id):
        return CategoriaRecebiveisModel.query.filter_by(id=id).first()


    def add(self):
        db.session.add(self)
        db.session.commit()


    def remove(self):
        db.session.delete(self)
        db.session.commit()


    def update(id, **dados):
      CategoriaRecebiveisModel.query.filter_by(id=id).update(dict(**dados))
      db.session.commit()


    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao
        }


    def __repr__(self):
        return '<Categoria_Recebiveis %r>' % self.id
