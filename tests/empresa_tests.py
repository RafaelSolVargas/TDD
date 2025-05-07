import sys
import os

from src.Empresa import Empresa

# Obtém o caminho absoluto do diretório do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona os diretórios ao sys.path
sys.path.insert(0, os.path.join(project_root, "src"))
sys.path.insert(0, os.path.join(project_root, "tests"))

import unittest

class EmpresasTest(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa()

    def test_criar_empresa_retorna_lista_projetos_vazia(self):
        projetos = self.empresa.projetos()

        self.assertListEqual(projetos, [])

    def test_criar_projeto_retorna_objeto_projeto_criado_com_nome(self):
        projeto = self.empresa.criar_projeto(1, 'Projeto X')

        self.assertEqual(projeto.name, 'Projeto X')

    def test_criar_projeto_retorna_projeto_com_id(self):
        projeto = self.empresa.criar_projeto(2, 'Projeto X')

        self.assertEqual(projeto.id, 2)