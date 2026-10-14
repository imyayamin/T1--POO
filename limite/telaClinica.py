class TelaClinica:
    def tela_opcoes(self):
            print("\n========== CLÍNICAS ==========")
            print("1 - Listar clinicas")
            print("2 - Cadastrar clinica")
            print("3 - Remover clinica")
            print("0 - Sair")
            print("==============================")
        
            try:
                return int(input("Escolha uma opção: "))
            except ValueError:
                return "Opção invalída"