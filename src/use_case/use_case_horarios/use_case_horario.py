from src.interfaces.interface_use_case.interface_horarios import InterfacehorariosUseCase
from src.infra.repositorio.horarios.horarios import InserirHorario
from typing import Type


class HorarioUseCase(InterfacehorariosUseCase):

    def __init__(self, horario_repository: Type[InserirHorario]):
        self.horario_repository = horario_repository

    def criar_horarios(self, horario, status):

        validade_entry = isinstance(horario, str) \
                         and isinstance(status, bool)

        try:
            if validade_entry:

                response = self.horario_repository.criar_horarios(
                    horario=horario,
                    status=status
                )

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def listar_horarios(self):

        try:
            response = self.horario_repository.listar_horarios()

            return {'success': True, 'data': response}

        except:

            return {'success': False, 'data': None}

    def encontrar_horarios_por_id(self, id_horario):

        validade_entry = isinstance(id_horario, int)

        try:
            if validade_entry:

                response = self.horario_repository.encontrar_horarios_por_id(id_horario)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def encontrar_horarios_por_status(self, status):

        validade_entry = isinstance(status,bool)

        try:
            if validade_entry:

                response = self.horario_repository.encontrar_horarios_por_status(status)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

    def deletar_horarios(self, id_horario):

        validade_entry = isinstance(id_horario, int)

        try:
            if validade_entry:

                response = self.horario_repository.deletar_horarios(id_horario=id_horario)

                return {'success': True, 'data': response}
            else:
                return {'success': False, 'data': 'dados invalidos'}
        except:

            return {'success': False, 'data': None}

