class TelaRelatorio:
    def tela_opcoes(self):
        print("\n========== RELATÓRIOS ==========")
        print("1 - Clínicas com mais atendimentos")
        print("2 - Atendimentos mais caros e mais baratos")
        print("3 - Procedimentos mais realizados")
        print("4 - Procedimentos mais caros e mais baratos")
        print("0 - Voltar")
        print("================================")

        try:
            return int(input("Escolha um relatório: "))
        except ValueError:
            return None

    def mostra_clinicas_com_mais_atendimentos(self, resultado):
        print("\nClínicas com maior número de atendimentos:")
        for clinica, quantidade in resultado:
            print(f"- {clinica.nome}: {quantidade} atendimento(s)")

    def mostra_atendimentos_extremos(self, mais_caros, mais_baratos):
        print("\nAtendimento(s) mais caro(s):")
        for atendimento, valor in mais_caros:
            self.__mostra_atendimento(atendimento, valor)

        print("\nAtendimento(s) mais barato(s):")
        for atendimento, valor in mais_baratos:
            self.__mostra_atendimento(atendimento, valor)

    def __mostra_atendimento(self, atendimento, valor):
        print(
            f"- {atendimento.data.isoformat()} às "
            f"{atendimento.horario_inicio.strftime('%H:%M')} | "
            f"Paciente: {atendimento.paciente.nome} | "
            f"Clínica: {atendimento.clinica.nome} | "
            f"Total: R$ {valor:.2f}"
        )

    def mostra_procedimentos_populares(self, populares):
        print("\nProcedimento(s) mais realizado(s):")
        for ocorrencias in populares:
            procedimento = ocorrencias[0][0]
            print(
                f"- {procedimento.descricao}: "
                f"{len(ocorrencias)} realização(ões)"
            )

    def mostra_procedimentos_extremos(self, mais_caros, mais_baratos):
        print("\nProcedimento(s) mais caro(s):")
        for procedimento, atendimento in mais_caros:
            self.__mostra_procedimento(procedimento, atendimento)

        print("\nProcedimento(s) mais barato(s):")
        for procedimento, atendimento in mais_baratos:
            self.__mostra_procedimento(procedimento, atendimento)

    def __mostra_procedimento(self, procedimento, atendimento):
        print(
            f"- {procedimento.descricao}: R$ {procedimento.custo:.2f} | "
            f"Paciente: {atendimento.paciente.nome} | "
            f"Data: {atendimento.data.isoformat()}"
        )

    def mostra_mensagem(self, mensagem):
        print(mensagem)