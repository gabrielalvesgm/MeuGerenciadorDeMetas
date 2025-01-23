# teste.create.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.usuario import create_user



#TESTE CREATE USER
def main():
    connection = create_connection()

    # CRIAR UM USUÁRIO
    if connection: #informações necessárias para criar um user:
        user_id = create_user(connection, "Teste2", "teste2@email.com", "senha_forte")
        print(f"Usuário criado com ID: {user_id}")

if __name__ == "__main__":
    main()
