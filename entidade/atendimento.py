from paciente import Paciente
from profissional import Profissional
from clinica import Clinica
from datetime import date, time

class Atendimento:

    def __init__(self, clinica: Clinica, paciente: Paciente, profissional: Profissional, data: date, horario_inicio: time, horario_fim: time, tipoAtendimento: str,valor: float):
        if isinstance(clinica, Clinica):
            self.__clinica = clinica
        if isinstance(paciente, Paciente):
            self.__paciente = paciente
        if isinstance(profissional, Profissional):
            self.__profissional = profissional
        if isinstance(data, date):
            self.__data = data
        if isinstance(horario_inicio, time):
            self.__horario_inicio = horario_inicio
        if isinstance(horario_fim, time):
            self.__horario_fim = horario_fim
        if isinstance(tipoAtendimento, str):
            self.__tipoAtendimento = tipoAtendimento
        if isinstance(valor, float):
            self.__valor = valor
        self.__acompanhante = self.__paciente.acompanhante #tenho que verificar isso depois

        self.__pagamentos = []
        self.__procedimentos = []

    @property
    def clinica(self):
        return self.__clinica

    @property
    def paciente(self):
        return self.__paciente

    @property
    def profissional(self):
        return self.__profissional

    @property
    def data(self):
        return self.__data

    @property
    def horario_inicio(self):
        return self.__horario_inicio

    @property
    def horario_fim(self):
        return self.__horario_fim

    @property
    def tipoAtendimento(self):
        return self.__tipoAtendimento

    @property
    def valor(self):
        return self.__valor

    @property
    def acompanhante(self):
        return self.__acompanhante

    @property
    def pagamentos(self):
        return self.__pagamentos

    @property
    def procedimentos(self):
        return self.__procedimentos

    @clinica.setter
    def clinica(self, clinica: Clinica):
        self.__clinica = clinica

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @profissional.setter
    def profissional(self, profissional: Profissional):
        self.__profissional = profissional

    @data.setter
    def data(self, data: date):
        self.__data = data

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: time):
        self.__horario_inicio = horario_inicio

    @horario_fim.setter
    def horario_fim(self, horario_fim: time):
        self.__horario_fim = horario_fim

    @tipoAtendimento.setter
    def tipoAtendimento(self, tipoAtendimento: str):
        self.__tipoAtendimento = tipoAtendimento

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    def adicionar_procedimento(self, procedimento):

        if procedimento is None:
            return "Procedimento inválido!"

        self.__procedimentos.append(procedimento)

        return "Procedimento adicionado com sucesso!"

    def valor_total_procedimentos(self):

        return sum(
            procedimento.custo
            for procedimento in self.__procedimentos
        )

    def valor_total(self):

        return self.__valor + self.valor_total_procedimentos()

    def calcular_valor_restante(self):

        total_pago = sum(
            pagamento.valor_pago
            for pagamento in self.__pagamentos
        )

        return self.valor_total() - total_pago

    def registrar_pagamento(self, pagamento):

        if pagamento.atendimento != self:
            return "Pagamento não pertence a este atendimento!"

        if pagamento.data_pagamento > self.__data:
            return "Pagamento deve ser realizado até a data do atendimento!"

        if pagamento.valor_pago <= 0:
            return "O valor pago deve ser maior que zero!"

        valor_restante = self.calcular_valor_restante()

        if valor_restante <= 0:
            return "O atendimento já foi totalmente pago."

        if pagamento.valor_pago > valor_restante:
            return "Valor pago não pode ser maior que o valor restante!"
        
        if not pagamento.processar_pagamento():
            return "Dados do pagamento inválidos!"

        self.__pagamentos.append(pagamento)

        novo_valor_restante = self.calcular_valor_restante()

        if novo_valor_restante == 0:
            return "Pagamento do atendimento concluído!"

        return "Pagamento registrado com sucesso! " f"\nValor restante: R$ {novo_valor_restante:.2f}"
