from typing import Type
from src.use_case.use_case_horarios.use_case_horario import HorarioUseCase
from src.presenters.erros.http_erros import HttpErrors
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.interfaces.interface_controller.interface_horario_controller import RouteInterfaceHorario


class RegisterHorarioController(RouteInterfaceHorario):
    """ Class controller """

    def __init__(self, register_horario_use_case: Type[HorarioUseCase]):
        self.register_horario_use_case = register_horario_use_case

    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ method to call use case """

        response = None

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if(
                "horario" in query_string_params and
                "status" in query_string_params

            ):
                horario = http_request.query['horario']
                status = http_request.query['status']

                response = self.register_horario_use_case.criar_horarios(
                    horario=horario,
                    status=status
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

            response = self.register_horario_use_case.listar_horarios()

            return HttpResponse(status_code=200, body=response['data'])

        except:
            return {'success': False, "data": None}

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "id_horario" in query_string_params:

                response = self.register_horario_use_case.encontrar_horarios_por_id(http_request.query['id_horario'])
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

    def route_select_by_status(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ select by id controller """

        if http_request.query:

            query_string_params = (
                http_request.query.keys()
            )  # pega todas as chaves dentro de query

            if "status" in query_string_params:

                response = self.register_horario_use_case.encontrar_horarios_por_status(http_request.query['status'])
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

            if "id_horario" in query_string_params:

                id_horario = http_request.query['id_horario']

                response = self.register_horario_use_case.deletar_horarios(id_horario=id_horario)

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