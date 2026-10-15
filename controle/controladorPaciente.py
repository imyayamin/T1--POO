from entidade.paciente import Paciente
from limite.telaPaciente import TelaPaciente
from exceptions.exceptions import (AcompanhanteObrigatorioException, PacienteRepetidoException, PacienteNaoEncontradoException, EntradaInvalidaException, ListaVaziaException)

class ControladorPaciente:

    def __init__(self, controladorgeral):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()
        self.__controladorgeral = controladorgeral

    @property
    def pacientes(self):
        return self.__pacientes

    def pega_paciente_por_cpf(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def incluir_paciente(self):
        try:
            dados = self.__tela_paciente.pega_dados_paciente()
        except EntradaInvalidaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return

        nome = dados["nome"]
        celular = dados["celular"]
        cpf = dados["cpf"]
        idade = dados["idade"]

        try:
            if idade < 0:
                raise ValueError("A idade do paciente deve ser não negativa.")

            if self.pega_paciente_por_cpf(cpf) is not None:
                raise PacienteRepetidoException(cpf)

            acompanhante = None
            if 0 <= idade < 18:
                self.__tela_paciente.mostra_mensagem(
                    "Paciente menor de idade. Informe o acompanhante:"
                )
                acompanhante = self.__tela_paciente.pega_dados_acompanhante()
                if not acompanhante:
                    raise AcompanhanteObrigatorioException()

            novo_paciente = Paciente(nome, celular, cpf, idade, acompanhante)
            self.__pacientes.append(novo_paciente)
            self.__tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")

        except (ValueError, PacienteRepetidoException, AcompanhanteObrigatorioException) as e:
            self.__tela_paciente.mostra_mensagem(str(e))

    def listar_pacientes(self):
        if not self.__pacientes:
            raise ListaVaziaException("pacientes")
        self.__tela_paciente.lista_pacientes(self.__pacientes)
        return self.__pacientes

    def remover_paciente(self):
        try:
            self.listar_pacientes()
        except ListaVaziaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return
        
        try:
            cpf = self.__tela_paciente.seleciona_paciente()
        except EntradaInvalidaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return

        try:
            paciente = self.pega_paciente_por_cpf(cpf)
            if paciente is None:
                raise PacienteNaoEncontradoException(cpf)
            self.__pacientes.remove(paciente)
            self.__tela_paciente.mostra_mensagem("Paciente removido com sucesso!")
        except PacienteNaoEncontradoException as e:
            self.__tela_paciente.mostra_mensagem(str(e))

    def retornar(self):
        self.__controladorgeral.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_pacientes,
            2: self.incluir_paciente,
            3: self.remover_paciente,
            0: self.retornar,
        }
        while True:
            opcao = self.__tela_paciente.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_paciente.mostra_mensagem("Opção inválida.")
                continue
            try:
                funcao()
            except ListaVaziaException as e:
                self.__tela_paciente.mostra_mensagem(str(e))