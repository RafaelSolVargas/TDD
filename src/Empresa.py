from typing import List
from src.Funcionario import Funcionario
from src.Projeto import Projeto 


class Empresa():
    def __init__(self):
        self.__projetos: List[Projeto] = []
        self.__funcionarios: List[Funcionario] = []

    def projetos(self):
        return self.__projetos
    
    def criar_projeto(self, id, name) -> Projeto:
        projeto = Projeto(id, name)
        
        self.__projetos.append(projeto)

        return projeto
    
    def criar_funcionario(self, id, name) -> Funcionario:
        funcionario = Funcionario(id, name)

        self.__funcionarios.append(funcionario)

        return funcionario
    
    def pegar_projeto(self, projetoId) -> Projeto:
        for projeto in self.__projetos:
            if projeto.id == projetoId:
                return projeto

    def adicionar_funcionario_em_projeto(self, funcionarioId, projetoId):
        for funcionario in self.__funcionarios:
            if funcionario.id == funcionarioId: 
                for projeto in self.__projetos:
                    if projeto.id == projetoId:
                        projeto.funcionarios.append(funcionario)