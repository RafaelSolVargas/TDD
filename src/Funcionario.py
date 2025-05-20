from typing import List
from src.EnumsApp import Status
from src.Ocorrencia import Ocorrencia

class Funcionario:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.ocorrencias: List[Ocorrencia] = []

    def quantidade_ocorrencias_abertas(self) -> int:
        count = 0
        for ocorrencia in self.ocorrencias:
            if (ocorrencia.status is Status.Aberto):
                count += 1

        return count
    
    def eh_responsavel_ocorrencia(self, ocorrenciaId) -> bool:
        for ocorrencia in self.ocorrencias:
            if ocorrencia.id == ocorrenciaId:
                return True
            
        return False