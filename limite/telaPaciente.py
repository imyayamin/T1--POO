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
        while True:
            try:
                nome = str(input("Nome: "))
                if nome.strip() != "":
                    break
                print("O nome não pode estar vazio.")
            except ValueError:
                print("Entrada inválida. Digite um nome válido.")

        while True:
            try:
                celular = int(input("Celular (apenas números): "))
                break
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros para o celular.")

        while True:
            try:
                cpf = int(input("CPF (apenas números): "))
                break
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros para o CPF.")

        while True:
            try:
                idade = int(input("Idade: "))
                if idade > 0:
                    break
                print("A idade deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro para a idade.")

        return {"nome": nome, "celular": celular, "cpf": cpf, "idade": idade}

    def pega_dados_acompanhante(self):
        print("-------- DADOS ACOMPANHANTE ----------")
        try:
            nome = str(input("Nome do acompanhante: "))
        except ValueError:
            print("Entrada inválida. Digite um nome válido.")
        return nome

    def seleciona_paciente(self):
        try:
            return int(input("CPF do paciente: "))
        except ValueError:
            return None

    def lista_pacientes(self, pacientes):
        print("\nPacientes cadastrados:")
        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i} - {paciente.nome} - CPF: {paciente.cpf} - Idade: {paciente.idade}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
