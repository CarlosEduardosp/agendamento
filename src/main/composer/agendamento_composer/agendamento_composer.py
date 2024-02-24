from src.interfaces.interface_adapter.interface_adapter_agendamento import RouteInterfaceAgendamento
from src.presenters.controllers.controller_agendamento.controller_agendamento import RegisterAgendamentoController
from src.use_case.use_case_agendamento.agendamento import AgendamentoUseCase
from src.infra.repositorio.agendamento.agendamento import Inseriragendamento


def register_agendamento_composer() -> RouteInterfaceAgendamento:
    """ composing register pessoa route """

    repository = Inseriragendamento()
    use_case = AgendamentoUseCase(repository)
    registrar_agendamento_route = RegisterAgendamentoController(use_case)

    return registrar_agendamento_route