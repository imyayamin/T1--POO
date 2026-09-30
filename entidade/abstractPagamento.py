from abc import ABC, abstractmethod
from datetime import date
from atendimento import Atendimento
from paciente import Paciente

class Pagamento(ABC):
    def __init__(self, data_pagamento: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        self.__data_pagamento = data_pagamento
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    @property
    def atendimento(self):
        return self.__atendimento

    @property
    def paciente(self):
        return self.__paciente

    @property
    def valor_pago(self):
        return self.__valor_pago

    @data_pagamento.setter
    def data_pagamento(self, data_pagamento: date):
        self.__data_pagamento = data_pagamento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        self.__atendimento = atendimento

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago

    @abstractmethod
    def processar_pagamento(self):
        pass
    