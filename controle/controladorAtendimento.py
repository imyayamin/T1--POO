from entidade.atendimento import Atendimento
from limite.telaAtendimento import TelaAtendimento
from exceptions.exceptions import ListaVaziaException
from datetime import time

class ControladorAtendimento:
    def __init__(self, controladorGeral, ControladorClinica, ControladorPaciente, ControladorProfissional):
        self.__atendimentos = []
        self.__controladorGeral = controladorGeral
        self.__controladorClinica = ControladorClinica
        self.__controladorPaciente = ControladorPaciente
        self.__controladorProfissional = ControladorProfissional
        self.__tela_atendimento = TelaAtendimento(
            self, 
            self.__controladorClinica, 
            self.__controladorPaciente, 
            self.__controladorProfissional
        )

    @property
    def atendimentos(self):
        return self.__atendimentos

    def abre_tela(self):
        self.__tela_atendimento.agendar_atendimento()

    def horario_dentro_da_clinica(self, clinica, horario_inicio, horario_fim):
        abertura = time(clinica.horario_inicial)
        fechamento = time(clinica.horario_final) if clinica.horario_final < 24 else time.max
        return horario_inicio >= abertura and horario_fim <= fechamento
    
    def agendar_atendimento(self, clinica, paciente, profissional, data, tipoAtendimento):
        if clinica not in self.__controladorClinica.clinicas:
            return "Clínica não cadastrada!"
        if paciente not in self.__controladorPaciente.pacientes:
            return "Paciente não cadastrado!"
        if profissional not in self.__controladorProfissional.profissionais:
            return "Profissional não cadastrado!"

        if horario_fim <= horario_inicio:
            return "O horário final deve ser maior que o inicial!"

        if not self.horario_dentro_da_clinica(clinica, horario_inicio, horario_fim):
            return (f"Fora do horário da clínica "
                    f"({clinica.horario_inicial}h às {clinica.horario_final}h)!")

        for atendimento in self.__atendimentos:
            conflito = (
                atendimento.data == data
                and atendimento.profissional == profissional
                and horario_inicio < atendimento.horario_fim
                and horario_fim > atendimento.horario_inicio
            )
            if conflito:
                return "Horário não disponível!"

        valor = self.obter_valor_atendimento(tipoAtendimento)
        if valor is None:
            return "Tipo de atendimento inválido!"

        novo = Atendimento(clinica, paciente, profissional, data,
                           horario_inicio, horario_fim, tipoAtendimento, valor)
        self.__atendimentos.append(novo)
        return "Atendimento agendado com sucesso!"

    def obter_valor_atendimento(self, tipoAtendimento):

        valores = {
            "Consulta": 100,
            "Exame": 150,
            "Retorno": 70,
            "Outro": 120
        }

        return valores.get(tipoAtendimento)