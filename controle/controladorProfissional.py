from entidade.profissional import Profissional

class ControladorProfissional:
    def __init__(self):
        self.__profissionais = []

    @property
    def profissionais(self):
        return self.__profissionais

    def cadastrar_profissional(self, nome, celular, cpf, especialidade, registro_profissional):

        for profissional in self.__profissionais:

            if profissional.cpf == cpf:
                return "Profissional já cadastrado!"

        novo_profissional = Profissional(nome, celular, cpf, especialidade, registro_profissional)

        self.__profissionais.append(novo_profissional)

        return "Profissional cadastrado com sucesso!"

    def listar_profissionais(self):
        lista_profissionais = []
        for profissional in self.__profissionais:
            lista_profissionais.append(profissional)
        return lista_profissionais

    def editar_profissional(self):


    def remover_profissional(self):