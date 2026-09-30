from entidade.clinica import Clinica

class ControladorClinica:
    def __init__(self):
        self.__clinicas = []

    def cadastrar_clinica(self, nome, cidade, descricao):
        for clinica in self.__clinicas:
            if clinica.nome == nome:
                print("Clínica já cadastrada!")
                return
        
        nova_clinica = Clinica(nome, cidade, descricao)
        self.__clinicas.append(nova_clinica)