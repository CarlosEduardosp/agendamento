from fastapi import APIRouter
from src.main.adapter.adapter_horario.adapter_horario import AdapterHorario
from src.main.composer.horario_composer.horario_composer import register_horario_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.get('/select_horario_by_id/{id_horario}')
async def select_horario_by_id(id_horario: int):
    """
    selecionar todos os horarios no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterHorario(
        api_route=register_horario_composer(),
        data={"id_horario": id_horario}
    )

    response = request.select_by_id_adapter()

    lista = []
    for i in response.body:
        dados = {
            "id_horario": i['id_horario'],
            "horario": i['horario'],
            "status": i['status'],
        }
        lista.append(dados)

    return lista
