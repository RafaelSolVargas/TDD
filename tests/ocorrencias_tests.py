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

    ### CRIACAO DE OCORRENCIA
    def test_criar_ocorrencia_sucesso(self):
        projeto = self.empresa.pegar_projeto(1)

        result = projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)

        self.assertEqual(result, 'Sucesso')
        self.assertEqual(len(projeto.ocorrencias), 1)

    def test_criar_ocorrencia_mesmo_id_da_erro(self):
        projeto = self.empresa.pegar_projeto(1)

        resultOne = projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        resultTwo = projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        
        self.assertEqual(resultOne, 'Sucesso')
        self.assertEqual(resultTwo, 'Ocorrencia com esse ID ja existe')

    def test_criar_ocorrencia_funcionario_fora_projeto_da_erro(self):
        projeto = self.empresa.pegar_projeto(1)

        result = projeto.criar_ocorrencia(2, 2, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)

        self.assertEqual(result, 'Funcionario nao esta em projeto')

    def test_criar_ocorrencia_funcionario_da_erro_muitas_ocorrencia_diferente_projeto(self):
        projetoOne = self.empresa.pegar_projeto(1)
        projetoTwo = self.empresa.pegar_projeto(2)
 
        projetoOne.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(2, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(3, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(4, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(5, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        
        projetoTwo.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(2, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(3, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(4, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(5, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projetoTwo.criar_ocorrencia(6, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)

        self.assertEqual(result, 'Funcionario esta com muitas ocorrencias')

    def test_criar_ocorrencia_funcionario_da_erro_muitas_ocorrencia(self):
        projeto = self.empresa.pegar_projeto(1)

        result = ''
        for x in range(11): 
            result = projeto.criar_ocorrencia(x, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)

        self.assertEqual(result, 'Funcionario esta com muitas ocorrencias')

    def test_criar_ocorrencia_funcionario_atualiza_quantidade_ocorrencias(self):
        projeto = self.empresa.pegar_projeto(1)
        funcionario = projeto.pegar_funcionario(1)

        result = projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)

        self.assertEqual(result, 'Sucesso')
        self.assertEqual(funcionario.quantidade_ocorrencias_abertas(), 1)
    ##################################### CRIACAO DE OCORRENCIA

    ##### FECHAR OCORRENCIA
    def test_funcionario_fechar_ocorrencia_retorna_ok_atualiza_status(self):
        projeto = self.empresa.pegar_projeto(1)
        funcionario = projeto.pegar_funcionario(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.fechar_ocorrencia(1, 1)

        self.assertEqual(result, 'Sucesso')
        self.assertEqual(funcionario.quantidade_ocorrencias_abertas(), 0)

    def test_funcionario_fechar_ocorrencia_inexistente_gera_erro(self):
        projeto = self.empresa.pegar_projeto(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.fechar_ocorrencia(-1, 1)

        self.assertEqual(result, 'Ocorrencia nao existe')

    def test_funcionario_inexistente_fechar_ocorrencia_gera_erro(self):
        projeto = self.empresa.pegar_projeto(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.fechar_ocorrencia(1, -1)

        self.assertEqual(result, 'Funcionario nao esta em projeto')

    def test_funcionario_fechar_ocorrencia_nao_dele_gera_erro(self):
        projeto = self.empresa.pegar_projeto(2)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.fechar_ocorrencia(1, 2)

        self.assertEqual(result, 'Funcionario nao eh responsavel por ocorrencia')

    def test_funcionario_fechar_ocorrencia_fechada_gera_erro(self):
        projeto = self.empresa.pegar_projeto(1)
        funcionario = projeto.pegar_funcionario(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.fechar_ocorrencia(1, 1)
        result = projeto.fechar_ocorrencia(1, 1)

        self.assertEqual(result, 'Ocorrencia ja fechada')
        self.assertEqual(funcionario.quantidade_ocorrencias_abertas(), 0)

    def test_funcionario_eh_responsavel_ocorrencia_retorna_false(self):
        projeto = self.empresa.pegar_projeto(1)
        funcionario = projeto.pegar_funcionario(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = funcionario.eh_responsavel_ocorrencia(2)

        self.assertEqual(result, False)

    def test_funcionario_remover_ocorrencia_nao_possui_retorna_none(self):
        projeto = self.empresa.pegar_projeto(1)
        funcionario = projeto.pegar_funcionario(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = funcionario.remover_ocorrencia(2)

        self.assertEqual(result, None)
    ##################################### FECHAR OCORRENCIA

    ##### MODIFICACAO FUNCIONARIO
    def test_modificar_resposavel_retorna_sucesso(self):
        projeto = self.empresa.pegar_projeto(2)
        funcionarioOne = projeto.pegar_funcionario(1)
        funcionarioTwo = projeto.pegar_funcionario(2)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.modificar_responsavel(1, 2)

        self.assertEqual(result, 'Sucesso')
        self.assertEqual(funcionarioOne.quantidade_ocorrencias_abertas(), 0)
        self.assertEqual(funcionarioTwo.quantidade_ocorrencias_abertas(), 1)

    def test_modificar_resposavel_inexistente_retorna_erro(self):
        projeto = self.empresa.pegar_projeto(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.modificar_responsavel(1, -1)

        self.assertEqual(result, 'Funcionario nao encontrado')

    def test_modificar_resposavel_ocorrencia_inexistente_retorna_erro(self):
        projeto = self.empresa.pegar_projeto(1)

        projeto.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projeto.modificar_responsavel(-1, 1)

        self.assertEqual(result, 'Ocorrencia nao encontrada')

    def test_modificar_resposavel_ocorrencia_muitas_ocorrencias_retorna_erro(self):
        projetoOne = self.empresa.pegar_projeto(1)
        projetoTwo = self.empresa.pegar_projeto(2)
 
        projetoOne.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(2, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(3, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(4, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoOne.criar_ocorrencia(5, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        
        projetoTwo.criar_ocorrencia(1, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(2, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(3, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(4, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        projetoTwo.criar_ocorrencia(5, 1, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
       
        projetoTwo.criar_ocorrencia(6, 2, 'Resumo', Status.Aberto, Tipo.Tarefa, Prioridade.Alta)
        result = projetoTwo.modificar_responsavel(6, 1)

        self.assertEqual(result, 'Funcionario novo esta com muitas ocorrencias')
    ##################################### MODIFICACAO FUNCIONARIO