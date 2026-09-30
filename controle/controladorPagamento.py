#Após o agendamento, deve ser feito o controle dos pagamentos dos atendimentos. O sistema deve
#permitir pagamentos parciais (parcelamento). O registro do pagamento deve conter: data,
#atendimento, paciente, valor pago, e deve ser possível calcular o valor restante.
class ControladorPagamento:

    def registrar_pagamento(self, atendimento, data_pagamento, valor):

        if data_pagamento > atendimento.data:
            return "Pagamento deve ser realizado até a data do atendimento!"
