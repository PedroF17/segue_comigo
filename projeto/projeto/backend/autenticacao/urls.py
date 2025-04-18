from django.contrib import admin
from django.urls import *
from rest_framework_simplejwt.views import TokenRefreshView

from .views import * 

urlpatterns = [
    path("utilizador_registo/", RegistroContaView.as_view()),
    path('utilizador_token/', TokenLoginView.as_view(), name='custom_token_obtain'),
    #path('utilizador_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('utilizador_alt/senha', AlterarSenhaView.as_view()),
    path('utilizador_check/admin', VerificarAdminView.as_view()),
    path('utilizador_check/condutor', VerificarCondutorView.as_view()),
    path('utilizador_check/passageiro', VerificarPassageiroView.as_view()),
]


