from django.contrib import admin
from django.urls import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('viagem/passageiro/create/', PassageiroView.as_view()), #requer autenticacao
    path('viagem/passageiro/create/<int:pk>', PassageiroView.as_view()), #requer autenticacao
    path('viagem/reserva/', ReservaView.as_view()), #requer autenticacao
    path('viagem/reserva/<int:pk>/', ReservaView.as_view()), #requer autenticacao
    path('viagem/reserva_condutor/', CondutorReservaView.as_view()), #requer autenticacao
    path('viagem/reserva_condutor/<int:pk>/', CondutorReservaView.as_view()), #requer autenticacao
    path('viagem/reserva_condutor/cancel/<int:pk>/', CancelarReservaView.as_view()), #requer autenticacao
    path('viagem/reserva/confirm/<int:pk>/', FinalizarReservaView.as_view()), #requer autenticacao
    path('viagem/reserva/confirm2/<int:pk>/', FinalizarReserva2View.as_view()), #requer autenticacao
    path('viagem/viagem/associate/', AssociarViagemView.as_view()), #requer autenticacao
    path('viagem/viagem/list/', PassageiroAssociarViagemView.as_view()), #requer autenticacao
    path('viagem/viagem/list_condutor/', PassageiroAssociarViagemView.as_view()), #requer autenticacao
    path('viagem/desvio/', DesvioView.as_view()), #requer autenticacao
    path('viagem/desvio/<int:pk>/', DesvioView.as_view()), #requer autenticacao
    path('viagem/desvio_condutor/', CondutorDesvioView.as_view()), #requer autenticacao
    path('viagem/desvio_condutor/<int:pk>/', CondutorDesvioView.as_view()), #requer autenticacao
    path('viagem/viagem/start/<int:pk>/', IniciarViagemView.as_view()), #requer autenticacao
    path('viagem/viagem/finish/<int:pk>/', FinalizarViagemView.as_view()), #requer autenticacao
    path('viagem/ponto/', PontoView.as_view()),
    path('viagem/ponto/<int:pk>/', PontoView.as_view()),
] 

