from util.db import db


class GastosModel(db.Model):
    __tablename__ = 'tb_gastos'


    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    valor = db.Column(db.Float)
    descricao = db.Column(db.String(70))
    categoria_gastos_id = db.Column(db.Integer, db.ForeignKey('tb_categoria_gastos.id'))
    usuario_id = db.Column(db.Integer, db.ForeignKey('tb_usuario.id'))


    def __init__(self, valor, descricao, id_usuario, categoria_gastos_id, usuario_id):
        self.valor = valor
        self.descricao = descricao
        self.id_usuario = id_usuario
        self.categoria_gastos_id = categoria_gastos_id
        self.usuario_id = usuario_id


 # API Methods:


    def get_all():
        if GastosModel.find_all() == []:
            return {}
        return GastosModel.find_all()


    def get_by_id(id):
        found = GastosModel.find_by_id(id)
        if found:
            return found.json()
        return {}


    def post(self):
        GastosModel.add(self)


    def put(id, **dados):
        GastosModel.update(id, **dados)


    def delete(self):
        GastosModel.remove(self)


# Class methods:


    @classmethod
    def find_all(cls):
        return [found.json() for found in cls.query.all()]


    @classmethod
    def find_by_id(cls, id):
        return GastosModel.query.filter_by(id=id).first()


    def add(self):
        db.session.add(self)
        db.session.commit()


    def remove(self):
        db.session.delete(self)
        db.session.commit()


    def update(id, **dados):
      GastosModel.query.filter_by(id=id).update(dict(**dados))
      db.session.commit()


    def json(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'descricao': self.descricao,
            'id_usuario': self.id_usuario,
            'id_categoria_model': self.id_categoria_gastos,
            'categoria_gastos_id' : self.categoria_gastos_id,
            'usuario_id' : self.usuario_id 
        }


    def __repr__(self):
        return '<Gasto %r>' % self.id
