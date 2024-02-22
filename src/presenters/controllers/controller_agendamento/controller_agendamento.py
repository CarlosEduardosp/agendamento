from typing import Type
from src.use_case.use_case_agendamento.agendamento import AgendamentoUseCase
from src.presenters.erros.http_erros import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.interfaces.interface_controller.interface_agendamento_controller import RouteInterfaceAgendamento


class RegisterAgendamentoController(RouteInterfaceAgendamento):
    """ Class controller """

    def __init__(self, register_agendamento_use_case: Type[AgendamentoUseCase]):
        self.register_agendamento_use_case = register_agendamento_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "id_servico" in query_string_params and
                "id_cliente" in query_string_params and
                "horario" in query_string_params and
                "data" in query_string_params
            ):
                id_servico = http_request.query['id_servico']
                id_cliente = http_request.query['id_cliente']
                horario = http_request.query['horario']
                data = http_request.query['data']

                response = self.register_agendamento_use_case.criar_agendamento(
                    id_servico=id_servico,
                    id_cliente=id_cliente,
                    horario=horario,
                    data=data
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

            response = self.register_agendamento_use_case.listar_agendamentos()


            return HttpResponse(status_code=200, body=response['data'])

        except:
            return {'success': False, "data": None}

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "id_cliente" in query_string_params:

                response = self.register_agendamento_use_case.encontrar_agendamento_por_id_by_cliente(http_request.query['id_cliente'])
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

            if "id_agendamento" in query_string_params:

                id_agendamento = http_request.query['id_agendamento']

                response = self.register_agendamento_use_case.deletar_agendamento(id_agendamento=id_agendamento)

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