from limite.telaProfissional import TelaProfissional
from entidade.profissional import Profissional
from exceptions.exceptions import (
    ListaVaziaException,
    ProfissionalRepetidoException,
    ProfissionalNaoEncontradoException,
)


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
        try:
            dados = self.__validar_dados_profissional(
                self.__tela_profissional.pega_dados_profissional()
            )
            if self.pega_profissional_por_cpf(dados["cpf"]) is not None:
                raise ProfissionalRepetidoException(dados["cpf"])
            self.__profissionais.append(Profissional(**dados))
            self.__tela_profissional.mostra_mensagem(
                "Profissional cadastrado com sucesso."
            )
        except (ValueError, ProfissionalRepetidoException) as e:
            self.__tela_profissional.mostra_mensagem(str(e))


    def alterar_profissional(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem(
                "Nenhum profissional cadastrado."
            )
            return
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        if cpf_profissional is None:
            return
        profissional = self.pega_profissional_por_cpf(cpf_profissional)
        if profissional is None:
            self.__tela_profissional.mostra_mensagem(
                str(ProfissionalNaoEncontradoException(cpf_profissional))
            )
            return

        try:
            dados = self.__validar_dados_profissional(
                self.__tela_profissional.pega_dados_profissional(),
                profissional,
            )
            profissional.nome = dados["nome"]
            profissional.celular = dados["celular"]
            profissional.cpf = dados["cpf"]
            profissional.especialidade = dados["especialidade"]
            profissional.registro_profissional = dados["registro_profissional"]
            self.__tela_profissional.mostra_mensagem(
                "Profissional atualizado com sucesso."
            )
        except (ValueError, ProfissionalRepetidoException) as e:
            self.__tela_profissional.mostra_mensagem(str(e))

    def __validar_dados_profissional(self, dados, profissional_atual=None):
        nome = str(dados.get("nome", "")).strip()
        celular = "".join(
            caractere
            for caractere in str(dados.get("celular", ""))
            if caractere.isdigit()
        )
        cpf = "".join(
            caractere
            for caractere in str(dados.get("cpf", ""))
            if caractere.isdigit()
        )
        especialidade = str(dados.get("especialidade", "")).strip()
        registro = str(dados.get("registro_profissional", "")).strip()

        if not nome or not especialidade:
            raise ValueError("Nome e especialidade não podem estar vazios.")
        if len(celular) not in (10, 11):
            raise ValueError("O telefone deve conter DDD e 10 ou 11 dígitos.")
        if len(cpf) != 11:
            raise ValueError("O CPF deve conter 11 dígitos.")
        if not registro.isdigit():
            raise ValueError("O registro profissional deve conter apenas números.")
        existente = self.pega_profissional_por_cpf(cpf)
        if existente is not None and existente is not profissional_atual:
            raise ProfissionalRepetidoException(cpf)

        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "especialidade": especialidade,
            "registro_profissional": registro,
        }

    def lista_profissionais(self):
        if not self.__profissionais:
            raise ListaVaziaException("profissionais")
        self.__tela_profissional.lista_profissionais(self.__profissionais)
        return self.__profissionais

    def excluir_profissional(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem(
                "Nenhum profissional cadastrado."
            )
            return
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        if cpf_profissional is None:
            return
        profissional = self.pega_profissional_por_cpf(cpf_profissional)
        if profissional is None:
            self.__tela_profissional.mostra_mensagem(
                str(ProfissionalNaoEncontradoException(cpf_profissional))
            )
            return
        if any(
            atendimento.profissional is profissional
            for atendimento in self.__controladorGeral.controlador_atendimento.atendimentos
        ):
            self.__tela_profissional.mostra_mensagem(
                "Não é possível remover um profissional vinculado a atendimentos."
            )
            return
        self.__profissionais.remove(profissional)
        self.__tela_profissional.mostra_mensagem(
            "Profissional removido com sucesso."
        )

    def abre_tela(self):
        lista_opcoes = {
            1: self.lista_profissionais,
            2: self.incluir_profissional,
            3: self.alterar_profissional,
            4: self.excluir_profissional,
        }

        while True:
            opcao = self.__tela_profissional.tela_opcoes()
            if opcao == 0:
                return
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_profissional.mostra_mensagem(
                    "Digite uma opção válida."
                    if opcao is not None
                    else "Digite uma opção numérica."
                )
                continue
            try:
                funcao()
            except ListaVaziaException as e:
                self.__tela_profissional.mostra_mensagem(str(e))
        