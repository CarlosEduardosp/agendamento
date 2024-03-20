from fastapi import APIRouter
from src.main.adapter.adapter_cliente.adapter_cliente import AdapterCliente
from src.main.composer.cliente_composer.cliente_composer import register_cliente_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.delete('/delete_cliente')
async def delete_cliente(id: int):
    """
    Deleta cliente do banco de dados pelo Id de registro.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterCliente(
        api_route=register_cliente_composer(),
        data={'cliente_id': id}
    )

    response = request.delete_adapter()

    return response
