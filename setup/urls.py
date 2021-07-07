from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, ListaAlunosMatriculados, ListaProvasCursos, MatriculaViewSet, ListaMatriculasAluno, PerguntasViewSet, ProfessoresViewSet, ProvasViewSet, ModeloProvaViewSet, ListaModeloProva
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Escola",
      default_version='v1',
      description="Provedor local de provas e questões para alunos e cursos desenvolvido para implementação de conhecimento em Django Rest",
      terms_of_service="#",
      contact=openapi.Contact(email="isabellebussmann@hotmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')
router.register('professores', ProfessoresViewSet, basename='Professores')
router.register('provas', ProvasViewSet, basename='Provas')
router.register('perguntas', PerguntasViewSet, basename='Perguntas')
router.register('modeloprova', ModeloProvaViewSet, basename='Modelo Prova')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    path('cursos/<int:pk>/provas/', ListaProvasCursos.as_view()),
    path('provas/<int:pk>/perguntas/', ListaModeloProva.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
