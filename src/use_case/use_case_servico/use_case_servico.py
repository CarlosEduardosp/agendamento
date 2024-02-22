from src.interfaces.interface_use_case.interface_servico import InterfaceServicoUseCase
from src.infra.repositorio.servico.servico import InserirServico
from typing import Type


class ServicoUseCase(InterfaceServicoUseCase):

    def __init__(self, servico_repository: Type[InserirServico]):
        self.servico_repository = servico_repository

    def criar_servico(self, nome_servico, descricao_servico):

        validade_entry = isinstance(nome_servico, str) \
                         and isinstance(descricao_servico, str)

        try:
            if validade_entry:

                response = self.servico_repository.criar_servico(
                    nome_servico=nome_servico,
                    descricao_servico=descricao_servico
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def listar_servico(self):

        try:
            response = self.servico_repository.listar_servico()

            return {'success': True, 'data': response}

        except:

            return {'success': False, 'data': None}

    def encontrar_servico_por_id(self, id_servico):

        validade_entry = isinstance(id_servico, int)

        try:
            if validade_entry:

                response = self.servico_repository.encontrar_servico_por_id(id_servico=id_servico)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def deletar_servico(self, id_servico):

        validade_entry = isinstance(id_servico, int)

        try:
            if validade_entry:

                response = self.servico_repository.deletar_servico(
                    id_servico=id_servico
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def atualizar_servico(self, id_servico, nome_servico, descricao_servico):

        validade_entry = isinstance(nome_servico, str) \
                         and isinstance(descricao_servico, str) and \
                        isinstance(id_servico, int)

        try:
            if validade_entry:

                response = self.servico_repository.atualizar_servico(
                    nome_servico=nome_servico,
                    descricao_servico=descricao_servico,
                    id_servico=id_servico
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}
