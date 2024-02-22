from src.infra.configs.connection.connection_db import conectar_db
from src.infra.configs.connection.fechar_conexao import fechar_conexao_db
from src.interfaces.interface_repositorio.interface_servico import InterfaceServicoRepository


class InserirServico(InterfaceServicoRepository):

    def criar_servico(self, nome_servico, descricao_servico):

        # conectando ao banco
        connection = conectar_db()

        # criando um cursor
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO servico(nome_servico, descricao_servico)"
                       f"VALUES('{nome_servico}', '{descricao_servico}')")

        connection.commit()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return 'Serviço Inserido com sucesso'


    def listar_servico(self):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM servico;")

        connection.commit()

        response = cursor.fetchall()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return response

    def encontrar_servico_por_id(self, id_servico):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM servico WHERE id_servico = {id_servico};")

            connection.commit()

            response = cursor.fetchone()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return response

        except:
            return 'Ocorreu um erro ao selecionar servico.'


    def deletar_servico(self, id_servico):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"DELETE FROM servico WHERE id_servico = {id_servico}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return "sevico deletado com sucesso"

        except:
            return 'Ocorreu um erro ao deletar'


    def atualizar_servico(self, id_servico, nome_servico, descricao_servico):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(
                f"UPDATE servico SET "
                f"id_servico = '{id_servico}',"
                f"nome_servico = '{nome_servico}',"
                f"descricao_servico = '{descricao_servico}'"                                
                f"WHERE id_servico = {id_servico}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return "servico atualizada com sucesso"

        except:
            return 'Ocorreu um erro ao atualizar'

