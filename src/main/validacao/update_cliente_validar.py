from pydantic import BaseModel


class UpdateItem(BaseModel):
    """ classe para atualizar e validar dados de cliente."""

    id: int
    nome: str
    data_nascimento: str
    telefone1: str
    telefone2: str
    email: str
    senha: str
