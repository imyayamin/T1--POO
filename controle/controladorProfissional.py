from limite.telaProfissional import TelaProfissional
from entidade.profissional import Profissional
from exceptions.exceptions import ProfissionalRepetidoException


class ControladorProfissional:

    def __init__(self, controlador_sistema):
        self.__profissionais = []
        self.__tela_profissional = TelaProfissional()
        self.__controlador_sistema = controlador_sistema

    @property
    def profissionais(self):
        return self.__profissionais

    def pega_profissional_por_cpf(self, cpf: int):
        for profissional in self.__profissionais:
            if profissional.cpf == cpf:
                return profissional
        return None

    def incluir_profissional(self):
        dados_profissional = self.__tela_profissional.pega_dados_profissional()
        cpf = dados_profissional["cpf"]
        profissional = self.pega_profissional_por_cpf(cpf)
        try:
            if profissional is None:
                profissional = Profissional(
                    dados_profissional["nome"],
                    dados_profissional["celular"],
                    dados_profissional["cpf"],
                    dados_profissional["especialidade"],
                    dados_profissional["registro_profissional"],
                )
                self.__profissionais.append(profissional)
                self.__tela_profissional.mostra_mensagem("Profissional cadastrado com sucesso!")
            else:
                raise ProfissionalRepetidoException(cpf)
        except ProfissionalRepetidoException as e:
            self.__tela_profissional.mostra_mensagem(e)

    def alterar_profissional(self):
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        if cpf_profissional is None:
            return
        profissional = self.pega_profissional_por_cpf(cpf_profissional)

        if profissional is not None:
            novos_dados_profissional = self.__tela_profissional.pega_dados_profissional()

            # Verifica se o novo CPF já pertence a outro profissional
            outro = self.pega_profissional_por_cpf(novos_dados_profissional["cpf"])
            if outro is not None and outro is not profissional:
                self.__tela_profissional.mostra_mensagem(
                    "ATENÇÃO: Já existe outro profissional com esse CPF."
                )
                return

            profissional.nome = novos_dados_profissional["nome"]
            profissional.celular = novos_dados_profissional["celular"]
            profissional.cpf = novos_dados_profissional["cpf"]
            profissional.especialidade = novos_dados_profissional["especialidade"]
            profissional.registro_profissional = novos_dados_profissional["registro_profissional"]
            self.lista_profissionais()
        else:
            self.__tela_profissional.mostra_mensagem("ATENÇÃO: Profissional não existente")

    def lista_profissionais(self):
        if not self.__profissionais:
            self.__tela_profissional.mostra_mensagem("Nenhum profissional cadastrado.")
            return
        for profissional in self.__profissionais:
            self.__tela_profissional.mostra_profissional({
                "nome": profissional.nome,
                "celular": profissional.celular,
                "cpf": profissional.cpf,
                "especialidade": profissional.especialidade,
                "registro_profissional": profissional.registro_profissional,
            })

    def excluir_profissional(self):
        self.lista_profissionais()
        cpf_profissional = self.__tela_profissional.seleciona_profissional()
        if cpf_profissional is None:
            return
        profissional = self.pega_profissional_por_cpf(cpf_profissional)

        if profissional is not None:
            self.__profissionais.remove(profissional)
            self.__tela_profissional.mostra_mensagem("Profissional removido com sucesso!")
            self.lista_profissionais()
        else:
            self.__tela_profissional.mostra_mensagem("ATENÇÃO: Profissional não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_profissional,
            2: self.alterar_profissional,
            3: self.lista_profissionais,
            4: self.excluir_profissional,
            0: self.retornar,
        }

        continua = True
        while continua:
            opcao = self.__tela_profissional.tela_opcoes()
            funcao = lista_opcoes.get(opcao)
            if funcao is None:
                self.__tela_profissional.mostra_mensagem("Opção inválida.")
                continue
            funcao()