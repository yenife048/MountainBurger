from django.shortcuts import render

# Create your views here.
def formularios(request):
    
    return render(request, "iniciar sesion/inicios.html")

def formu(request):
    
    return render(request, "Recuperar contraseña/recup.html")

