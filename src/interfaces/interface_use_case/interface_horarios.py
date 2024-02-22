from abc import ABC, abstractmethod


class InterfacehorariosUseCase(ABC):
    @abstractmethod
    def criar_horarios(self, horario, status):
        pass

    @abstractmethod
    def listar_horarios(self):
        pass

    @abstractmethod
    def encontrar_horarios_por_status(self, status):
        pass

    @abstractmethod
    def encontrar_horarios_por_id(self, id_horario):
        pass

    @abstractmethod
    def deletar_horarios(self, id_horario):
        pass