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

    def selecionar_procedimento(self, procedimentos):
        print("\nProcedimentos deste atendimento:")
        for indice, procedimento in enumerate(procedimentos, start=1):
            print(
                f"{indice} - {procedimento.descricao} | "
                f"R$ {procedimento.custo:.2f}"
            )

        while True:
            try:
                escolha = int(input("Escolha o procedimento para editar: "))
            except ValueError:
                print("Digite um número válido.")
                continue

            if 1 <= escolha <= len(procedimentos):
                return procedimentos[escolha - 1]
            print("Opção inválida.")

    def lista_procedimentos(self, registros):
        if not registros:
            self.mostra_mensagem("Nenhum procedimento cadastrado.")
            return
        print("\nProcedimentos cadastrados:")
        for indice, (procedimento, atendimento) in enumerate(registros, start=1):
            print(
                f"{indice} - {procedimento.descricao} | "
                f"R$ {procedimento.custo:.2f} | "
                f"Paciente: {atendimento.paciente.nome} | "
                f"Atendimento: {atendimento.data.isoformat()} "
                f"{atendimento.horario_inicio.strftime('%H:%M')} | "
                f"Profissional: {procedimento.profissional.nome}"
            )

    def selecionar_registro_procedimento(self, registros, acao):
        if not registros:
            self.mostra_mensagem("Nenhum procedimento cadastrado.")
            return None
        self.lista_procedimentos(registros)
        while True:
            try:
                escolha = int(input(f"Escolha o procedimento para {acao}: "))
            except ValueError:
                self.mostra_mensagem("Digite um número válido.")
                continue
            if 1 <= escolha <= len(registros):
                return registros[escolha - 1]
            self.mostra_mensagem("Opção inválida.")

    def confirmar_remocao(self):
        return input("Confirma a remoção? (s/n): ").strip().lower() == "s"

    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}")