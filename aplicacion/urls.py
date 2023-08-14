from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

    path('', index, name="inicio"),

    path('ciclistas/', CiclistaList.as_view(), name="ciclistas"),
    path('create_ciclista/', CiclistaCreate.as_view(), name="create_ciclista"),
    path('detail_ciclista/<int:pk>/', CiclistaDetail.as_view(), name="detail_ciclista"),
    path('update_ciclista/<int:pk>/', CiclistaUpdate.as_view(), name="update_ciclista"),
    path('delete_ciclista/<int:pk>/', CiclistaDelete.as_view(), name="delete_ciclista"),

    path('carreras/', CarreraList.as_view(), name="carreras"),
    path('create_carrera/', CarreraCreate.as_view(), name="create_carrera"),
    path('detail_carrera/<int:pk>/', CarreraDetail.as_view(), name="detail_carrera"),
    path('update_carrera/<int:pk>/', CarreraUpdate.as_view(), name="update_carrera"),
    path('delete_carrera/<int:pk>/', CarreraDelete.as_view(), name="delete_carrera"),

    path('rankings/', RankingList.as_view(), name="rankings"),
    path('create_ranking/', RankingCreate.as_view(), name="create_ranking"),
    path('detail_ranking/<int:pk>/', RankingDetail.as_view(), name="detail_ranking"),
    path('update_ranking/<int:pk>/', RankingUpdate.as_view(), name="update_ranking"),
    path('delete_ranking/<int:pk>/', RankingDelete.as_view(), name="delete_ranking"),

    path('grupos/', GrupoList.as_view(), name="grupos"),
    path('create_grupo/', GrupoCreate.as_view(), name="create_grupo"),
    path('detail_grupo/<int:pk>/', GrupoDetail.as_view(), name="detail_grupo"),
    path('update_grupo/<int:pk>/', GrupoUpdate.as_view(), name="update_grupo"),
    path('delete_grupo/<int:pk>/', GrupoDelete.as_view(), name="delete_grupo"),

    path('login/', login_request, name="login"),
    path('logout', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),
    
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('acercaDeMi/', views.about, name='acerca_de_mi'),
]