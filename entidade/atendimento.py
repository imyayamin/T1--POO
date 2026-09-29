#Cada atendimento deve conter: clínica, paciente, profissional, data, horário (início e fim), tipo de
#atendimento (consulta, exame, retorno, etc.) e valo
from paciente import Paciente
from profissional import Profissional
from clinica import Clinica
from datetime import date, time

class Atendimento:
    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, data: date, horario_inicio: time, horario_fim: time, tipoAtendimento: str):
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__tipoAtendimento = tipoAtendimento

