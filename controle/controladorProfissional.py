from limite.telaProfissional import TelaProfissional
from entidade.profissional import Profissional
from exceptions.exceptions import (ProfissionalRepetidoException, ProfissionalNaoEncontradoException, ListaVaziaException)


class ControladorProfissional:

    def __init__(self, controladorGeral):
        self.__profissionais = []
        self.__tela_profissional = TelaProfissional()
        self.__controladorGeral = controladorGeral

    @property
    def profissionais(self):
        return self.__profissionais

    def pega_profissional_por_cpf(self, cpf: str):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

    def incluir_profissional(self):
        dados_profissional = self.__tela_profissional.pega_dados_profissional()
        celular = "".join(
            caractere
            for caractere in str(dados_profissional["celular"])
            if caractere.isdigit()
        )
        cpf = "".join(
            caractere
            for caractere in str(dados_profissional["cpf"])
            if caractere.isdigit()
        )
        registro = str(dados_profissional["registro_profissional"]).strip()

        if len(celular) not in (10, 11):
            self.__tela_profissional.mostra_mensagem(
                "O telefone deve conter DDD e 10 ou 11 dígitos."
            )
            return
        if len(cpf) != 11:
            self.__tela_profissional.mostra_mensagem(
                "O CPF deve conter 11 dígitos."
            )
            return
        if not registro.isdigit():
            self.__tela_profissional.mostra_mensagem(
                "O registro profissional deve conter apenas números."
            )
            return

        dados_profissional["celular"] = celular
        dados_profissional["cpf"] = cpf
        dados_profissional["registro_profissional"] = registro
        p = self.pega_profissional_por_cpf(dados_profissional["cpf"])

        try:
            if p is None:
                profissional = Profissional(
                dados_profissional["nome"],
                dados_profissional["celular"],
                dados_profissional["cpf"],
                dados_profissional["especialidade"],
                dados_profissional["registro_profissional"]
                )
                self.__profissionais.append(profissional)
            else:
                raise ProfissionalRepetidoException(dados_profissional["cpf"])
        except ProfissionalRepetidoException as e:
            self.__tela_profissional.mostra_mensagem(e)


    def alterar_profissional(self):
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        profissional = self.pega_profissional_por_cpf(cpf_profissional)

        try:
            if(profissional is not None):
                novos_dados_profissional = self.__tela_profissional.pega_dados_profissional()
                cpf_existente = self.pega_profissional_por_cpf(
                    novos_dados_profissional["cpf"]
                )
                if cpf_existente is not None and cpf_existente is not profissional:
                    self.__tela_profissional.mostra_mensagem(
                        "Já existe um profissional cadastrado com esse CPF."
                    )
                    return

                profissional.nome = novos_dados_profissional["nome"]
                profissional.celular = novos_dados_profissional["celular"]
                profissional.cpf = novos_dados_profissional["cpf"]
                profissional.especialidade = novos_dados_profissional["especialidade"]
                profissional.registro_profissional = novos_dados_profissional["registro_profissional"]
                self.lista_profissionais()
        except ProfissionalNaoEncontradoException as e:
            self.__tela_profissional.mostra_mensagem(e)

    def lista_profissionais(self):
        if not self.__profissionais:
            raise ListaVaziaException("profissionais")
        self.__tela_profissional.lista_profissionais(self.__profissionais)
        return self.__profissionais

    def excluir_profissional(self):
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        if cpf_profissional is None:
            return
        profissional = self.pega_profissional_por_cpf(cpf_profissional)
        try:
            if profissional is not None:
                self.__profissionais.remove(profissional)
                self.__tela_profissional.mostra_mensagem("Profissional removido com sucesso!")
                self.lista_profissionais()
        except ProfissionalNaoEncontradoException as e:
            self.__tela_profissional.mostra_mensagem(e)

    def retornar(self):
        self.__controladorGeral.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.lista_profissionais,
            2: self.incluir_profissional,
            3: self.alterar_profissional,
            4: self.excluir_profissional,
            0: self.retornar,
        }

        while True:
            opcao = self.__tela_profissional.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_profissional.mostra_mensagem("Opção inválida.")
                continue
            try:
                funcao()
            except ListaVaziaException as e:
                self.__tela_profissional.mostra_mensagem(str(e))
        