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
from .serializers import *
#----------------------------------------------------------------------------------
# def registro(request):
#
#     if request.method == 'POST':
#         nombres = request.POST['nombres']
#         apellidos = request.POST['apellidos']
#         codigo = request.POST['codigo']
#         usuario = request.POST['usuario']
#         plan = request.POST['plan']
#         email = request.POST['email']
#         contrasena1 = request.POST['contrasena1']
#         contrasena2 = request.POST['contrasena2']
#
#         if contrasena1==contrasena2:
#             if Estudiante.objects.filter(username=usuario).exists() or Estudiante.objects.filter(codigo_estudiante=codigo).exists():
#                 print('El usuario ya se encuentra registrado')
#             elif Estudiante.objects.filter(email=email).exists():
#                 print('El correo ya existe')
#             else:
#                 user = Estudiante.objects.create_user(username=usuario, first_name=nombres, last_name=apellidos, password=contrasena1, email=email, codigo_estudiante=codigo, plan=plan, is_active=True, is_staff=False, is_superuser=False)
#                 user = user.save();
#                 print('Usuario Creado')
#
#         else:
#             print('Las contraseñas no coinciden')
#
#         return redirect('curso/index')
#         #render(request, 'index.html', {})
#             #redirect('/curso/index')
#     else:
#         return render(request, 'registro.html', {})
# -----------------------------------------------------------------------------------

class EstudianteList(generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
#    permission_classes = (IsAuthenticated, )
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

# class EstudianteCreate(APIView):
#     def post(self, request, format=None):
#         serializer = EstudianteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudianteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
#    permission_classes = (IsAuthenticated, )
#    authentication_class = (TokenAuthentication,)

class DocenteList(generics.ListCreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class DocenteCreate(generics.CreateAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
#    permission_classes = (IsAuthenticated, )
#    authentication_class = (TokenAuthentication,)

class DocenteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer
#    permission_classes = (IsAuthenticated, )
#    authentication_class = (TokenAuthentication,)

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
