from django.test import TestCase
from escola.models import Aluno, Curso

class AlunoModelTestCase(TestCase):

    def setUp(self):
        self.aluno = Aluno(
            nome = 'Isabelle',
            email = 'isabellebussmann@hotmail.com',
            cpf = 35971759884,
            rg =  561016677,
            data_nascimento = 5/28/1998,
            celular = '12 98291-6028',
        )

    def test_verifica_atributos_do_aluno(self):
        """Teste que verifica os atributos de um aluno"""
        self.assertEqual(self.aluno.nome, 'Isabelle')
        self.assertEqual(self.aluno.email, 'isabellebussmann@hotmail.com')
        self.assertEqual(self.aluno.cpf, 35971759884)
        self.assertEqual(self.aluno.rg, 561016677)
        self.assertEqual(self.aluno.data_nascimento, 5/28/1998)
        self.assertEqual(self.aluno.celular, '12 98291-6028')
        self.assertEqual(self.aluno.foto, "")

class CursoModelTestCase(TestCase):

    def setUp(self):
        self.curso = Curso(
            codigo_curso = 'CT1',
            descricao = 'Curso teste 1',
        )

    def test_verifica_atributos_do_curso(self):
        """Teste que verifica os atributos de um curso"""
        self.assertEqual(self.curso.codigo_curso, 'CT1')
        self.assertEqual(self.curso.descricao, 'Curso teste 1')
        self.assertEqual(self.curso.nivel, 'B')
