from src.infra.repositorio.servico.servico import InserirServico
from src.use_case.use_case_servico.use_case_servico import ServicoUseCase
from src.presenters.controllers.controller_servico.controller_servico import RegisterServicoController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker

faker = Faker()


def test_criar_servico_controller():

      repositorio = InserirServico()
      usecase = ServicoUseCase(repositorio)
      registercontroller = RegisterServicoController(usecase)

      http_request = HttpRequest()

      data = {
        'nome_servico':faker.name(),
        'descricao_servico':faker.text()
      }

      http_request.query = data
      http_request.body = None

      response = registercontroller.route_insert(http_request=http_request)

      print(response)


def test_select_servico_controller():
    repositorio = InserirServico()
    usecase = ServicoUseCase(repositorio)
    registercontroller = RegisterServicoController(usecase)

    http_request = HttpRequest()

    data = {}

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_all(http_request=http_request)

    print(response)


def test_encontrar_id_servico_controller():
    repositorio = InserirServico()
    usecase = ServicoUseCase(repositorio)
    registercontroller = RegisterServicoController(usecase)

    http_request = HttpRequest()

    data = {
        'id_servico': 1
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response)


def test_deletar_servico_controller():
    repositorio = InserirServico()
    usecase = ServicoUseCase(repositorio)
    registercontroller = RegisterServicoController(usecase)

    http_request = HttpRequest()

    data = {
        'id_servico': 3
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_delete(http_request=http_request)

    print(response)


def test_update_servico_controller():
    repositorio = InserirServico()
    usecase = ServicoUseCase(repositorio)
    registercontroller = RegisterServicoController(usecase)

    http_request = HttpRequest()

    data = {
        'nome_servico': faker.name(),
        'descricao_servico': faker.text(),
        'id_servico': 2
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_update(http_request=http_request)

    print(response)
