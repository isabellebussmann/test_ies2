from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula, Pergunta, Professor, Prova, ModeloProva
from escola.validators import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos"})
        if not celular_valido (data['celular']):
            raise serializers.ValidationError({'celular': "O número de celular deve seguir este modelo: 11 91234-1234 (respeitando os espaços e traço)"})
        return data

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasAlunosSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prova
        fields = '__all__'

class PerguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'

class ListaProvasCursosSerializer(serializers.ModelSerializer):
    professor = serializers.ReadOnlyField(source='professor.nome')
    curso = serializers.ReadOnlyField(source='curso.descricao_prova')
    class Meta:
        model = Prova
        fields = ['professor', 'curso', 'descricao_prova']

class ModeloProvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeloProva
        fields = '__all__'

class ListaModeloProvaSerializer(serializers.ModelSerializer):
    questoes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='questao')
    class Meta:
        model = ModeloProva
        fields = ['questoes']
