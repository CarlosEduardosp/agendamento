from src.interfaces.interface_adapter.interface_horario_adapter import RouteInterfaceHorario
from src.presenters.controllers.controller_horario.controller_horario import RegisterHorarioController
from src.use_case.use_case_horarios.use_case_horario import HorarioUseCase
from src.infra.repositorio.horarios.horarios import InserirHorario


def register_horario_composer() -> RouteInterfaceHorario:
    """ composing register pessoa route """

    repository = InserirHorario()
    use_case = HorarioUseCase(repository)
    registrar_horario_route = RegisterHorarioController(use_case)

    return registrar_horario_route
