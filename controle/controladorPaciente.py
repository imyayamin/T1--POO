from entidade.paciente import Paciente
from limite.telaPaciente import TelaPaciente
from exceptions.exceptions import (AcompanhanteObrigatorioException, PacienteRepetidoException,)

class ControladorPaciente:
    def __init__(self, controladorgeral):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()
        self.__controladorgeral = controladorgeral

    @property
    def pacientes(self):
        return self.__pacientes

    def cadastrar_paciente(self, nome, celular, cpf, idade, acompanhante=None):

        if not isinstance(idade, int) or idade < 0:
            raise ValueError("A idade do paciente deve ser um número inteiro não negativo.")

        for paciente in self.__pacientes:

            if paciente.cpf == cpf:
                raise PacienteRepetidoException(cpf)

        if idade < 18:
            #botar um paciente

        novo_paciente = Paciente(nome, celular, cpf, idade, acompanhante)

        self.__pacientes.append(novo_paciente)

        return "Paciente cadastrado com sucesso!"

    def listar_pacientes(self):
        self.__tela_paciente.lista_pacientes(self.__pacientes)
        return self.__pacientes

    def remover_paciente(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__pacientes.remove(paciente)
                return "Paciente removido com sucesso!"
        return "Paciente não encontrado."

    def abre_tela(self):
            lista_opcoes = {
                1: self.listar_pacientes,
                2: self.cadastrar_paciente,
                3: self.remover_paciente,
                4: self.__controladorgeral.abre_tela,
            }
    
            while True:
                opcao_escolhida = self.__telaGeral.tela_opcoes()
    
                funcao_escolhida = lista_opcoes.get(opcao_escolhida)
    
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    print("Opção inválida.")