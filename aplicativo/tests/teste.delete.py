import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.metas import delete_meta, get_metas_by_user
from aplicativo.models.usuario import delete_user

# DELETE META
def test_delete_meta():
    connection = create_connection()
    if connection:
        try:
            user_id = 1 #ID USUÁRIO
            meta_id = 1 #ID META

            result = delete_meta(connection, user_id, meta_id)
            assert result is True, "Falha ao deletar meta"
            
            print("Meta deletada com sucesso.")
        except Exception as e:
            print(f"Erro no teste de deletar meta: {e}")
        finally:
            connection.close()

# DELETE USER
def test_delete_user():
    connection = create_connection()
    if connection:
        try:
            email = "Marcos@email.com"
            senha = "123456"

            result = delete_user(connection, email, senha)
            if result == "Usuário deletado com sucesso.":
                print("Test DELETE USER - Sucesso")
            else:
                print(f"Test DELETE USER - Falhou: {result}")
        except Exception as e:
            print(f"Erro no teste de deletar usuário: {e}")
        finally:
            connection.close()

# Chamar os testes
if __name__ == "__main__":
    test_delete_meta()
    test_delete_user()
