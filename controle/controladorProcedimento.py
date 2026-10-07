from entidade.procedimento import Procedimento
from limite.telaProcedimento import TelaProcedimento


class ControladorProcedimento:

    def __init__(self, controladorGeral, controladorAtendimento, controladorProfissional):
        self.__controladorGeral = controladorGeral
        self.__controladorAtendimento = controladorAtendimento
        self.__controladorProfissional = controladorProfissional
        self.__telaProcedimento = TelaProcedimento()

    def abre_tela(self):
        atendimento = self.__telaProcedimento.escolher_atendimento(self.__controladorAtendimento.atendimentos)

        profissional = self.__telaProcedimento.escolher_profissional(self.__controladorProfissional.profissionais)

        descricao = self.__telaProcedimento.informar_descricao()
        custo = self.__telaProcedimento.informar_custo()

        mensagem = self.registrar_procedimento(atendimento, descricao, custo, profissional)

        self.__telaProcedimento.mostra_mensagem(mensagem)

    def registrar_procedimento(self, atendimento, descricao, custo, profissional):
        if atendimento not in self.__controladorAtendimento.atendimentos:
            return "Atendimento não encontrado."

        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não encontrado."

        if not descricao.strip():
            return "A descrição do procedimento não pode ser vazia."

        if custo <= 0:
            return "O custo do procedimento deve ser maior que zero."

        procedimento = Procedimento(descricao, custo, profissional)

        atendimento.adicionar_procedimento(procedimento)

        return "Procedimento cadastrado com sucesso!"