from django.contrib import admin
from django.urls import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import * 

urlpatterns = [
    path('comunicacao/ocorrencia/', OcorrenciaView.as_view()), #requer autenticacao
    path('comunicacao/ocorrencia/<int:pk>/', OcorrenciaView.as_view()), #requer autenticacao
    path('comunicacao/ocorrencia/read/', AdminOcorrenciaView.as_view()), #requer autenticacao
    path('comunicacao/ocorrencia/read/<int:pk>/', AdminOcorrenciaView.as_view()), #requer autenticacao
    path('comunicacao/tipo_ocorrencia/', TipoOcorrenciaView.as_view()), 
    path('comunicacao/tipo_ocorrencia/<int:pk>/', TipoOcorrenciaView.as_view()),
    path('comunicacao/tipo_alerta/', TipoAlertaView.as_view()), 
    path('comunicacao/tipo_alerta/<int:pk>/', TipoAlertaView.as_view()),
    path('comunicacao/alerta/', AlertaView.as_view()), #requer autenticacao
    path('comunicacao/alerta/<int:pk>/', AlertaView.as_view()), #requer autenticacao
    path('comunicacao/utilizador_alerta/', UtilizadorAlertaView.as_view()), #requer autenticacao
    path('comunicacao/utilizador_alerta/<int:pk>/', UtilizadorAlertaView.as_view()), #requer autenticacao
    #path('comunicacao/mensagem/', MensagemView.as_view()),
]


