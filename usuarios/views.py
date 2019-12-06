from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .models import *
#from django.contrib.auth.models import User, auth
from .serializers import EstudianteSerializer, DocenteSerializer

from .permisos import IsOwnerProfileOrReadOnly
#----------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------

class EstudianteList(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = (IsAuthenticated, )

    # def perform_create(self, serializer):
    #     user=self.request.user
    #     serializer.save(user=user)
    # authentication_class = (TokenAuthentication,)

class EstudianteCreate(generics.CreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Testimonials fetched',
            'data': response.data
        })
#
#
#
class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)
#    authentication_class = (TokenAuthentication,)

# class DocenteCreate(generics.CreateAPIView):
#     queryset = Docente.objects.all()
#     serializer_class = DocenteSerializer
#    permission_classes = (IsAuthenticated, )
#    authentication_class = (TokenAuthentication,)


#    permission_classes = (IsAuthenticated, )
#    authentication_class = (TokenAuthentication,)
class DocenteList(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
#    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
#
# class DocenteCreate(generics.CreateAPIView):
#     queryset = Docente.objects.all()
#     serializer_class = DocenteSerializer
# #    permission_classes = (IsAuthenticated, )
# #    authentication_class = (TokenAuthentication,)
#
class DocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:estudiante_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)

class Logout(APIView):
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
