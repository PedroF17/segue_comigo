from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# -------------------------------------

# Ficheiro com todas funções do Backend

# -------------------------------------

"""

class UtilizadorView(APIView):

    def post(self, request):
        data = request.data
        serializer = UtilizadorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Utilizador adicionado com successo", safe=False)
        return JsonResponse("Falha ao adicionar utilizador", safe=False)

    def get_student(self, pk):
        try:
            student = Utilizador.objects.get(id_utilizador=pk)
            return student
        except Utilizador.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = UtilizadorSerializer(data)
        else:
            data = Utilizador.objects.all()
            serializer = UtilizadorSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        utilizador_to_update = Utilizador.objects.get(id_utilizador=pk)
        serializer = UtilizadorSerializer(
            instance=utilizador_to_update, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Utilizador atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao atualizar Utilizador")

    def delete(self, request, pk):
        utilizador_to_delete = Utilizador.objects.get(id_utilizador=pk)
        utilizador_to_delete.delete()
        return JsonResponse("Student Deleted Successfully", safe=False)

"""
