from ..entidades.clientes import create_clientes_table_query
from ..entidades.agendamento import create_agendamento_table_query
from ..entidades.servico import create_servico_table_query
from ..entidades.horarios_disponiveis import create_horarios_disponiveis_table_query
from ..connection.connection_db import conectar_db
from ..connection.fechar_conexao import fechar_conexao_db
import psycopg2
from psycopg2.extras import DictCursor


def create_table():
    """Cria as tabelas no banco de dados."""

    # conectando ao banco
    conn = conectar_db()
    connection = conn['connection']

    # criando um cursor
    cursor = connection.cursor(cursor_factory=DictCursor)

    try:

        # Executa os comandos SQL para criar as tabelas, se quiser criar mais de uma tabela, basta adicionar abaixo.
        cursor.execute(create_clientes_table_query)
        cursor.execute(create_agendamento_table_query)
        cursor.execute(create_servico_table_query)
        cursor.execute(create_horarios_disponiveis_table_query)

        # Commit da transação
        connection.commit()
        print("Tabelas criadas com sucesso!")

    except psycopg2.Error as e:
        print(f"Erro ao criar as tabelas: {e}")

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection, connection_pool=conn['connection_pool'])


