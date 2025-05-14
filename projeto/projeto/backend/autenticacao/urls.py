from django.contrib import admin
from django.urls import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import * 

urlpatterns = [
    path('utilizador/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('utilizador/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('utilizador/create/', CreateAccountView.as_view(), name='create_account'), #requer autenticacao
    path('utilizador/create_first/', FirstCreateAccountView.as_view(), name='first_create_account'),
    path('utilizador/new_password/', ChangePasswordView.as_view(), name='change_password'), #requer autenticacao
    path('utilizador/view/', AccountView.as_view(), name='account_view'), #requer autenticacao
    path('utilizador/grupo/view/', GrupoView.as_view(), name='grupo_view'), #requer autenticacao
    path('utilizador/grupo/view/code/', CodigoGrupoView.as_view(), name='codigo_grupo_view'), #requer autenticacao
    path('utilizador/grupo/view/code/<int:pk>/', CodigoGrupoView.as_view(), name='codigo_grupo_view'), #requer autenticacao
    path('utilizador/contacto/', ContactoView.as_view(), name='contacto_view'), #requer autenticacao
    path('utilizador/contacto/<int:pk>/', ContactoView.as_view(), name='contacto_view'), #requer autenticacao
    path('utilizador/morada/', MoradaView.as_view(), name='morada_view'), #requer autenticacao
    path('utilizador/morada/<int:pk>/', MoradaView.as_view(), name='morada_view'), #requer autenticacao
    path('utilizador/tipo_contacto/', TipoContactoView.as_view(), name='tipo_contacto_view'),
    path('utilizador/tipo_contacto/<int:pk>/', TipoContactoView.as_view(), name='tipo_contacto_view'),
    path('utilizador/estado_civil/', EstadoCivilView.as_view(), name='estado_civil_view'),
    path('utilizador/estado_civil/<int:pk>/', EstadoCivilView.as_view(), name='estado_civil_view'),
    path('utilizador/nacionalidade/', NacionalidadeView.as_view(), name='nacionalidade_view'),
    path('utilizador/nacionalidade/<int:pk>/', NacionalidadeView.as_view(), name='nacionalidade_view'),
    path('utilizador/pais/', PaisView.as_view(), name='pais_view'),
    path('utilizador/pais/<int:pk>/', PaisView.as_view(), name='pais_view'),
    path('utilizador/distrito/', DistritoView.as_view(), name='distrito_view'),
    path('utilizador/distrito/<int:pk>/', DistritoView.as_view(), name='distrito_view'),
    path('utilizador/conselho/', ConselhoView.as_view(), name='conselho_view'),
    path('utilizador/conselho/<int:pk>/', ConselhoView.as_view(), name='conselho_view'),
    path('utilizador/freguesia/', FreguesiaView.as_view(), name='freguesia_view'),
    path('utilizador/freguesia/<int:pk>/', FreguesiaView.as_view(), name='freguesia_view'),
    path('utilizador/check_admin/', CheckAdminView.as_view(), name='check_admin'),
    path('utilizador/check_condutor/', CheckCondutorView.as_view(), name='check_condutor'),
    path('utilizador/check_passageiro/', CheckPassageiroView.as_view(), name='check_passageiro'),
]


