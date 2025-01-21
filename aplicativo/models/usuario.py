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
    query = "SELECT * FROM usuario WHERE email = %s"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            return user
    except Exception as e:
        print(f"Erro ao buscar usuario: {e}")
        return None