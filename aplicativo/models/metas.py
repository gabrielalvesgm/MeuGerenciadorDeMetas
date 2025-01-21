#MÉTODO POST META
def create_meta(connection, user_id, nome_meta, descricao_meta, prazo_meta):
    query = """INSERT INTO metas (user_id, nome_meta, descricao_meta, prazo_meta)
               VALUES (%s, %s, %s, %s) RETURNING id"""
    values = (user_id, nome_meta, descricao_meta, prazo_meta)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            meta_id = cursor.fetchone()[0]
            connection.commit()
            return meta_id
    except Exception as e:
        print(f"Erro ao criar meta: {e}")
        return None



#MÉTODO GET META
def get_metas_by_user(connection, user_id):
    query = "SELECT * FROM metas WHERE user_id = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (user_id,))
            metas = cursor.fetchall()
            return metas
    except Exception as e:
        print(f"Erro ao buscar metas: {e}")
        return None



#MÉTODO DELETE META

def delete_meta(connection, usuario_id, meta_id):
    query = "DELETE FROM metas WHERE user_id = %s AND ID = %s"
    values = (usuario_id, meta_id)

    try:
        with connection.cursor() as cursor:  # Corrigido para o cursor ser tratado corretamente
            cursor.execute(query, values)
            connection.commit()
            rows_deleted = cursor.rowcount
            if rows_deleted > 0:
                print("Meta deletada com sucesso!")
                return True
            else:
                print("Meta não encontrada ou não pertence ao usuário informado.")
                return False
    except Exception as e:  # Corrigido para capturar corretamente o erro do psycopg2
        print(f"Erro ao deletar meta: {e}")
        return False
    finally:
        if connection:  # Removido underline, pois connection não é mais sublinhado
            cursor.close()
            connection.close()
    