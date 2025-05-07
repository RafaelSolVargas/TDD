import sys
import os
from unittest.mock import patch


# Obtém o caminho absoluto do diretório do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Adiciona os diretórios ao sys.path
sys.path.insert(0, os.path.join(project_root, "src"))
sys.path.insert(0, os.path.join(project_root, "tests"))

import unittest

class EmpresasTest(unittest.TestCase):
    def test_criar_empresa_retorna_lista_projetos_vazia(self):
        empresa = Empresa()
        
        projetos = empresa.projetos()

        self.assertListEqual(projetos, [])