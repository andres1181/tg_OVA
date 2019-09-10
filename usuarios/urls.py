from django.urls import include, path
#from Gestion_OVA import views as viewsOVA
#from . import views
from .views import EstudianteList

urlpatterns = [
    path('estudiante/', EstudianteList.as_view(), name = 'estudiante_list'),
#     path('curso/', include('Gestion_OVA.urls')),
# #    path('', viewsOVA.index, name='index'),
#     path('registro', views.registro),

]
