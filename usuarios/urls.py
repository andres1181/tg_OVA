from django.urls import include, path
from Gestion_OVA import views as viewsOVA
from . import views

urlpatterns = [

    path('curso/', include('Gestion_OVA.urls')),
#    path('', viewsOVA.index, name='index'),
    path('registro', views.registro),

]
