from faker import Faker
from .servico import InserirServico


faker = Faker()


def test_criar_servico():

    servico = InserirServico()

    response = servico.criar_servico(
        nome_servico=faker.name(),
        descricao_servico=faker.text()
    )

    print(response)


def test_listar_servico():
    servico = InserirServico()

    response = servico.listar_servico()

    print(response)


def test_encontrar_serv_id():
    servico = InserirServico()

    response = servico.encontrar_servico_por_id(
        id_servico=1
    )

    print(response)


def test_deletar_servico():
    servico = InserirServico()

    response = servico.deletar_servico(
        id_servico=2
    )

    print(response)


def test_atualizar_servico():
    servico = InserirServico()

    response = servico.atualizar_servico(
        id_servico=3,
        nome_servico='serviço atualizado',
        descricao_servico='descrição do serviço'
    )

    print(response)