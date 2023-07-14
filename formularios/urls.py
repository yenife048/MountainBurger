from django.urls import path

from . import views

urlpatterns = [
    path('formularios/', views.formularios, name='Formularios'),
    path('formu/', views.formu, name='Formu'),
]

