from typing import Type, Dict
from src.interfaces.interface_adapter.interface_cliente_adapter import RouteInterfaceCliente as Route
from src.presenters.helpers.http_models import HttpRequest, HttpResponse
from src.presenters.erros.http_erros import HttpErrors


class AdapterCliente:

    def __init__(self, api_route: Type[Route], data: Type[Dict]) -> any:
        self.api_route = api_route
        self.data = data
        self.query_data = data.keys()

    def insert_adapter(self):
        if "nome" and "data_nascimento" and "telefone1" and "telefone2" and "email" and "senha" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_insert(http_request)

            return response

        return self.__error()

    def select_adapter(self):
        http_request = HttpRequest(query=self.data)
        response = self.api_route.route_select_all(http_request)

        return response

    def select_by_id_adapter(self):
        if "cliente_id" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_select_by_id(http_request)
            return response

        return self.__error()

    def delete_adapter(self):
        if "cliente_id" in self.query_data:
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_delete(http_request)

            return response

        return self.__error()

    def update_adapter(self):
        if (
                "cliente_id"
                and "nome"
                and "data_nascimento"
                and "telefone1"
                and "telefone2"
                and "email"
                and "senha"
                in self.query_data
        ):
            http_request = HttpRequest(query=self.data)
            response = self.api_route.route_update(http_request)

            return response

        return self.__error()

    def __error(self):
        http_error = HttpErrors()
        return http_error.error_422()