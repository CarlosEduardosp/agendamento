import datetime

from pydantic import BaseModel


class ItemHorario(BaseModel):
    """ classe para inserir e validar dados em agendamento."""

    horario: str
    status: bool
