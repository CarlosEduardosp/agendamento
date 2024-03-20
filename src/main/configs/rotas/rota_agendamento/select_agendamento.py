from fastapi import APIRouter
from src.main.adapter.adapter_agendamento.adapter_agendamento import AdapterAgendamento
from src.main.composer.agendamento_composer.agendamento_composer import register_agendamento_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.get('/select_agendamento')
async def select_agendamento():
    """
    seleciona os agendamentos no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={}
    )

    response = request.select_adapter()

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
