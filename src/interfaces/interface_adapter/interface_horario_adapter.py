from typing import Type
from abc import ABC, abstractmethod
from src.presenters.helpers.http_models import HttpRequest, HttpResponse


class RouteInterfaceHorario(ABC):
    """Interface to Routes"""

    @abstractmethod
    def route_insert(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_select_all(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_select_by_status(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_select_by_id(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")

    def route_delete(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Route"""

        raise Exception("Should implement method: route")
