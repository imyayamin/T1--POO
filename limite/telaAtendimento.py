from datetime import date, time

class TelaAtendimento:
    def __init__(self, controladorAtendimento, controladorClinica, controladorPaciente, controladorProfissional):
        self.__controladorAtendimento = (controladorAtendimento)
        self.__controladorClinica = (controladorClinica)
        self.__controladorPaciente = (controladorPaciente)
        self.__controladorProfissional = (controladorProfissional)

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
        print("1 - Consulta")
        print("2 - Exame")
        print("3 - Retorno")
        print("4 - Outro")

        tipos = {"1": "Consulta", "2": "Exame", "3": "Retorno", "4": "Outro"}
        tipo = tipos.get(input("Escolha o tipo de atendimento: ").strip())
        if tipo is None:
            print("Opção inválida. Escolha um tipo válido.")
        return tipo

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

    def agendar_atendimento(self):
        clinica = self.escolher_clinica()
        if clinica is None:
            return "Não foi possível selecionar a clínica."

        paciente = self.escolher_paciente()
        if paciente is None:
            return "Não foi possível selecionar o paciente."

        profissional = self.escolher_profissional()
        if profissional is None:
            return "Não foi possível selecionar o profissional."

        data = self.informar_data()

        while True:
            horario_inicio = self.informar_horario_inicio()
            horario_fim = self.informar_horario_fim()

            if horario_fim <= horario_inicio:
                print("Erro: o horário final deve ser maior que o inicial.")
                continue

            if not self.__controladorAtendimento.horario_dentro_da_clinica(
                    clinica, horario_inicio, horario_fim):
                print(f"Erro: a clínica funciona das {clinica.horario_inicial}h "
                      f"às {clinica.horario_final}h.")
                continue
            break

        tipo = None
        while tipo is None:
            tipo = self.escolher_tipo_atendimento()

        return self.__controladorAtendimento.agendar_atendimento(
            clinica, paciente, profissional, data, horario_inicio, horario_fim, tipo
        )