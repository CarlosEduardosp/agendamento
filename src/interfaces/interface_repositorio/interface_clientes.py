from abc import ABC, abstractmethod


class InterfaceClienteRepository(ABC):
    @abstractmethod
    def criar_cliente(self, nome, data_nascimento, telefone1, telefone2, email, senha):
        pass

    @abstractmethod
    def listar_clientes(self):
        pass

    @abstractmethod
    def encontrar_cliente_por_id(self, cliente_id):
        pass

    @abstractmethod
    def atualizar_cliente(self, cliente_id, nome, data_nascimento, telefone1, telefone2, email, senha):
        pass

    @abstractmethod
    def deletar_cliente(self, cliente_id):
        pass