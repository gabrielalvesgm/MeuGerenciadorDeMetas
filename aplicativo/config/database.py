import psycopg2
from psycopg2 import Error

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="gerenciador_metas",
            user="postgres",
            password="123456",
            port="5432"
        )
        print(f"Conexão com o PostgreSQL estabelecida com sucesso!")
        return connection
    except Error as e:
        print(f"Erro ao conectar com o PostgreSQL: {e}")
        return None

#def create_user(username, email, password):
    connection = create_connection()
    if connection is None:
        return False
    
    cursor = connection.cursor()
    query = "INSERT INTO usuario (username, email, password) VALUES (%s, %s, %s)"
    values = (username, email, password)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Usuário criado com sucesso!")
        return True
    except Error as e:
        print(f"Erro ao criar usuário: {e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()

#def read_user():
    connection = create_connection()
    if connection is None:
        return []
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM usuario")
    users = cursor.fetchall()

    for usuario in users:
        print(usuario)
        
    cursor.close()
    connection.close()
    return users

#def update_meta_status(meta_id, novo_status):
    connection = create_connection()
    if connection is None:
        return False
    
    cursor = connection.cursor()
    query = "UPDATE Metas SET status_meta = %s WHERE ID = %s"
    values = (novo_status, meta_id)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Status da meta atualizado com sucesso!")
        return True
    except Error as e:
        print(f"Erro ao atualizar status da meta: {e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()

#def delete_user(usuario_id):
    connection = create_connection()
    if connection is None:
        return False
    
    cursor = connection.cursor()
    query = "DELETE FROM usuario WHERE ID = %s"
    values = (usuario_id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Usuário excluído com sucesso!")
        return True
    except Error as e:
        print(f"Erro ao excluir usuário: {e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()

#def create_meta(usuario_id, nome_meta, descricao, prazo, status):
    connection = create_connection()
    if connection is None:
        return None

    cursor = connection.cursor()
    query = """
    INSERT INTO metas (usuario_id, nome_meta, descricao, prazo, status)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id;
    """
    
    try:
        cursor.execute(query, (usuario_id, nome_meta, descricao, prazo, status))
        connection.commit()
        meta_id = cursor.fetchone()
        if meta_id:
            return meta_id[0]
        else:
            return None
    except Exception as e:
        connection.rollback()
        print(f"Erro ao criar meta: {e}")
        return None
    finally:
        if connection:
            cursor.close()
            connection.close()
