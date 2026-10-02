from entidade.acompanhante import Acompanhante

class ControladorAcompanhante:
    def __init__(self):
        self.__acompanhantes = []

    @property
    def acompanhantes(self):
        return self.__acompanhantes
    
    def cadastrar_acompanhante(self, nome, celular, cpf, idade):
        if idade < 18:
            return "Acompanhantes devem ser maiores de 18 anos!"
        
        for acompanhante in self.__acompanhantes:
            if acompanhante.cpf == cpf:
                return "Acompanhante já cadastrado!"
            
        novo_acompanhante = acompanhante(nome, celular, cpf, idade)
        self.__acompanhantes.append(novo_acompanhante)
