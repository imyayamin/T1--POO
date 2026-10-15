import re


class TelaProfissional:

    def tela_opcoes(self):
        print("\n========== PROFISSIONAIS ==========")
        print("1 - Listar profissionais")
        print("2 - Cadastrar profissional")
        print("3 - Editar profissional")
        print("4 - Remover profissional")
        print("0 - Voltar")
        print("===================================")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return None

    def lista_profissionais(self, profissionais):
        print("\nProfissionais cadastrados:")
        
        for i, profissional in enumerate(profissionais, start=1):
            print(f"{i} - {profissional.nome} - {profissional.cpf}")

    def pega_dados_profissional(self):
        print("-------- DADOS PROFISSIONAL ----------")
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
                especialidade = str(input("Especialidade: "))
                if especialidade.strip() != "":
                    break
                print("A especialidade não pode estar vazia.")
            except ValueError:
                print("Entrada inválida. Digite uma especialidade válida.")
        while True:
            registro_profissional = re.sub(
                r"\D",
                "",
                input("Registro profissional (apenas números): ").strip(),
            )
            if registro_profissional:
                break
            print("O registro profissional deve conter números.")

        return {"nome": nome, "celular": celular, "cpf": cpf, "especialidade": especialidade, "registro_profissional": registro_profissional}

    def seleciona_profissional(self):
        cpf = re.sub(
            r"\D",
            "",
            input("CPF do profissional (11 dígitos): ").strip(),
        )
        if len(cpf) == 11:
            return cpf
        self.mostra_mensagem("CPF inválido.")
        return None

    def mostra_mensagem(self, mensagem):
        print(mensagem)
