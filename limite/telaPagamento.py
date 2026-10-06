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

            case "3": #adicionar a possibilidade de parcelas
                numero_cartao = input("Digite o número do cartão: ").strip()
                bandeira = input("Digite a bandeira do cartão: ").strip().lower()

                print("\nParcelas disponíveis:")

                for i in range(1, 4):#parcela em até 3x só
                    valor_parcela = atendimento.valor / i
                    print(f"{i}x - R$ {valor_parcela:.2f}")

                parcela = int(input("Em quantas vezes gostaria de pagar?"))
                if parcela == 0 or parcela > 3: #isso pode virar um exception
                    return "Quantidade de parcelas inválidas."
                else:
                    valor_parcela = atendimento.valor/parcela #vai ter que usar isso em algum lugar do controle
                    print(f"Seu pagamento no valor de R${atendimento.valor} será pago em {parcela} vezes de R${valor_parcela}")
                            
                pagamento = PagamentoCartao(data_pagamento, atendimento, paciente, valor_pago, numero_cartao, bandeira)

            case _:
                return "Opção inválida!" #adicionar exception

        return pagamento