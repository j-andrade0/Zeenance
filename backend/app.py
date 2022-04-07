# Importacoes de arquivos e bibliotecas
import json
from flask import Flask, jsonify
from flask_cors import CORS
from util.db import db
from flask_jwt_extended import JWTManager
from blocklist import BLOCKLIST


# Configuracoes
config_file = open('config/dev.json') 
config = json.load(config_file)


app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']
app.config['JWT_SECRET_KEY'] = config['JWT_SECRET_KEY']
app.config['JWT_BLOCKLIST_ENABLED'] = config['JWT_BLOCKLIST_ENABLED']


# Api's imports:

from api.usuario_api import usuario_api
from api.categoria_gastos_api import categoria_gastos_api


# Registro das api's no Blueprint

app.register_blueprint(usuario_api)
app.register_blueprint(categoria_gastos_api)



# Configuração JWT
jwt = JWTManager(app)


# Configuracao de logout JWT
@jwt.token_in_blocklist_loader
def verifica_blocklist(self, token):
    return token['jti'] in BLOCKLIST

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    return jsonify({'msg': 'Voce esta deslogado!'}), 401 # unauthorized


@app.before_first_request
def create_database():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
