class TelaPagamento:

    def realizar_pagamento(self, controlador_pagamento, data_pagamento, atendimento, paciente):

        mensagem = controlador_pagamento.realizar_pagamento(data_pagamento, atendimento, paciente)

        self.mostrar_mensagem(mensagem)

    def escolher_tipo(self):
        print("\nFORMA DE PAGAMENTO")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de crédito")

        return input("Digite a opção: ").strip()

    def informar_valor(self):
        while True:
            try:
                valor = float(input("Digite o valor a pagar: R$ "))

                if valor <= 0:
                    print("O valor deve ser maior que zero.")
                    continue

                return valor

            except ValueError:
                print("Digite um valor válido.")

    def informar_cpf(self):
        return input("Digite o CPF do pagador: ").strip()

    def informar_cartao(self):
        return input("Digite o número do cartão: ").strip()

    def informar_bandeira(self):
        return input("Digite a bandeira do cartão: ").strip().lower()

    def informar_parcelas(self, valor):
        print("\nPARCELAMENTO")

        for i in range(1, 4):
            valor_parcela = valor / i
            print(f"{i}x - R$ {valor_parcela:.2f}")

        while True:
            try:
                parcelas = int(input("Em quantas vezes deseja pagar? "))

                if parcelas < 1 or parcelas > 3:
                    print(
                        "Quantidade de parcelas inválida. "
                        "Escolha entre 1 e 3."
                    )
                    continue

                return parcelas

            except ValueError:
                print("Digite um número válido.")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)