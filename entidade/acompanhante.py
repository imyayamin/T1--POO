from pessoa import Pessoa

class Acompanhante(Pessoa):
    def __init__(self, nome: str, celular: str, cpf: str, idade: int):
        if isinstance(nome, str) and isinstance(celular, str) and isinstance(cpf, str):
            super().__init__(nome, celular, cpf)
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade