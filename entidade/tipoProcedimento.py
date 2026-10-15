class TipoProcedimento:
    def __init__(self, nome: str, valor: float):
        self.__nome = nome.strip()
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome.strip()

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor
