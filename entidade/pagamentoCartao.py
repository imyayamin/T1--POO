import re

from .abstractPagamento import Pagamento

class PagamentoCartao(Pagamento):

    def __init__(self, data_pagamento, atendimento, paciente, valor_pago, numero_cartao, bandeira, parcela):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)

        self.__numero_cartao = re.sub(r"[\s-]", "", numero_cartao)
        self.__bandeira = bandeira.strip().lower()
        self.__parcela = parcela

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @property
    def parcela(self):
        return self.__parcela

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        self.__numero_cartao = numero_cartao

    @bandeira.setter
    def bandeira(self, bandeira: str):
        self.__bandeira = bandeira

    @parcela.setter
    def parcela(self, parcela: int):
        self.__parcela = parcela

    def processar_pagamento(self):

        if not self.__numero_cartao.isdigit():
            return False

        if len(self.__numero_cartao) != 16:
            return False

        if self.__bandeira not in ["visa", "mastercard", "elo"]:
            return False

        if not isinstance(self.__parcela, int) or not 1 <= self.__parcela <= 3:
            return False

        return True