from src.main.composer.horario_composer.horario_composer import register_horario_composer
from src.main.adapter.adapter_horario.adapter_horario import AdapterHorario
from faker import Faker


faker = Faker()


def test_insert_adapter():

    buscar = AdapterHorario(
        api_route=register_horario_composer(),
        data={
            "horario": '20h',
            "status": False,
        },
    )
    response = buscar.insert_adapter()

    print(response)


def test_select():

    buscar = AdapterHorario(
        api_route=register_horario_composer(),
        data={}
    )

    response = buscar.select_adapter()

    print(response)


def test_select_by_id():

    buscar = AdapterHorario(
        api_route=register_horario_composer(),
        data={"id_horario": 2}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def test_select_by_status():

    buscar = AdapterHorario(
        api_route=register_horario_composer(),
        data={"status": False}
    )

    response = buscar.select_by_status_adapter()
    print(response)


def test_delete_adapter():

    buscar = AdapterHorario(
        api_route=register_horario_composer(),
        data={
            'id_horario': 1
        }
    )

    response = buscar.delete_adapter()
    print(response)
