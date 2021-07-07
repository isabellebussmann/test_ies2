import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from escola.models import Aluno, Curso, Matricula

def criando_alunos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = '{}@{}'.format(nome.lower(),fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        celular = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        data_nascimento = fake.date_between(start_date='-60y', end_date='-15y')
        p = Aluno(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, data_nascimento=data_nascimento)
        p.save()

def criando_cursos(quantidade_de_cursos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_cursos):
        codigo_curso = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Fundamentos', 'Python intermediário','Python Avançado', 'Python para Data Science', 'Python/React']
        descricao = random.choice(descs)
        descs.remove(descricao)
        nivel = random.choice("BIA")
        c = Curso(codigo_curso=codigo_curso,descricao=descricao, nivel=nivel)
        c.save()

criando_alunos(200)
criando_cursos(5)