
from entidade.atendimento import Atendimento
from limite.telaAtendimento import TelaAtendimento
from exceptions.exceptions import (
        ListaVaziaException,
        EntradaInvalidaException,
        AtendimentoNaoEncontradoException,
        HorarioInvalidoException
    )



class ControladorAtendimento:
    def __init__(self, controladorGeral, ControladorClinica,
                 ControladorPaciente, ControladorProfissional):
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
        self.__tela_atendimento.abre_tela()

    def agendar_atendimento_tela(self):
        mensagem = self.__tela_atendimento.agendar_atendimento()

        if mensagem is not None:
            self.__tela_atendimento.mostra_mensagem(mensagem)
            

    def lista_atendimentos_tela(self):
        try:
            self.lista_atendimentos()
        except ListaVaziaException as e:
            self.__tela_atendimento.mostra_mensagem(str(e))

    def horario_dentro_da_clinica(self, clinica, horario_inicio, horario_fim):
        horario_funcionamento_inicial = clinica.horario_funcionamento_inicial
        horario_funcionamento_final = clinica.horario_funcionamento_final

        return (
            horario_inicio >= horario_funcionamento_inicial
            and horario_fim <= horario_funcionamento_final
        )
    


    def agendar_atendimento(self, clinica, paciente, profissional,
                            data, horario_inicio, horario_fim,
                            tipoAtendimento):

        if clinica not in self.__controladorClinica.clinicas:
            return "Clínica não cadastrada!"

        if paciente not in self.__controladorPaciente.pacientes:
            return "Paciente não cadastrado!"

        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não cadastrado!"

        if horario_fim <= horario_inicio:
            return "O horário final deve ser maior que o inicial!"

        if not self.horario_dentro_da_clinica(
            clinica, horario_inicio, horario_fim
        ):
            return (
                f"Fora do horário da clínica "
                f"({clinica.horario_inicial}h às "
                f"{clinica.horario_final}h)!"
            )

        for atendimento in self.__atendimentos:
            conflito = (
                atendimento.data == data
                and atendimento.profissional == profissional
                and horario_inicio < atendimento.horario_fim
                and horario_fim > atendimento.horario_inicio
            )

            if conflito:
                return "Horário não disponível!"

        valor = self.obter_valor_atendimento(tipoAtendimento)

        if valor is None:
            return "Tipo de atendimento inválido!"

        novo = Atendimento(
            clinica, paciente, profissional, data,
            horario_inicio, horario_fim, tipoAtendimento, valor
        )

        self.__atendimentos.append(novo)
        return "Atendimento agendado com sucesso!"


    def pega_atendimento_por_data_horario(self, data, horario_inicio):
        for atendimento in self.__atendimentos:
            if (
                atendimento.data == data
                and atendimento.horario_inicio == horario_inicio
            ):
                return atendimento

        return None


    def lista_atendimentos(self):
        if not self.__atendimentos:
            raise ListaVaziaException("atendimentos")

        self.__tela_atendimento.lista_atendimentos(
            self.__atendimentos
        )

        return self.__atendimentos


    def alterar_atendimento(self):
        try:
            self.lista_atendimentos()
        except ListaVaziaException as e:
            self.__tela_atendimento.mostra_mensagem(str(e))
            return

        try:
            dados = self.__tela_atendimento.seleciona_atendimento()
        except EntradaInvalidaException as e:
            self.__tela_atendimento.mostra_mensagem(str(e))
            return

        try:
            atendimento = self.pega_atendimento_por_data_horario(
                dados["data"],
                dados["horario_inicio"]
            )

            if atendimento is None:
                raise AtendimentoNaoEncontradoException()

        except AtendimentoNaoEncontradoException as e:
            self.__tela_atendimento.mostra_mensagem(str(e))
            return

        try:
            novos_dados = (
                self.__tela_atendimento.pega_dados_atendimento()
            )
        except EntradaInvalidaException as e:
            self.__tela_atendimento.mostra_mensagem(str(e))
            return

        try:
            clinica = novos_dados["clinica"]
            paciente = novos_dados["paciente"]
            profissional = novos_dados["profissional"]
            data = novos_dados["data"]
            horario_inicio = novos_dados["horario_inicio"]
            horario_fim = novos_dados["horario_fim"]
            tipo_atendimento = novos_dados["tipoAtendimento"]

            if clinica not in self.__controladorClinica.clinicas:
                raise ValueError("Clínica não cadastrada!")

            if paciente not in self.__controladorPaciente.pacientes:
                raise ValueError("Paciente não cadastrado!")

            if profissional not in self.__controladorProfissional.profissionais:
                raise ValueError("Profissional não cadastrado!")

            if horario_inicio >= horario_fim:
                raise HorarioInvalidoException()

            if not self.horario_dentro_da_clinica(
                clinica, horario_inicio, horario_fim
            ):
                raise ValueError(
                    "Horário fora do funcionamento da clínica!"
                )

            for outro in self.__atendimentos:
                if outro is atendimento:
                    continue

                conflito = (
                    outro.data == data
                    and outro.profissional == profissional
                    and horario_inicio < outro.horario_fim
                    and horario_fim > outro.horario_inicio
                )

                if conflito:
                    raise ValueError("Horário não disponível!")

            valor = self.obter_valor_atendimento(tipo_atendimento)

            if valor is None:
                raise ValueError("Tipo de atendimento inválido!")

            atendimento.clinica = clinica
            atendimento.paciente = paciente
            atendimento.profissional = profissional
            atendimento.data = data
            atendimento.horario_inicio = horario_inicio
            atendimento.horario_fim = horario_fim
            atendimento.tipoAtendimento = tipo_atendimento
            atendimento.valor = valor

            self.__tela_atendimento.mostra_mensagem(
                "Atendimento alterado com sucesso!"
            )

        except (
            HorarioInvalidoException,
            ValueError,
            KeyError
        ) as e:
            self.__tela_atendimento.mostra_mensagem(str(e))


    def excluir_atendimento(self):
        try:
            if not self.__atendimentos:
                raise ListaVaziaException("atendimentos")

            atendimento = self.__tela_atendimento.seleciona_atendimento()

            if atendimento is None:
                self.__tela_atendimento.mostra_mensagem(
                    "Exclusão cancelada."
                )
                return

            self.__atendimentos.remove(atendimento)

            self.__tela_atendimento.mostra_mensagem(
                "Atendimento removido com sucesso!"
            )

        except ListaVaziaException as e:
            self.__tela_atendimento.mostra_mensagem(str(e))

    def obter_valor_atendimento(self, tipoAtendimento):
        valores = {
            "Consulta": 100,
            "Exame": 150,
            "Retorno": 70,
            "Outro": 120
        }

        return valores.get(tipoAtendimento)
