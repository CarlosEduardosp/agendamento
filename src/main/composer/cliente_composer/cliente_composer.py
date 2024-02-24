from src.interfaces.interface_adapter.interface_cliente_adapter import RouteInterfaceCliente
from src.presenters.controllers.controller_clientes.controller_cliente import RegisterClienteController
from src.use_case.use_case_clientes.use_case_clientes import ClientesUseCase
from src.infra.repositorio.clientes.clientes import InserirCliente


def register_cliente_composer() -> RouteInterfaceCliente:
    """ composing register pessoa route """

    repository = InserirCliente()
    use_case = ClientesUseCase(repository)
    registrar_cliente_route = RegisterClienteController(use_case)

    return registrar_cliente_route
