#teste.create.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.usuario import create_user
from aplicativo.models.metas import create_meta

def main():
    connection = create_connection()

#CRIAR UM USUÁRIO
    if connection:
        user_id = create_user(connection, "Julia Vitória", "jv917345@gmail.com", "ilovetaylorswift")
        print(f"Usuário criado com ID: {user_id}")
