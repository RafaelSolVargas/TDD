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

    def criar_ocorrencia(self, id: int, responsavelId: int, resumo: str, status: Status, tipo: Tipo, prioridade: Prioridade):
        self.ocorrencias.append(Ocorrencia(id, responsavelId, resumo, status, tipo, prioridade))