from flask import Flask
from aplicativo.routes import auth_bp, usuario_bp
from aplicativo.models.auth import init_jwt

app = Flask(__name__)

# Configuração da chave secreta do JWT
app.config["JWT_SECRET_KEY"] = "sua_chave_secreta_segura"

# Inicialização do JWT
init_jwt(app)

# Registro das rotas do Blueprint
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(usuario_bp, url_prefix="/usuario")

if __name__ == "__main__":
    app.run(debug=True)
