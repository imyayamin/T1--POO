from datetime import date, time

class TelaAtendimento:

    def __init__(self, controladorAtendimento, controladorClinica, controladorPaciente, controladorProfissional, controladorAcompanhante):
        self.__controladorAtendimento = (controladorAtendimento)
        self.__controladorClinica = (controladorClinica)
        self.__controladorPaciente = (controladorPaciente)
        self.__controladorProfissional = (controladorProfissional)
        self.__controladorAcompanhante = (controladorAcompanhante)

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

    def escolher_acompanhante(self):

        acompanhantes = (self.__controladorAcompanhante.acompanhantes)

        if not acompanhantes:
            print("Nenhum acompanhante cadastrado.")
            return None

        print("\nAcompanhantes cadastrados:")

        for i, acompanhante in enumerate(acompanhantes, start=1):
            print(f"{i} - {acompanhante.nome}")

        while True:

            try:
                opcao = int(input("Escolha o acompanhante: "))

                if 1 <= opcao <= len(acompanhantes):
                    return acompanhantes[opcao - 1]

                print("Opção inválida.")

            except ValueError:

                print("Digite um número válido.")

    def escolher_tipo_atendimento(self):

        print("\nTipos de atendimento:")
        print("1 - Consulta")
        print("2 - Exame")
        print("3 - Retorno")
        print("4 - Outro")

        opcao = input("Escolha o tipo de atendimento: ").strip()

        match opcao:

            case "1":
                return "Consulta"

            case "2":
                return "Exame"

            case "3":
                return "Retorno"

            case "4":
                return "Outro"#deixar informar

            case _:
                return None

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
            return (
                "Não foi possível selecionar o profissional."
            )

        data = self.informar_data()

        horario_inicio = (self.informar_horario_inicio())

        horario_fim = (self.informar_horario_fim())

        tipoAtendimento = (self.escolher_tipo_atendimento())

        if tipoAtendimento is None:
            return "Tipo de atendimento inválido!"

        acompanhante = None

        if paciente.idade < 18:

            while acompanhante is None:

                acompanhante = (self.escolher_acompanhante())

                if acompanhante is None:
                    print("Você precisa escolher um acompanhante.")

        resultado = (self.__controladorAtendimento.agendar_atendimento(clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, acompanhante))

        return resultado