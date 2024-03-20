import datetime

from pydantic import BaseModel


class ItemAgendamento(BaseModel):
    """ classe para inserir e validar dados em agendamento."""

    id_servico: int
    id_cliente: int
    horario: str
    data: str


