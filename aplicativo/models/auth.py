from flask_jwt_extended import JWTManager
from flask import jsonify

# Configuração do JWT
jwt = JWTManager()

# Callback para personalizar o retorno quando o token estiver ausente
@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Token de acesso ausente"}), 401  # Unauthorized

# Callback para personalizar o retorno quando o token for inválido ou expirado
@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"msg": "Token de acesso inválido"}), 401  # Unauthorized

@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"msg": "Token expirado, faça login novamente"}), 401  # Unauthorized

# Função para inicializar o JWT no app principal
def init_jwt(app):
    jwt.init_app(app)
