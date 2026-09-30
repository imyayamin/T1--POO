from entidade.profissional import Profissional

class Controladorprofissional:
    def __init__(self):
        self.__profissionais = []

    def cadastrar_profissional(self, nome, celular, cpf, especialidade, registro_profissional):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                print("profissional já cadastrado!")
                return
        
        novo_profissional = Profissional(nome, celular, cpf, especialidade, registro_profissional)
        self.__profissionais.append(novo_profissional)