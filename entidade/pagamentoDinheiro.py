from pagamento import Pagamento
from datetime import date
from atendimento import Atendimento
from paciente import Paciente

class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        super().__init__(data, atendimento, paciente, valor_pago)