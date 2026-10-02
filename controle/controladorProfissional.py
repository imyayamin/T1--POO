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
                return "profissional já cadastrado!"
        
        novo_profissional = Profissional(nome, celular, cpf, especialidade, registro_profissional)
        self.__profissionais.append(novo_profissional)