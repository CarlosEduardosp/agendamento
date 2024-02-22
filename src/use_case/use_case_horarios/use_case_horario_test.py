from .use_case_horario import HorarioUseCase
from src.infra.repositorio.horarios.horarios import InserirHorario
from faker import Faker

faker = Faker()


def test_horario_use_case():
    repository = InserirHorario()
    horario = HorarioUseCase(repository)

    try:

        response = horario.criar_horarios(
            horario='10h',
            status=True
        )

        print('use case horario ok', response)

    except:
        print('ocorreu um erro no use case horarios.')


def test_select_horario_use_case():
    repository = InserirHorario()
    horario = HorarioUseCase(repository)

    try:

        response = horario.listar_horarios()
        print('Select horarios ok', response)

    except:

        print('ocorreu um erro no use case horarios.')


def test_encontrar_id_use_case():
    repository = InserirHorario()
    horario = HorarioUseCase(repository)

    try:

        response = horario.encontrar_horarios_por_id(
            id_horario=2
        )

        print('use case select por id ok', response)

    except:
        print('ocorreu um erro no use case horario.')


def test_encontrar_status_use_case():
    repository = InserirHorario()
    horario = HorarioUseCase(repository)

    try:

        response = horario.encontrar_horarios_por_status(
            status=True
        )

        print('use case select por status ok', response)

    except:
        print('ocorreu um erro no use case horario.')


def test_deletar_agendamento_use_case():
    repository = InserirHorario()
    horario = HorarioUseCase(repository)

    try:

        response = horario.deletar_horarios(
            id_horario=3
        )

        print('use case deletar por id_horario ok', response)

    except:
        print('ocorreu um erro no use case horario.')
