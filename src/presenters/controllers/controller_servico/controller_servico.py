from typing import Type
from src.use_case.use_case_servico.use_case_servico import InserirServico
from src.presenters.erros.http_erros import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.interfaces.interface_controller.interface_servico_controller import RouteInterfaceServico


class RegisterServicoController(RouteInterfaceServico):
    """ Class controller """

    def __init__(self, register_servico_use_case: Type[InserirServico]):
        self.register_servico_use_case = register_servico_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "nome_servico" in query_string_params and
                "descricao_servico" in query_string_params
            ):
                nome_servico = http_request.query['nome_servico']
                descricao_servico = http_request.query['descricao_servico']

                response = self.register_servico_use_case.criar_servico(
                    nome_servico=nome_servico,
                    descricao_servico=descricao_servico
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

            response = self.register_servico_use_case.listar_servico()

            return HttpResponse(status_code=200, body=response['data'])

        except:
            return {'success': False, "data": None}

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "id_servico" in query_string_params:

                response = self.register_servico_use_case.encontrar_servico_por_id(http_request.query['id_servico'])
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

            if "id_servico" in query_string_params:

                id_servico = http_request.query['id_servico']

                response = self.register_servico_use_case.deletar_servico(id_servico=id_servico)

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
                "nome_servico" in query_string_params and
                "descricao_servico" in query_string_params and
                "id_servico" in query_string_params
            ):
                nome_servico = http_request.query['nome_servico']
                descricao_servico = http_request.query['descricao_servico']
                id_servico = http_request.query['id_servico']

                response = self.register_servico_use_case.atualizar_servico(
                    nome_servico=nome_servico,
                    descricao_servico=descricao_servico,
                    id_servico=id_servico
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