from entidade.paciente import Paciente
from limite.telaPaciente import TelaPaciente
from exceptions.exceptions import (AcompanhanteObrigatorioException, PacienteRepetidoException, PacienteNaoEncontradoException, EntradaInvalidaException, ListaVaziaException)

class ControladorPaciente:

    def __init__(self, controladorGeral):
        self.__pacientes = []
        self.__tela_paciente = TelaPaciente()
        self.__controladorGeral = controladorGeral

    @property
    def pacientes(self):
        return self.__pacientes

    def pega_paciente_por_cpf(self, cpf):
        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente
        return None

    def incluir_paciente(self):
        try:
            dados = self.__tela_paciente.pega_dados_paciente()
        except EntradaInvalidaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return

        try:
            dados = self.__validar_dados_paciente(dados)
            acompanhante = self.__obter_acompanhante(dados["idade"])
            novo_paciente = Paciente(
                dados["nome"],
                dados["celular"],
                dados["cpf"],
                dados["idade"],
                acompanhante,
            )
            self.__pacientes.append(novo_paciente)
            self.__tela_paciente.mostra_mensagem("Paciente cadastrado com sucesso!")
        except (ValueError, PacienteRepetidoException, AcompanhanteObrigatorioException) as e:
            self.__tela_paciente.mostra_mensagem(str(e))

    def alterar_paciente(self):
        try:
            self.listar_pacientes()
        except ListaVaziaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return

        cpf = self.__tela_paciente.seleciona_paciente()
        if cpf is None:
            return
        paciente = self.pega_paciente_por_cpf(cpf)
        if paciente is None:
            self.__tela_paciente.mostra_mensagem(
                str(PacienteNaoEncontradoException(cpf))
            )
            return

        try:
            dados = self.__validar_dados_paciente(
                self.__tela_paciente.pega_dados_paciente(),
                paciente,
            )
            acompanhante = self.__obter_acompanhante(dados["idade"])
            paciente.nome = dados["nome"]
            paciente.celular = dados["celular"]
            paciente.cpf = dados["cpf"]
            paciente.idade = dados["idade"]
            paciente.acompanhante = acompanhante
            self.__tela_paciente.mostra_mensagem(
                "Paciente atualizado com sucesso."
            )
        except (ValueError, PacienteRepetidoException, AcompanhanteObrigatorioException) as e:
            self.__tela_paciente.mostra_mensagem(str(e))

    def __validar_dados_paciente(self, dados, paciente_atual=None):
        nome = str(dados.get("nome", "")).strip()
        celular = "".join(
            caractere
            for caractere in str(dados.get("celular", ""))
            if caractere.isdigit()
        )
        cpf = "".join(
            caractere
            for caractere in str(dados.get("cpf", ""))
            if caractere.isdigit()
        )
        idade = dados.get("idade")

        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        if len(celular) not in (10, 11):
            raise ValueError("O telefone deve conter DDD e 10 ou 11 dígitos.")
        if len(cpf) != 11:
            raise ValueError("O CPF deve conter 11 dígitos.")
        if not isinstance(idade, int) or not 0 <= idade <= 120:
            raise ValueError("A idade deve estar entre 0 e 120 anos.")

        existente = self.pega_paciente_por_cpf(cpf)
        if existente is not None and existente is not paciente_atual:
            raise PacienteRepetidoException(cpf)
        return {
            "nome": nome,
            "celular": celular,
            "cpf": cpf,
            "idade": idade,
        }

    def __obter_acompanhante(self, idade):
        if idade >= 18:
            return None
        self.__tela_paciente.mostra_mensagem(
            "Paciente menor de idade. Informe o acompanhante:"
        )
        acompanhante = self.__tela_paciente.pega_dados_acompanhante()
        if not acompanhante or not acompanhante.strip():
            raise AcompanhanteObrigatorioException()
        return acompanhante.strip()

    def listar_pacientes(self):
        if not self.__pacientes:
            raise ListaVaziaException("pacientes")
        self.__tela_paciente.lista_pacientes(self.__pacientes)
        return self.__pacientes

    def remover_paciente(self):
        try:
            self.listar_pacientes()
        except ListaVaziaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return
        
        try:
            cpf = self.__tela_paciente.seleciona_paciente()
        except EntradaInvalidaException as e:
            self.__tela_paciente.mostra_mensagem(str(e))
            return
        if cpf is None:
            return

        try:
            paciente = self.pega_paciente_por_cpf(cpf)
            if paciente is None:
                raise PacienteNaoEncontradoException(cpf)
            if any(
                atendimento.paciente is paciente
                for atendimento in self.__controladorGeral.controlador_atendimento.atendimentos
            ):
                self.__tela_paciente.mostra_mensagem(
                    "Não é possível remover um paciente vinculado a atendimentos."
                )
                return
            self.__pacientes.remove(paciente)
            self.__tela_paciente.mostra_mensagem("Paciente removido com sucesso!")
        except PacienteNaoEncontradoException as e:
            self.__tela_paciente.mostra_mensagem(str(e))

    def abre_tela(self):
        lista_opcoes = {
            1: self.listar_pacientes,
            2: self.incluir_paciente,
            3: self.remover_paciente,
            4: self.alterar_paciente,
        }
        while True:
            opcao = self.__tela_paciente.tela_opcoes()
            if opcao == 0:
                return
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_paciente.mostra_mensagem(
                    "Digite uma opção válida."
                    if opcao is not None
                    else "Digite uma opção numérica."
                )
                continue
            try:
                funcao()
            except ListaVaziaException as e:
                self.__tela_paciente.mostra_mensagem(str(e))