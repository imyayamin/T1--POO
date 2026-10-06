from profissional import Profissional

class Procedimento:

    def __init__(self, descricao: str, custo: float, profissional: Profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    def descricao(self):
        return self.__descricao

    @property
    def custo(self):
        return self.__custo

    @property
    def profissional(self):
        return self.__profissional

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @custo.setter
    def custo(self, custo: float):
        self.__custo = custo

    @profissional.setter
    def profissional(self, profissional: Profissional):
        self.__profissional = profissional