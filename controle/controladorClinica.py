from entidade.clinica import Clinica

class ControladorClinica:

    def __init__(self):
        self.__clinicas = []

    @property
    def clinicas(self):
        return self.__clinicas

    def cadastrar_clinica(self, nome, cidade, descricao, horario_funcionamento_inicial, horario_funcionamento_final):

        for clinica in self.__clinicas:

            if clinica.nome == nome and clinica.cidade == cidade:
                return "Clínica já cadastrada!"

        if horario_funcionamento_inicial >= horario_funcionamento_final:
            return "Horário inicial deve ser anterior ao horário final!"
            

        nova_clinica = Clinica(nome, cidade, descricao, horario_funcionamento_inicial, horario_funcionamento_final)

        self.__clinicas.append(nova_clinica)

        return "Clínica cadastrada com sucesso!"