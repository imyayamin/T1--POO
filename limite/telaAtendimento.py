from datetime import date, time

class TelaAtendimento:

    def __init__(self, controladorAtendimento, controladorClinica, controladorPaciente,controladorProfissional, controladorAcompanhante):#não precisa de import já que tão passando pelo construtor
        self.__controladorAtendimento = controladorAtendimento
        self.__controladorClinica = controladorClinica
        self.__controladorPaciente = controladorPaciente
        self.__controladorProfissional = controladorProfissional
        self.__controladorAcompanhante = controladorAcompanhante

    def escolher_clinica(self):
        clinicas = self.__controladorClinica.clinicas

        if not clinicas:
            return None

        print("\nClínicas cadastradas:")

        for i, clinica in enumerate(clinicas, start=1):#coloquei pra começar em 1 apenas por estetica pra lista ficar bonitinha no print
            print(f"{i} - {clinica.nome}")

        opcao = int(input("Escolha a clínica: "))

        if opcao < 1 or opcao > len(clinicas):
            return None

        return clinicas[opcao - 1]# pra igualar com o real valor da opção já que a lista começa em 1 e não em 0

    def escolher_paciente(self):
        pacientes = self.__controladorPaciente.pacientes

        if not pacientes:
            return None

        print("\nPacientes cadastrados:")

        for i, paciente in enumerate(pacientes, start=1):#coloquei pra começar em 1 apenas por estetica pra lista ficar bonitinha no print
            print(f"{i} - {paciente.nome}")

        opcao = int(input("Escolha o paciente: "))

        if opcao < 1 or opcao > len(pacientes):
            return None

        return pacientes[opcao - 1]# pra igualar com o real valor da opção já que a lista começa em 1 e não em 0

    def escolher_profissional(self):
        profissionais = self.__controladorProfissional.profissionais

        if not profissionais:
            return None

        print("\nProfissionais cadastrados:")

        for i, profissional in enumerate(profissionais, start=1):#coloquei pra começar em 1 apenas por estetica pra lista ficar bonitinha no print
            print(f"{i} - {profissional.nome}")

        opcao = int(input("Escolha o profissional: "))

        if opcao < 1 or opcao > len(profissionais):
            return None

        return profissionais[opcao - 1]# pra igualar com o real valor da opção já que a lista começa em 1 e não em 0

    def escolher_acompanhante(self):
        acompanhantes = self.__controladorAcompanhante.acompanhantes

        if not acompanhantes:
            return None

        print("\nAcompanhantes cadastrados:")

        for i, acompanhante in enumerate(acompanhantes, start=1):#coloquei pra começar em 1 apenas por estetica pra lista ficar bonitinha no print
            print(f"{i} - {acompanhante.nome}")

        opcao = int(input("Escolha o acompanhante: "))

        if opcao < 1 or opcao > len(acompanhantes):
            return None

        return acompanhantes[opcao - 1]# pra igualar com o real valor da opção já que a lista começa em 1 e não em 0

    def agendar_atendimento(self, clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante):
        clinica = self.escolher_clinica()
        profissional = self.escolher_profissional()
        paciente = self.escolher_paciente()

        data = date.fromisoformat(input("Digite a data do atendimento (AAAA-MM-DD): "))

        horario_inicio = time.fromisoformat(input("Digite o horário de início (HH:MM): "))

        horario_fim = time.fromisoformat(input("Digite o horário de fim (HH:MM): "))


        print("\nTipos de atendimento:")
        print("1 - Consulta")
        print("2 - Exame")
        print("3 - Retorno")
        print("4 - Outro")

        opcao = input("Escolha o tipo de atendimento: ").strip()

        match opcao:
            case "1":
                tipoAtendimento = "Consulta"

            case "2":
                tipoAtendimento = "Exame"

            case "3":
                tipoAtendimento = "Retorno"

            case "4":
                tipoAtendimento = input("Digite o tipo de atendimento: ").strip()

            case _:
                return "Tipo de atendimento inválido!"

        valor = float(input("Digite o valor do atendimento: "))#isso me parece errado acho que deviamos fazer uma tabela de preços

        acompanhante = None

        if paciente.idade < 18:
            while acompanhante is None:#entra em um loop e só sai se apresentar sua acompanhante
                acompanhante = self.escolher_acompanhante()

                if acompanhante is None:
                    print("Você precisa escolher um acompanhante.")

        # Envia os dados para o controlador
        resultado = self.__controladorAtendimento.agendar_atendimento(clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante)

        return resultado