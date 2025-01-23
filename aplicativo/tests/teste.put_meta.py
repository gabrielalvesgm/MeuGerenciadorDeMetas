import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from aplicativo.config.database import create_connection
from aplicativo.models.metas import update_meta



#TESTE PUT META
def test_update_meta():
    connection = create_connection()
    if connection:
        try:
            user_id = 5  #ID DO USUÁRIO 
            meta_id = 5  #ID DA META QUE SERÁ ATUALIZADA

            #Solicitações para o usuário
            campo = "nome_meta"
            novo_valor = "Teste atualizado com PUT"

            resultado = update_meta(connection, user_id, meta_id, campo, novo_valor)
            if "sucesso" in resultado:
                print("Test PUT Meta - Sucesso:", resultado)
            else:
                print("Test PUT Meta - Falhou:", resultado)
        except Exception as e:
            print(f"Erro no teste de atualizar meta: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    test_update_meta()
