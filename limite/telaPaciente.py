class TelaPaciente:
    def tela_opcoes(self):
        print("\n========== PACIENTES ==========")
        print("1 - Listar pacientes")
        print("2 - Cadastrar paciente")
        print("3 - Remover paciente")
        print("0 - Retornar")
        print("==============================")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    def pega_dados_paciente(self):
        print("-------- DADOS PACIENTE ----------")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
        return {"nome": nome, "celular": celular, "cpf": cpf, "idade": idade,}

    def pega_dados_acompanhante(self):
        print("-------- DADOS ACOMPANHANTE ----------")
        nome = input("Nome do acompanhante: ")
        return nome

    def seleciona_paciente(self):
        try:
            return int(input("CPF do paciente: "))
        except ValueError:
            return None

    def lista_pacientes(self, pacientes):
        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return
        print("\nPacientes cadastrados:")
        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i} - {paciente.nome} - CPF: {paciente.cpf} - Idade: {paciente.idade}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def pega_acompanhante(self):
        return input("Nome do acompanhante: ").strip()
