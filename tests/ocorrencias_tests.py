import sys
import os

from src.Empresa import Empresa
from src.EnumsApp import Status, Prioridade, Tipo

# Obtém o caminho absoluto do diretório do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona os diretórios ao sys.path
sys.path.insert(0, os.path.join(project_root, "src"))
sys.path.insert(0, os.path.join(project_root, "tests"))

import unittest

class OcorrenciasTest(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa()
        self.empresa.criar_projeto(1, 'Projeto X')
        self.empresa.criar_projeto(2, 'Projeto Y')
        self.empresa.criar_funcionario(1, 'Worker One')
        self.empresa.criar_funcionario(2, 'Worker Two')
        self.empresa.adicionar_funcionario_em_projeto(1, 1)
        self.empresa.adicionar_funcionario_em_projeto(1, 2)
        self.empresa.adicionar_funcionario_em_projeto(2, 2)

    def test_criar_ocorrencia_sucesso(self):
        projeto = self.empresa.pegar_projeto(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)

        self.assertEqual(len(projeto.ocorrencias), 1)
