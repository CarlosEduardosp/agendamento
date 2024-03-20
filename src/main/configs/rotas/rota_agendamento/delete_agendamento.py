from fastapi import APIRouter
from src.main.adapter.adapter_agendamento.adapter_agendamento import AdapterAgendamento
from src.main.composer.agendamento_composer.agendamento_composer import register_agendamento_composer

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.delete('/delete_agendamento')
async def delete_agendamento(id_agendamento: int):
    """
    deletar os agendamentos no banco de dados pelo id agendamento.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={'id_agendamento': id_agendamento}
    )

    response = request.delete_adapter()

    return {'success': 200, 'body': response}
