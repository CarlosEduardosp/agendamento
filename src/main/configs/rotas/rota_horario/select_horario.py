from fastapi import APIRouter
from src.main.adapter.adapter_horario.adapter_horario import AdapterHorario
from src.main.composer.horario_composer.horario_composer import register_horario_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.get('/select_horario')
async def select_horario():
    """
    selecionar todos os horarios no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterHorario(
        api_route=register_horario_composer(),
        data={}
    )

    response = request.select_adapter()

    lista = []
    for i in response.body:
        dados = {
            "id_horario": i['id_horario'],
            "horario": i['horario'],
            "status": i['status'],
        }
        lista.append(dados)

    return lista
