import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.metas import create_meta



#TESTE CREATE META
def test_create_meta():
    connection = create_connection()

    if connection:
        try:
            email = "teste2@email.com"  #Email em que a meta será criada.

            nome_meta = "Teste criar meta" #nome da meta
            descricao_meta = "Testar POST META2" #descrição da meta
            prazo_meta = "2025-03-01" #prazo da meta (EUA Date)

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
