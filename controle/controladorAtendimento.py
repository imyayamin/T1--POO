#O sistema deve permitir o agendamento de atendimentos (consultas) entre pacientes e profissionais.
#Cada atendimento deve conter: clínica, paciente, profissional, data, horário (início e fim), tipo de
#atendimento (consulta, exame, retorno, etc.) e valor.
#Além disso, deve ser possível registrar procedimentos ou serviços realizados durante o atendimento.
#Cada procedimento deve conter: descrição, custo, e profissional responsável.

#Considere algumas regras:
#1. Somente pacientes com mais de 18 anos completos podem realizar atendimentos de forma independente.
#2. Os atendimentos devem ocorrer dentro do período de funcionamento da clínica.
#3. Os pagamentos devem ser realizados até a data do atendimento.

from entidade.atendimento import Atendimento

class ControladorAtendimento:
    def __init__(self, controladorClinica, controladorPaciente, controladorProfissional, controladorAcompanhante):
        self.__atendimentos = []
        self.__controladorClinica = controladorClinica
        self.__controladorPaciente = controladorPaciente
        self.__controladorProfissional = controladorProfissional
        self.__controladorAcompanhante = controladorAcompanhante


    def agendar_atendimento(self, clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante = None):

        if clinica not in self.__controladorClinica.clinicas:
            return "Clínica não cadastrada!"

        if paciente not in self.__controladorPaciente.pacientes:
            return "Paciente não cadastrado!"

        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não cadastrado!"

        if paciente.idade < 18:
            if acompanhante is None:
                return "Paciente menor de idade precisa de acompanhante!"

            if acompanhante not in self.__controladorAcompanhante.acompanhantes:
                return "Acompanhante não cadastrado!"

        if horario_inicio < clinica.horario_funcionamento_inicial:
            return "Horário de inicio fora do funcionamento da clinica!"

        if horario_fim > clinica.horario_funcionamento_final:
                    return "Horário de fim fora do funcionamento da clinica!"

        if horario_inicio >= horario_fim:
            return "O horário de início deve ser anterior ao horário de fim!"

        for atendimento in self.__atendimentos:
             if (atendimento.data == data and atendimento.profissional == profissional and horario_inicio < atendimento.horario_fim and horario_fim > atendimento.horario_inicio):
                return "Horário não disponível!"

        novoAtendimento = Atendimento( clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, valor, acompanhante)
        self.__atendimentos.append(novoAtendimento)
        
        return "Atendimento agendado com sucesso!"
