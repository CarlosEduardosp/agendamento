from fastapi import APIRouter
from src.main.adapter.adapter_servico.adapter_servico import AdapterServico
from src.main.composer.servico_composer.servico_composer import register_servico_composer
from src.main.validacao.inserir_servico_validar import ItemServico

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.get('/select_servico_by_id/{id_servico}')
async def select_servico_by_id(id_servico: int):
    """
    Select serviço no banco de dados pelo id servico.
    """
    # Criando uma instância do AdapterServico
    request = AdapterServico(
        api_route=register_servico_composer(),
        data={"id_servico": id_servico}
    )

    response = request.select_by_id_adapter()

    lista = []
    for i in response.body:
        dados = {
            "id_servico": i['id_servico'],
            "nome_servico": i['nome_servico'],
            "descricao_servico": i['descricao_servico'],
        }

        lista.append(dados)

    return {"success": 200, "body": lista}
