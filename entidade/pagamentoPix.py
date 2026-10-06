from abstractPagamento import Pagamento


class PagamentoPix(Pagamento):

    def __init__(self, data_pagamento, atendimento, paciente, valor_pago, cpf_pagador):
        super().__init__(data_pagamento, atendimento, paciente, valor_pago)

        self.__cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador

    def processar_pagamento(self):

        if not self.__cpf_pagador.isdigit():
            return False

        if len(self.__cpf_pagador) != 11:
            return False

        return True