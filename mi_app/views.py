from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Zapatilla, Comentario
from .forms import ActualizacionZapatilla, FormularioCambioPassword, FormularioEdicion, FormularioArticuloNuevo, FormularioRegistroUsuario, FormularioComentario


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'mi_app/inicio.html'

class LoginPagina(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

class RegistroPagina(FormView):
    template_name = 'mi_app/registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'mi_app/edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'mi_app/passwordCambio.html'
    success_url = reverse_lazy('password_exitoso')

def password_exitoso(request):
    return render(request, 'mi_app/passwordExitoso.html', {})


# Nike

class NikeLista(LoginRequiredMixin, ListView):
    context_object_name = 'nike'
    queryset = Zapatilla.objects.filter(zapatilla__startswith='nike')
    template_name = 'mi_app/listaNike.html'
    login_url = '/login/'

class NikeDetalle(LoginRequiredMixin, DetailView):
    model = Zapatilla
    context_object_name = 'nike'
    template_name = 'mi_app/nikeDetalle.html'

class NikeUpdate(LoginRequiredMixin, UpdateView):
    model = Zapatilla
    form_class = ActualizacionZapatilla
    success_url = reverse_lazy('nike')
    context_object_name = 'nike'
    template_name = 'mi_app/nikeEdicion.html'

class NikeDelete(LoginRequiredMixin, DeleteView):
    model = Zapatilla
    success_url = reverse_lazy('nike')
    context_object_name = 'nike'
    template_name = 'mi_app/nikeBorrado.html'

# Adidas

class AdidasLista(LoginRequiredMixin, ListView):
    context_object_name = 'adidas'
    queryset = Zapatilla.objects.filter(zapatilla__startswith='adidas')
    template_name = 'mi_app/listaAdidas.html'

class AdidasDetalle(LoginRequiredMixin,DetailView):
    model = Zapatilla
    context_object_name = 'adidas'
    template_name = 'mi_app/adidasDetalle.html'

class AdidasUpdate(LoginRequiredMixin, UpdateView):
    model = Zapatilla
    form_class = ActualizacionZapatilla
    success_url = reverse_lazy('adidas')
    context_object_name = 'adidas'
    template_name = 'mi_app/adidasEdicion.html'

class AdidasDelete(LoginRequiredMixin, DeleteView):
    model = Zapatilla
    success_url = reverse_lazy('adidas')
    context_object_name = 'adidas'
    template_name = 'mi_app/adidasBorrado.html'

# Jordan

class JordanLista(LoginRequiredMixin, ListView):
    context_object_name = 'jordan'
    queryset = Zapatilla.objects.filter(zapatilla__startswith='jordan')
    template_name = 'mi_app/listaJordan.html'

class JordanDetalle(LoginRequiredMixin, DetailView):
    model = Zapatilla
    context_object_name = 'jordan'
    template_name = 'mi_app/jordanDetalle.html'

class JordanUpdate(LoginRequiredMixin, UpdateView):
    model = Zapatilla
    form_class = ActualizacionZapatilla
    success_url = reverse_lazy('jordan')
    context_object_name = 'jordan'
    template_name = 'mi_app/jordanEdicion.html'

class JordanDelete(LoginRequiredMixin, DeleteView):
    model = Zapatilla
    success_url = reverse_lazy('jordan')
    context_object_name = 'jordan'
    template_name = 'mi_app/jordanBorrado.html'

# Otro

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Zapatilla.objects.filter(zapatilla__startswith='otro')
    template_name = 'mi_app/listaOtros.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Zapatilla
    context_object_name = 'otro'
    template_name = 'mi_app/otroDetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Zapatilla
    form_class = ActualizacionZapatilla
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'mi_app/otroEdicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Zapatilla
    success_url = reverse_lazy('otros')
    context_object_name = 'otro'
    template_name = 'mi_app/otroBorrado.html'

# Articulo Nuevo

class ArticuloNuevo(LoginRequiredMixin, CreateView):
    model = Zapatilla
    form_class = FormularioArticuloNuevo
    success_url = reverse_lazy('home')
    template_name = 'mi_app/articuloNuevo.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArticuloNuevo, self).form_valid(form)

# COMENTARIOS

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'mi_app/comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# ACERCA DE MI

def about(request):
    return render(request, 'mi_app/acercaDeMi.html', {})
