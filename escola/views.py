from rest_framework import viewsets, generics, filters, status
from escola.models import Aluno, Curso, Matricula, Pergunta, Professor, Prova
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunosSerializer, ListaAlunosMatriculadosSerializer, PerguntasSerializer, ProfessorSerializer, ProvaSerializer, ListaProvasCursosSerializer, ModeloProvaSerializer, ModeloProva, ListaModeloProvaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

class ProfessoresViewSet(viewsets.ModelViewSet):
    """ Exibindo professores """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['descricao']
    search_fields = ['codigo_curso', 'descricao']
    http_method_names = ['get', 'put', 'post', 'path']

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response

class MatriculaViewSet(viewsets.ModelViewSet):
    """ Listando todas as matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    @method_decorator(cache_page(40))
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunosSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

class ProvasViewSet(viewsets.ModelViewSet):
    queryset = Prova.objects.all()
    serializer_class = ProvaSerializer

class PerguntasViewSet(viewsets.ModelViewSet):
    queryset = Pergunta.objects.all()
    serializer_class = PerguntasSerializer

class ListaProvasCursos(generics.ListAPIView):
    """ Listando Provas por Curso"""
    def get_queryset(self):
        queryset = Prova.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaProvasCursosSerializer

class ModeloProvaViewSet(viewsets.ModelViewSet):
    queryset = ModeloProva.objects.all()
    serializer_class = ModeloProvaSerializer

class ListaModeloProva(generics.ListAPIView):
    """ Listando Perguntas por Prova """
    def get_queryset(self):
        queryset = ModeloProva.objects.filter(prova=self.kwargs['pk'])
        return queryset
    serializer_class = ListaModeloProvaSerializer

