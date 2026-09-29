class Clinica:
    def __init__(self, nome: str, localizacao: str, descricao: str):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @property
    def localizacao(self):
        return self.__localizacao

    @property
    def descricao(self):
        return self.__descricao

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @localizacao.setter
    def localizacao(self, localizacao: str):
        self.__localizacao = localizacao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao