from datetime import time

class Clinica:

    def __init__(self, nome: str, cidade: str, descricao: str, horario_funcionamento_inicial: time, horario_funcionamento_final: time):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__horario_funcionamento_inicial = (horario_funcionamento_inicial)
        self.__horario_funcionamento_final = (horario_funcionamento_final)

    @property
    def nome(self):
        return self.__nome

    @property
    def cidade(self):
        return self.__cidade

    @property
    def descricao(self):
        return self.__descricao

    @property
    def horario_funcionamento_inicial(self):
        return self.__horario_funcionamento_inicial

    @property
    def horario_funcionamento_final(self):
        return self.__horario_funcionamento_final

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @horario_funcionamento_inicial.setter
    def horario_funcionamento_inicial(self, horario_funcionamento_inicial: time):
        self.__horario_funcionamento_inicial = (horario_funcionamento_inicial)

    @horario_funcionamento_final.setter
    def horario_funcionamento_final(self, horario_funcionamento_final: time):
        self.__horario_funcionamento_final = (horario_funcionamento_final)