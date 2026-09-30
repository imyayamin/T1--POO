class Clinica:
    def __init__(self, nome: str, cidade: str, descricao: str):
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def cidade(self):
        return self.__cidade

    @property
    def descricao(self):
        return self.__descricao

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao