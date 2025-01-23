import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.metas import get_metas_by_email



#TESTE GET META
def test_get_metas_by_email():
    connection = create_connection()

    if connection:
        try:
            email = "teste@email.com" #Email do usuário que quer ver as metas.

            metas = get_metas_by_email(connection, email)

            if metas:
                print(f"Metas encontradas para o e-mail {email}: {metas}")
            else:
                print("Nenhuma meta encontrada para o e-mail fornecido.")

        except Exception as e:
            print(f"Erro no teste de busca de metas pelo e-mail: {e}")
        finally:
            connection.close()

if __name__ == "__main__":
    test_get_metas_by_email()
