#usuarios.py

#Método POST USER
def create_user(connection, username, email, password):
    query = "INSERT INTO usuario (username, email, password) VALUES (%s, %s, %s) RETURNING id"
    values = (username, email, password)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            user_id = cursor.fetchone()[0]
            connection.commit()
            return user_id
    except Exception as e:
        print(f"Erro ao criar usuario: {e}")
        return None
    
    

#Método GET USER
def get_user_by_email(connection, email):
    query = "SELECT id, nome FROM usuarios WHERE email = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (email,))
            return cursor.fetchone()
    except Exception as e:
        print(f"Erro ao buscar usuário pelo e-mail: {e}")
        return None

    
    
#Método DELETE USER
def delete_user(connection, email, senha):
    try:
        query_user = "SELECT id, senha FROM usuarios WHERE email = %s"
        with connection.cursor() as cursor:
            cursor.execute(query_user, (email,))
            user = cursor.fetchone()

            if not user:
                return "Usuário não encontrado."

            user_id, senha_armazenada = user

            if senha != senha_armazenada:
                return "Senha incorreta."

            query_metas = "SELECT COUNT(*) FROM metas WHERE user_id = %s"
            cursor.execute(query_metas, (user_id,))
            metas_count = cursor.fetchone()[0]

            if metas_count > 0:
                return "Só é possível deletar um usuário que tem metas ativas, é necessário deletar suas metas antes."

            query_delete_user = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(query_delete_user, (user_id,))
            connection.commit()

            return "Usuário deletado com sucesso."
    except Exception as e:
        return f"Erro ao deletar usuário: {e}"