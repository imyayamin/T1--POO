import math


class TelaTipoAtendimento:
    def tela_opcoes(self):
        print("\n======= TIPOS DE ATENDIMENTO =======")
        print("1 - Listar tipos")
        print("2 - Cadastrar tipo")
        print("3 - Alterar tipo")
        print("4 - Remover tipo")
        print("0 - Voltar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return None

    def lista_tipos(self, tipos):
        print("\nTipos de atendimento cadastrados:")
        for indice, tipo in enumerate(tipos, start=1):
            print(f"{indice} - {tipo.nome} | R$ {tipo.valor:.2f}")

    def seleciona_tipo(self, tipos):
        if not tipos:
            return None
        self.lista_tipos(tipos)
        while True:
            try:
                escolha = int(input("Escolha o tipo: "))
            except ValueError:
                print("Digite um número válido.")
                continue
            if 1 <= escolha <= len(tipos):
                return tipos[escolha - 1]
            print("Opção inválida.")

    def pega_dados_tipo(self):
        while True:
            nome = input("Nome do tipo de atendimento: ").strip()
            if nome:
                break
            print("O nome não pode estar vazio.")

        while True:
            try:
                valor = float(input("Valor do tipo de atendimento: R$ ").replace(",", "."))
                if math.isfinite(valor) and valor > 0:
                    return {"nome": nome, "valor": valor}
                print("O valor deve ser maior que zero.")
            except ValueError:
                print("Digite um valor numérico válido.")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
