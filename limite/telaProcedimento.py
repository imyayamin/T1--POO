class TelaProcedimento:
    def informar_descricao(self):
        while True:
            descricao = input("Nome/descrição do procedimento: ").strip()
            if descricao:
                return descricao
            print("A descrição do procedimento não pode ser vazia.")

    def informar_custo(self):
        while True:
            try:
                custo = float(
                    input("Valor do procedimento: R$ ").replace(",", ".")
                )
                if custo > 0:
                    return custo
                print("O valor do procedimento deve ser maior que zero.")
            except ValueError:
                print("Digite um valor numérico válido.")

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")