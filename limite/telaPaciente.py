class TelaPaciente:
    def tela_opcoes(self):
            print("\n========== PACIENTES ==========")
            print("1 - Listar paciente")
            print("2 - Cadastrar paciente")
            print("3 - Remover paciente")
            print("0 - Sair")
            print("==============================")
    
            try:
                return int(input("Escolha uma opção: "))
            except ValueError:
                return "Opção invalída"

    def lista_pacientes(self):
        pacientes = self.__controladorPaciente.pacientes
        
        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return None
        
        print("\nPacientes cadastrados:")
        
        for i, paciente in enumerate(pacientes, start=1):
            print(f"{i} - {paciente.nome}")