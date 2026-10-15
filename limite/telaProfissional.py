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
                especialidade = str(input("Especialidade: "))
                if especialidade.strip() != "":
                    break
                print("A especialidade não pode estar vazia.")
            except ValueError:
                print("Entrada inválida. Digite uma especialidade válida.")
        while True:
            try:
                registro_profissional = int(input("Registro profissional (apenas números): "))
                break
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros para o registro profissional.")

        return {"nome": nome, "celular": celular, "cpf": cpf, "especialidade": especialidade, "registro_profissional": registro_profissional}

    def seleciona_profissional(self):
        try:
            return int(input("CPF do profissional: "))
        except ValueError:
            self.mostra_mensagem("CPF inválido.")
            return None

    def mostra_mensagem(self, mensagem):
        print(mensagem)
