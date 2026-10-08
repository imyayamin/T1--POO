class TelaPaciente:
    def tela_opcoes(self):
            print("\n========== PACIENTES ==========")
            print("1 - Listar paciente")
            print("2 - Cadastrar paciente")
            print("3 - Cadastrar acompanhante")
            print("4 - Remover paciente")
            print("0 - Sair")
            print("==============================")
    
            try:
                return int(input("Escolha uma opção: "))
            except ValueError:
                return "Opção invalída"