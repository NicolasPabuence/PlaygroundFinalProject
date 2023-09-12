from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.lista_zapatos, name='lista_zapatos'),
    path('detalle_zapato/<int:zapato_id>/', views.detalle_zapato, name='detalle_zapato'),
    path('categorias/', views.categorias, name='categorias'),
    path('zapatos_por_categoria/<int:categoria_id>/', views.zapatos_por_categoria, name='zapatos_por_categoria'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('contacto/', views.contacto, name='contacto'),
]
