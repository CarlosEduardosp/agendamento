from fastapi import APIRouter
from src.main.adapter.adapter_servico.adapter_servico import AdapterServico
from src.main.composer.servico_composer.servico_composer import register_servico_composer
from src.main.validacao.inserir_servico_validar import ItemServico

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.delete('/delete_servico_by_id')
async def delete_servico_by_id(id_servico: int):
    """
    deleta serviço no banco de dados pelo id servico.
    """
    # Criando uma instância do AdapterServico
    request = AdapterServico(
        api_route=register_servico_composer(),
        data={"id_servico": id_servico}
    )

    response = request.delete_adapter()

    return {"success": 200, "body": response}
