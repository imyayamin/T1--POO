from entidade.pagamentoCartao import PagamentoCartao
from entidade.pagamentoDinheiro import PagamentoDinheiro
from entidade.pagamentoPix import PagamentoPix

class ControladorPagamento:

    def realizar_pagamento(self, tipo, data_pagamento, atendimento, paciente, valor_pago=None, cpf_pagador=None, numero_cartao=None, bandeira=None, parcelas=None):

        if atendimento.calcular_valor_restante() <= 0:
            return "O atendimento já foi totalmente pago."

        match tipo:

            case "1":
                return self.__realizar_pagamento_dinheiro(data_pagamento, atendimento, paciente, valor_pago)

            case "2":
                return self.__realizar_pagamento_pix(data_pagamento, atendimento, paciente, valor_pago, cpf_pagador)

            case "3":
                return self.__realizar_pagamento_cartao(data_pagamento, atendimento, paciente, numero_cartao, bandeira, parcelas)

            case _:
                return "Opção inválida."

    def __realizar_pagamento_dinheiro(self, data_pagamento, atendimento, paciente, valor_pago):

        pagamento = PagamentoDinheiro(data_pagamento, atendimento, paciente, valor_pago)

        return atendimento.registrar_pagamento(pagamento)

    def __realizar_pagamento_pix(self, data_pagamento, atendimento, paciente, valor_pago, cpf_pagador):

        pagamento = PagamentoPix(data_pagamento, atendimento, paciente, valor_pago, cpf_pagador)

        return atendimento.registrar_pagamento(pagamento)

    def __realizar_pagamento_cartao(self, data_pagamento, atendimento, paciente, numero_cartao, bandeira, parcelas):

        valor_restante = (
            atendimento.calcular_valor_restante()
        )

        pagamento = PagamentoCartao(data_pagamento, atendimento, paciente, valor_restante, numero_cartao, bandeira, parcelas)

        return atendimento.registrar_pagamento(pagamento)