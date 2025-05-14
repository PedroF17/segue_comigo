from django.contrib import admin
from django.urls import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('condutor/create/', CondutorView.as_view()), #requer autenticacao
    path('condutor/create/<int:pk>/', CondutorView.as_view()), #requer autenticacao
    path('condutor/list/', AdminCondutorView.as_view()), #requer autenticacao
    path('condutor/marca_veiculo/', MarcaVeiculoView.as_view()),
    path('condutor/marca_veiculo/<int:pk>/', MarcaVeiculoView.as_view()),
    path('condutor/cor_veiculo/', CorVeiculoView.as_view()),
    path('condutor/cor_veiculo/<int:pk>/', CorVeiculoView.as_view()),
    path('condutor/tipo_veiculo/', TipoVeiculoView.as_view()),
    path('condutor/tipo_veiculo/<int:pk>/', TipoVeiculoView.as_view()),
    path('condutor/tipo_categoria/', TipoCategoriaView.as_view()),
    path('condutor/tipo_categoria/<int:pk>/', TipoCategoriaView.as_view()),
    path('condutor/veiculo/', VeiculoView.as_view()), #requer autenticacao
    path('condutor/veiculo/<int:pk>/', VeiculoView.as_view()), #requer autenticacao
    path('condutor/condutor_veiculo/', CondutorVeiculoView.as_view()), #requer autenticacao
    path('condutor/condutor_associar/<int:pk>/', AssociarCondutorVeiculoView.as_view()), #requer autenticacao
    path('condutor/veiculo_status/<int:pk>/', EstadoVeiculoView.as_view()), #requer autenticacao
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
