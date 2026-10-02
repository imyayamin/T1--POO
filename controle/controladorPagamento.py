#Após o agendamento, deve ser feito o controle dos pagamentos dos atendimentos. O sistema deve
#permitir pagamentos parciais (parcelamento). O registro do pagamento deve conter: data,
#atendimento, paciente, valor pago, e deve ser possível calcular o valor restante.
from entidade.pagamentoPix import PagamentoPix
from entidade.pagamentoCartao import PagamentoCartao
from entidade.pagamentoDinheiro import PagamentoDinheiro

class ControladorPagamento:

    def __init__(self):
        self.__pagamentos = []

    def registrar_pagamento(self, atendimento, data_pagamento, valor_pago, tipo_pagamento):

        if data_pagamento > atendimento.data:
            return "Pagamento deve ser realizado até a data do atendimento!"

        if valor_pago <= 0:
            return "O valor pago deve ser maior que zero!"

        valor_restante = self.calcular_valor_restante(atendimento)

        if valor_pago > valor_restante:
            return "Valor pago não pode ser maior que o valor restante!"

        if tipo_pagamento == "pix":
            pagamento = PagamentoPix(atendimento, data_pagamento, valor_pago)

        elif tipo_pagamento == "cartao":
            pagamento = PagamentoCartao(atendimento, data_pagamento, valor_pago)

        elif tipo_pagamento == "dinheiro":
            pagamento = PagamentoDinheiro(atendimento, data_pagamento, valor_pago)

        else:
            return "Tipo de pagamento inválido!"

        self.__pagamentos.append(pagamento)

        return pagamento.verificar_pagamento()

    def calcular_valor_restante(self, atendimento):

        total_pago = sum(
            pagamento.valor_pago
            for pagamento in self.__pagamentos
            if pagamento.atendimento == atendimento
        )

        return atendimento.valor - total_pago