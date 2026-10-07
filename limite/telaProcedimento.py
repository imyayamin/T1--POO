class TelaProcedimento:

    def escolher_atendimento(self, atendimentos):
        if not atendimentos:
            self.mostra_mensagem("Nenhum atendimento cadastrado.")
            return None

        print("\n========== ATENDIMENTOS ==========")

        for i, atendimento in enumerate(atendimentos):
            print(
                f"{i + 1} - "
                f"Paciente: {atendimento.paciente.nome} | "
                f"Data: {atendimento.data} | "
                f"Tipo: {atendimento.tipo_atendimento}"
            )

        while True:
            try:
                opcao = int(input("Escolha o atendimento: "))

                if 1 <= opcao <= len(atendimentos):
                    return atendimentos[opcao - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    def escolher_profissional(self, profissionais):
        if not profissionais:
            self.mostra_mensagem("Nenhum profissional cadastrado.")
            return None

        print("\n========== PROFISSIONAIS ==========")

        for i, profissional in enumerate(profissionais):
            print(
                f"{i + 1} - "
                f"{profissional.nome} | CPF: {profissional.cpf}"
            )

        while True:
            try:
                opcao = int(input("Escolha o profissional responsável: "))

                if 1 <= opcao <= len(profissionais):
                    return profissionais[opcao - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    def informar_descricao(self):
        return input("Descrição do procedimento: ")

    def informar_custo(self):
        while True:
            try:
                return float(input("Custo do procedimento: "))
            except ValueError:
                print("Digite um valor numérico válido.")

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")