class TelaGeral:

    def tela_opcoes(self):
        print("\n========== CLÍNICA ==========")
        print("1 - Cadastrar paciente")
        print("2 - Cadastrar profissional")
        print("3 - Cadastrar clínica")
        print("4 - Cadastrar acompanhante")
        print("5 - Agendar atendimento")
        print("6 - Registrar pagamento")
        print("7 - Registrar procedimento")
        print("0 - Sair")
        print("==============================")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return "Opção invalída"