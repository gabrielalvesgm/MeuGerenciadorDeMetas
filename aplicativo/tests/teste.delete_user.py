import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.usuario import delete_user




#TESTE DELETE USER
def test_delete_user():
    connection = create_connection()
    if connection:
        try:
            email = "teste2@email.com"
            senha = "senha_forte"

            result = delete_user(connection, email, senha)
            if result == "Usuário deletado com sucesso.":
                print("Test DELETE USER - Sucesso")
            else:
                print(f"Test DELETE USER - Falhou: {result}")
        except Exception as e:
            print(f"Erro no teste de deletar usuário: {e}")
        finally:
            connection.close()


if __name__ == "__main__":
    test_delete_user()
