from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):

	use_in_migrations = True

	def create_user(self, email, codigo, nombres, apellidos, is_estudiante, password=None):
		if not email:
			raise ValueError('El usuario debe tener un email')
		if not codigo:
			raise ValueError('El usuario debe tener un código')
		if not nombres:
			raise ValueError('El usuario debe tener al menos un nombre')
		if not apellidos:
			raise ValueError('El usuario debe tener al menos un apellido')

		user = self.model(
			email=self.normalize_email(email),
			codigo=codigo,
			nombres=nombres,
			apellidos=apellidos,
			is_estudiante=is_estudiante
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, codigo, nombres, apellidos, is_estudiante, password):
        user = self.create_user(
            email,
            password=password,
            codigo=codigo,
			nombres=nombres,
			apellidos=apellidos,
			is_estudiante=is_estudiante
        )
        user.staff = True
        user.save(using=self._db)
        return user
	def create_superuser(self, email, codigo, nombres, apellidos, is_estudiante, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			codigo=codigo,
			nombres=nombres,
			apellidos=apellidos,
			is_estudiante=is_estudiante
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class EstudiantePerfil(AbstractBaseUser):

	username                = None
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	codigo 				    = models.CharField(max_length=10, unique=True)
    nombres 				= models.CharField(max_length=100)
    apellidos 				= models.CharField(max_length=100)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
    is_estudiante		    = models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'codigo'
	REQUIRED_FIELDS = ['codigo', 'email', 'nombres', 'apellidos']

	objects = UsuarioManager()

	def __str__(self):
		return self.codigo

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True
