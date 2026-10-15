from entidade.procedimento import Procedimento
from limite.telaProcedimento import TelaProcedimento


class ControladorProcedimento:
    def __init__(self, controladorGeral, controladorAtendimento, controladorProfissional):
        self.__controladorGeral = controladorGeral
        self.__controladorAtendimento = controladorAtendimento
        self.__controladorProfissional = controladorProfissional
        self.__telaProcedimento = TelaProcedimento()

    def abre_tela(self, atendimento):
        if atendimento is None:
            return False

        while True:
            descricao = self.__telaProcedimento.informar_descricao()
            custo = self.__telaProcedimento.informar_custo()
            mensagem = self.registrar_procedimento(
                atendimento,
                descricao,
                custo,
            )
            self.__telaProcedimento.mostra_mensagem(mensagem)
            if mensagem == "Procedimento cadastrado com sucesso!":
                return True

    def registrar_procedimento(self, atendimento, descricao, custo):
        if atendimento not in self.__controladorAtendimento.atendimentos:
            return "Atendimento não encontrado."

        profissional = atendimento.profissional
        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não encontrado."

        if not descricao.strip():
            return "A descrição do procedimento não pode ser vazia."

        if not custo > 0:
            return "O valor do procedimento deve ser maior que zero."

        procedimento = Procedimento(descricao, custo, profissional)
        resultado = atendimento.adicionar_procedimento(procedimento)
        if resultado != "Procedimento adicionado com sucesso!":
            return resultado

        return "Procedimento cadastrado com sucesso!"