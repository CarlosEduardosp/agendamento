from faker import Faker
from .horarios import InserirHorario


faker = Faker()


def test_criar_horario():

    horario = InserirHorario()

    response = horario.criar_horarios(
        horario='08:30h',
        status=True
    )

    print(response)


def test_listar_horarios():
    horario = InserirHorario()

    response = horario.listar_horarios()

    print(response)


def test_encontrar_horario_id():
    horario = InserirHorario()
    response = horario.encontrar_horarios_por_id(id_horario=1)

    print(response)


def test_encontrar_horario_status():
    horario = InserirHorario()
    response = horario.encontrar_horarios_por_status(status=True)

    print(response)


def test_deletar_horario():
    horario = InserirHorario()

    response = horario.deletar_horarios(
        id_horario=3
    )
    print(response)


