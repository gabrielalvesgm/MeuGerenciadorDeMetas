import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.usuario import create_user
from aplicativo.models.metas import create_meta, delete_meta

def main():
    connection = create_connection()

    if connection:
        # Teste para criar um usuário
        user_id = create_user(connection, "Marcos", "Marcos@email.com", "123456")
        print(f"Usuário criado com ID: {user_id}")

        # Teste para criar uma meta
        if user_id:
            meta_id = create_meta(connection, user_id, "Estudar Java", "Con cluir o curso Spring", "2025-03-01")
            print(f"Meta criada com ID: {meta_id}")

if __name__ == "__main__":
    main()