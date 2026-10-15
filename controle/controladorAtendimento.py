from entidade.atendimento import Atendimento
from .controladorClinica import ControladorClinica
from .controladorPaciente import ControladorPaciente
from .controladorProfissional import ControladorProfissional

class ControladorAtendimento:
    def __init__(self, controladorClinica: ControladorClinica, controladorPaciente: ControladorPaciente, controladorProfissional: ControladorProfissional, controladorAcompanhante: ControladorProfissional):
        self.__atendimentos = []
        self.__controladorClinica = controladorClinica
        self.__controladorPaciente = controladorPaciente
        self.__controladorProfissional = controladorProfissional

    @property
    def atendimentos(self):
        return self.__atendimentos

    

    def agendar_atendimento(self, clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, acompanhante=None):

        if clinica not in self.__controladorClinica.clinicas:
            return "Clínica não cadastrada!"

        if horario_inicio < clinica.horario_funcionamento_inicial:
            return "Horário de inicio fora do funcionamento da clinica!"

        if horario_fim > clinica.horario_funcionamento_final:
            return "Horário de fim fora do funcionamento da clinica!"

        if horario_inicio >= horario_fim:
            return "O horário de início deve ser anterior ao horário de fim!"

        for atendimento in self.__atendimentos:
            conflito = (
                atendimento.data == data
                and atendimento.profissional == profissional
                and horario_inicio < atendimento.horario_fim
                and horario_fim > atendimento.horario_inicio
            )

            if conflito:
                return "Horário não disponível!"

        novoAtendimento = Atendimento( clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante)
        self.__atendimentos.append(novoAtendimento)
        
        valor = self.__obter_valor_atendimento(tipoAtendimento)

        if valor is None:
            return "Tipo de atendimento inválido!"

        novo_atendimento = Atendimento(clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante)

        self.__atendimentos.append(novo_atendimento)

        return "Atendimento agendado com sucesso!"

    def __obter_valor_atendimento(self, tipoAtendimento):

        valores = {
            "Consulta": 100,
            "Exame": 150,
            "Retorno": 70,
            "Outro": 120
        }

        return valores.get(tipoAtendimento)