from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nueva-receta/', views.crear_receta, name='crear_receta'),
    path('nuevo-autor/', views.crear_autor, name='crear_autor'),
    path('nuevo-tipo/', views.crear_tipo, name='crear_tipo'),
    path('buscar/', views.buscar_receta, name='buscar_receta'),
    path('receta/', views.listar_recetas, name='listar_recetas'),
]
