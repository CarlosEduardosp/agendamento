from pydantic import BaseModel


class UpdateItem(BaseModel):
    """ classe para atualizar e validar dados de serviços."""

    id_servico: int
    nome_servico: str
    descricao_servico: str

