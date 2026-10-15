from entidade.pagamentoCartao import PagamentoCartao
from entidade.pagamentoDinheiro import PagamentoDinheiro
from entidade.pagamentoPix import PagamentoPix
from limite.telaPagamento import TelaPagamento

class ControladorPagamento:
    def __init__(self, controladorGeral):
        self.__controladorGeral = controladorGeral
        self.__tela_pagamento = TelaPagamento()

    @property
    def pagamentos(self):
        return [
            pagamento
            for atendimento in self.__controladorGeral.controlador_atendimento.atendimentos
            for pagamento in atendimento.pagamentos
        ]

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_pagamento,
            2: self.listar_pagamentos,
            3: self.editar_pagamento,
            4: self.remover_pagamento,
        }

        while True:
            opcao = self.__tela_pagamento.tela_opcoes()
            if opcao == 0:
                return

            funcao = opcoes.get(opcao)
            if funcao is None:
                self.__tela_pagamento.mostrar_mensagem("Opção inválida.")
                continue
            funcao()

    def realizar_pagamento(self, tipo, data_pagamento, atendimento, paciente, valor_pago=None, cpf_pagador=None, numero_cartao=None, bandeira=None, parcelas=None):

        if atendimento not in self.__controladorGeral.controlador_atendimento.atendimentos:
            return "Atendimento não cadastrado."

        if atendimento.calcular_valor_restante() <= 0:
            return "O atendimento já foi totalmente pago."

        match tipo:

            case "1":
                return self.__realizar_pagamento_dinheiro(data_pagamento, atendimento, paciente, valor_pago)

            case "2":
                return self.__realizar_pagamento_pix(data_pagamento, atendimento, paciente, valor_pago, cpf_pagador)

            case "3":
                return self.__realizar_pagamento_cartao(
                    data_pagamento,
                    atendimento,
                    paciente,
                    valor_pago,
                    numero_cartao,
                    bandeira,
                    parcelas,
                )

            case _:
                return "Opção inválida."

    def __realizar_pagamento_dinheiro(self, data_pagamento, atendimento, paciente, valor_pago):

        pagamento = PagamentoDinheiro(data_pagamento, atendimento, paciente, valor_pago)

        return atendimento.registrar_pagamento(pagamento)

    def __realizar_pagamento_pix(self, data_pagamento, atendimento, paciente, valor_pago, cpf_pagador):

        pagamento = PagamentoPix(data_pagamento, atendimento, paciente, valor_pago, cpf_pagador)

        return atendimento.registrar_pagamento(pagamento)

    def __realizar_pagamento_cartao(
        self,
        data_pagamento,
        atendimento,
        paciente,
        valor_pago,
        numero_cartao,
        bandeira,
        parcelas,
    ):
        pagamento = PagamentoCartao(
            data_pagamento,
            atendimento,
            paciente,
            valor_pago,
            numero_cartao,
            bandeira,
            parcelas,
        )

        return atendimento.registrar_pagamento(pagamento)

    def cadastrar_pagamento(self):
        dados = self.__tela_pagamento.pega_dados_pagamento(
            self.__controladorGeral.controlador_atendimento.atendimentos
        )
        if dados is None:
            return

        mensagem = self.realizar_pagamento(**dados)
        self.__tela_pagamento.mostrar_mensagem(mensagem)

    def listar_pagamentos(self):
        registros = self.__registros_pagamento()
        self.__tela_pagamento.lista_pagamentos(registros)
        return self.pagamentos

    def editar_pagamento(self):
        registros = self.__registros_pagamento()
        if not registros:
            self.__tela_pagamento.mostrar_mensagem(
                "Nenhum pagamento cadastrado."
            )
            return

        registro = self.__tela_pagamento.seleciona_pagamento(registros)
        if registro is None:
            return

        pagamento_original, atendimento_original = registro
        dados = self.__tela_pagamento.pega_dados_pagamento(
            self.__controladorGeral.controlador_atendimento.atendimentos
        )
        if dados is None:
            return

        pagamentos_antes = {
            id(pagamento) for pagamento in dados["atendimento"].pagamentos
        }
        atendimento_original.remover_pagamento(pagamento_original)
        mensagem = self.realizar_pagamento(**dados)
        novo_pagamento_criado = any(
            id(pagamento) not in pagamentos_antes
            for pagamento in dados["atendimento"].pagamentos
        )
        if not novo_pagamento_criado:
            resultado_restauracao = atendimento_original.registrar_pagamento(
                pagamento_original
            )
            if pagamento_original not in atendimento_original.pagamentos:
                self.__tela_pagamento.mostrar_mensagem(
                    "Falha ao restaurar o pagamento original: "
                    f"{resultado_restauracao}"
                )
            self.__tela_pagamento.mostrar_mensagem(mensagem)
            return

        self.__tela_pagamento.mostrar_mensagem(
            "Pagamento atualizado com sucesso."
        )

    def remover_pagamento(self):
        registros = self.__registros_pagamento()
        if not registros:
            self.__tela_pagamento.mostrar_mensagem(
                "Nenhum pagamento cadastrado."
            )
            return

        registro = self.__tela_pagamento.seleciona_pagamento(registros)
        if registro is None:
            return

        pagamento, atendimento = registro
        if not self.__tela_pagamento.confirmar_remocao():
            self.__tela_pagamento.mostrar_mensagem("Remoção cancelada.")
            return

        if atendimento.remover_pagamento(pagamento):
            self.__tela_pagamento.mostrar_mensagem(
                "Pagamento removido com sucesso."
            )
        else:
            self.__tela_pagamento.mostrar_mensagem(
                "Não foi possível remover o pagamento."
            )

    def __registros_pagamento(self):
        return [
            (pagamento, atendimento)
            for atendimento in self.__controladorGeral.controlador_atendimento.atendimentos
            for pagamento in atendimento.pagamentos
        ]