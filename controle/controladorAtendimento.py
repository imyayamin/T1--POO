from entidade.atendimento import Atendimento
from limite.telaAtendimento import TelaAtendimento
from datetime import time

class ControladorAtendimento:
    def __init__(
        self,
        controladorGeral,
        ControladorClinica,
        ControladorPaciente,
        ControladorProfissional,
        ControladorTipoAtendimento,
    ):
        self.__atendimentos = []
        self.__controladorGeral = controladorGeral
        self.__controladorClinica = ControladorClinica
        self.__controladorPaciente = ControladorPaciente
        self.__controladorProfissional = ControladorProfissional
        self.__controladorTipoAtendimento = ControladorTipoAtendimento
        self.__tela_atendimento = TelaAtendimento()

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_atendimento,
            2: self.listar_atendimentos,
            3: self.editar_atendimento,
            4: self.remover_atendimento,
            5: self.listar_procedimentos,
            6: self.__controladorGeral.controlador_procedimento.editar_procedimento_menu,
            7: self.__controladorGeral.controlador_procedimento.remover_procedimento,
            8: self.__controladorGeral.controlador_procedimento.adicionar_procedimento_menu,
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

    def listar_procedimentos(self):
        self.__controladorGeral.controlador_procedimento.listar_procedimentos()
        self.__controladorGeral.controlador_tipo_procedimento.listar_tipos()

    def horario_dentro_da_clinica(self, clinica, horario_inicio, horario_fim):
        try:
            hora_abertura = clinica.horario_funcionamento_inicial
            hora_fechamento = clinica.horario_funcionamento_final
            if (
                not 0 <= hora_abertura <= 23
                or not 1 <= hora_fechamento <= 24
            ):
                return False
            abertura = time(hour=hora_abertura)
            fechamento = (
                time(hour=hora_fechamento)
                if hora_fechamento < 24
                else time.max
            )
            return horario_inicio >= abertura and horario_fim <= fechamento
        except (AttributeError, TypeError, ValueError):
            return False

    def __pega_dados_atendimento(self):
        return self.__tela_atendimento.pega_dados_atendimento(
            self.__controladorClinica.clinicas,
            self.__controladorPaciente.pacientes,
            self.__controladorProfissional.profissionais,
            self.__controladorTipoAtendimento.tipos,
        )
    
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
        if valor is None:
            return "Tipo de atendimento inválido!"

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
        dados = self.__pega_dados_atendimento()
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

        dados = self.__pega_dados_atendimento()
        if dados is None:
            return

        mensagem_validacao = self.validar_atendimento(
            **dados,
            atendimento_ignorado=atendimento,
        )
        if mensagem_validacao is not None:
            self.__tela_atendimento.mostra_mensagem(mensagem_validacao)
            return

        if atendimento.pagamentos and dados["paciente"] is not atendimento.paciente:
            self.__tela_atendimento.mostra_mensagem(
                "Não é possível trocar o paciente de um atendimento que já "
                "possui pagamentos."
            )
            return
        if any(
            pagamento.data_pagamento > dados["data"]
            for pagamento in atendimento.pagamentos
        ):
            self.__tela_atendimento.mostra_mensagem(
                "A nova data do atendimento não pode ser anterior à data de "
                "um pagamento já registrado."
            )
            return

        dados_procedimento = None
        if self.__tela_atendimento.pergunta_editar_procedimento():
            controlador_procedimento = (
                self.__controladorGeral.controlador_procedimento
            )
            dados_procedimento = (
                controlador_procedimento.pega_dados_edicao(atendimento)
            )
            if dados_procedimento is None:
                return

            procedimento, descricao, custo = dados_procedimento

        valor_base_novo = self.obter_valor_atendimento(
            dados["tipo_atendimento"]
        )
        total_procedimentos_novo = atendimento.valor_total_procedimentos()
        if dados_procedimento is not None:
            total_procedimentos_novo += custo - procedimento.custo
        total_pago = sum(
            pagamento.valor_pago for pagamento in atendimento.pagamentos
        )
        if valor_base_novo + total_procedimentos_novo < total_pago:
            self.__tela_atendimento.mostra_mensagem(
                "O novo valor do atendimento não pode ser menor que "
                "o total já pago."
            )
            return

        if dados_procedimento is not None:
            mensagem_edicao = (
                self.__controladorGeral.controlador_procedimento
                .editar_procedimento(
                    atendimento,
                    procedimento,
                    descricao,
                    custo,
                    dados["profissional"],
                    valor_base_novo,
                )
            )
            if mensagem_edicao != "Procedimento atualizado com sucesso.":
                self.__tela_atendimento.mostra_mensagem(mensagem_edicao)
                return

        atendimento.clinica = dados["clinica"]
        atendimento.paciente = dados["paciente"]
        atendimento.profissional = dados["profissional"]
        for procedimento in atendimento.procedimentos:
            procedimento.profissional = dados["profissional"]
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

        if atendimento.pagamentos:
            self.__tela_atendimento.mostra_mensagem(
                "Remova os pagamentos deste atendimento antes de removê-lo."
            )
            return

        self.__atendimentos.remove(atendimento)
        self.__tela_atendimento.mostra_mensagem(
            "Atendimento removido com sucesso."
        )

    def obter_valor_atendimento(self, tipoAtendimento):
        tipo = self.__controladorTipoAtendimento.pega_tipo_por_nome(
            tipoAtendimento
        )
        return None if tipo is None else tipo.valor

    def selecionar_atendimento(self):
        if not self.__atendimentos:
            self.__tela_atendimento.mostra_mensagem(
                "Nenhum atendimento cadastrado."
            )
            return None
        self.listar_atendimentos()
        return self.__tela_atendimento.seleciona_atendimento(
            self.__atendimentos
        )
