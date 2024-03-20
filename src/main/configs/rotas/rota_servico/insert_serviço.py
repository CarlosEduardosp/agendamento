from fastapi import APIRouter
from src.main.adapter.adapter_servico.adapter_servico import AdapterServico
from src.main.composer.servico_composer.servico_composer import register_servico_composer
from src.main.validacao.inserir_servico_validar import ItemServico

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.post('/insert_servico')
async def insert_servico(item: ItemServico):
    """
    inserir serviço no banco de dados.
    """
    # Criando uma instância do AdapterServico
    request = AdapterServico(
        api_route=register_servico_composer(),
        data={
            "nome_servico": item.nome_serviço,
            "descricao_servico": item.descricao_servico,
        }
    )

    response = request.insert_adapter()

    return response
