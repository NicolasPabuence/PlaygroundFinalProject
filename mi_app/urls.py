from django import views
from django.urls import path
from .views import AdidasDelete, ArticuloNuevo, AdidasDetalle, AdidasLista, JordanLista, NikeLista, OtroLista, AdidasUpdate, JordanDetalle, JordanUpdate, JordanDelete, OtroDetalle, NikeDelete, NikeDetalle, NikeUpdate, OtroUpdate, OtroDelete, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, HomeView, ComentarioPagina
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaGuitarras/', NikeLista.as_view(), name='nike'),
    path('listaBajos/', AdidasLista.as_view(), name='adidas'),
    path('listaJordan/', JordanLista.as_view(), name='jordan'),
    path('listaOtros/', OtroLista.as_view(), name='otros'),

    path('nikeDetalle/<int:pk>/', NikeDetalle.as_view(), name='nike'),
    path('adidasDetalle/<int:pk>/', AdidasDetalle.as_view(), name='adidas'),
    path('jordanDetalle/<int:pk>/', JordanDetalle.as_view(), name='jordan'),
    path('otroDetalle/<int:pk>/', OtroDetalle.as_view(), name='otro'),

    path('nikeEdicion/<int:pk>/', NikeUpdate.as_view(), name='nike_editar'),
    path('adidasEdicion/<int:pk>/', AdidasUpdate.as_view(), name='adidas_editar'),
    path('jordanEdicion/<int:pk>/', JordanUpdate.as_view(), name='jordan_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),

    path('nikeBorrado/<int:pk>/', NikeDelete.as_view(), name='nike_eliminar'),
    path('adidasBorrado/<int:pk>/', AdidasDelete.as_view(), name='adidas_eliminar'),
    path('jordanBorrado/<int:pk>/', JordanDelete.as_view(), name='jordan_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('articuloNuevo/', ArticuloNuevo.as_view(), name='nuevo'),

    path('nikeDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('adidasDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('jordamDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercaDeMi/', views.about, name='acercaDeMi'),
]

