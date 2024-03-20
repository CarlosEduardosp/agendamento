from fastapi import APIRouter
from src.main.adapter.adapter_cliente.adapter_cliente import AdapterCliente
from src.main.composer.cliente_composer.cliente_composer import register_cliente_composer
from src.main.validacao.inserir_cliente_validar import Item

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.post('/insert_cliente')
async def insert_cliente(item: Item):
    """
    inserir cliente no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterCliente(
        api_route=register_cliente_composer(),
        data={
            "nome": item.nome,
            "data_nascimento": item.data_nascimento,
            "telefone1": item.telefone1,
            "telefone2": item.telefone2,
            "email": item.email,
            "senha": item.senha
        }
    )

    response = request.insert_adapter()

    return response
