from entidade.paciente import Paciente
from exceptions.exceptions import PacienteRepetidoException

class ControladorPaciente:

    def __init__(self):
        self.__pacientes = []

    @property
    def pacientes(self):
        return self.__pacientes

    def cadastrar_paciente(self, nome, celular, cpf, idade):

        for paciente in self.__pacientes:

            if paciente.cpf == cpf:
                raise PacienteRepetidoException(novo_paciente.cpf)

        novo_paciente = Paciente(nome, celular, cpf, idade)

        self.__pacientes.append(novo_paciente)

        return "Paciente cadastrado com sucesso!"