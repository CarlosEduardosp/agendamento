from src.infra.repositorio.agendamento.agendamento import Inseriragendamento
from src.use_case.use_case_agendamento.agendamento import AgendamentoUseCase
from src.presenters.controllers.controller_agendamento.controller_agendamento import RegisterAgendamentoController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker

faker = Faker()


def test_criar_agendamento_controller():

      repositorio = Inseriragendamento()
      usecase = AgendamentoUseCase(repositorio)
      registercontroller = RegisterAgendamentoController(usecase)

      http_request = HttpRequest()

      data = {
        'id_servico': 10,
        'id_cliente': 3,
        'horario': '10h',
        'data': faker.date()
      }

      http_request.query = data
      http_request.body = None

      response = registercontroller.route_insert(http_request=http_request)

      print(response)


def test_select_agendamento_controller():
    repositorio = Inseriragendamento()
    usecase = AgendamentoUseCase(repositorio)
    registercontroller = RegisterAgendamentoController(usecase)

    http_request = HttpRequest()

    data = {}

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_all(http_request=http_request)

    print(response)


def test_encontrar_id_agendamento_controller():
    repositorio = Inseriragendamento()
    usecase = AgendamentoUseCase(repositorio)
    registercontroller = RegisterAgendamentoController(usecase)

    http_request = HttpRequest()

    data = {
        'id_cliente': 1
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response)


def test_deletar_agendamento_controller():
    repositorio = Inseriragendamento()
    usecase = AgendamentoUseCase(repositorio)
    registercontroller = RegisterAgendamentoController(usecase)

    http_request = HttpRequest()

    data = {
        'id_agendamento': 2
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_delete(http_request=http_request)

    print(response)
