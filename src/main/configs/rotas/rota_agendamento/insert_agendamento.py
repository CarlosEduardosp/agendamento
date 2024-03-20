from fastapi import APIRouter
from src.main.adapter.adapter_agendamento.adapter_agendamento import AdapterAgendamento
from src.main.composer.agendamento_composer.agendamento_composer import register_agendamento_composer
from src.main.validacao.inserir_agendamento_validar import ItemAgendamento

# Criando o objeto APIRouter
router = APIRouter()


# Definindo a rota para a seleção de clientes
@router.post('/insert_agendamento')
async def insert_agendamento(item: ItemAgendamento):
    """
    inserir agendamento no banco de dados.
    """
    # Criando uma instância do AdapterCliente
    request = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={
            "id_servico": item.id_servico,
            "id_cliente": item.id_cliente,
            "horario": item.horario,
            "data": item.data
        }
    )

    response = request.insert_adapter()

    return response
