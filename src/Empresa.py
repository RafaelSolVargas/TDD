from src.Funcionario import Funcionario
from src.Projeto import Projeto 


class Empresa():
    def __init__(self):
        self.__projetos = []
        self.__funcionarios = []

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