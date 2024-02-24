from src.main.composer.servico_composer.servico_composer import register_servico_composer
from src.main.adapter.adapter_servico.adapter_servico import AdapterServico
from faker import Faker


faker = Faker()


def test_insert_adapter():

    buscar = AdapterServico(
        api_route=register_servico_composer(),
        data={
            "nome_servico": faker.name(),
            "descricao_servico": faker.text(),
        },
    )
    response = buscar.insert_adapter()

    print(response)


def test_select():

    buscar = AdapterServico(
        api_route=register_servico_composer(),
        data={}
    )

    response = buscar.select_adapter()

    print(response)


def test_select_by_id():

    buscar = AdapterServico(
        api_route=register_servico_composer(),
        data={"id_servico": 12}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def test_delete_adapter():

    buscar = AdapterServico(
        api_route=register_servico_composer(),
        data={
            'id_servico': 8
        }
    )

    response = buscar.delete_adapter()
    print(response)


def test_update_adapter():

    buscar = AdapterServico(
        api_route=register_servico_composer(),
        data={
            "nome_servico": faker.name(),
            "descricao_servico": faker.text(),
            "id_servico": 1
        },
    )
    response = buscar.update_adapter()

    print(response)

