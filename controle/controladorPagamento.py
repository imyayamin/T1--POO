class ControladorPagamento:

    def __init__(self):
        self.__pagamentos = []

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

        if valor_restante == 0:
            return "Pagamento do atendimento concluído!"

        return f"Pagamento registrado com sucesso! Valor restante: R$ {valor_restante:.2f}"

    def calcular_valor_restante(self, atendimento):

        total_pago = sum(
            pagamento.valor_pago
            for pagamento in self.__pagamentos
            if pagamento.atendimento == atendimento
        )

        return atendimento.valor - total_pago