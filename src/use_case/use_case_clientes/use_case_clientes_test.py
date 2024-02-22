from faker import Faker
from src.use_case.use_case_clientes.use_case_clientes import ClientesUseCase
from src.infra.repositorio.clientes.clientes import InserirCliente

faker = Faker()


def test_inserir_cliente_use_case():

    repository = InserirCliente()
    pessoa = ClientesUseCase(repository)

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
    repository = InserirCliente()
    pessoa = ClientesUseCase(repository)

    response = pessoa.listar_clientes()

    print(response)


def test_select_cliente_id():
    repository = InserirCliente()
    pessoa = ClientesUseCase(repository)

    response = pessoa.encontrar_cliente_por_id(cliente_id=2)

    print(response)


def test_deletar():
    repository = InserirCliente()
    pessoa = ClientesUseCase(repository)

    response = pessoa.deletar_cliente(cliente_id=4)

    print(response)


def test_update():
    repository = InserirCliente()
    pessoa = ClientesUseCase(repository)

    cliente_id = 1

    response = pessoa.atualizar_cliente(
        cliente_id=cliente_id,
        nome='atualizado',
        data_nascimento=str(faker.random_number(digits=8)),
        telefone1=faker.name(),
        telefone2=faker.name(),
        email=faker.email(),
        senha=faker.password()
    )

    print(response)
