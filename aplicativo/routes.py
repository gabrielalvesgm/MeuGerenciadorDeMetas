from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from aplicativo.config.database import create_connection
from aplicativo.models.usuario import get_user_by_email, create_user

auth_bp = Blueprint("auth", __name__)

#Método register: Registro de usuário
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    password = data.get("password")

    #Valida obrigatoriedade dos campos
    if not nome or not email or not password:
        return jsonify({"msg": "Todos os campos são obrigatórios"}), 400

    connection = create_connection()

    try:
        #Verifica se o email já tem cadastro.
        user = get_user_by_email(connection, email)
        if user:
            return jsonify({"msg": "Este Email já esta registrado."}), 409  # Conflict

        #####Hashed meaning: produced by or involving the assignment of a numeric or alphanumeric string to a piece of data via a function or algorithm whose output values are all the same number of bits in length.
        hashed_password = generate_password_hash(password)

        create_user(connection, nome, email, hashed_password)

        return jsonify({"msg": "Usuário registrado com sucesso"}), 201  # Created
    except Exception as e:
        return jsonify({"msg": f"Erro ao registrar usuário: {e}"}), 500  # Internal Server Error
    finally:
        connection.close()


# Método 2: Login de usuário
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    # Validações básicas
    if not email or not password:
        return jsonify({"msg": "Email e senha são obrigatórios"}), 400

    connection = create_connection()

    try:
        # Verifica se o usuário existe
        user = get_user_by_email(connection, email)
        if not user:
            return jsonify({"msg": "Usuário não encontrado"}), 404  # Not Found

        # Verifica se a senha está correta
        if not check_password_hash(user["senha"], password):
            return jsonify({"msg": "Senha incorreta!"}), 401  # Unauthorized

        # Gera o token JWT
        access_token = create_access_token(identity=user["id"])
        return jsonify({"access_token": access_token}), 200  # Success
    except Exception as e:
        return jsonify({"msg": f"Erro ao fazer login: {e}"}), 500  # Internal Server Error
    finally:
        connection.close()


# Método 3: Perfil do usuário autenticado
@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = get_jwt_identity()  # Pega o ID do usuário do token JWT

    connection = create_connection()
    try:
        # Recupera os dados do usuário autenticado
        user = get_user_by_email(connection, user_id)

        if not user:
            return jsonify({"msg": "Usuário não encontrado"}), 404  # Not Found

        # Retorna os dados do usuário
        return jsonify({
            "id": user["id"],
            "nome": user["nome"],
            "email": user["email"]
        }), 200  # Success
    except Exception as e:
        return jsonify({"msg": f"Erro ao recuperar dados: {e}"}), 500  # Internal Server Error
    finally:
        connection.close()
