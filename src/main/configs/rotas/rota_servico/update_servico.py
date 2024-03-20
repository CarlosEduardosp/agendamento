from fastapi import APIRouter
from src.main.adapter.adapter_servico.adapter_servico import AdapterServico
from src.main.composer.servico_composer.servico_composer import register_servico_composer
from src.main.validacao.update_servico_validar import UpdateItem

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.put('/update_servico')
async def update_servico(item: UpdateItem):
    """
    inserir serviço no banco de dados.
    """
    # Criando uma instância do AdapterServico
    request = AdapterServico(
        api_route=register_servico_composer(),
        data={
            "id_servico": item.id_servico,
            "nome_servico": item.nome_servico,
            "descricao_servico": item.descricao_servico,
        }
    )

    response = request.update_adapter()

    return response
