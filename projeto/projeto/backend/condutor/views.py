import contextlib
from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
import os

from projeto.models import *
from .serializers import *
from autenticacao.views import *


"""
CONDUTOR - CRUD do Condutor

    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        documento_reg_criminal (input file)
        documento_comprov_residencia (input file)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [PUT]
        Headers: 
        Authorization Bearer (access token) 

        Body:
        documento_reg_criminal (input file)
        documento_comprov_residencia (input file)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

"""
class CondutorView(APIView):
    permission_classes = [IsAuthenticated]

    
    def post(self, request):
        user = request.user
        serializer = CondutorCreateSerializer(data=request.data, partial=True)

        total_condutores = Condutor.objects.filter(utilizadorid_utilizador=user).count()

        if serializer.is_valid() and total_condutores == 0:
            serializer.save(
                utilizadorid_utilizador=user,
                data_criacao=timezone.now().date(),
                reputacao=0
            )
            return JsonResponse("Condutor adicionado com sucesso.", safe=False)

        return JsonResponse(serializer.errors, safe=False, status=400)

    def get(self, request):
        user = request.user

        condutores = Condutor.objects.filter(utilizadorid_utilizador=user)
        serializer = CondutorSerializer(condutores, many=True, context={"request": request})
        return Response(serializer.data)

    def put(self, request):
        user = request.user

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CondutorEditSerializer(condutor, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(reputacao=0)
            return Response({
                "mensagem": "Dados atualizados com sucesso.",
                "condutor": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Remove os ficheiros associados
        if condutor.doc_reg_criminal and os.path.isfile(condutor.doc_reg_criminal.path):
            os.remove(condutor.doc_reg_criminal.path)
        if condutor.doc_comprov_residencia and os.path.isfile(condutor.doc_comprov_residencia.path):
            os.remove(condutor.doc_comprov_residencia.path)

        condutor.delete()
        return JsonResponse("Condutor deletado com sucesso.", safe=False)


"""
VEICULO e CONDUTOR_VEICULO - CRUD do Veículo
 
    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        matricula (input)
        data_criacao (input)
        tipoveiculo_id_tipo_veiculo (input)
        cor_veiculoid_cor_veiculo (input)
        modelo_veiculoid_modelo_veiculo (input)
        documento_arquivo (input file)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [PUT]
        Headers: 
        Authorization Bearer (access token) 

        Body:
        matricula (input)
        data_criacao (input)
        tipoveiculo_id_tipo_veiculo (input)
        cor_veiculoid_cor_veiculo (input)
        modelo_veiculoid_modelo_veiculo (input)
        documento_arquivo (input file)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

    [GET] "Condutor"
        Headers: 
        Authorization Bearer (access token)

"""

class VeiculoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        veiculo_serializer = CreateVeiculoSerializer(data=request.data)

        if veiculo_serializer.is_valid():
            veiculo = veiculo_serializer.save(ativo=0)
        else:
            return JsonResponse(veiculo_serializer.errors, safe=False, status=400)

        condutor_veiculo_data = {
            "documento_arquivo": request.data.get("documento_arquivo", ""),
            "data_emissao": request.data.get("data_emissao", None),
            "data_validade": request.data.get("data_validade", None),
            "condutorid_condutor": condutor.id_condutor,
            "veiculoid_veiculo": veiculo.id_veiculo,
        }

        condutor_veiculo_serializer = CreateCondutorVeiculoSerializer(data=condutor_veiculo_data)

        if condutor_veiculo_serializer.is_valid():
            condutor_veiculo_serializer.save(data_emissao=timezone.now().date(),data_validade=timezone.now().date() + timedelta(days=365))
            return JsonResponse("Veículo e vínculo Condutor-Veículo criados com sucesso.", safe=False)
        else:
            veiculo.delete()
            return JsonResponse(condutor_veiculo_serializer.errors, safe=False, status=400)

    def get(self, request):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        grupo = user.grupoid_grupo

        utilizadores_do_grupo = Utilizador.objects.filter(grupoid_grupo=grupo)

        condutores = Condutor.objects.filter(utilizadorid_utilizador__in=utilizadores_do_grupo)

        condutor_veiculos = CondutorVeiculo.objects.filter(condutorid_condutor__in=condutores)

        serializer = CondutorVeiculoSerializer(condutor_veiculos, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor_veiculo = CondutorVeiculo.objects.get(
                id_condutor_veiculo=pk,
                condutorid_condutor=condutor
            )
        except CondutorVeiculo.DoesNotExist:
            return Response({
                "erro": "CondutorVeiculo não pertence ao condutor autenticado."
            }, status=status.HTTP_403_FORBIDDEN)

        veiculo = Veiculo.objects.get(id_veiculo=condutor_veiculo.id_condutor_veiculo)

        serializer_veiculo = CreateVeiculoSerializer(veiculo, data=request.data, partial=True)
        serializer_condutor_veiculo = EditCondutorVeiculoSerializer(condutor_veiculo, data=request.data, partial=True)

        if serializer_veiculo.is_valid() & serializer_condutor_veiculo.is_valid():
            serializer_veiculo.save()
            serializer_condutor_veiculo.save(
                condutorid_condutor=condutor,
                veiculoid_veiculo=veiculo
            )
            return Response({
                "mensagem": "Dados atualizados com sucesso.",
                "condutor_veiculo": serializer_condutor_veiculo.data,
                "veiculo": serializer_veiculo.data
            }, status=status.HTTP_200_OK)

        return Response({
            "condutor_veiculo_errors": serializer_condutor_veiculo.errors,
            "veiculo_errors": serializer_veiculo.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor_veiculo = CondutorVeiculo.objects.get(id_condutor_veiculo=pk, condutorid_condutor=condutor)
        except CondutorVeiculo.DoesNotExist:
            return Response({"erro": "CondutorVeiculo não encontrado ou não pertence ao condutor autenticado."}, status=status.HTTP_403_FORBIDDEN)

        veiculo = condutor_veiculo.veiculoid_veiculo

        condutor_veiculo.delete()

        condutor_veiculos_restantes = CondutorVeiculo.objects.filter(veiculoid_veiculo=veiculo).exists()

        if not condutor_veiculos_restantes:
            veiculo.delete()
            return Response({
                "mensagem": "CondutorVeiculo e veículo associados foram deletados com sucesso."
            }, status=status.HTTP_200_OK)

        return Response({
            "mensagem": "CondutorVeiculo deletado com sucesso. O veículo ainda está associado a outros condutores."
        }, status=status.HTTP_200_OK)
    

class CondutorVeiculoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        condutor_veiculos = CondutorVeiculo.objects.filter(condutorid_condutor=condutor)

        serializer = CondutorVeiculoSerializer(condutor_veiculos, many=True, context={"request": request})
        return Response(serializer.data, status=200)


"""
VEICULO e CONDUTOR_VEICULO - Associar Condutor a um Veículo
 

    [POST]
        Headers: 
        Authorization Bearer (access token) 

"""
class AssociarCondutorVeiculoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor não encontrado para o utilizador logado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            veiculo = Veiculo.objects.get(id_veiculo=pk)
        except Veiculo.DoesNotExist:
            return Response({"erro": "Veículo não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        existe_associacao = CondutorVeiculo.objects.filter(condutorid_condutor=condutor, veiculoid_veiculo=veiculo).exists()
        if existe_associacao:
            return Response({"erro": "Este condutor já está associado a este veículo."}, status=status.HTTP_400_BAD_REQUEST)

        condutor_veiculo = CondutorVeiculo.objects.create(
            condutorid_condutor=condutor,
            veiculoid_veiculo=veiculo,
            data_emissao=timezone.now().date(),
            data_validade=timezone.now().date(),
            documento_arquivo=None
        )

        return Response({
            "mensagem": "Condutor associado com sucesso ao veículo.",
            "id_condutor_veiculo": condutor_veiculo.id_condutor_veiculo
        }, status=status.HTTP_201_CREATED)


"""
MARCA_VEICULO - Listar Marcas de Veículo
 
    [GET]

"""
class MarcaVeiculoView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get_marca_veiculo(self, pk):
        try:
            marca_veiculo = MarcaVeiculo.objects.get(id_marca_veiculo=pk)
            return marca_veiculo
        except MarcaVeiculo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        if pk:
            data = self.get_marca_veiculo(pk)
            serializer = MarcaVeiculoSerializer(data)
        else:
            data = MarcaVeiculo.objects.all()
            serializer = MarcaVeiculoSerializer(data, many=True)
        return Response(serializer.data)


"""
MARCA_VEICULO - Alterar Status do Veiculo
 
    [PUT]

"""
class EstadoVeiculoView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        if not CheckAdminView.check_admin(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            veiculo = Veiculo.objects.get(id_veiculo=pk)
        except Veiculo.DoesNotExist:
            return Response({"erro": "Veículo não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Alterna valor do campo ativo
        veiculo.ativo = 0 if veiculo.ativo == 1 else 1
        veiculo.save()

        return Response({
            "mensagem": "Estado do veículo atualizado com sucesso.",
            "id_veiculo": veiculo.id_veiculo,
            "ativo": veiculo.ativo
        }, status=status.HTTP_200_OK)


"""
COR_VEICULO - Listar Cores de Veículo
 
    [GET]

"""
class CorVeiculoView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get_cor_veiculo(self, pk):
        try:
            cor_veiculo = CorVeiculo.objects.get(id_cor_veiculo=pk)
            return cor_veiculo
        except CorVeiculo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        if pk:
            data = self.get_cor_veiculo(pk)
            serializer = CorVeiculoSerializer(data)
        else:
            data = CorVeiculo.objects.all()
            serializer = CorVeiculoSerializer(data, many=True)
        return Response(serializer.data)


"""
TIPO_VEICULO - Listar Tipos de Veículo
 
    [GET]

"""
class TipoVeiculoView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get_tipo_veiculo(self, pk):
        try:
            tipo_veiculo = TipoVeiculo.objects.get(id_tipo_veiculo=pk)
            return tipo_veiculo
        except TipoVeiculo.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        if pk:
            data = self.get_tipo_veiculo(pk)
            serializer = TipoVeiculoSerializer(data)
        else:
            data = TipoVeiculo.objects.all()
            serializer = TipoVeiculoSerializer(data, many=True)
        return Response(serializer.data)


"""
TIPO_CATEGORIA - Listar Tipos de Categoria
 
    [GET]

"""
class TipoCategoriaView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get_tipo_categoria(self, pk):
        try:
            tipo_categoria = TipoCategoria.objects.get(id_tipo_categoria=pk)
            return tipo_categoria
        except TipoCategoria.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        if pk:
            data = self.get_tipo_categoria(pk)
            serializer = TipoCategoriaSerializer(data)
        else:
            data = TipoCategoria.objects.all()
            serializer = TipoCategoriaSerializer(data, many=True)
        return Response(serializer.data)
