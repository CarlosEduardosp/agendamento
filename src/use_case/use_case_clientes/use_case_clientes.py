from src.interfaces.interface_use_case.interface_clientes import InterfaceClienteUseCase
from src.infra.repositorio.clientes.clientes import InserirCliente
from typing import Type


class ClientesUseCase(InterfaceClienteUseCase):

    def __init__(self, cliente_repository: Type[InserirCliente]):
        self.cliente_repository = cliente_repository

    def criar_cliente(self, nome, data_nascimento, telefone1, telefone2, email, senha):

        validade_entry = isinstance(nome, str) and \
                         isinstance(data_nascimento, str) and \
                         isinstance(telefone1, str) and \
                         isinstance(telefone2, str) and \
                         isinstance(email, str) and \
                         isinstance(senha, str)

        try:
            if validade_entry:

                response = self.cliente_repository.criar_cliente(
                    nome=nome,
                    data_nascimento=data_nascimento,
                    telefone1=telefone1,
                    telefone2=telefone2,
                    email=email,
                    senha=senha
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def listar_clientes(self):

        try:
            response = self.cliente_repository.listar_clientes()

            return {'success': True, 'data': response}

        except:

            return {'success': False, 'data': None}

    def encontrar_cliente_por_id(self, cliente_id):

        validade_entry = isinstance(cliente_id, int)

        try:
            if validade_entry:

                response = self.cliente_repository.encontrar_cliente_por_id(cliente_id=cliente_id)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def deletar_cliente(self, cliente_id):

        validade_entry = isinstance(cliente_id, int)

        try:
            if validade_entry:

                response = self.cliente_repository.deletar_cliente(cliente_id=cliente_id)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def atualizar_cliente(self, cliente_id, nome, data_nascimento, telefone1, telefone2, email, senha):

        validade_entry = isinstance(nome, str) and \
                         isinstance(data_nascimento, str) and \
                         isinstance(telefone1, str) and \
                         isinstance(telefone2, str) and \
                         isinstance(email, str) and \
                         isinstance(senha, str) and \
                         isinstance(cliente_id, int)

        try:
            if validade_entry:

                response = self.cliente_repository.atualizar_cliente(
                    cliente_id=cliente_id,
                    nome=nome,
                    data_nascimento=data_nascimento,
                    telefone1=telefone1,
                    telefone2=telefone2,
                    email=email,
                    senha=senha
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}
