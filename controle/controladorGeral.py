from controle.controladorPaciente import ControladorPaciente
from controle.controladorProfissional import ControladorProfissional
from controle.controladorClinica import ControladorClinica
from controle.controladorAcompanhante import ControladorAcompanhante
from controle.controladorAtendimento import ControladorAtendimento
from controle.controladorPagamento import ControladorPagamento
from controle.controladorProcedimento import ControladorProcedimento

from limite.telaGeral import TelaGeral


class ControladorGeral:

    def __init__(self):
        self.__controladorAcompanhante = ControladorPaciente(self)
        self.__controladorProfissional = ControladorProfissional(self)
        self.__controladorClinica = ControladorClinica(self)
        self.__controladorAcompanhante = ControladorAcompanhante(self)

        self.__controladorAtendimento = ControladorAtendimento(self, self.__controladorClinica, self.__controladorAcompanhante, self.__controladorProfissional, self.__controladorAcompanhante)
        self.__controladorPagamento = ControladorPagamento(self)
        self.__controladorProcedimento = ControladorProcedimento(self, self.__controladorAtendimento, self.__controladorProfissional)
        self.__telaGeral = TelaGeral()

    @property
    def controlador_paciente(self):
        return self.__controladorAcompanhante

    @property
    def controlador_profissional(self):
        return self.__controladorProfissional

    @property
    def controlador_clinica(self):
        return self.__controladorClinica

    @property
    def controlador_acompanhante(self):
        return self.__controladorAcompanhante

    @property
    def controlador_atendimento(self):
        return self.__controladorAtendimento

    @property
    def controlador_pagamento(self):
        return self.__controladorPagamento

    @property
    def controlador_procedimento(self):
        return self.__controlador_procedimento

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_paciente(self):
        self.__controladorAcompanhante.abre_tela()

    def cadastra_profissional(self):
        self.__controladorProfissional.abre_tela()

    def cadastra_clinica(self):
        self.__controladorClinica.abre_tela()

    def cadastra_acompanhante(self):
        self.__controladorAcompanhante.abre_tela()

    def cadastra_atendimento(self):
        self.__controladorAtendimento.abre_tela()

    def cadastra_pagamento(self):
        self.__controladorPagamento.abre_tela()

    def cadastra_procedimento(self):
        self.__controladorProcedimento.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_paciente,
            2: self.cadastra_profissional,
            3: self.cadastra_clinica,
            4: self.cadastra_acompanhante,
            5: self.cadastra_atendimento,
            6: self.cadastra_pagamento,
            7: self.cadastra_procedimento,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__telaGeral.tela_opcoes()

            funcao_escolhida = lista_opcoes.get(opcao_escolhida)

            if funcao_escolhida:
                funcao_escolhida()
            else:
                print("Opção inválida.")