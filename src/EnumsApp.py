from enum import Enum

class Status(Enum):
    Aberto = 1
    Fechado = 2

class Tipo(Enum):
    Tarefa = 1
    Bug = 2
    Melhoria = 3

class Prioridade(Enum):
    Alta = 1
    Media = 2
    Baixa = 3