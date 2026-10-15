from collections import Counter, defaultdict

from limite.telaRelatorio import TelaRelatorio


class ControladorRelatorio:
    def __init__(self, controladorClinica, controladorAtendimento):
        self.__controladorClinica = controladorClinica
        self.__controladorAtendimento = controladorAtendimento
        self.__tela_relatorio = TelaRelatorio()

    def abre_tela(self):
        opcoes = {
            1: self.relatorio_clinicas,
            2: self.relatorio_atendimentos,
            3: self.relatorio_procedimentos_populares,
            4: self.relatorio_valores_procedimentos,
        }

        while True:
            opcao = self.__tela_relatorio.tela_opcoes()
            if opcao == 0:
                return

            funcao = opcoes.get(opcao)
            if funcao is None:
                self.__tela_relatorio.mostra_mensagem("Opção inválida.")
                continue
            funcao()

    def relatorio_clinicas(self):
        atendimentos = self.__controladorAtendimento.atendimentos
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Não há atendimentos cadastrados para gerar este relatório."
            )
            return

        contagem = Counter(atendimento.clinica for atendimento in atendimentos)
        maior_numero = max(contagem.values())
        resultado = [
            (clinica, quantidade)
            for clinica, quantidade in contagem.items()
            if quantidade == maior_numero
        ]
        self.__tela_relatorio.mostra_clinicas_com_mais_atendimentos(resultado)

    def relatorio_atendimentos(self):
        atendimentos = self.__controladorAtendimento.atendimentos
        if not atendimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Não há atendimentos cadastrados para gerar este relatório."
            )
            return

        valores = [
            (atendimento, atendimento.valor_total())
            for atendimento in atendimentos
        ]
        maior_valor = max(valor for _, valor in valores)
        menor_valor = min(valor for _, valor in valores)
        mais_caros = [
            (atendimento, valor)
            for atendimento, valor in valores
            if valor == maior_valor
        ]
        mais_baratos = [
            (atendimento, valor)
            for atendimento, valor in valores
            if valor == menor_valor
        ]
        self.__tela_relatorio.mostra_atendimentos_extremos(
            mais_caros,
            mais_baratos,
        )

    def relatorio_procedimentos_populares(self):
        procedimentos = self.__listar_procedimentos()
        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Não há procedimentos cadastrados para gerar este relatório."
            )
            return

        agrupados = defaultdict(list)
        for procedimento, atendimento in procedimentos:
            chave = " ".join(procedimento.descricao.split()).casefold()
            agrupados[chave].append((procedimento, atendimento))

        quantidade_maxima = max(
            len(ocorrencias) for ocorrencias in agrupados.values()
        )
        populares = [
            ocorrencias
            for ocorrencias in agrupados.values()
            if len(ocorrencias) == quantidade_maxima
        ]
        self.__tela_relatorio.mostra_procedimentos_populares(populares)

    def relatorio_valores_procedimentos(self):
        procedimentos = self.__listar_procedimentos()
        if not procedimentos:
            self.__tela_relatorio.mostra_mensagem(
                "Não há procedimentos cadastrados para gerar este relatório."
            )
            return

        maior_custo = max(
            procedimento.custo for procedimento, _ in procedimentos
        )
        menor_custo = min(
            procedimento.custo for procedimento, _ in procedimentos
        )
        mais_caros = [
            registro
            for registro in procedimentos
            if registro[0].custo == maior_custo
        ]
        mais_baratos = [
            registro
            for registro in procedimentos
            if registro[0].custo == menor_custo
        ]
        self.__tela_relatorio.mostra_procedimentos_extremos(
            mais_caros,
            mais_baratos,
        )

    def __listar_procedimentos(self):
        return [
            (procedimento, atendimento)
            for atendimento in self.__controladorAtendimento.atendimentos
            for procedimento in atendimento.procedimentos
        ]