from entidade.clinica import Clinica
from limite.telaClinica import TelaClinica
from exceptions.exceptions import (ListaVaziaException, ClinicaRepetidaException, ClinicaNaoEncontradaException, HorarioInvalidoException, EntradaInvalidaException)

class ControladorClinica:

    def __init__(self, controladorGeral):
        self.__clinicas = []
        self.__tela_clinica = TelaClinica()
        self.__controladorGeral = controladorGeral

    @property
    def clinicas(self):
        return self.__clinicas

    def pega_clinica_por_nome(self, nome: str):
        for clinica in self.__clinicas:
            if clinica.nome == nome:
                return clinica
        return None

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

            if (
                not isinstance(horario_inicial, int)
                or not isinstance(horario_final, int)
                or not 0 <= horario_inicial <= 23
                or not 1 <= horario_final <= 24
                or horario_inicial >= horario_final
            ):
                raise HorarioInvalidoException()

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

            if any(
                atendimento.clinica is clinica
                for atendimento in self.__controladorGeral.controlador_atendimento.atendimentos
            ):
                self.__tela_clinica.mostra_mensagem(
                    "Não é possível remover uma clínica vinculada a atendimentos."
                )
                return
            self.__clinicas.remove(clinica)
            self.__tela_clinica.mostra_mensagem("Clínica removida com sucesso!")
        except ClinicaNaoEncontradaException as e:
            self.__tela_clinica.mostra_mensagem(str(e))

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_clinicas,
            2: self.incluir_clinica,
            3: self.remover_clinica,
        }
        while True:
            opcao = self.__tela_clinica.tela_opcoes()
            if opcao == 0:
                return
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_clinica.mostra_mensagem(
                    "Digite uma opção válida."
                    if opcao is not None
                    else "Digite uma opção numérica."
                )
                continue
            
            try:
                funcao()
            except ListaVaziaException as e:
                self.__tela_clinica.mostra_mensagem(str(e))
    