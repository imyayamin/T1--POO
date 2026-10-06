from entidade.pagamentoCartao import PagamentoCartao
from entidade.pagamentoDinheiro import PagamentoDinheiro
from entidade.pagamentoPix import PagamentoPix

class ControladorPagamento:

    def __init__(self, tela_pagamento):
        self.__pagamentos = []
        self.__tela = tela_pagamento

    def realizar_pagamento(self, data_pagamento, atendimento, paciente):

        tipo = self.__tela.escolher_tipo()

        valor_restante = self.calcular_valor_restante(atendimento)

        if valor_restante <= 0:
            return "O atendimento já foi totalmente pago."

        match tipo:

            case "1":
                return self.__realizar_pagamento_dinheiro(data_pagamento, atendimento, paciente, valor_restante)

            case "2":
                return self.__realizar_pagamento_pix(data_pagamento, atendimento, paciente, valor_restante)

            case "3":
                return self.__realizar_pagamento_cartao(data_pagamento, atendimento, paciente, valor_restante)

            case _:
                return "Opção inválida."

    def __realizar_pagamento_dinheiro(self, data_pagamento, atendimento, paciente, valor_restante):

        valor_pago = self.__tela.informar_valor()

        if valor_pago > valor_restante:
            return "Valor pago não pode ser maior que o valor restante!"

        pagamento = PagamentoDinheiro(data_pagamento, atendimento, paciente, valor_pago)

        return self.registrar_pagamento(pagamento)

    def __realizar_pagamento_pix(self, data_pagamento, atendimento, paciente, valor_restante):

        cpf_pagador = self.__tela.informar_cpf()
        valor_pago = self.__tela.informar_valor()

        if valor_pago > valor_restante:
            return "Valor pago não pode ser maior que o valor restante!"

        pagamento = PagamentoPix(data_pagamento, atendimento, paciente, valor_pago, cpf_pagador)

        return self.registrar_pagamento(pagamento)

    def __realizar_pagamento_cartao(self, data_pagamento, atendimento, paciente, valor_restante):

        numero_cartao = self.__tela.informar_cartao()
        bandeira = self.__tela.informar_bandeira()

        parcelas = self.__tela.informar_parcelas(valor_restante)

        pagamento = PagamentoCartao(data_pagamento, atendimento, paciente, valor_restante, numero_cartao, bandeira, parcelas)

        return self.registrar_pagamento(pagamento)

    def registrar_pagamento(self, pagamento):

        atendimento = pagamento.atendimento

        if pagamento.data_pagamento > atendimento.data:
            return "Pagamento deve ser realizado até a data do atendimento!"

        if pagamento.valor_pago <= 0:
            return "O valor pago deve ser maior que zero!"

        valor_restante = self.calcular_valor_restante(atendimento)

        if pagamento.valor_pago > valor_restante:
            return "Valor pago não pode ser maior que o valor restante!"

        if not pagamento.processar_pagamento():
            return "Dados do pagamento inválidos!"

        self.__pagamentos.append(pagamento)

        novo_valor_restante = self.calcular_valor_restante(atendimento)

        if novo_valor_restante == 0:
            return "Pagamento do atendimento concluído!"

        return (
            f"Pagamento registrado com sucesso! "
            f"Valor restante: R$ {novo_valor_restante:.2f}")

    def calcular_valor_restante(self, atendimento):

        total_pago = sum(
            pagamento.valor_pago
            for pagamento in self.__pagamentos
            if pagamento.atendimento == atendimento)

        return atendimento.valor - total_pago

