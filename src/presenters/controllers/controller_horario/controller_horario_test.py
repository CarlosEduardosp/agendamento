from src.infra.repositorio.horarios.horarios import InserirHorario
from src.use_case.use_case_horarios.use_case_horario import HorarioUseCase
from src.presenters.controllers.controller_horario.controller_horario import RegisterHorarioController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker

faker = Faker()


def test_criar_horario_controller():

      repositorio = InserirHorario()
      usecase = HorarioUseCase(repositorio)
      registercontroller = RegisterHorarioController(usecase)

      http_request = HttpRequest()

      data = {
        'horario': '11h',
        'status': True

      }

      http_request.query = data
      http_request.body = None

      response = registercontroller.route_insert(http_request=http_request)

      print(response)


def test_select_horario_controller():
    repositorio = InserirHorario()
    usecase = HorarioUseCase(repositorio)
    registercontroller = RegisterHorarioController(usecase)


    http_request = HttpRequest()

    data = {}

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_all(http_request=http_request)

    print(response)


def test_encontrar_id_horario_controller():
    repositorio = InserirHorario()
    usecase = HorarioUseCase(repositorio)
    registercontroller = RegisterHorarioController(usecase)


    http_request = HttpRequest()

    data = {
        'id_horario': 1
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response)


def test_encontrar_status_horario_controller():
    repositorio = InserirHorario()
    usecase = HorarioUseCase(repositorio)
    registercontroller = RegisterHorarioController(usecase)

    http_request = HttpRequest()

    data = {
        'status': True
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_by_status(http_request=http_request)

    print(response)


def test_deletar_horario_controller():
    repositorio = InserirHorario()
    usecase = HorarioUseCase(repositorio)
    registercontroller = RegisterHorarioController(usecase)

    http_request = HttpRequest()

    data = {
        'id_agendamento': 2
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_delete(http_request=http_request)

    print(response)
