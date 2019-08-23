from django.shortcuts import render, redirect
#from django.contrib.auth.models import User, auth
from .models import Usuario, Estudiante

def registro(request):

    if request.method == 'POST':
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        codigo = request.POST['codigo']
        usuario = request.POST['usuario']
        plan = request.POST['plan']
        email = request.POST['email']
        contrasena1 = request.POST['contrasena1']
        contrasena2 = request.POST['contrasena2']

        if contrasena1==contrasena2:
            if Estudiante.objects.filter(username=usuario).exists() or Estudiante.objects.filter(codigo_estudiante=codigo).exists():
                print('El usuario ya se encuentra registrado')
            elif Estudiante.objects.filter(email=email).exists():
                print('El correo ya existe')
            else:
                user = Estudiante.objects.create_user(username=usuario, first_name=nombres, last_name=apellidos, password=contrasena1, email=email, codigo_estudiante=codigo, plan=plan, is_active=True, is_staff=False, is_superuser=False)
                user = user.save();
                print('Usuario Creado')

        else:
            print('Las contraseñas no coinciden')

            return redirect('/curso/index')
    else:
        return render(request, 'registro.html', {})
