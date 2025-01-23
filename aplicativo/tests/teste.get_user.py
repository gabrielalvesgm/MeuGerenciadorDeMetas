# teste.get_user.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from aplicativo.config.database import create_connection
from aplicativo.models.usuario import get_user_by_email



#TESTE GET USER
def test_get_user_by_email():
    connection = create_connection()
    if connection:
        try:
            #Simualação de login e senha para teste:
            email = input("Digite o e-mail do usuário: ")
            password = input("Digite a senha do usuário: ")

            #buscando usuário por email e senha
            user = get_user_by_email(connection, email, password)

            if user:
                print(f"Sucesso: Usuário encontrado\nID: {user['id']}\nNome: {user['nome']}\nE-mail: {user['email']}")
            else:
                print("Erro na busca: Usuário não encontrado ou senha incorreta.")
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
        finally:
            connection.close()

# Chamar o teste
if __name__ == "__main__":
    test_get_user_by_email()
