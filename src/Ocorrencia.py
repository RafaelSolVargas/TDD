from src.EnumsApp import Prioridade, Status, Tipo


class Ocorrencia:
    def __init__(self, id: int, responsavelId: int, resumo: str, status: Status, tipo: Tipo, prioridade: Prioridade):
        self.id = id
        self.resumo = resumo
        self.status = status
        self.tipo = tipo
        self.prioridade = prioridade
        self.responsavelId = responsavelId