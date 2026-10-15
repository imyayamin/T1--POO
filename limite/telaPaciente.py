import re


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
            celular = re.sub(
                r"\D",
                "",
                input("Celular (com DDD, 10 ou 11 dígitos): ").strip(),
            )
            if len(celular) in (10, 11):
                break
            print("Telefone inválido. Informe DDD e número (10 ou 11 dígitos).")

        while True:
            cpf = re.sub(
                r"\D",
                "",
                input("CPF (11 dígitos): ").strip(),
            )
            if cpf.isdigit() and len(cpf) == 11:
                break
            print("CPF inválido. Informe os 11 dígitos.")

        while True:
            try:
                idade = int(input("Idade: "))
                if 0 <= idade <= 120:
                    break
                print("A idade deve estar entre 0 e 120 anos.")
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
        cpf = re.sub(r"\D", "", input("CPF do paciente (11 dígitos): ").strip())
        if len(cpf) == 11:
            return cpf
        self.mostra_mensagem("CPF inválido.")
        return None

    def lista_pacientes(self, pacientes):
        print("\nPacientes cadastrados:")
        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i} - {paciente.nome} - CPF: {paciente.cpf} - Idade: {paciente.idade}")

    def mostra_mensagem(self, mensagem):
        print(mensagem)
