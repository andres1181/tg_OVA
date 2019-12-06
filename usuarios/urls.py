from django.urls import include, path
#from Gestion_ova import views as viewsova
#from . import views
from .views import *

urlpatterns = [
    path('crear_estudiante/', EstudianteCreate.as_view(), name = 'crear_estudiante'),
#    path('crear_docente/', DocenteCreate.as_view(), name = 'crear_docente'),
    # path('usuario/', UsuarioList.as_view(), name = 'usuario_list'),
    # path('usuario/<int:pk>', UsuarioDetail.as_view(), name = 'usuario_detail'),
    path('estudiante/', EstudianteList.as_view(), name = 'estudiante_list'),
    path('estudiante/<int:pk>', EstudianteDetail.as_view(), name = 'estudiante_detail'),
    path('docente/', DocenteList.as_view(), name = 'docente_list'),
    path('docente/<int:pk>', DocenteDetail.as_view(), name = 'docente_detail'),
#     path('curso/', include('Gestion_ova.urls')),
# #    path('', viewsova.index, name='index'),
#     path('registro', views.registro),

]
