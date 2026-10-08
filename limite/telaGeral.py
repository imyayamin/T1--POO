class TelaGeral:

    def tela_opcoes(self):
        print("\n========== CLÍNICA ==========")
        print("1 - pacientes")
        print("2 - profissionais")
        print("3 - clinicas")
        print("4 - ")
        print("5 - Agendar atendimento")
        print("6 - Registrar pagamento")
        print("7 - Registrar procedimento")
        print("0 - Sair")
        print("==============================")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return "Opção invalída"