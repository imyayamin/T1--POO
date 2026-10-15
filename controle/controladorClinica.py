from entidade.clinica import Clinica
from limite.telaClinica import TelaClinica
from exceptions.exceptions import (ListaVaziaException, ClinicaRepetidaException, ClinicaNaoEncontradaException, HorarioInvalidoException, EntradaInvalidaException)

class ControladorClinica:

    def __init__(self, controladorgeral):
        self.__clinicas = []
        self.__tela_clinica = TelaClinica()
        self.__controladorgeral = controladorgeral

    @property
    def clinicas(self):
        return self.__clinicas

    def incluir_clinica(self):
        try:
            dados_clinica = self.__tela_clinica.pega_dados_clinica()
        except EntradaInvalidaException as e:
            self.__tela_clinica.mostra_mensagem(str(e))
            return

        try:
            horario_inicial = dados_clinica["horario_inicial"]
            horario_final = dados_clinica["horario_final"]
            nome = dados_clinica["nome"]

            # Validação de horário
            if horario_inicial >= horario_final:
                raise HorarioInvalidoException()

            # Validação de duplicidade
            if self.pega_clinica_por_nome(nome) is not None:
                raise ClinicaRepetidaException(nome)

            nova_clinica = Clinica(
                nome,
                dados_clinica["cidade"],
                dados_clinica["descricao"],
                horario_inicial,
                horario_final
            )
            self.__clinicas.append(nova_clinica)
            self.__tela_clinica.mostra_mensagem("Clínica cadastrada com sucesso!")

        except (HorarioInvalidoException, ClinicaRepetidaException) as e:
            self.__tela_clinica.mostra_mensagem(str(e))

    def listar_clinicas(self):
        if not self.__clinicas:
            raise ListaVaziaException("clínicas")
        self.__tela_clinica.lista_clinicas(self.__clinicas)
        return self.__clinicas

    def remover_clinica(self):
        try:
            self.listar_clinicas()
        except ListaVaziaException as e:
            self.__tela_clinica.mostra_mensagem(str(e))
            return

        try:
            nome = self.__tela_clinica.seleciona_clinica()
        except EntradaInvalidaException as e:
            self.__tela_clinica.mostra_mensagem(str(e))
            return

        try:
            clinica = self.pega_clinica_por_nome(nome)
            if clinica is None:
                raise ClinicaNaoEncontradaException(nome)

            self.__clinicas.remove(clinica)
            self.__tela_clinica.mostra_mensagem("Clínica removida com sucesso!")
        except ClinicaNaoEncontradaException as e:
            self.__tela_clinica.mostra_mensagem(str(e))

    def retornar(self):
        self.__controladorgeral.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_clinicas,
            2: self.incluir_clinica,
            3: self.remover_clinica,
            0: self.retornar,
        }
        while True:
            opcao = self.__tela_clinica.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_clinica.mostra_mensagem("Opção inválida.")
                continue
            
            try:
                funcao()
            except ListaVaziaException as e:
                self.__tela_clinica.mostra_mensagem(str(e))
    