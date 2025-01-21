import psycopg2

def create_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="gerenciador_metas",
            user="postgres",
            password="123456",
            port="5432",
            options="-c client_encoding=UTF8"
)

        return connection
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados Postgre: {e}")
        return None
