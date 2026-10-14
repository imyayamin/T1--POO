from pessoa import Pessoa

class Paciente(Pessoa):

    def __init__(self, nome: str, celular: str, cpf: str, idade: int):
        super().__init__(nome, celular, cpf)
        self.__idade = idade
        self.__acompanhante = None

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def acompanhante(self):
        return self.__acompanhante

    @acompanhante.setter
    def acompanhante(self, acompanhante):
        self.__acompanhante = acompanhante