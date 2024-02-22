from abc import ABC, abstractmethod


class InterfaceServicoRepository(ABC):
    @abstractmethod
    def criar_servico(self, nome_servico, descricao_servico):
        pass

    @abstractmethod
    def listar_servico(self):
        pass

    @abstractmethod
    def encontrar_servico_por_id(self, id_servico):
        pass

    @abstractmethod
    def atualizar_servico(self, id_servico, nome_servico, descricao_servico):
        pass

    @abstractmethod
    def deletar_servico(self, id_servico):
        pass