from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import *
from .form import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "aplicacion/base.html")

def carreras(request):
    ctx = {"carreras": Carrera.objects.all()}
    return render(request, "aplicacion/carreras.html", ctx)

def ciclistas(request):
    ctx = {"ciclistas": Ciclista.objects.all()}
    return render(request, "aplicacion/ciclistas.html", ctx)

def grupos(request):
    ctx = {"grupos": Grupo.objects.all()}
    return render(request, "aplicacion/grupos.html", ctx)

def rankings(request):
    ctx = {"rankings": Ranking.objects.all()}
    return render(request, "aplicacion/rankings.html", ctx)

#_________Listas Ciclistas______##

class CiclistaList(LoginRequiredMixin, ListView):
    model = Ciclista

class CiclistaCreate(LoginRequiredMixin, CreateView):
    model = Ciclista
    fields= ['nombre', 'apellido', 'edad']
    success_url=  reverse_lazy('ciclistas')

class CiclistaDetail(LoginRequiredMixin, DetailView):
    model = Ciclista

class CiclistaUpdate(LoginRequiredMixin,UpdateView):
    model = Ciclista
    fields= ['nombre', 'apellido', 'edad']
    success_url=  reverse_lazy('ciclistas')

class CiclistaDelete(LoginRequiredMixin, DeleteView):
    model = Ciclista
    success_url=  reverse_lazy('ciclistas')

    #_________Listas Carreras______##

class CarreraList(LoginRequiredMixin, ListView):
    model = Carrera

class CarreraCreate(LoginRequiredMixin, CreateView):
    model = Carrera
    fields= ['nombre', 'etapa', 'km', 'tipo']
    success_url=  reverse_lazy('carreras')

class CarreraDetail(LoginRequiredMixin, DetailView):
    model = Carrera

class CarreraUpdate(LoginRequiredMixin, UpdateView):
    model = Carrera
    fields= ['nombre', 'etapa', 'km', 'tipo']
    success_url=  reverse_lazy('carreras')

class CarreraDelete(LoginRequiredMixin, DeleteView):
    model = Carrera
    success_url=  reverse_lazy('carreras')

#_________Listas rankings______##

class RankingList(LoginRequiredMixin, ListView):
    model = Ranking

class RankingCreate(LoginRequiredMixin, CreateView):
    model = Ranking
    fields= ['nombre', 'clasificacion']
    success_url=  reverse_lazy('rankings')

class RankingDetail(LoginRequiredMixin, DetailView):
    model = Ranking

class RankingUpdate(LoginRequiredMixin, UpdateView):
    model = Ranking
    fields= ['nombre', 'clasificacion']
    success_url=  reverse_lazy('rankings')

class RankingDelete(LoginRequiredMixin, DeleteView):
    model = Ranking
    success_url=  reverse_lazy('rankings')

#_________Listas Grupos______##

class GrupoList(LoginRequiredMixin, ListView):
    model = Grupo

class GrupoCreate(LoginRequiredMixin, CreateView):
    model = Grupo
    fields= ['nombre']
    success_url=  reverse_lazy('grupos')

class GrupoDetail(LoginRequiredMixin, DetailView):
    model = Grupo

class GrupoUpdate(LoginRequiredMixin, UpdateView):
    model = Grupo
    fields= ['nombre']
    success_url=  reverse_lazy('grupos')

class GrupoDelete(LoginRequiredMixin, DeleteView):
    model = Grupo
    success_url=  reverse_lazy('grupos')

    #_________Login Logout Register______##

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Datos Inválidos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 
    return render(request, "aplicacion/registro.html", {"form": form}) 

#_____registracion de usuarios_____

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            
            #_______es lo viejo

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: 
                avatarViejo[0].delete()
            
            #_____nuevo avatar
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            
            #____almacenn
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})


def about(request):
    return render(request, 'aplicacion/acercaDeMi.html', {})



