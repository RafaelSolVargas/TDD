from src.Projeto import Projeto 


class Empresa():
    def __init__(self):
        self.__projetos = []

    def projetos(self):
        return self.__projetos
    
    def criar_projeto(self, id, name) -> Projeto:
        projeto = Projeto(id, name)
        
        self.__projetos.append(projeto)

        return projeto