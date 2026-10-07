class PacienteRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O paciente com CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))


class ProfissionalRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O profissional com CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))


class AcompanhanteRepetidoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O acompanhante com CPF {} já existe"
        super().__init__(self.mensagem.format(cpf))


class ClinicaRepetidaException(Exception):
    def __init__(self, nome):
        self.mensagem = "A clínica {} já existe"
        super().__init__(self.mensagem.format(nome))


class PacienteNaoEncontradoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O paciente com CPF {} não foi encontrado"
        super().__init__(self.mensagem.format(cpf))


class ProfissionalNaoEncontradoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O profissional com CPF {} não foi encontrado"
        super().__init__(self.mensagem.format(cpf))


class AcompanhanteNaoEncontradoException(Exception):
    def __init__(self, cpf):
        self.mensagem = "O acompanhante com CPF {} não foi encontrado"
        super().__init__(self.mensagem.format(cpf))


class ClinicaNaoEncontradaException(Exception):
    def __init__(self, nome):
        self.mensagem = "A clínica {} não foi encontrada"
        super().__init__(self.mensagem.format(nome))


class AtendimentoNaoEncontradoException(Exception):
    def __init__(self):
        self.mensagem = "O atendimento não foi encontrado"
        super().__init__(self.mensagem)


class AtendimentoConflitanteException(Exception):
    def __init__(self):
        self.mensagem = "Já existe um atendimento nesse horário para este profissional"
        super().__init__(self.mensagem)


class HorarioInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "O horário informado está fora do horário de funcionamento da clínica"
        super().__init__(self.mensagem)


class AcompanhanteObrigatorioException(Exception):
    def __init__(self):
        self.mensagem = "Pacientes menores de 18 anos precisam de um acompanhante"
        super().__init__(self.mensagem)


class PagamentoInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "O pagamento informado é inválido"
        super().__init__(self.mensagem)


class PagamentoAcimaDoValorException(Exception):
    def __init__(self, valor):
        self.mensagem = "O valor do pagamento R$ {:.2f} é maior que o valor restante"
        super().__init__(self.mensagem.format(valor))


class PagamentoAposAtendimentoException(Exception):
    def __init__(self):
        self.mensagem = "O pagamento não pode ser realizado após a data do atendimento"
        super().__init__(self.mensagem)


class AtendimentoJaPagoException(Exception):
    def __init__(self):
        self.mensagem = "O atendimento já foi totalmente pago"
        super().__init__(self.mensagem)


class ProcedimentoInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "Os dados do procedimento são inválidos"
        super().__init__(self.mensagem)


class DescricaoProcedimentoVaziaException(Exception):
    def __init__(self):
        self.mensagem = "A descrição do procedimento não pode ser vazia"
        super().__init__(self.mensagem)


class ValorProcedimentoInvalidoException(Exception):
    def __init__(self, valor):
        self.mensagem = "O valor do procedimento R$ {:.2f} deve ser maior que zero"
        super().__init__(self.mensagem.format(valor))