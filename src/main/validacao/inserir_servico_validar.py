import datetime

from pydantic import BaseModel


class ItemServico(BaseModel):
    """ classe para inserir e validar dados em serviços."""

    nome_serviço: str
    descricao_servico: str
