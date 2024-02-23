from typing import Type
from src.use_case.use_case_clientes.use_case_clientes import ClientesUseCase
from src.presenters.erros.http_erros import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.interfaces.interface_controller.interface_cliente_controller import RouteInterfaceCliente


class RegisterClienteController(RouteInterfaceCliente):
    """ Class controller """

    def __init__(self, register_cliente_use_case: Type[ClientesUseCase]):
        self.register_cliente_use_case = register_cliente_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "nome" in query_string_params and
                "data_nascimento" in query_string_params and
                "telefone1" in query_string_params and
                "telefone2" in query_string_params and
                "email" in query_string_params and
                "senha" in query_string_params
            ):
                nome = http_request.query['nome']
                data_nascimento = http_request.query['data_nascimento']
                telefone1 = http_request.query['telefone1']
                telefone2 = http_request.query['telefone2']
                email = http_request.query['email']
                senha = http_request.query['senha']

                response = self.register_cliente_use_case.criar_cliente(
                    nome=nome,
                    data_nascimento=data_nascimento,
                    telefone1=telefone1,
                    telefone2=telefone2,
                    email=email,
                    senha=senha
                )

            else:
                response = {'success': False, 'data': None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

            # If no query in http_request
            http_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    def route_select_all(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select all controllers"""

        try:

            response = self.register_cliente_use_case.listar_clientes()

            return HttpResponse(status_code=200, body=response['data'])

        except:
            return {'success': False, "data": None}

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "cliente_id" in query_string_params:

                response = self.register_cliente_use_case.encontrar_cliente_por_id(http_request.query['cliente_id'])
                if response['success']:
                    return HttpResponse(status_code=200, body=response['data'])
                else:
                    return HttpResponse(status_code=400, body=response['data'])
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ delete controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "cliente_id" in query_string_params:

                cliente_id = http_request.query['cliente_id']

                response = self.register_cliente_use_case.deletar_cliente(cliente_id=cliente_id)

                return HttpResponse(status_code=200, body=response['data'])
            else:
                response = {'success': False, 'data': None}

        if response["success"] is False:
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

        return HttpResponse(status_code=200, body=response["data"])

        # If no query in http_request
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    def route_update(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "nome" in query_string_params and
                "data_nascimento" in query_string_params and
                "telefone1" in query_string_params and
                "telefone2" in query_string_params and
                "email" in query_string_params and
                "senha" in query_string_params and
                "cliente_id" in query_string_params
            ):
                nome = http_request.query['nome']
                data_nascimento = http_request.query['data_nascimento']
                telefone1 = http_request.query['telefone1']
                telefone2 = http_request.query['telefone2']
                email = http_request.query['email']
                senha = http_request.query['senha']
                cliente_id = http_request.query['cliente_id']

                response = self.register_cliente_use_case.atualizar_cliente(
                    nome=nome,
                    data_nascimento=data_nascimento,
                    telefone1=telefone1,
                    telefone2=telefone2,
                    email=email,
                    senha=senha,
                    cliente_id=cliente_id
                )

            else:
                response = {'success': False, 'data': None}

            if response["success"] is False:
                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )

            return HttpResponse(status_code=200, body=response["data"])

            # If no query in http_request
            http_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )