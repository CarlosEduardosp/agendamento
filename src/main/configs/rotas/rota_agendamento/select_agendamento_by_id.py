from fastapi import APIRouter
from src.main.adapter.adapter_agendamento.adapter_agendamento import AdapterAgendamento
from src.main.composer.agendamento_composer.agendamento_composer import register_agendamento_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.get('/select_agendamento_by_id/{id}')
async def select_agendamento_by_id(id: int):
    """
    seleciona os agendamentos no banco de dados por id do cliente.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={'id_cliente': id}
    )

    response = request.select_by_id_adapter()

    lista = []
    for i in response.body:
        dados = {
            "id": i['id_agendamento'],
            "id_servico": i['id_servico'],
            "id_cliente": i['id_cliente'],
            "data": i['data'],
            "horario": i['horario'],
        }
        lista.append(dados)

    return {'success': 200, 'body': lista}
