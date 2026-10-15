from datetime import date, time

class TelaAtendimento:
    def __init__(self, controladorAtendimento, controladorClinica, controladorPaciente, controladorProfissional):
        self.__controladorAtendimento = (controladorAtendimento)
        self.__controladorClinica = (controladorClinica)
        self.__controladorPaciente = (controladorPaciente)
        self.__controladorProfissional = (controladorProfissional)

    def tela_opcoes(self):
        print("\n========== ATENDIMENTOS ==========")
        print("1 - Cadastrar atendimento")
        print("2 - Listar atendimentos")
        print("3 - Editar atendimento")
        print("4 - Remover atendimento")
        print("0 - Voltar")
        print("==================================")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return None

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def escolher_clinica(self):

        clinicas = self.__controladorClinica.clinicas

        if not clinicas:
            print("Nenhuma clínica cadastrada.")
            return None

        print("\nClínicas cadastradas:")

        for i, clinica in enumerate(clinicas, start=1):
            print(f"{i} - {clinica.nome}")

        while True:
            try:
                opcao = int(input("Escolha a clínica: "))

                if 1 <= opcao <= len(clinicas):
                    return clinicas[opcao - 1]
                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    def escolher_paciente(self):
        pacientes = self.__controladorPaciente.pacientes

        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return None

        print("\nPacientes cadastrados:")
        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i} - {paciente.nome}")

        while True:
            try:
                opcao = int(input("Escolha o paciente: "))
                if 1 <= opcao <= len(pacientes):
                    return pacientes[opcao - 1]
                print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

    def escolher_profissional(self):
        profissionais = self.__controladorProfissional.profissionais

        profissionais = (self.__controladorProfissional.profissionais)

        if not profissionais:
            print("Nenhum profissional cadastrado.")
            return None

        print("\nProfissionais cadastrados:")

        for i, profissional in enumerate(profissionais, start=1):
            print(f"{i} - {profissional.nome}")

        while True:
            try:
                opcao = int(input("Escolha o profissional: "))

                if 1 <= opcao <= len(profissionais):
                    return profissionais[opcao - 1]

                print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

    def escolher_tipo_atendimento(self):
        print("\nTipos de atendimento:")
        print("1 - Consulta (R$ 100,00)")
        print("2 - Exame (R$ 150,00)")
        print("3 - Retorno (R$ 70,00)")
        print("4 - Outro (R$ 120,00)")

        tipos = {
            "1": "Consulta",
            "2": "Exame",
            "3": "Retorno",
            "4": "Outro",
        }
        while True:
            tipo = tipos.get(input("Escolha o tipo de atendimento: ").strip())
            if tipo is not None:
                return tipo
            print("Opção inválida. Escolha um tipo válido.")

    def informar_data(self):
        while True:

            try:
                return date.fromisoformat(input("Digite a data do atendimento(AAAA-MM-DD): "))

            except ValueError:

                print("Data inválida. Use o formato AAAA-MM-DD.")

    def informar_horario_inicio(self):

        while True:

            try:
                return time.fromisoformat(input("Digite o horário de início(HH:MM): "))

            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

    def informar_horario_fim(self):

        while True:

            try:
                return time.fromisoformat(input("Digite o horário de fim(HH:MM): "))

            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

    def pega_dados_atendimento(self):
        clinica = self.escolher_clinica()
        if clinica is None:
            return None

        paciente = self.escolher_paciente()
        if paciente is None:
            return None

        profissional = self.escolher_profissional()
        if profissional is None:
            return None

        tipo_atendimento = self.escolher_tipo_atendimento()
        data = self.informar_data()

        while True:
            horario_inicio = self.informar_horario_inicio()
            horario_fim = self.informar_horario_fim()

            if horario_fim <= horario_inicio:
                print("Erro: O horário final deve ser maior que o horário inicial.")
                continue

            if not self.__controladorAtendimento.horario_dentro_da_clinica(
                clinica, horario_inicio, horario_fim
            ):
                print(
                    "Erro: o atendimento deve estar dentro do horário da clínica "
                    f"({clinica.horario_funcionamento_inicial}h às "
                    f"{clinica.horario_funcionamento_final}h)."
                )
                continue
            break

        return {
            "clinica": clinica,
            "paciente": paciente,
            "profissional": profissional,
            "tipo_atendimento": tipo_atendimento,
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
        }

    def lista_atendimentos(self, atendimentos):
        if not atendimentos:
            self.mostra_mensagem("Nenhum atendimento cadastrado.")
            return

        print("\nAtendimentos cadastrados:")
        for indice, atendimento in enumerate(atendimentos, start=1):
            print(
                f"{indice} - {atendimento.data.isoformat()} | "
                f"{atendimento.horario_inicio.strftime('%H:%M')} às "
                f"{atendimento.horario_fim.strftime('%H:%M')} | "
                f"Paciente: {atendimento.paciente.nome} | "
                f"Profissional: {atendimento.profissional.nome} | "
                f"Clínica: {atendimento.clinica.nome} | "
                f"Tipo: {atendimento.tipoAtendimento} | "
                f"Procedimento(s): "
                f"{', '.join(procedimento.descricao for procedimento in atendimento.procedimentos)} | "
                f"Valor: R$ {atendimento.valor_total():.2f}"
            )

    def seleciona_atendimento(self, atendimentos):
        while True:
            try:
                escolha = int(input("Escolha o número do atendimento: "))
            except ValueError:
                self.mostra_mensagem("Digite um número válido.")
                continue

            if 1 <= escolha <= len(atendimentos):
                return atendimentos[escolha - 1]

            self.mostra_mensagem("Opção inválida.")