#metas.py
#MÉTODOS CRUD PARA METAS



# Método POST META
def create_meta(connection, email, nome_meta, descricao_meta, prazo_meta):
    query = """INSERT INTO metas (user_id, nome_meta, descricao_meta, prazo_meta)
               VALUES (%s, %s, %s, %s) RETURNING id"""
    
    # Busca o user_id pelo e-mail
    user_query = "SELECT id FROM usuario WHERE email = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(user_query, (email,))
            user_id = cursor.fetchone()
            if user_id:
                user_id = user_id[0]
                values = (user_id, nome_meta, descricao_meta, prazo_meta)
                cursor.execute(query, values)
                meta_id = cursor.fetchone()[0]
                connection.commit()
                return meta_id
            else:
                print("Usuário não encontrado com o e-mail fornecido.")
                return None
    except Exception as e:
        print(f"Erro ao criar meta: {e}")
        return None
    
    

# Método GET META
def get_metas_by_email(connection, email):
    query = """
        SELECT metas.*
        FROM metas
        JOIN usuario ON metas.user_id = usuario.id
        WHERE usuario.email = %s
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (email,))
            metas = cursor.fetchall()
            return metas
    except Exception as e:
        print(f"Erro ao buscar metas pelo e-mail: {e}")
        return None



#MÉTODO DELETE META
def delete_meta(connection, usuario_id, meta_id):
    query = "DELETE FROM metas WHERE user_id = %s AND ID = %s"
    values = (usuario_id, meta_id)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted > 0:
                print("Meta deletada com sucesso!")
                return True
            else:
                print("Meta não encontrada ou não pertence a este usuário.")
                return False
    except Exception as e:
        print(f"Erro ao deletar meta: {e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()



#MÉTODO PUT META
def update_meta(connection, user_id, meta_id, campo, novo_valor):
    
    #Verificando se o id da meta pertence ao usuário.
    query_meta = "SELECT id FROM metas WHERE id = %s AND user_id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query_meta, (meta_id, user_id))
            meta = cursor.fetchone()

            if not meta:
                return "Meta não encontrada ou não pertence ao usuário."

            #validação do campo que o usuário quer atualizar.
            campos_validos = ["nome_meta", "descricao_meta", "prazo_meta", "status_meta"]
            if campo not in campos_validos:
                return "Campo inválido. Escolha entre: nome_meta, descricao_meta, prazo_meta, status_meta."

            #atualizando a meta:
            query_update = f"UPDATE metas SET {campo} = %s WHERE id = %s"
            cursor.execute(query_update, (novo_valor, meta_id))
            connection.commit()
            return f"Campo '{campo}' atualizado com sucesso."
    except Exception as e:
        return f"Erro ao atualizar a meta: {e}"
