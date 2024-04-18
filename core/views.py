from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def clientes(request):
    return render(request, "core/clientes.html")

def proveedores(request):
    return render(request, "core/proveedores.html")

def usuarios(request):
    return render(request, "core/usuarios.html")

def inventario(request):
    return render(request, "core/inventario.html")

def servicios(request):
    return render(request, "core/servicios.html")

def registroServicios(request):
    return render(request, "core/registro-servicios.html")