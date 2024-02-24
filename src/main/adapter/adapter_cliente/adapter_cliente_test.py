from src.main.composer.cliente_composer.cliente_composer import register_cliente_composer
from src.main.adapter.adapter_cliente.adapter_cliente import AdapterCliente
from faker import Faker


faker = Faker()


def test_insert_adapter():

    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={
            'nome': faker.name(),
            'data_nascimento': str(faker.random_number(digits=8)),
            'telefone1': faker.name(),
            'telefone2': faker.name(),
            'email': faker.email(),
            'senha': faker.password()
        },
    )
    response = buscar.insert_adapter()

    print(response)


def test_select():

    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={}
    )

    response = buscar.select_adapter()

    print(response)


def test_select_by_id():

    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={"cliente_id": 5}
    )

    response = buscar.select_by_id_adapter()
    print(response)


def test_delete_adapter():

    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={
            'cliente_id': 2
        }
    )

    response = buscar.delete_adapter()
    print(response)


def test_update_adapter():

    buscar = AdapterCliente(
        api_route=register_cliente_composer(),
        data={
            "cliente_id": 5,
            'nome': 'teste_atualização',
            'data_nascimento': str(faker.random_number(digits=8)),
            'telefone1': faker.name(),
            'telefone2': faker.name(),
            'email': faker.email(),
            'senha': faker.password()
        },
    )
    response = buscar.update_adapter()

    print(response)
