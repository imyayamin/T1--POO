from abc import ABC, abstractmethod
from datetime import date
from atendimento import Atendimento
from paciente import Paciente
#talvez tenha que puxar o valor de atendimento

class Pagamento(ABC):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float):
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor_pago = valor_pago

    @property
    def data(self):
        return self.__data

    @property
    def atendimento(self):
        return self.__atendimento

    @property
    def paciente(self):
        return self.__paciente

    @property
    def valor_pago(self):
        return self.__valor_pago

    @data.setter
    def data(self, data: date):
        self.__data = data

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        self.__atendimento = atendimento

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self.__paciente = paciente

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago

    