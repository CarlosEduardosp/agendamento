from faker import Faker
from src.infra.repositorio.clientes.clientes import InserirCliente


faker = Faker()


def test_inserir_cliente():

    pessoa = InserirCliente()

    response = pessoa.criar_cliente(
        nome=faker.name(),
        data_nascimento=str(faker.random_number(digits=8)),
        telefone1=faker.name(),
        telefone2=faker.name(),
        email=faker.email(),
        senha=faker.password()
        )

    print(response)


def test_select_todos():

    pessoa = InserirCliente()

    response = pessoa.listar_clientes()

    print(response)


def test_select_cliente_id():

    pessoa = InserirCliente()

    response = pessoa.encontrar_cliente_por_id(cliente_id=1)

    print(response)


def test_deletar():

    pessoa = InserirCliente()

    response = pessoa.deletar_cliente(cliente_id=3)
    
    print(response)


def test_update():

    pessoas = InserirCliente()

    cliente_id = 1

    response = pessoas.atualizar_cliente(
        cliente_id=cliente_id,
        nome='atualizado',
        data_nascimento=str(faker.random_number(digits=8)),
        telefone1=faker.name(),
        telefone2=faker.name(),
        email=faker.email(),
        senha=faker.password()
    )

    print(response)
