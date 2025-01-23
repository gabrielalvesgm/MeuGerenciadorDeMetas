import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.metas import delete_meta




#TESTE DELETE META
def test_delete_meta():
    connection = create_connection()
    if connection:
        try:
            user_id = 6 #ID USUÁRIO DA META
            meta_id = 6 #ID DA META QUE SERÁ DELETADA

            result = delete_meta(connection, user_id, meta_id)
            assert result is True, "Falha ao deletar meta"
            
        except Exception as e:
            print(f"Erro no teste de deletar meta: {e}")
        finally:
            connection.close()
            
if __name__ == "__main__":
    test_delete_meta()