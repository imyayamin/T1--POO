from abstractPagamento import Pagamento

class PagamentoDinheiro(Pagamento):

    def processar_pagamento(self):
        return True