from entidade.paciente import Paciente
from limite.telaPaciente import TelaPaciente
from exceptions.exceptions import PacienteRepetidoException

class ControladorPaciente:

    def __init__(self, ):
        self.__pacientes = []
        self.tela_paciente = TelaPaciente

    @property
    def pacientes(self):
        return self.__pacientes

    def cadastrar_paciente(self, nome, celular, cpf, idade):

        for paciente in self.__pacientes:

            if paciente.cpf == cpf:
                raise PacienteRepetidoException(novo_paciente.cpf)

        novo_paciente = Paciente(nome, celular, cpf, idade)

        self.__pacientes.append(novo_paciente)

        return "Paciente cadastrado com sucesso!"

    def listar_pacientes(self):
        if not self.__pacientes:
            return "Nenhum paciente cadastrado."
        else:
            print("Lista de pacientes:")
            for paciente in self.__pacientes:
                self.__tela_paciente.mostra_paciente({"nome": paciente.nome, "celular": paciente.celular, "cpf": paciente.cpf, "idade": paciente.idade})

            
    def remover_paciente(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                self.__pacientes.remove(paciente)
                return "Paciente removido com sucesso!"
        return "Paciente não encontrado."

    def abre_tela(self):
        while True:
            opcao = self.tela_paciente.tela_opcoes()

            if opcao == 1:
                self.listar_pacientes()
            elif opcao == 2:
                self.cadastrar_paciente()
            elif opcao == 3:
                self.remover_paciente()
            elif opcao == 0:
                break
            else:
                print("Opção inválida. Tente novamente.")
    