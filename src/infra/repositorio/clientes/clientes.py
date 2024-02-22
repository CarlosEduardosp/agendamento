from src.infra.configs.connection.connection_db import conectar_db
from src.infra.configs.connection.fechar_conexao import fechar_conexao_db
from src.interfaces.interface_repositorio.interface_clientes import InterfaceClienteRepository


class InserirCliente(InterfaceClienteRepository):

    def criar_cliente(self, nome, data_nascimento, telefone1, telefone2, email, senha):

        # conectando ao banco
        connection = conectar_db()

        # criando um cursor
        cursor = connection.cursor()

        cursor.execute(f"INSERT INTO clientes(nome, data_nasc, telefone1, "
                       f"telefone2, email, senha)"
                       f"VALUES('{nome}', '{data_nascimento}', '{telefone1}',"
                       f"'{telefone2}', '{email}', '{senha}')")

        connection.commit()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return 'Cliente Inserido com sucesso'


    def listar_clientes(self):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM clientes;")

        connection.commit()

        response = cursor.fetchall()

        # fechando conexão com banco.
        fechar_conexao_db(cursor=cursor, connection=connection)

        return response

    def encontrar_cliente_por_id(self, cliente_id):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM clientes WHERE id_cliente = {cliente_id};")

            connection.commit()

            response = cursor.fetchone()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return response

        except:
            return 'Ocorreu um erro ao selecionar clientes.'


    def deletar_cliente(self, cliente_id):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(f"DELETE FROM clientes WHERE id_cliente = {cliente_id}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return "Pessoa deletado com sucesso"

        except:
            return 'Ocorreu um erro ao deletar'


    def atualizar_cliente(self, cliente_id, nome, data_nascimento, telefone1, telefone2, email, senha):

        # conectando ao banco
        connection = conectar_db()

        cursor = connection.cursor()

        try:
            cursor.execute(
                f"UPDATE clientes SET "
                f"nome = '{nome}',"
                f"data_nasc = '{data_nascimento}',"
                f"telefone1 = '{telefone1}',"
                f"telefone2 = '{telefone2}',"
                f"email = '{email}',"
                f"senha = '{senha}'"                
                f"WHERE id_cliente = {cliente_id}")
            connection.commit()

            # fechando conexão com banco.
            fechar_conexao_db(cursor=cursor, connection=connection)

            return "Pessoa atualizada com sucesso"

        except:
            return 'Ocorreu um erro ao atualizar'

