from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("clientes", views.clientes, name="clientes"),
    path("proveedores", views.proveedores, name="proveedores"),
    path("usuarios", views.usuarios, name="usuarios"),
    path("inventario", views.inventario, name="inventario"),
    path("servicios", views.servicios, name="servicios"),
    path("registro-servicios", views.registroServicios, name="registro-servicios"),




]
