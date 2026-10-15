
from datetime import date, time


class TelaAtendimento:
    def __init__(
        self,
        controladorAtendimento,
        controladorClinica,
        controladorPaciente,
        controladorProfissional
    ):
        self.__controladorAtendimento = controladorAtendimento
        self.__controladorClinica = controladorClinica
        self.__controladorPaciente = controladorPaciente
        self.__controladorProfissional = controladorProfissional

    # MENU PRINCIPAL

    def abre_tela(self):
        while True:
            print("\n===== MENU DE ATENDIMENTOS =====")
            print("1 - Agendar atendimento")
            print("2 - Listar atendimentos")
            print("3 - Editar atendimento")
            print("4 - Excluir atendimento")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.__controladorAtendimento.agendar_atendimento_tela()
            elif opcao == "2":
                self.__controladorAtendimento.lista_atendimentos_tela()
            elif opcao == "3":
                self.__controladorAtendimento.alterar_atendimento()
            elif opcao == "4":
                self.__controladorAtendimento.excluir_atendimento()
            elif opcao == "0":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    # ESCOLHER CLÍNICA

    def escolher_clinica(self):
        clinicas = self.__controladorClinica.clinicas

        if not clinicas:
            print("Nenhuma clínica cadastrada.")
            return None

        print("\n--- Clínicas cadastradas ---")

        for i, clinica in enumerate(clinicas, start=1):
            print(f"{i} - {clinica.nome}")

        while True:
            try:
                opcao = int(input("Escolha a clínica (0 para cancelar): "))

                if opcao == 0:
                    return None

                if 1 <= opcao <= len(clinicas):
                    return clinicas[opcao - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    # ESCOLHER PACIENTE

    def escolher_paciente(self):
        pacientes = self.__controladorPaciente.pacientes

        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return None

        print("\n--- Pacientes cadastrados ---")

        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i} - {paciente.nome}")

        while True:
            try:
                opcao = int(input("Escolha o paciente (0 para cancelar): "))

                if opcao == 0:
                    return None

                if 1 <= opcao <= len(pacientes):
                    return pacientes[opcao - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    # ESCOLHER PROFISSIONAL

    def escolher_profissional(self):
        profissionais = self.__controladorProfissional.profissionais

        if not profissionais:
            print("Nenhum profissional cadastrado.")
            return None

        print("\n--- Profissionais cadastrados ---")

        for i, profissional in enumerate(profissionais, start=1):
            print(f"{i} - {profissional.nome}")

        while True:
            try:
                opcao = int(
                    input("Escolha o profissional (0 para cancelar): ")
                )

                if opcao == 0:
                    return None

                if 1 <= opcao <= len(profissionais):
                    return profissionais[opcao - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    # ESCOLHER TIPO DE ATENDIMENTO

    def escolher_tipo_atendimento(self):
        tipos = {
            "1": "Consulta",
            "2": "Exame",
            "3": "Retorno",
            "4": "Outro"
        }

        while True:
            print("\n--- Tipos de atendimento ---")
            print("1 - Consulta")
            print("2 - Exame")
            print("3 - Retorno")
            print("4 - Outro")
            print("0 - Cancelar")

            opcao = input("Escolha o tipo: ").strip()

            if opcao == "0":
                return None

            tipo = tipos.get(opcao)

            if tipo is not None:
                return tipo

            print("Opção inválida. Escolha um tipo válido.")

    # INFORMAR DATA

    def informar_data(self):
        while True:
            try:
                entrada = input(
                    "Digite a data (AAAA-MM-DD) ou 0 para cancelar: "
                ).strip()

                if entrada == "0":
                    return None

                return date.fromisoformat(entrada)

            except ValueError:
                print("Data inválida. Use o formato AAAA-MM-DD.")

    # INFORMAR HORÁRIO INICIAL

    def informar_horario_inicio(self):
        while True:
            try:
                entrada = input(
                    "Digite o horário inicial (HH:MM) ou 0 para cancelar: "
                ).strip()

                if entrada == "0":
                    return None

                return time.fromisoformat(entrada)

            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

    # INFORMAR HORÁRIO FINAL

    def informar_horario_fim(self):
        while True:
            try:
                entrada = input(
                    "Digite o horário final (HH:MM) ou 0 para cancelar: "
                ).strip()

                if entrada == "0":
                    return None

                return time.fromisoformat(entrada)

            except ValueError:
                print("Horário inválido. Use o formato HH:MM.")

    # COLETAR DADOS DO ATENDIMENTO

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

        data = self.informar_data()
        if data is None:
            return None

        while True:
            horario_inicio = self.informar_horario_inicio()
            if horario_inicio is None:
                return None

            horario_fim = self.informar_horario_fim()
            if horario_fim is None:
                return None

            if horario_fim <= horario_inicio:
                print(
                    "Erro: o horário final deve ser maior que o inicial."
                )
                continue

            if not self.__controladorAtendimento.horario_dentro_da_clinica(
                clinica, horario_inicio, horario_fim
            ):
                print(
                    "Erro: a clínica funciona das "
                    f"{clinica.horario_funcionamento_inicial} às "
                    f"{clinica.horario_funcionamento_final}."
                )
                continue

            break

        tipo = self.escolher_tipo_atendimento()
        if tipo is None:
            return None

        return {
            "clinica": clinica,
            "paciente": paciente,
            "profissional": profissional,
            "data": data,
            "horario_inicio": horario_inicio,
            "horario_fim": horario_fim,
            "tipoAtendimento": tipo
        }

    # AGENDAR

    def agendar_atendimento(self):
        dados = self.pega_dados_atendimento()

        if dados is None:
            return "Agendamento cancelado."

        return self.__controladorAtendimento.agendar_atendimento(
            dados["clinica"],
            dados["paciente"],
            dados["profissional"],
            dados["data"],
            dados["horario_inicio"],
            dados["horario_fim"],
            dados["tipoAtendimento"]
        )

    # LISTAR

    def lista_atendimentos(self, atendimentos):
        print("\n===== ATENDIMENTOS AGENDADOS =====")

        for i, atendimento in enumerate(atendimentos, start=1):
            print(f"\n{i} - Data: {atendimento.data}")
            print(f"    Clínica: {atendimento.clinica.nome}")
            print(f"    Paciente: {atendimento.paciente.nome}")
            print(f"    Profissional: {atendimento.profissional.nome}")
            print(
                f"    Horário: {atendimento.horario_inicio} "
                f"às {atendimento.horario_fim}"
            )
            print(f"    Tipo: {atendimento.tipoAtendimento}")
            print(f"    Valor: R$ {atendimento.valor:.2f}")

    # SELECIONAR ATENDIMENTO PARA EDITAR OU EXCLUIR

    def seleciona_atendimento(self):
        atendimentos = self.__controladorAtendimento.atendimentos

        if not atendimentos:
            return None

        self.lista_atendimentos(atendimentos)

        while True:
            try:
                opcao = int(input(
                    "\nDigite o número do atendimento (0 para cancelar): "
                ))

                if opcao == 0:
                    return None

                if 1 <= opcao <= len(atendimentos):
                    return atendimentos[opcao - 1]

                print("Opção inválida.")

            except ValueError:
                print("Digite um número válido.")

    # MOSTRAR MENSAGENS

    def mostra_mensagem(self, mensagem):
        print(mensagem)
