from typing import Type, Dict
from src.interfaces.interface_adapter.interface_adapter_agendamento import RouteInterfaceAgendamento as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.erros.http_erros import HttpErrors


class AdapterAgendamento:

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data
        self.query_data = data.keys()

    def insert_adapter(self):
        if "id_servico" and "id_cliente" and "horario" and "data" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert(http_request)

            return response

        return self.__error()

    def select_adapter(self):
        http_request = HttpRequest(query=self.data)
        response = self.api_route.route_select_all(http_request)

        return response

    def select_by_id_adapter(self):
        if "id_cliente" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select_by_id(http_request)
            return response

        return self.__error()

    def delete_adapter(self):
        if "id_agendamento" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()