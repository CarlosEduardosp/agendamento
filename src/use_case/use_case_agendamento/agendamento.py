from src.interfaces.interface_use_case.interface_agendamento import InterfaceAgendamentoUseCase
from src.infra.repositorio.agendamento.agendamento import Inseriragendamento
from typing import Type


class AgendamentoUseCase(InterfaceAgendamentoUseCase):

    def __init__(self, agendamento_repository: Type[Inseriragendamento]):
        self.agendamento_repository = agendamento_repository

    def criar_agendamento(self, id_servico, data, horario, id_cliente):

        validade_entry = isinstance(id_servico, int) \
                         and isinstance(data, str) \
                         and isinstance(horario, str) \
                         and isinstance(id_cliente, int)

        try:
            if validade_entry:

                response = self.agendamento_repository.criar_agendamento(
                    id_servico=id_servico,
                    data=data,
                    horario=horario,
                    id_cliente=id_cliente
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def listar_agendamentos(self):

        try:
            response = self.agendamento_repository.listar_agendamentos()

            return {'success': True, 'data': response}

        except:

            return {'success': False, 'data': None}

    def encontrar_agendamento_por_id_by_cliente(self, id_cliente):

        validade_entry = isinstance(id_cliente, int)

        try:
            if validade_entry:

                response = self.agendamento_repository.encontrar_agendamento_por_id_by_cliente(id_cliente=id_cliente)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def deletar_agendamento(self, id_agendamento):

        validade_entry = isinstance(id_agendamento, int)

        try:
            if validade_entry:

                response = self.agendamento_repository.deletar_agendamento(id_agendamento=id_agendamento)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

