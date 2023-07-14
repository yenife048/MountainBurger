from django.urls import path

from . import views

urlpatterns = [
        path('', views.formularios, name='Formularios'),
        path('', views.formu, name='Formu'),
        
]