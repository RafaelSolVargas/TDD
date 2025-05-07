from typing import List
from src.Funcionario import Funcionario


class Projeto:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.funcionarios: List[Funcionario] = []