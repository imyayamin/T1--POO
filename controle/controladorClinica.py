from entidade.clinica import Clinica

class ControladorClinica:
    def __init__(self):
        self.__clinicas = []

    def cadastrar_clinica(self, nome, cidade, descricao, horario_funcionamento_inicial, horario_funcionamento_final):
        for clinica in self.__clinicas:
            if clinica.nome == nome and clinica.cidade == cidade: #pensando se criamos um codigo pra clinica ou nem
                print("Clínica já cadastrada!")
                return
        
        nova_clinica = Clinica(nome, cidade, descricao, horario_funcionamento_inicial, horario_funcionamento_final)
        self.__clinicas.append(nova_clinica)