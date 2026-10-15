import math

from entidade.tipoAtendimento import TipoAtendimento
from limite.telaTipoAtendimento import TelaTipoAtendimento


class ControladorTipoAtendimento:
    def __init__(self, controladorGeral):
        self.__controladorGeral = controladorGeral
        self.__tela_tipo_atendimento = TelaTipoAtendimento()
        self.__tipos = [
            TipoAtendimento("Consulta", 100),
            TipoAtendimento("Exame", 150),
            TipoAtendimento("Retorno", 70),
            TipoAtendimento("Outro", 120),
        ]

    @property
    def tipos(self):
        return self.__tipos

    def pega_tipo_por_nome(self, nome):
        if not isinstance(nome, str):
            return None
        return next(
            (tipo for tipo in self.__tipos if tipo.nome.casefold() == nome.casefold()),
            None,
        )

    def abre_tela(self):
        opcoes = {
            1: self.listar_tipos,
            2: self.cadastrar_tipo,
            3: self.editar_tipo,
            4: self.remover_tipo,
        }
        while True:
            opcao = self.__tela_tipo_atendimento.tela_opcoes()
            if opcao == 0:
                return
            funcao = opcoes.get(opcao)
            if funcao is None:
                self.__tela_tipo_atendimento.mostra_mensagem("Opção inválida.")
                continue
            funcao()

    def listar_tipos(self):
        self.__tela_tipo_atendimento.lista_tipos(self.__tipos)
        return self.__tipos

    def cadastrar_tipo(self):
        dados = self.__tela_tipo_atendimento.pega_dados_tipo()
        if (
            not dados["nome"].strip()
            or not math.isfinite(dados["valor"])
            or dados["valor"] <= 0
        ):
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Informe um nome e um valor maior que zero."
            )
            return
        if self.pega_tipo_por_nome(dados["nome"]) is not None:
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Já existe um tipo de atendimento com esse nome."
            )
            return
        self.__tipos.append(TipoAtendimento(**dados))
        self.__tela_tipo_atendimento.mostra_mensagem(
            "Tipo de atendimento cadastrado com sucesso."
        )

    def editar_tipo(self):
        if not self.__tipos:
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Nenhum tipo de atendimento cadastrado."
            )
            return
        tipo = self.__tela_tipo_atendimento.seleciona_tipo(self.__tipos)
        if tipo is None:
            return
        dados = self.__tela_tipo_atendimento.pega_dados_tipo()
        if (
            not dados["nome"].strip()
            or not math.isfinite(dados["valor"])
            or dados["valor"] <= 0
        ):
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Informe um nome e um valor maior que zero."
            )
            return
        tipo_com_nome_igual = self.pega_tipo_por_nome(dados["nome"])
        if tipo_com_nome_igual is not None and tipo_com_nome_igual is not tipo:
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Já existe um tipo de atendimento com esse nome."
            )
            return

        atendimentos = self.__controladorGeral.controlador_atendimento.atendimentos
        relacionados = [
            atendimento
            for atendimento in atendimentos
            if atendimento.tipoAtendimento == tipo.nome
        ]
        if any(
            atendimento.valor_total()
            - atendimento.valor
            + dados["valor"]
            < sum(p.valor_pago for p in atendimento.pagamentos)
            for atendimento in relacionados
        ):
            self.__tela_tipo_atendimento.mostra_mensagem(
                "O novo valor não pode ser menor que o total já pago em um "
                "atendimento deste tipo."
            )
            return

        nome_anterior = tipo.nome
        tipo.nome = dados["nome"]
        tipo.valor = dados["valor"]
        for atendimento in relacionados:
            atendimento.tipoAtendimento = tipo.nome
            atendimento.valor = tipo.valor
        self.__tela_tipo_atendimento.mostra_mensagem(
            f"Tipo '{nome_anterior}' atualizado com sucesso."
        )

    def remover_tipo(self):
        if not self.__tipos:
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Nenhum tipo de atendimento cadastrado."
            )
            return
        tipo = self.__tela_tipo_atendimento.seleciona_tipo(self.__tipos)
        if tipo is None:
            return
        usado = any(
            atendimento.tipoAtendimento == tipo.nome
            for atendimento in self.__controladorGeral.controlador_atendimento.atendimentos
        )
        if usado:
            self.__tela_tipo_atendimento.mostra_mensagem(
                "Não é possível remover um tipo utilizado por atendimentos."
            )
            return
        self.__tipos.remove(tipo)
        self.__tela_tipo_atendimento.mostra_mensagem(
            "Tipo de atendimento removido com sucesso."
        )
