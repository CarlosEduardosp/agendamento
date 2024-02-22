from .use_case_servico import ServicoUseCase
from src.infra.repositorio.servico.servico import InserirServico
from faker import Faker

faker = Faker()


def test_servico_use_case():
    repository = InserirServico()
    servico = ServicoUseCase(repository)

    try:

        response = servico.criar_servico(
            nome_servico=faker.name(),
            descricao_servico=faker.text()
        )

        print('use case servico ok', response)

    except:
        print('ocorreu um erro no use case serviço.')


def test_select_servico_use_case():
    repository = InserirServico()
    servico = ServicoUseCase(repository)

    try:

        response = servico.listar_servico()
        print('Select servico ok', response)

    except:

        print('ocorreu um erro no use case serviço.')


def test_encontrar_id_use_case():
    repository = InserirServico()
    servico = ServicoUseCase(repository)

    try:

        response = servico.encontrar_servico_por_id(id_servico=1)

        print('use case select por id ok', response)

    except:
        print('ocorreu um erro no use case serviço.')


def test_deletar_servico_use_case():
    repository = InserirServico()
    servico = ServicoUseCase(repository)

    try:

        response = servico.deletar_servico(id_servico=3)

        print('use case deletar por id_servico ok', response)

    except:
        print('ocorreu um erro no use case servico.')


def test_servico_update_use_case():
    repository = InserirServico()
    servico = ServicoUseCase(repository)

    try:

        response = servico.atualizar_servico(
            nome_servico=faker.name(),
            descricao_servico=faker.text(),
            id_servico=2
        )

        print('use case servico ok', response)

    except:
        print('ocorreu um erro no use case serviço.')
