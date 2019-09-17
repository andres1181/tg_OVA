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
from django.contrib import admin
from django.urls import include, path
from Gestion_OVA import views
from rest_framework.authtoken import views
from usuarios.views import Login, Logout
#from Gestion_Usuarios.api import UserAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_usuarios/1.0/', include(('usuarios.urls', 'api'))),
    path('api_ova/1.0/', include(('Gestion_OVA.urls', 'api_ova'))),
# #    path('register/1.0/', include(('Gestion_Usuarios.urls', 'api'))),
#     path('curso/', include('Gestion_ova.urls')),
#     path('register/', include('usuarios.urls')),
    path('api_generate_token/', views.obtain_auth_token),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
]
