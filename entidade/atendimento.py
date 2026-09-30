from paciente import Paciente
from profissional import Profissional
from clinica import Clinica
from datetime import date, time

class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, data: date, horario_inicio: time, horario_fim: time, tipoAtendimento: str, valor: float, acompanhante=None):
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipoAtendimento = tipoAtendimento
        self.__valor = valor
        self.__acompanhante = acompanhante

    @property
    def clinica(self):
        return self.__clinica

    @property
    def paciente(self):
        return self.__paciente

    @property
    def profissional(self):
        return self.__profissional

    @property
    def data(self):
        return self.__data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @property
    def tipoAtendimento(self):
        return self.__tipoAtendimento

    @property
    def valor(self):
        return self.__valor

    @property
    def acompanhante(self):
        return self.__acompanhante

    @clinica.setter
    def clinica(self, clinica: Clinica):
        self.__clinica = clinica

    @paciente.settter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @profissional.setter
    def profissional(self, profissional: Profissional):
        self.__profissional = profissional

    @data.setter
    def data(self, data: date):
        self.__data = data

    @horario_inicio.setter
    def horario_inicio(self, horario_incio: time):
        self.__horario_inicio = self.horario_inicio

    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        self.__horario_fim = horario_fim

    @tipoAtendimento.setter
    def tipoAtendimento(self, tipoAtendimento: str):
        self.__tipoAtendimento = tipoAtendimento

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

