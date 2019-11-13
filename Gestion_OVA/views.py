from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from .serializers import ObjetoSerializer, SubtemaSerializer, PreguntaSerializer, PreguntaSerializer, RespuestaPreguntaSerializer, RespuestaEstudianteSerializer, GrupoSerializer, SlideSerializer

from .models import Objeto, Subtema, Pregunta, RespuestaPregunta, RespuestaEstudiante, Grupo, Slide


class ObjetoList(generics.ListCreateAPIView):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer
"""     permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,) """

class ObjetoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Objeto.objects.all()
    serializer_class = ObjetoSerializer
"""     permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,) """
#---------------------------------------------------------------------------
class SubtemaList(generics.ListCreateAPIView):
    queryset = Subtema.objects.all()
    serializer_class = SubtemaSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_class = (TokenAuthentication,)

class SubtemaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtema.objects.all()
    serializer_class = SubtemaSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

#---------------------------------------------------------------------------

class SlideList(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    # permission_classes = (IsAuthenticated, )
    # authentication_class = (TokenAuthentication,)

class SlideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

#---------------------------------------------------------------------------

class PreguntaList(generics.ListCreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class PreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

#---------------------------------------------------------------------------

class RespuestaPreguntaList(generics.ListCreateAPIView):
    queryset = RespuestaPregunta.objects.all()
    serializer_class = RespuestaPreguntaSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class RespuestaPreguntaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespuestaPregunta.objects.all()
    serializer_class = RespuestaPreguntaSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

#---------------------------------------------------------------------------

class RespuestaEstudianteList(generics.ListCreateAPIView):
    queryset = RespuestaEstudiante.objects.all()
    serializer_class = RespuestaEstudianteSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class RespuestaEstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RespuestaEstudiante.objects.all()
    serializer_class = RespuestaEstudianteSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

#---------------------------------------------------------------------------

class GrupoList(generics.ListCreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class GrupoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

# from django.shortcuts import render, render_to_response
#
# # Create your views here.
# def index(resquest):
#     return render(resquest, 'index.html', {})
#
# def ova(resquest):
#     return render(resquest, 'ova.html', {})
#
# #def index(resquest):
# #    return render_to_response('index.html')
