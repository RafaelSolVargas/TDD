from typing import List
from src.Ocorrencia import Ocorrencia
from src.EnumsApp import Prioridade, Status, Tipo
from src.Funcionario import Funcionario


class Projeto:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.funcionarios: List[Funcionario] = []
        self.ocorrencias: List[Ocorrencia] = []

    def criar_ocorrencia(self, id: int, responsavelId: int, resumo: str, status: Status, tipo: Tipo, prioridade: Prioridade) -> str:
        ocorrencia = Ocorrencia(id, responsavelId, resumo, status, tipo, prioridade)
        
        ocorrenciaMesmoId = self.pegar_ocorrencia(id)

        if ocorrenciaMesmoId is not None:
            return 'Ocorrencia com esse ID ja existe'

        funcionarioProjeto = self.pegar_funcionario(responsavelId)
        if funcionarioProjeto is None:
            return 'Funcionario nao esta em projeto'

        quantFuncionarioProjetos = funcionarioProjeto.quantidade_ocorrencias_abertas()
        if quantFuncionarioProjetos >= 10:
            return 'Funcionario esta com muitas ocorrencias'

        self.ocorrencias.append(ocorrencia)
        funcionarioProjeto.ocorrencias.append(ocorrencia)

        return 'Sucesso'
    
    def fechar_ocorrencia(self, ocorrenciaId: int, responsavelId: int) -> str:
        ocorrencia = self.pegar_ocorrencia(ocorrenciaId)

        if ocorrencia is None:
            return 'Ocorrencia nao existe'

        funcionarioProjeto = self.pegar_funcionario(responsavelId)
        if funcionarioProjeto is None:
            return 'Funcionario nao esta em projeto'
        
        if funcionarioProjeto.eh_responsavel_ocorrencia(ocorrenciaId) == False:
            return 'Funcionario nao eh responsavel por ocorrencia'

        ocorrencia.status = Status.Fechado
        return 'Sucesso'
    
    def modificar_responsavel(self, ocorrenciaId: int, novoResponsavelId: int) -> str:
        ocorrencia = self.pegar_ocorrencia(ocorrenciaId)

        funcionarioVelho = self.pegar_funcionario(ocorrencia.responsavelId)
        funcionarioNovo = self.pegar_funcionario(novoResponsavelId)

        if funcionarioNovo is None:
            return 'Funcionario nao encontrado'

        ocorrencia.responsavelId = novoResponsavelId
        funcionarioVelho.remover_ocorrencia(ocorrenciaId)
        funcionarioNovo.ocorrencias.append(ocorrencia)

        return 'Sucesso'

    def pegar_funcionario(self, id) -> Funcionario:
        for funcionario in self.funcionarios:
            if funcionario.id == id:
                return funcionario
            
    def pegar_ocorrencia(self, id) -> Ocorrencia:
        for ocorrencia in self.ocorrencias:
            if ocorrencia.id == id:
                return ocorrencia