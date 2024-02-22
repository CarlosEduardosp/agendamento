from src.infra.configs.connection.connection_db import conectar_db
from src.infra.configs.connection.fechar_conexao import fechar_conexao_db
from src.interfaces.interface_repositorio.interface_horarios import InterfacehorariosRepository

class InserirHorario(InterfacehorariosRepository):

    def criar_horarios(self, horario, status):

        # conectando ao banco
        connection = conectar_db()

        # criando um cursor
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO horarios(horario, status)"
                       f"VALUES('{horario}', '{status}')")

        connection.commit()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return 'Horário Inserido com sucesso'


    def listar_horarios(self):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM horarios;")

        connection.commit()

        response = cursor.fetchall()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return response

    def encontrar_horarios_por_id(self, id_horario):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM horarios WHERE id_horario = {id_horario};")

            connection.commit()

            response = cursor.fetchone()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return response

        except:
            return 'Ocorreu um erro ao selecionar horario.'


    def encontrar_horarios_por_status(self, status):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM horarios WHERE status = {status};")

            connection.commit()

            response = cursor.fetchone()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return response

        except:
            return 'Ocorreu um erro ao selecionar horario.'


    def deletar_horarios(self, id_horario):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"DELETE FROM horarios WHERE id_horario = {id_horario}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return "horario deletado com sucesso"

        except:
            return 'Ocorreu um erro ao deletar'

