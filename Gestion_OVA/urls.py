"""tg_ova URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from .views import *

urlpatterns = [
    path('Objeto/', ObjetoList.as_view(), name = 'objeto_list'),
    path('Objeto/<int:pk>', ObjetoDetail.as_view(), name = 'objeto_detail'),
    path('Subtema/', SubtemaList.as_view(), name = 'subtema_list'),
    path('Subtema/<int:pk>', SubtemaDetail.as_view(), name = 'subtema_detail'),
    path('Slide/', SlideList.as_view(), name = 'slide_list'),
    path('Slide/<int:pk>', SlideDetail.as_view(), name = 'slide_detail'),
    path('Pregunta/', PreguntaList.as_view(), name = 'pregunta_list'),
    path('Pregunta/<int:pk>', PreguntaDetail.as_view(), name = 'pregunta_detail'),
    path('RespuestaPregunta/', RespuestaPreguntaList.as_view(), name = 'respuestaPregunta_list'),
    path('RespuestaPregunta/<int:pk>', RespuestaPreguntaDetail.as_view(), name = 'respuestaPregunta_detail'),
    path('RespuestaEstudiante/', RespuestaEstudianteList.as_view(), name = 'respuestaEstudiante_list'),
    path('RespuestaEstudiante/<int:pk>', RespuestaEstudianteDetail.as_view(), name = 'RespuestaEstudiante_detail'),
    path('Grupo/', GrupoList.as_view(), name = 'grupo_list'),
    path('Grupo/<int:pk>', GrupoDetail.as_view(), name = 'Grupo_detail'),
]
