from datetime import timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Avg, F
from django.db.models.functions import TruncMonth
from datetime import date

from .models import *

@login_required
def index(request):

    mes_actal = date.today().month

    data = {
            'productos_total': Inventario.objects.aggregate(total=Sum('cantidad'))['total'],
            'ventas_mensuales': Venta.objects.filter(fecha__month=mes_actal).count(),
            'ingresos_mensuales': Venta.objects.filter(fecha__month=mes_actal).aggregate(total_ventas=Sum('total'))['total_ventas'] or 0.0,
            'servicios_facturados': ServicioFacturacion.objects.filter(fecha_emision__month=mes_actal).count(),
            'ingresos_servicios': ServicioFacturacion.objects.aggregate(total=Sum('servicios__precio'))['total'],
            'ultimas_ventas': Venta.objects.all().order_by('-fecha')[:8]
    }
    return render(request, "core/index.html", data )

def inicioSesion(request):
    return render(request, "core/login.html")

@login_required
def clientes(request):
    return render(request, "core/clientes.html")

@login_required()
def usuarios(request):
    return render(request, "core/usuarios.html")

@login_required
def productos(request):
    data = {
        'productos_total': len(Producto.objects.all()),
        'ventas_hoy': len(Venta.objects.filter(fecha=timezone.now().date())),
        'ventas_ayer': len(Venta.objects.filter(fecha=timezone.now().date()-timedelta(days=1))),
        'ventas_total': len(Venta.objects.all())
    }
    return render(request, "core/productos.html", data)

@login_required
def ventas(request):
    return render(request, "core/ventas.html")

@login_required
def ventas_menu(request):
    return render(request, "core/ventas-menu.html")

@login_required
def registroVentas(request):
    return render(request, "core/registro-ventas.html")

@login_required
def transacciones(request):
    return render(request, "core/transacciones.html")

@login_required
def proveedores(request):
    return render(request, "core/proveedores.html")

@login_required
def facturas(request):
    return render(request, "core/facturas.html")

@login_required
def servicios(request):
    return render(request, "core/servicios.html")

@login_required
def servicios_menu(request):
    return render(request, "core/servicios-menu.html")

@login_required
def registroServicios(request):
    return render(request, "core/registro-servicios.html")

@login_required
def servicioFacturado(request):
    return render(request, "core/servicios-facturado.html")

def login_view(request):

    if request.user.is_authenticated:
        print("ola")
        return redirect('index')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
	
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "core/login.html", {
                "message": "Nombre de usuario o contraseña incorrectos."
            })
	
    return render(request, "core/login.html")

@login_required  
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("inicio-sesion"))