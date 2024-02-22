from abc import ABC, abstractmethod


class InterfaceAgendamentoRepository(ABC):
    @abstractmethod
    def criar_agendamento(self, id_servico, data, horario, id_cliente):
        pass

    @abstractmethod
    def listar_agendamentos(self):
        pass

    @abstractmethod
    def encontrar_agendamento_por_id_by_cliente(self, id_cliente):
        pass

    @abstractmethod
    def deletar_agendamento(self, id_agendamento):
        pass