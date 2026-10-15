
import math

from entidade.tipoProcedimento import TipoProcedimento
from limite.telaAtendimento import TelaAtendimento


class ControladorTipoProcedimento:
    def __init__(self, controladorGeral):
        self.__controladorGeral = controladorGeral
        self.__tela_tipo_procedimento = TelaAtendimento()
        self.__tipos = [
            TipoProcedimento("Limpeza dentária", 150),
            TipoProcedimento("Restauração", 200),
            TipoProcedimento("Extração dentária", 250),
            TipoProcedimento("Clareamento dental", 500),
            TipoProcedimento("Tratamento de canal", 800),
            TipoProcedimento("Aplicação de flúor", 80),
            TipoProcedimento("Radiografia odontológica", 100),
            TipoProcedimento("Implante dentário", 1500),
            TipoProcedimento("Aparelho ortodôntico", 1200),
            TipoProcedimento("Avaliação odontológica", 100),
        ]

    @property
    def tipos(self):
        return self.__tipos

    def pega_tipo_por_nome(self, nome):
        if not isinstance(nome, str):
            return None

        return next(
            (
                tipo
                for tipo in self.__tipos
                if tipo.nome.casefold() == nome.casefold()
            ),
            None,
        )

    def listar_tipos(self):
        self.__tela_tipo_procedimento.lista_tipos_procedimento(self.__tipos)
        return self.__tipos

    def seleciona_tipo(self):
        return self.__tela_tipo_procedimento.seleciona_tipo_procedimento(
            self.__tipos
        )

    def cadastrar_tipo(self):
        dados = self.__tela_tipo_procedimento.pega_dados_tipo_procedimento()

        nome = dados["nome"].strip()
        valor = dados["valor"]

        if (
            not nome
            or not isinstance(valor, (int, float))
            or isinstance(valor, bool)
            or not math.isfinite(valor)
            or valor <= 0
        ):
            self.__tela_tipo_procedimento.mostra_mensagem(
                "Informe um nome e um valor maior que zero."
            )
            return

        if self.pega_tipo_por_nome(nome) is not None:
            self.__tela_tipo_procedimento.mostra_mensagem(
                "Já existe um tipo de procedimento com esse nome."
            )
            return

        dados["nome"] = nome
        self.__tipos.append(TipoProcedimento(**dados))

        self.__tela_tipo_procedimento.mostra_mensagem(
            "Tipo de procedimento cadastrado com sucesso."
        )

    def editar_tipo(self):
        if not self.__tipos:
            self.__tela_tipo_procedimento.mostra_mensagem(
                "Nenhum tipo de procedimento cadastrado."
            )
            return

        tipo = self.__tela_tipo_procedimento.seleciona_tipo_procedimento(
            self.__tipos
        )

        if tipo is None:
            return

        dados = self.__tela_tipo_procedimento.pega_dados_tipo_procedimento()

        nome = dados["nome"].strip()
        valor = dados["valor"]

        if (
            not nome
            or not isinstance(valor, (int, float))
            or isinstance(valor, bool)
            or not math.isfinite(valor)
            or valor <= 0
        ):
            self.__tela_tipo_procedimento.mostra_mensagem(
                "Informe um nome e um valor maior que zero."
            )
            return

        tipo_com_nome_igual = self.pega_tipo_por_nome(nome)

        if tipo_com_nome_igual is not None and tipo_com_nome_igual is not tipo:
            self.__tela_tipo_procedimento.mostra_mensagem(
                "Já existe um tipo de procedimento com esse nome."
            )
            return

        nome_anterior = tipo.nome

        tipo.nome = nome
        tipo.valor = valor

        self.__tela_tipo_procedimento.mostra_mensagem(
            f"Tipo de procedimento '{nome_anterior}' "
            "atualizado com sucesso."
        )

    def remover_tipo(self):
        if not self.__tipos:
            self.__tela_tipo_procedimento.mostra_mensagem(
                "Nenhum tipo de procedimento cadastrado."
            )
            return

        tipo = self.__tela_tipo_procedimento.seleciona_tipo_procedimento(
            self.__tipos
        )

        if tipo is None:
            return

        self.__tipos.remove(tipo)

        self.__tela_tipo_procedimento.mostra_mensagem(
            "Tipo de procedimento removido com sucesso."
        )
