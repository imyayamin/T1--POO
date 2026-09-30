from abstractPagamento import Pagamento
from datetime import date
from atendimento import Atendimento
from paciente import Paciente

class PagamentoPix(Pagamento):
    def __init__(self, data_pagamento: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float, cpf_pagador: str):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)
        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador
        