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

    def listar_profissionais(self, profissionais):
        profissionais = self.__controladorProfissional.profissionais
        
        if not profissionais:
            print("Nenhum profissional cadastrado.")
            return None
        
        print("\nProfissionais cadastrados:")
        
        for i, profissional in enumerate(profissionais, start=1):
            print(f"{i} - {profissional.nome} - {profissional.cpf}")

    def pega_dados_profissional(self):
        print("-------- DADOS PROFISSIONAL ----------")
        nome = input("Nome: ")
        celular = input("Celular: ")
        cpf = input("CPF: ")
        especialidade = input("Especialidade: ")
        registro_profissional = input("Registro profissional: ")

        return {"nome": nome, "celular": celular, "cpf": cpf, "especialidade": especialidade, "registro_profissional": registro_profissional}

    def seleciona_profissional(self):
        try:
            return int(input("CPF do profissional: "))
        except ValueError:
            self.mostra_mensagem("CPF inválido.")
            return None

    def mostra_mensagem(self, mensagem):
        print(mensagem)
