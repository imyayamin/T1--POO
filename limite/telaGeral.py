class TelaGeral:

    def tela_opcoes(self):
        print("\n========== CLÍNICA ==========")
        print("1 - pacientes")
        print("2 - profissionais")
        print("3 - clinicas")
        print("4 - Agendar atendimento")
        print("5 - Registrar pagamento")
        print("6 - Registrar procedimento")
        print("0 - Sair")
        print("==============================")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return "Opção invalída"