from src.main.composer.agendamento_composer.agendamento_composer import register_agendamento_composer
from src.main.adapter.adapter_agendamento.adapter_agendamento import AdapterAgendamento
from faker import Faker


faker = Faker()


def test_insert_adapter():

    buscar = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={
            "id_servico": 55,
            "id_cliente": 2,
            "horario": '9h',
            "data": faker.date()
        },
    )
    response = buscar.insert_adapter()

    print(response)


def test_select():

    buscar = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={}
    )

    response = buscar.select_adapter()

    print(response)


def test_select_by_id():

    buscar = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={"id_cliente": 2}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def test_delete_adapter():

    buscar = AdapterAgendamento(
        api_route=register_agendamento_composer(),
        data={
            'id_agendamento': 2
        }
    )

    response = buscar.delete_adapter()
    print(response)
