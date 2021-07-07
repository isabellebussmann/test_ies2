from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    rg = models.CharField(max_length=9, unique=True, verbose_name='RG')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    celular = models.CharField(max_length=14)
    foto = models.ImageField(blank=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=10, verbose_name='Código do Curso')
    descricao = models.CharField(max_length=100, verbose_name='Descrição')
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B', verbose_name='Nível')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default="M",
                               verbose_name='Período')


class Professor(models.Model):
    user = models.OneToOneField('auth.user', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)

    def __str__(self):
        return self.nome


class Prova(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    publicada = models.BooleanField(default=False)
    descricao_prova = models.CharField(max_length=255, verbose_name='Descrição da Prova')
    data = models.DateField(auto_now_add=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao_prova

class Pergunta(models.Model):
    questao = models.CharField(max_length=255, verbose_name='Questão')
    alt1_correta = models.CharField(max_length=255, verbose_name='Alternativa A (correta)')
    alt2_errada = models.CharField(max_length=255, verbose_name='Alternativa B')
    alt3_errada = models.CharField(max_length=255, verbose_name='Alternativa C')
    alt4_errada = models.CharField(max_length=255, verbose_name='Alternativa D')
    alt5_errada = models.CharField(max_length=255, verbose_name='Alternativa E')

    def __str__(self):
        return self.questao

class ModeloProva(models.Model):
    prova = models.ManyToManyField(Prova)
    questoes = models.ManyToManyField(Pergunta, verbose_name='Questões')




