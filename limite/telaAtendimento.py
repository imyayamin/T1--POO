from datetime import date, time


class TelaAtendimento:

    def __init__(self, controladorAtendimento):
        self.__controladorAtendimento = controladorAtendimento

    def agendar_atendimento(self, clinica, paciente, profissional):

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
                tipoAtendimento = input(
                    "Digite o tipo de atendimento: "
                ).strip()

            case _:
                return "Tipo de atendimento inválido!" #Outra exception sepá

        valor = float(input("Digite o valor do atendimento: "))

        acompanhante = None

        if paciente.idade < 18:
            acompanhante = input("Informe o acompanhante: ")

        resultado = self.__controladorAtendimento.agendar_atendimento(clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante)

        return resultado