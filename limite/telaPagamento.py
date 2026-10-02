from entidade.pagamentoCartao import PagamentoCartao
from entidade.pagamentoDinheiro import PagamentoDinheiro
from entidade.pagamentoPix import PagamentoPix


class TelaPagamento:

    def escolher_tipo(self, data_pagamento, atendimento, paciente, valor_pago):

        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de crédito")

        resposta = input("Digite a opção: ").strip()

        match resposta:

            case "1":
                pagamento = PagamentoDinheiro(data_pagamento, atendimento, paciente, valor_pago)

            case "2":
                cpf_pagador = input("Digite o CPF do pagador: ").strip()

                pagamento = PagamentoPix(data_pagamento, atendimento, paciente, valor_pago, cpf_pagador)

            case "3":
                numero_cartao = input("Digite o número do cartão: ").strip()
                bandeira = input("Digite a bandeira do cartão: ").strip().lower()

                pagamento = PagamentoCartao(data_pagamento, atendimento, paciente, valor_pago, numero_cartao, bandeira)

            case _:
                return "Opção inválida!" #adicionar exception

        return pagamento