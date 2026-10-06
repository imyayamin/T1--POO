class TelaPagamento:

    def realizar_pagamento(self, controlador_pagamento, data_pagamento, atendimento, paciente):

        tipo = self.escolher_tipo()

        match tipo:

            case "1":

                valor_pago = self.informar_valor()

                mensagem = (controlador_pagamento.realizar_pagamento(tipo, data_pagamento, atendimento, paciente, valor_pago=valor_pago))

            case "2":

                cpf_pagador = self.informar_cpf()
                valor_pago = self.informar_valor()

                mensagem = (controlador_pagamento.realizar_pagamento(tipo, data_pagamento, atendimento, paciente, valor_pago=valor_pago, cpf_pagador=cpf_pagador))

            case "3":

                numero_cartao = self.informar_cartao()
                bandeira = self.informar_bandeira()
                parcelas = self.informar_parcelas()

                mensagem = (controlador_pagamento.realizar_pagamento(tipo, data_pagamento, atendimento, paciente, numero_cartao=numero_cartao, bandeira=bandeira, parcelas=parcelas))

            case _:
                mensagem = "Opção inválida."

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
                valor = float(
                    input("Digite o valor a pagar: R$ " ))

                if valor <= 0:
                    print(  "O valor deve ser maior que zero.")
                    continue

                return valor

            except ValueError:

                print( "Digite um valor válido.")

    def informar_cpf(self):

        return input("Digite o CPF do pagador: ").strip()

    def informar_cartao(self):

        return input( "Digite o número do cartão: ").strip()

    def informar_bandeira(self):

        return input( "Digite a bandeira do cartão: ").strip().lower()

    def informar_parcelas(self):

        print("\nPARCELAMENTO")

        print("1x")
        print("2x")
        print("3x")

        while True:

            try:
                parcelas = int(input( "Em quantas vezes deseja pagar? "))

                if parcelas < 1 or parcelas > 3:

                    print("Quantidade de parcelas inválida. Escolha entre 1 e 3." )

                    continue

                return parcelas

            except ValueError:

                print( "Digite um número válido.")

    def mostrar_mensagem(self, mensagem):

        print(mensagem)