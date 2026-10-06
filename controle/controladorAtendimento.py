from entidade.atendimento import Atendimento

class ControladorAtendimento:

    def __init__(self, controladorClinica, controladorPaciente, controladorProfissional, controladorAcompanhante):
        self.__atendimentos = []

        self.__controladorClinica = controladorClinica
        self.__controladorPaciente = controladorPaciente
        self.__controladorProfissional = controladorProfissional
        self.__controladorAcompanhante = controladorAcompanhante

    @property
    def atendimentos(self):
        return self.__atendimentos

    def agendar_atendimento(self, clinica, paciente, profissional, data, horario_inicio, horario_fim, tipoAtendimento, acompanhante=None):

        if clinica not in self.__controladorClinica.clinicas:
            return "Clínica não cadastrada!"

        if paciente not in self.__controladorPaciente.pacientes:
            return "Paciente não cadastrado!"

        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não cadastrado!"

        if paciente.idade < 18:

            if acompanhante is None:
                return "Paciente menor de idade, precisa de acompanhante!"

            if acompanhante not in self.__controladorAcompanhante.acompanhantes:
                return "Acompanhante não cadastrado!"

        if horario_inicio < clinica.horario_funcionamento_inicial:
            return "Horário de início fora do funcionamento da clínica!"

        if horario_fim > clinica.horario_funcionamento_final:
            return "Horário de fim fora do funcionamento da clínica!"

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