from src.infra.configs.connection.connection_db import conectar_db
from src.infra.configs.connection.fechar_conexao import fechar_conexao_db
from src.interfaces.interface_repositorio.interface_agendamento import InterfaceAgendamentoRepository


class Inseriragendamento(InterfaceAgendamentoRepository):

    def criar_agendamento(self, id_servico, data, horario, id_cliente):

        # conectando ao banco
        connection = conectar_db()

        # criando um cursor
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO agendamento(id_servico, data, horario, id_cliente)"
                       f"VALUES('{id_servico}', '{data}', '{horario}', '{id_cliente}')")

        connection.commit()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return 'Agendamento Inserido com sucesso'


    def listar_agendamentos(self):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM agendamento;")

        connection.commit()

        response = cursor.fetchall()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return response

    def encontrar_agendamento_por_id_by_cliente(self, id_cliente):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM agendamento WHERE id_cliente = {id_cliente};")

            connection.commit()

            response = cursor.fetchall()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return response

        except:
            return 'Ocorreu um erro ao selecionar agendamento.'


    def deletar_agendamento(self, id_agendamento):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"DELETE FROM agendamento WHERE id_agendamento = {id_agendamento}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return "Agendamento deletado com sucesso"

        except:
            return 'Ocorreu um erro ao deletar'

