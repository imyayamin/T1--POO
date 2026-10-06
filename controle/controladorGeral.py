from controladorPaciente import ControladorPaciente
from controladorProfissional import ControladorProfissional
from controladorClinica import ControladorClinica
from controladorAcompanhante import ControladorAcompanhante
from controladorAtendimento import ControladorAtendimento
from controladorPagamento import ControladorPagamento

class ControladorGeral:

    def __init__(self):

        self.__controladorPaciente = (ControladorPaciente())
        self.__controladorProfissional = (ControladorProfissional())
        self.__controladorClinica = (ControladorClinica())
        self.__controladorAcompanhante = (ControladorAcompanhante())
        self.__controladorAtendimento = (ControladorAtendimento(self.__controladorClinica, self.__controladorPaciente, self.__controladorProfissional, self.__controladorAcompanhante))
        self.__controladorPagamento = (ControladorPagamento())

    @property
    def controladorPaciente(self):
        return self.__controladorPaciente

    @property
    def controladorProfissional(self):
        return self.__controladorProfissional

    @property
    def controladorClinica(self):
        return self.__controladorClinica

    @property
    def controladorAcompanhante(self):
        return self.__controladorAcompanhante

    @property
    def controladorAtendimento(self):
        return self.__controladorAtendimento

    @property
    def controladorPagamento(self):
        return self.__controladorPagamento