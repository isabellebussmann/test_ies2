from django.contrib import admin
from escola.models import Aluno, Professor, Curso, Matricula, Prova, Pergunta, ModeloProva

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf')
    list_per_page = 20
    ordering = ('nome',)

admin.site.register(Aluno, Alunos)

class Professores(admin.ModelAdmin):
    list_display = ('id', 'user')

admin.site.register(Professor, Professores)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)

class Provas(admin.ModelAdmin):
    list_display = ('professor', 'data', 'publicada')

admin.site.register(Prova, Provas)

class Perguntas(admin.ModelAdmin):
    list_display = ('questao', 'alt1_correta')

admin.site.register(Pergunta, Perguntas)

class ModeloProvas(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(ModeloProva, ModeloProvas)
