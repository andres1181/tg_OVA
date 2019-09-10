from django.db import models
from django.contrib.auth.models import AbstractUser
#https://www.youtube.com/watch?v=kh4YFQrvVyE&list=PLMbRqrU_kvbRzgD2s7JHvJxGs6FdvFjg9&index=6

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres', max_length=30)
    apellidos = models.CharField('Apellidos', max_length=30)
    username = models.CharField('NickName', max_length=10) #codigo Estudiante
    email = models.EmailField()
    password = models.CharField('Contraseña', max_length=10)

    # def _str_(self):
    #     return '{0},{1},{2}'.format(self.username,self.nombres, self.apellidos)

    class Meta:
       abstract = True
#-----------------------------------------------------------------
# class Usuario(AbstractUser):
#     id = models.AutoField(primary_key = True)
#
#     def __str__(self):

class Estudiante(Usuario):
    codigo_estudiante = models.CharField(unique=True, max_length=10) #codigo Estudiante
    plan = models.CharField(max_length=4)

    # def _str_(self):
    #     return '{0},{1},{2},{3}'.format(self.username,self.nombres, self.apellidos, self.codigo_estudiante)

class Docente(Usuario):
    codigo_docente = models.CharField(unique=True, max_length=10) #codigo de  profesor

    # def _str_(self):
    #     return '{0},{1},{2},{3}'.format(self.username,self.nombres, self.apellidos, self.codigo_docente)



    # def _str_(self):
    #     return '{0},{1},{2},{3}'.format(self.cod_grupo,self.fecha_creacion, self.apellidos, self.id_Docente)
