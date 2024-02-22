import psycopg2


def conectar_db():

    connection = None

    try:

        # Conecta ao banco de dados recém-criado
        connection = psycopg2.connect(
            user="teste_postgre_kadu_user",
            password="PmyhHT6Y2cf7z7kaTrYj4Vl2woF8DHia",
            host="dpg-cn829iacn0vc738kfc8g-a.oregon-postgres.render.com",
            port="5432",
            database="agendamento_db_test"
        )

        """
        # Conecta ao banco de dados recém-criado
        connection = psycopg2.connect(
            user="postgres",
            password="071419",
            host="localhost",
            port="5432",
            database="testando_db"
        )"""

        # retorna uma variável com a conexão
        return connection

    except psycopg2.Error as e:
        print(f"Erro ao conectar com o banco: {e}")

