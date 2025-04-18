from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password

from projeto.models import *
from .serializers import *


# Função Registo de conta
class RegistroContaView(APIView):

    def post(self, request):
        serializer = UtilizadorRegistroSerializer(data=request.data)

        if serializer.is_valid():
            utilizador = serializer.save()

            response_data = UtilizadorRegistroSerializer(utilizador).data

            return Response({
                "mensagem": "Conta criada com sucesso.",
                "utilizador": response_data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Função Login pela tokenização JWT 
class TokenLoginView(APIView):

    def post(self, request):
        serializer = CustomTokenSerializer(data=request.data)
        
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


# Função Alterar senha do Utilizador
class AlterarSenhaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        usuario = request.user  
        serializer = AlterarSenhaSerializer(usuario, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Senha alterada com sucesso!"}, status=200)
        return Response(serializer.errors, status=400)


# Função Verificar se e ADMIN
class VerificarAdminView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request, *args, **kwargs):
        usuario = request.user  

        try:
            administrador = Administrador.objects.get(utilizadorid_utilizador=usuario)
            return Response({'is_admin': True}, status=200)
        except ObjectDoesNotExist:
            return Response({'is_admin': False}, status=200)


# Função Verificar se e CONDUTOR
class VerificarCondutorView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request, *args, **kwargs):
        usuario = request.user  

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=usuario)
            return Response({'is_admin': True}, status=200)
        except ObjectDoesNotExist:
            return Response({'is_admin': False}, status=200)


# Função Verificar se e PASSAGEIRO
class VerificarPassageiroView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request, *args, **kwargs):
        usuario = request.user  

        try:
            passageiro = Passageiro.objects.get(utilizadorid_utilizador=usuario)
            return Response({'is_admin': True}, status=200)
        except ObjectDoesNotExist:
            return Response({'is_admin': False}, status=200)


# Função Atualizar dados pessoais do Utilizador
class AtualizarDadosPessoaisView(APIView):
    permission_classes = [IsAuthenticated]  

    def put(self, request, *args, **kwargs):
        usuario = request.user  

        serializer = AtualizarDadosPessoaisSerializer(usuario, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Dados pessoais atualizados com sucesso."}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CRUD Contactos
class ContactoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = ContactoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Contacto adicionado com successo", safe=False)
        return JsonResponse("Falha ao adicionar contacto", safe=False)

    def get_contacto(self, pk):
        try:
            student = Contacto.objects.get(id_contacto=pk)
            return student
        except Contacto.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_contacto(pk)
            serializer = ContactoSerializer(data)
        else:
            data = Contacto.objects.all()
            serializer = ContactoSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        contacto_to_update = Contacto.objects.get(id_contacto=pk)
        serializer = ContactoSerializer(
            instance=contacto_to_update, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Contacto atualizado com Sucesso", safe=False)
        return JsonResponse("Falha ao atualizar Contacto")

    def delete(self, request, pk):
        contacto_to_delete = Contacto.objects.get(id_contacto=pk)
        contacto_to_delete.delete()
        return JsonResponse("Contacto deletado com sucesso", safe=False)


# CRUD Tipo Contactos
class TipoContactoView(APIView):
    permission_classes = [IsAuthenticated]

    def get_tipo_contacto(self, pk):
        try:
            tipo_contacto = TipoContacto.objects.get(id_contacto=pk)
            return tipo_contacto
        except TipoContacto.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_tipo_contacto(pk)
            serializer = TipoContactoSerializer(data)
        else:
            data = TipoContacto.objects.all()
            serializer = TipoContactoSerializer(data, many=True)
        return Response(serializer.data)


# CRUD Grupos
class GrupoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = GrupoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Grupo adicionado com successo", safe=False)
        return JsonResponse("Falha ao adicionar grupo", safe=False)

    def get_grupo(self, pk):
        try:
            grupo = Grupo.objects.get(id_grupo=pk)
            return grupo
        except Grupo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_grupo(pk)
            serializer = GrupoSerializer(data)
        else:
            data = Grupo.objects.all()
            serializer = GrupoSerializer(data, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        grupo_to_delete = Grupo.objects.get(id_grupo=pk)
        grupo_to_delete.delete()
        return JsonResponse("Grupo deletado com sucesso", safe=False)


# CRUD Morada
class MoradaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = MoradaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Morada adicionada com successo", safe=False)
        return JsonResponse("Falha ao adicionar Morada", safe=False)

    def get_morada(self, pk):
        try:
            morada = Morada.objects.get(id_morada=pk)
            return grupo
        except Morada.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_morada(pk)
            serializer = MoradaSerializer(data)
        else:
            data = Morada.objects.all()
            serializer = MoradaSerializer(data, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        morada_to_delete = Morada.objects.get(id_morada=pk)
        morada_to_delete.delete()
        return JsonResponse("Morada deletada com sucesso", safe=False)


# CRUD Freguesia
class FreguesiaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = FreguesiaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Freguesia adicionada com successo", safe=False)
        return JsonResponse("Falha ao adicionar Freguesia", safe=False)

    def get_freguesia(self, pk):
        try:
            grupo = Freguesia.objects.get(id_freguesia=pk)
            return freguesia
        except Freguesia.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_freguesia(pk)
            serializer = FreguesiaSerializer(data)
        else:
            data = Freguesia.objects.all()
            serializer = FreguesiaSerializer(data, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        freguesia_to_delete = Freguesia.objects.get(id_freguesia=pk)
        freguesia_to_delete.delete()
        return JsonResponse("Grupo deletado com sucesso", safe=False)


# CRUD Conselho
class ConselhoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = ConselhoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Conselho adicionado com successo", safe=False)
        return JsonResponse("Falha ao adicionar Conselho", safe=False)

    def get_conselho(self, pk):
        try:
            conselho = Conselho.objects.get(id_conselho=pk)
            return conselho
        except Conselho.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_conselho(pk)
            serializer = ConselhoSerializer(data)
        else:
            data = Conselho.objects.all()
            serializer = ConselhoSerializer(data, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        conselho_to_delete = Conselho.objects.get(id_grupo=pk)
        conselho_to_delete.delete()
        return JsonResponse("Conselho deletado com sucesso", safe=False)


# CRUD Distrito
class DistritoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = DistritoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Distrito adicionado com successo", safe=False)
        return JsonResponse("Falha ao adicionar distrito", safe=False)

    def get_distrito(self, pk):
        try:
            distrito = Distrito.objects.get(id_distrito=pk)
            return distrito
        except Distrito.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_distrito(pk)
            serializer = DistritoSerializer(data)
        else:
            data = Distrito.objects.all()
            serializer = DistritoSerializer(data, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        distrito_to_delete = Distrito.objects.get(id_distrito=pk)
        distrito_to_delete.delete()
        return JsonResponse("Distrito deletado com sucesso", safe=False)


# CRUD Pais
class PaisView(APIView):
    permission_classes = [IsAuthenticated]

    def get_pais(self, pk):
        try:
            pais = Pais.objects.get(id_pais=pk)
            return pais
        except Pais.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_pais(pk)
            serializer = GrupoPais(data)
        else:
            data = Pais.objects.all()
            serializer = GrupoSerializer(data, many=True)
        return Response(serializer.data)


# CRUD Nacionalidade
class NacionalidadeView(APIView):
    permission_classes = [IsAuthenticated]

    def get_nacionalidade(self, pk):
        try:
            nacionalidade = Nacionalidade.objects.get(id_nacionalidade=pk)
            return grupo
        except Nacionalidade.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_nacionalidade(pk)
            serializer = NacionalidadeSerializer(data)
        else:
            data = Nacionalidade.objects.all()
            serializer = NacionalidadeSerializer(data, many=True)
        return Response(serializer.data)


