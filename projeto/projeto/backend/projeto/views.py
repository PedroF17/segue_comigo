from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

