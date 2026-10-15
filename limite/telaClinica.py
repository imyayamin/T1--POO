from exceptions.exceptions import (ListaVaziaException, ClinicaRepetidaException, ClinicaNaoEncontradaException, HorarioInvalidoException, EntradaInvalidaException)

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

    def lista_clinicas(self, clinicas):
        print("\nClínicas cadastradas:")
        for i, clinica in enumerate(clinicas, start=1):
            print(f"{i} - {clinica.nome} | Cidade: {clinica.cidade} | Horário: {clinica.horario_inicial}h às {clinica.horario_final}h")

    def pega_dados_clinica(self):
        print("-------- DADOS CLÍNICA ----------")
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
                cidade = str(input("Cidade: "))
                if cidade.strip() != "":
                    break
                print("A cidade não pode estar vazia.")
            except ValueError:
                print("Entrada inválida. Digite uma cidade válida.")
        while True:
            try:
                descricao = str(input("Descrição: "))
                if descricao.strip() != "":
                    break
                print("A descrição não pode estar vazia.")
            except ValueError:
                print("Entrada inválida. Digite uma descrição válida.")
        
        try:
            horario_inicial = int(input("Horário inicial (ex: 8): "))
            horario_final = int(input("Horário final (ex: 18): "))
        except ValueError:
            raise EntradaInvalidaException("horário")

        return {
            "nome": nome,
            "cidade": cidade,
            "descricao": descricao,
            "horario_inicial": horario_inicial,
            "horario_final": horario_final
        }

    def seleciona_clinica(self):
        return input("Digite o nome da clínica: ")

    def mostra_mensagem(self, mensagem):
        print(mensagem)