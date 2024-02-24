from src.interfaces.interface_adapter.interface_servico_adapter import RouteInterfaceServico
from src.presenters.controllers.controller_servico.controller_servico import RegisterServicoController
from src.use_case.use_case_servico.use_case_servico import ServicoUseCase
from src.infra.repositorio.servico.servico import InserirServico


def register_servico_composer() -> RouteInterfaceServico:
    """ composing register pessoa route """

    repository = InserirServico()
    use_case = ServicoUseCase(repository)
    registrar_servico_route = RegisterServicoController(use_case)

    return registrar_servico_route