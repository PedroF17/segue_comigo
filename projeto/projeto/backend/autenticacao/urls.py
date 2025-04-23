from django.contrib import admin
from django.urls import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import * 

urlpatterns = [
    path('utilizador/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('utilizador/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('utilizador/create/', CreateAccountView.as_view()),
    path('utilizador/create_first/', FirstCreateAccountView.as_view()),
    path('utilizador/new_password/', ChangePasswordView.as_view()),
    path('utilizador/view/', AccountView.as_view()),
    path('utilizador/grupo/view/', GrupoView.as_view()),
    path('utilizador/contacto/', ContactoView.as_view()),
    path('utilizador/contacto/<int:pk>/', ContactoView.as_view()),
    path('utilizador/morada/', MoradaView.as_view()),
    path('utilizador/morada/<int:pk>/', MoradaView.as_view()),
    path('utilizador/tipo_contacto/', TipoContactoView.as_view()),
    path('utilizador/tipo_contacto/<int:pk>/', TipoContactoView.as_view()),
    path('utilizador/estado_civil/', EstadoCivilView.as_view()),
    path('utilizador/estado_civil/<int:pk>/', EstadoCivilView.as_view()),
    path('utilizador/pais/', PaisView.as_view()),
    path('utilizador/pais/<int:pk>/', PaisView.as_view()),
    path('utilizador/distrito/', DistritoView.as_view()),
    path('utilizador/distrito/<int:pk>/', DistritoView.as_view()),
    path('utilizador/conselho/', ConselhoView.as_view()),
    path('utilizador/conselho/<int:pk>/', ConselhoView.as_view()),
    path('utilizador/freguesia/', FreguesiaView.as_view()),
    path('utilizador/freguesia/<int:pk>/', FreguesiaView.as_view()),

    path('check_admin/', CheckAdminView.as_view()),
    path('check_condutor/', CheckCondutorView.as_view()),
    path('check_passageiro/', CheckPassageiroView.as_view()),
]


