from fastapi import APIRouter
from src.main.adapter.adapter_horario.adapter_horario import AdapterHorario
from src.main.composer.horario_composer.horario_composer import register_horario_composer

# Criando o objeto APIRouter
router = APIRouter()


@router.delete('/delete_horario_by_id')
async def delete_horario_by_id(id_horario: int):
    """
    selecionar todos os horarios no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterHorario(
        api_route=register_horario_composer(),
        data={"id_horario": id_horario}
    )

    response = request.delete_adapter()

    return response
