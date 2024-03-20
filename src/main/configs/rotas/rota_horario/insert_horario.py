from fastapi import APIRouter
from src.main.adapter.adapter_horario.adapter_horario import AdapterHorario
from src.main.composer.horario_composer.horario_composer import register_horario_composer
from src.main.validacao.inserir_horario_validar import ItemHorario

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.post('/insert_horario')
async def insert_horario(item: ItemHorario):
    """
    inserir horario no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterHorario(
        api_route=register_horario_composer(),
        data={
            "horario": item.horario,
            "status": item.status,
        }
    )

    response = request.insert_adapter()

    return response
