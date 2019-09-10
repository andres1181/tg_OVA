from django.db import models

class Objeto(models.Model):

    id = models.AutoField(primary_key = True)
    introduccion = models.CharField(max_length=200)
    resumen = models.CharField(max_length=200)
    avance = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)


class Subtema(models.Model):
    id = models.AutoField(primary_key = True)
    id_ova = models.ForeignKey(Objeto, on_delete=models.CASCADE)
    contenido =  models.CharField(max_length=200)

class Pregunta(models.Model):
    id = models.AutoField(primary_key = True)
    id_Subtema = models.ForeignKey(Subtema, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=200)


class RespuestaPregunta(models.Model):
    id = models.AutoField(primary_key = True)
    id_Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=200) #Correcta/Incorrecta

class RespuestaEstudiante(models.Model): #Respuesta del Estudiante a una pregunta
    id_Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_Estudiante = models.ForeignKey('usuarios.Estudiante', on_delete=models.CASCADE)
    estado = models.CharField(max_length=200) #Correcta/Incorrecta

class Grupo(models.Model):
    id = models.AutoField(primary_key = True)
    id_Docente = models.ForeignKey('usuarios.Docente', on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField('usuarios.Estudiante')
    objetos_virtuales = models.ManyToManyField(Objeto)
    cod_grupo = models.CharField(unique=True, max_length=10)
    fecha_creacion = models.DateField()
    num_estudiantes = models.IntegerField()
