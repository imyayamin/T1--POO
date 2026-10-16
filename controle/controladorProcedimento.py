import math

from entidade.procedimento import Procedimento
from exceptions.exceptions import (
    AtendimentoNaoEncontradoException,
    DescricaoProcedimentoVaziaException,
    ProcedimentoInvalidoException,
    ValorProcedimentoInvalidoException,
)
from limite.telaProcedimento import TelaProcedimento


class ControladorProcedimento:
    def __init__(self, controladorGeral, controladorAtendimento, controladorProfissional):
        self.__controladorGeral = controladorGeral
        self.__controladorAtendimento = controladorAtendimento
        self.__controladorProfissional = controladorProfissional
        self.__telaProcedimento = TelaProcedimento()

    @property
    def procedimentos(self):
        return [
            (procedimento, atendimento)
            for atendimento in self.__controladorAtendimento.atendimentos
            for procedimento in atendimento.procedimentos
        ]

    def abre_tela(self, atendimento):
        if atendimento is None:
            return False

        while True:
            descricao = self.__telaProcedimento.informar_descricao()
            custo = self.__telaProcedimento.informar_custo()
            try:
                mensagem = self.registrar_procedimento(
                    atendimento,
                    descricao,
                    custo,
                )
            except (
                AtendimentoNaoEncontradoException,
                DescricaoProcedimentoVaziaException,
                ProcedimentoInvalidoException,
                ValorProcedimentoInvalidoException,
            ) as erro:
                self.__telaProcedimento.mostra_mensagem(str(erro))
                return False
            self.__telaProcedimento.mostra_mensagem(mensagem)
            if mensagem == "Procedimento cadastrado com sucesso!":
                return True

    def pega_dados_edicao(self, atendimento):
        if not atendimento.procedimentos:
            self.__telaProcedimento.mostra_mensagem(
                "Este atendimento não possui procedimentos para editar."
            )
            return None

        procedimento = self.__telaProcedimento.selecionar_procedimento(
            atendimento.procedimentos
        )
        if procedimento is None:
            return None

        descricao = self.__telaProcedimento.informar_descricao()
        custo = self.__telaProcedimento.informar_custo()
        return procedimento, descricao, custo

    def listar_procedimentos(self):
        registros = self.procedimentos
        self.__telaProcedimento.lista_procedimentos(registros)
        return registros

    def adicionar_procedimento_menu(self):
        atendimento = self.__controladorAtendimento.selecionar_atendimento()
        if atendimento is None:
            return

        tipo = self.__controladorGeral.controlador_tipo_procedimento.seleciona_tipo()
        if tipo is None:
            return

        try:
            mensagem = self.registrar_procedimento(
                atendimento,
                tipo.nome,
                tipo.valor,
            )
        except (
            AtendimentoNaoEncontradoException,
            DescricaoProcedimentoVaziaException,
            ProcedimentoInvalidoException,
            ValorProcedimentoInvalidoException,
        ) as erro:
            mensagem = str(erro)
        self.__telaProcedimento.mostra_mensagem(mensagem)

    def editar_procedimento_menu(self):
        registros = self.procedimentos
        registro = self.__telaProcedimento.selecionar_registro_procedimento(
            registros,
            "editar",
        )
        if registro is None:
            return
        procedimento, atendimento = registro
        descricao = self.__telaProcedimento.informar_descricao()
        custo = self.__telaProcedimento.informar_custo()
        try:
            mensagem = self.editar_procedimento(
                atendimento,
                procedimento,
                descricao,
                custo,
                atendimento.profissional,
            )
        except (
            DescricaoProcedimentoVaziaException,
            ValorProcedimentoInvalidoException,
        ) as erro:
            mensagem = str(erro)
        self.__telaProcedimento.mostra_mensagem(mensagem)

    def remover_procedimento(self):
        registros = self.procedimentos
        registro = self.__telaProcedimento.selecionar_registro_procedimento(
            registros,
            "remover",
        )
        if registro is None:
            return
        procedimento, atendimento = registro
        if not self.__telaProcedimento.confirmar_remocao():
            self.__telaProcedimento.mostra_mensagem("Remoção cancelada.")
            return
        try:
            mensagem = self.remover_procedimento_do_atendimento(
                atendimento,
                procedimento,
            )
        except AtendimentoNaoEncontradoException as erro:
            mensagem = str(erro)
        self.__telaProcedimento.mostra_mensagem(mensagem)

    def editar_procedimento(
        self,
        atendimento,
        procedimento,
        descricao,
        custo,
        profissional,
        valor_base=None,
    ):
        if procedimento not in atendimento.procedimentos:
            return "Procedimento não pertence a este atendimento."
        if not isinstance(descricao, str) or not descricao.strip():
            raise DescricaoProcedimentoVaziaException()
        descricao = descricao.strip()
        try:
            custo = float(custo)
        except (TypeError, ValueError):
            return "O valor do procedimento deve ser numérico."
        if not math.isfinite(custo) or custo <= 0:
            raise ValorProcedimentoInvalidoException(custo)
        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não encontrado."

        total_pago = sum(
            pagamento.valor_pago for pagamento in atendimento.pagamentos
        )
        if valor_base is None:
            valor_base = atendimento.valor
        novo_total = (
            valor_base
            + atendimento.valor_total_procedimentos()
            - procedimento.custo
            + custo
        )
        if novo_total < total_pago:
            return (
                "O novo valor do atendimento não pode ser menor que "
                "o total já pago."
            )

        procedimento.descricao = descricao
        procedimento.custo = custo
        procedimento.profissional = profissional
        return "Procedimento atualizado com sucesso."

    def remover_procedimento_do_atendimento(
        self,
        atendimento,
        procedimento,
    ):
        if atendimento not in self.__controladorAtendimento.atendimentos:
            raise AtendimentoNaoEncontradoException()
        if procedimento not in atendimento.procedimentos:
            return "Procedimento não pertence a este atendimento."
        novo_total = atendimento.valor_total() - procedimento.custo
        total_pago = sum(
            pagamento.valor_pago for pagamento in atendimento.pagamentos
        )
        if novo_total < total_pago:
            return (
                "Não é possível remover o procedimento porque o novo total "
                "ficaria menor que o valor já pago."
            )
        atendimento.procedimentos.remove(procedimento)
        return "Procedimento removido com sucesso."

    def registrar_procedimento(self, atendimento, descricao, custo):
        if atendimento not in self.__controladorAtendimento.atendimentos:
            raise AtendimentoNaoEncontradoException()

        profissional = atendimento.profissional
        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não encontrado."

        if not isinstance(descricao, str) or not descricao.strip():
            raise DescricaoProcedimentoVaziaException()
        descricao = descricao.strip()

        try:
            custo = float(custo)
        except (TypeError, ValueError):
            return "O valor do procedimento deve ser numérico."
        if not math.isfinite(custo) or custo <= 0:
            raise ValorProcedimentoInvalidoException(custo)

        procedimento = Procedimento(descricao, custo, profissional)
        resultado = atendimento.adicionar_procedimento(procedimento)
        if resultado != "Procedimento adicionado com sucesso!":
            return resultado

        return "Procedimento cadastrado com sucesso!"