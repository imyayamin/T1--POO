from entidade.atendimento import Atendimento
from limite.telaAtendimento import TelaAtendimento
from datetime import time

class ControladorAtendimento:
    def __init__(self, controladorGeral, ControladorClinica, ControladorPaciente, ControladorProfissional):
        self.__atendimentos = []
        self.__controladorGeral = controladorGeral
        self.__controladorClinica = ControladorClinica
        self.__controladorPaciente = ControladorPaciente
        self.__controladorProfissional = ControladorProfissional
        self.__tela_atendimento = TelaAtendimento(
            self, 
            self.__controladorClinica, 
            self.__controladorPaciente, 
            self.__controladorProfissional
        )

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_atendimento,
            2: self.listar_atendimentos,
            3: self.editar_atendimento,
            4: self.remover_atendimento,
        }

        while True:
            opcao = self.__tela_atendimento.tela_opcoes()
            if opcao == 0:
                return

            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida is None:
                self.__tela_atendimento.mostra_mensagem("Opção inválida.")
                continue

            funcao_escolhida()

    def horario_dentro_da_clinica(self, clinica, horario_inicio, horario_fim):
        abertura = time(hour=clinica.horario_funcionamento_inicial)
        fechamento = (
            time(hour=clinica.horario_funcionamento_final)
            if clinica.horario_funcionamento_final < 24
            else time.max
        )
        return horario_inicio >= abertura and horario_fim <= fechamento
    
    def agendar_atendimento(
        self, clinica, paciente, profissional, data,
        horario_inicio, horario_fim, tipo_atendimento
    ):
        mensagem_validacao = self.validar_atendimento(
            clinica,
            paciente,
            profissional,
            data,
            horario_inicio,
            horario_fim,
            tipo_atendimento,
        )
        if mensagem_validacao is not None:
            return mensagem_validacao

        valor = self.obter_valor_atendimento(tipo_atendimento)
        novo = Atendimento(
            clinica,
            paciente,
            profissional,
            data,
            horario_inicio,
            horario_fim,
            tipo_atendimento,
            valor,
        )
        self.__atendimentos.append(novo)
        return "Atendimento agendado com sucesso!"

    def validar_atendimento(
        self, clinica, paciente, profissional, data,
        horario_inicio, horario_fim, tipo_atendimento,
        atendimento_ignorado=None,
    ):
        if clinica not in self.__controladorClinica.clinicas:
            return "Clínica não cadastrada!"
        if paciente not in self.__controladorPaciente.pacientes:
            return "Paciente não cadastrado!"
        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não cadastrado!"

        if horario_fim <= horario_inicio:
            return "O horário final deve ser maior que o inicial!"

        if not self.horario_dentro_da_clinica(clinica, horario_inicio, horario_fim):
            return (
                "Fora do horário da clínica "
                f"({clinica.horario_funcionamento_inicial}h às "
                f"{clinica.horario_funcionamento_final}h)!"
            )

        for atendimento in self.__atendimentos:
            if atendimento is atendimento_ignorado:
                continue

            conflito = (
                atendimento.data == data
                and atendimento.profissional == profissional
                and horario_inicio < atendimento.horario_fim
                and horario_fim > atendimento.horario_inicio
            )
            if conflito:
                return "Horário não disponível!"

        if self.obter_valor_atendimento(tipo_atendimento) is None:
            return "Tipo de atendimento inválido!"

        return None

    def cadastrar_atendimento(self):
        dados = self.__tela_atendimento.pega_dados_atendimento()
        if dados is None:
            return

        resultado = self.agendar_atendimento(**dados)
        self.__tela_atendimento.mostra_mensagem(resultado)

    def listar_atendimentos(self):
        self.__tela_atendimento.lista_atendimentos(self.__atendimentos)
        return self.__atendimentos

    def editar_atendimento(self):
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        self.listar_atendimentos()
        atendimento = self.__tela_atendimento.seleciona_atendimento(
            self.__atendimentos
        )
        if atendimento is None:
            return

        dados = self.__tela_atendimento.pega_dados_atendimento()
        if dados is None:
            return

        mensagem_validacao = self.validar_atendimento(
            **dados,
            atendimento_ignorado=atendimento,
        )
        if mensagem_validacao is not None:
            self.__tela_atendimento.mostra_mensagem(mensagem_validacao)
            return

        atendimento.clinica = dados["clinica"]
        atendimento.paciente = dados["paciente"]
        atendimento.profissional = dados["profissional"]
        atendimento.data = dados["data"]
        atendimento.horario_inicio = dados["horario_inicio"]
        atendimento.horario_fim = dados["horario_fim"]
        atendimento.tipoAtendimento = dados["tipo_atendimento"]
        atendimento.valor = self.obter_valor_atendimento(
            dados["tipo_atendimento"]
        )
        self.__tela_atendimento.mostra_mensagem(
            "Atendimento atualizado com sucesso."
        )

    def remover_atendimento(self):
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return

        self.listar_atendimentos()
        atendimento = self.__tela_atendimento.seleciona_atendimento(
            self.__atendimentos
        )
        if atendimento is None:
            return

        self.__atendimentos.remove(atendimento)
        self.__tela_atendimento.mostra_mensagem(
            "Atendimento removido com sucesso."
        )

    def obter_valor_atendimento(self, tipoAtendimento):

        valores = {
            "Consulta": 100,
            "Exame": 150,
            "Retorno": 70,
            "Outro": 120
        }

        return valores.get(tipoAtendimento)