from faker import Faker
from .agendamento import Inseriragendamento


faker = Faker()

def test_inserir_agendamento():

    agenda = Inseriragendamento()

    response = agenda.criar_agendamento(
        id_cliente=1,
        id_servico=1,
        data=faker.date(),
        horario='10h'
    )

    print(response)


def test_selecionar_agendamentos():

    agenda = Inseriragendamento()

    response = agenda.listar_agendamentos()

    print(response )


def test_selecionar_agendamentos_id():

    agenda = Inseriragendamento()

    response = agenda.encontrar_agendamento_por_id_by_cliente(
        id_cliente=1
    )

    print(response)


def test_deletar_agendamentos():

    agenda = Inseriragendamento()

    response = agenda.deletar_agendamento(id_agendamento=1)

    print(response )