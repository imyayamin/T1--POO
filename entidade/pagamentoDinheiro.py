from abstractPagamento import Pagamento
from datetime import date
from atendimento import Atendimento
from paciente import Paciente

class PagamentoDinheiro(Pagamento):
    def __init__(self, data_pagamento: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)

    def processar_pagamento(self):
                return True