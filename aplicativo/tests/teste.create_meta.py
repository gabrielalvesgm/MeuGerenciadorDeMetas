import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.metas import create_meta

def test_create_meta():
    connection = create_connection()

    if connection:
        try:
            email = "teste@email.com"  #Email em que a meta será criada.

            nome_meta = "Teste create_meta"
            descricao_meta = "Testar meu POST meta"
            prazo_meta = "2025-03-01"

            #Chama o método POST META
            meta_id = create_meta(connection, email, nome_meta, descricao_meta, prazo_meta)

            if meta_id:
                print(f"Meta criada com ID: {meta_id}")
            else:
                print("Falha ao criar meta. Verifique o e-mail ou tente novamente.")

        except Exception as e:
            print(f"Erro no teste de criação de meta: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    test_create_meta()
