from django.test import TestCase
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.aluno = Aluno(
            nome='Isabelle',
            email='isabellebussmann@hotmail.com',
            cpf='35971759884',
            rg='561016677',
            data_nascimento='5/28/1998',
            celular='12 98291-6028',
            foto=None
        )
        self.serializer = AlunoSerializer(instance=self.aluno)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'cpf', 'rg', 'data_nascimento', 'celular', 'foto']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.aluno.nome)
        self.assertEqual(data['email'], self.aluno.email)
        self.assertEqual(data['cpf'], self.aluno.cpf)
        self.assertEqual(data['rg'], self.aluno.rg)
        self.assertEqual(data['data_nascimento'], self.aluno.data_nascimento)
        self.assertEqual(data['celular'], self.aluno.celular)
        self.assertEqual(data['foto'], self.aluno.foto)

