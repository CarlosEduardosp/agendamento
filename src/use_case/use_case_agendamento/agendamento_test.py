from .agendamento import AgendamentoUseCase
from src.infra.repositorio.agendamento.agendamento import Inseriragendamento
from faker import Faker

faker = Faker()


def test_agendamento_use_case():

    repository = Inseriragendamento()
    agendar = AgendamentoUseCase(repository)

    try:

        response = agendar.criar_agendamento(
            id_servico=2,
            id_cliente=3,
            horario='08:00',
            data=faker.date()
        )

        print('use case inserir ok', response)

    except:
        print('ocorreu um erro no use case agendamento.')


def test_select_agendamento_use_case():
    
    repository = Inseriragendamento()
    agendar = AgendamentoUseCase(repository)


    
    try:

        response = agendar.listar_agendamentos()
        print('Select agendamento ok', response)
    
    except:
        
        print('ocorreu um erro no use case agendamento.')


def test_encontrar_id_use_case():

    repository = Inseriragendamento()
    agendar = AgendamentoUseCase(repository)

    try:

        response = agendar.encontrar_agendamento_por_id_by_cliente(
            id_cliente=1
        )

        print('use case select por id ok', response)

    except:
        print('ocorreu um erro no use case agendamento.')


def test_deletar_agendamento_use_case():

    repository = Inseriragendamento()
    agendar = AgendamentoUseCase(repository)

    try:

        response = agendar.deletar_agendamento(id_agendamento=2)

        print('use case deletar por id_agendamento ok', response)

    except:
        print('ocorreu um erro no use case agendamento.')
