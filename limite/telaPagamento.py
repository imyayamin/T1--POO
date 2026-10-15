from datetime import date
import re

from entidade.pagamentoCartao import PagamentoCartao
from entidade.pagamentoDinheiro import PagamentoDinheiro
from entidade.pagamentoPix import PagamentoPix


class TelaPagamento:
    def tela_opcoes(self):
        print("\n========== PAGAMENTOS ==========")
        print("1 - Realizar pagamento")
        print("2 - Listar pagamentos")
        print("3 - Alterar pagamento")
        print("4 - Remover pagamento")
        print("0 - Voltar")
        print("================================")

        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return None

    def pega_dados_pagamento(self, atendimentos):
        atendimentos_pendentes = [
            atendimento
            for atendimento in atendimentos
            if atendimento.procedimentos
            and atendimento.calcular_valor_restante() > 0
        ]
        atendimento = self.seleciona_atendimento(atendimentos_pendentes)
        if atendimento is None:
            return None

        data_pagamento = self.informar_data()
        tipo = self.escolher_tipo()
        if tipo is None:
            return None

        valor_procedimentos = atendimento.valor_total_procedimentos()
        valor_a_pagar = min(
            valor_procedimentos,
            atendimento.calcular_valor_restante(),
        )
        dados = {
            "tipo": tipo,
            "data_pagamento": data_pagamento,
            "atendimento": atendimento,
            "paciente": atendimento.paciente,
            "valor_pago": valor_a_pagar,
        }
        self.mostrar_mensagem(
            f"Valor a pagar pelo(s) procedimento(s): "
            f"R$ {dados['valor_pago']:.2f}"
        )

        if tipo == "2":
            dados["cpf_pagador"] = self.informar_cpf()
        elif tipo == "3":
            dados["numero_cartao"] = self.informar_cartao()
            dados["bandeira"] = self.informar_bandeira()
            dados["parcelas"] = self.informar_parcelas()

        return dados

    def seleciona_atendimento(self, atendimentos):
        if not atendimentos:
            self.mostrar_mensagem("Nenhum atendimento cadastrado.")
            return None

        print("\nAtendimentos:")
        for indice, atendimento in enumerate(atendimentos, start=1):
            print(
                f"{indice} - {atendimento.data.isoformat()} "
                f"{atendimento.horario_inicio.strftime('%H:%M')} | "
                f"{atendimento.paciente.nome} | Procedimento(s): "
                f"{', '.join(procedimento.descricao for procedimento in atendimento.procedimentos)} | "
                f"Valor do(s) procedimento(s): "
                f"R$ {atendimento.valor_total_procedimentos():.2f}"
            )

        while True:
            try:
                escolha = int(input("Escolha o atendimento: "))
            except ValueError:
                self.mostrar_mensagem("Digite um número válido.")
                continue

            if 1 <= escolha <= len(atendimentos):
                return atendimentos[escolha - 1]
            self.mostrar_mensagem("Opção inválida.")

    def seleciona_pagamento(self, registros):
        self.lista_pagamentos(registros)
        while True:
            try:
                escolha = int(input("Escolha o pagamento: "))
            except ValueError:
                self.mostrar_mensagem("Digite um número válido.")
                continue

            if 1 <= escolha <= len(registros):
                return registros[escolha - 1]
            self.mostrar_mensagem("Opção inválida.")

    def lista_pagamentos(self, registros):
        if not registros:
            self.mostrar_mensagem("Nenhum pagamento cadastrado.")
            return

        print("\nPagamentos cadastrados:")
        for indice, (pagamento, atendimento) in enumerate(registros, start=1):
            tipo, detalhe = self.__detalhes_pagamento(pagamento)
            print(
                f"{indice} - {pagamento.data_pagamento.isoformat()} | "
                f"{tipo} | R$ {pagamento.valor_pago:.2f} | "
                f"Paciente: {pagamento.paciente.nome} | "
                f"Atendimento: {atendimento.data.isoformat()} "
                f"{atendimento.horario_inicio.strftime('%H:%M')}"
                f"{detalhe}"
            )

    def __detalhes_pagamento(self, pagamento):
        if isinstance(pagamento, PagamentoPix):
            return "PIX", f" | CPF pagador: {pagamento.cpf_pagador}"
        if isinstance(pagamento, PagamentoCartao):
            return (
                "Cartão",
                f" | final {pagamento.numero_cartao[-4:]} "
                f"| {pagamento.bandeira} | {pagamento.parcela}x",
            )
        if isinstance(pagamento, PagamentoDinheiro):
            return "Dinheiro", ""
        return "Outro", ""

    def confirmar_remocao(self):
        return input("Confirma a remoção? (s/n): ").strip().lower() == "s"

    def informar_data(self):
        while True:
            try:
                return date.fromisoformat(
                    input("Data do pagamento (AAAA-MM-DD): ").strip()
                )
            except ValueError:
                self.mostrar_mensagem("Data inválida. Use o formato AAAA-MM-DD.")

    def escolher_tipo(self):
        print("\nFORMA DE PAGAMENTO")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão de crédito")

        tipo = input("Digite a opção: ").strip()
        if tipo not in ("1", "2", "3"):
            self.mostrar_mensagem("Opção inválida.")
            return None
        return tipo

    def informar_valor(self):
        while True:
            try:
                valor = float(input("Digite o valor a pagar: R$ ").replace(",", "."))
                if valor <= 0:
                    self.mostrar_mensagem("O valor deve ser maior que zero.")
                    continue
                return valor
            except ValueError:
                self.mostrar_mensagem("Digite um valor válido.")

    def informar_cpf(self):
        while True:
            cpf = re.sub(
                r"[.\-\s]",
                "",
                input("Digite o CPF do pagador (11 dígitos): ").strip(),
            )
            if cpf.isdigit() and len(cpf) == 11:
                return cpf
            self.mostrar_mensagem(
                "CPF inválido. Informe os 11 dígitos do CPF."
            )

    def informar_cartao(self):
        while True:
            numero = re.sub(
                r"[\s-]",
                "",
                input("Digite o número do cartão (16 dígitos): ").strip(),
            )
            if numero.isdigit() and len(numero) == 16:
                return numero
            self.mostrar_mensagem(
                "Número inválido. Informe os 16 dígitos do cartão."
            )

    def informar_bandeira(self):
        bandeiras = {"visa", "mastercard", "elo"}
        while True:
            bandeira = input(
                "Digite a bandeira do cartão (Visa, Mastercard ou Elo): "
            ).strip().lower()
            if bandeira in bandeiras:
                return bandeira
            self.mostrar_mensagem(
                "Bandeira inválida. Escolha Visa, Mastercard ou Elo."
            )

    def informar_parcelas(self):
        while True:
            try:
                parcelas = int(input("Em quantas vezes deseja pagar (1 a 3)? "))
                if 1 <= parcelas <= 3:
                    return parcelas
                self.mostrar_mensagem(
                    "Quantidade de parcelas inválida. Escolha entre 1 e 3."
                )
            except ValueError:
                self.mostrar_mensagem("Digite um número válido.")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
