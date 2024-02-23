from src.infra.repositorio.clientes.clientes import InserirCliente
from src.use_case.use_case_clientes.use_case_clientes import ClientesUseCase
from src.presenters.controllers.controller_clientes.controller_cliente import RegisterClienteController
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from faker import Faker

faker = Faker()


def test_criar_cliente_controller():

      repositorio = InserirCliente()
      usecase = ClientesUseCase(repositorio)
      registercontroller = RegisterClienteController(usecase)

      http_request = HttpRequest()

      data = {
        'nome': faker.name(),
        'data_nascimento': str(faker.random_number(digits=8)),
        'telefone1': faker.name(),
        'telefone2': faker.name(),
        'email': faker.email(),
        'senha': faker.password()
      }

      http_request.query = data
      http_request.body = None

      response = registercontroller.route_insert(http_request=http_request)

      print(response)


def test_select_cliente_controller():
    repositorio = InserirCliente()
    usecase = ClientesUseCase(repositorio)
    registercontroller = RegisterClienteController(usecase)

    http_request = HttpRequest()

    data = {}

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_all(http_request=http_request)

    print(response)


def test_encontrar_id_cliente_controller():
    repositorio = InserirCliente()
    usecase = ClientesUseCase(repositorio)
    registercontroller = RegisterClienteController(usecase)

    http_request = HttpRequest()

    data = {
        'cliente_id': 1
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_select_by_id(http_request=http_request)

    print(response)


def test_deletar_cliente_controller():
    repositorio = InserirCliente()
    usecase = ClientesUseCase(repositorio)
    registercontroller = RegisterClienteController(usecase)

    http_request = HttpRequest()

    data = {
        'cliente_id': 2
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_delete(http_request=http_request)

    print(response)


def test_update_cliente_controller():
    repositorio = InserirCliente()
    usecase = ClientesUseCase(repositorio)
    registercontroller = RegisterClienteController(usecase)

    http_request = HttpRequest()

    data = {
        'nome': faker.name(),
        'data_nascimento': str(faker.random_number(digits=8)),
        'telefone1': faker.name(),
        'telefone2': faker.name(),
        'email': faker.email(),
        'senha': faker.password(),
        'cliente_id': 3
    }

    http_request.query = data
    http_request.body = None

    response = registercontroller.route_update(http_request=http_request)

    print(response)
