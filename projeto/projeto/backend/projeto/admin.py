from django.contrib import admin
from django.apps import apps
from .models import *

app_models = apps.get_app_config(__name__.split('.')[0]).get_models() # Obter todas tabelas

models_list = list(app_models)
# models_list = [Student] # Obter tabelas à escolha

admin.site.register(models_list)
