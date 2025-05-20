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

    def criar_ocorrencia(self, id: int, responsavelId: int, resumo: str, status: Status, tipo: Tipo, prioridade: Prioridade) -> bool:
        ocorrencia = Ocorrencia(id, responsavelId, resumo, status, tipo, prioridade)
        
        ocorrenciaMesmoId = self.pegar_ocorrencia(id)

        if ocorrenciaMesmoId is not None:
            return False

        self.ocorrencias.append(ocorrencia)

        return True

    def pegar_ocorrencia(self, id):
        for ocorrencia in self.ocorrencias:
            if ocorrencia.id == id:
                return ocorrencia