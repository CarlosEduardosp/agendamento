from pydantic import BaseModel


class Item(BaseModel):
    """ classe para inserir e validar dados de cliente."""

    nome: str
    data_nascimento: str
    telefone1: str
    telefone2: str
    email: str
    senha: str
