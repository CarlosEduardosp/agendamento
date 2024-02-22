
def fechar_conexao_db(cursor: None, connection: None):

    # Fecha a conexão com o banco de dados
    if connection:
        cursor.close()
        connection.close()
        print("Conexão com banco encerrada.")
