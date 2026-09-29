from pagamento import Pagamento
from datetime import date
from atendimento import Atendimento
from paciente import Paciente

class PagamentoCartao(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente, valor_pago: float, numero_cartao: int, bandeira: str):
        super().__init__(data, atendimento, paciente, valor_pago)
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: int):
        self.__numero_cartao = numero_cartao

    @bandeira.setter
    def bandeira(self, bandeira: str):
        self.__bandeira = bandeira