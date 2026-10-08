class telaProfissional:
    def tela_opcoes(self):
            print("\n========== PROFISSIONAIS ==========")
            print("1 - Listar profissionais")
            print("3 - Cadastrar profissional")
            print("4 - Editar profissional")
            print("5 - Remover profissional")
            print("0 - Sair")
            print("==============================")
    
            try:
                return int(input("Escolha uma opção: "))
            except ValueError:
                return "Opção invalída"