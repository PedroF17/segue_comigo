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
from django.shortcuts import get_object_or_404

from projeto.models import *
from .serializers import *
from autenticacao.views import *


"""
OCORRENCIA - CRUD da Ocorrencia

    [POST]
        Headers:
        Authorization Bearer (access token)

        Body:
        descricao (input)
        viagemid_viagem (input)
        tipo_ocorrenciaid_tipo_ocorrencia (input)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [PUT]
        Headers: 
        Authorization Bearer (access token) 

        Body:
        descricao (input)
        tipo_ocorrenciaid_tipo_ocorrencia (input)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

    [GET]
        Headers:
        Authorization Bearer (access token)

    [PUT] "Admin"
        Headers: 
        Authorization Bearer (access token)


"""

class OcorrenciaView(APIView):
    permission_classes = [IsAuthenticated]


    def post(self, request, pk=None):
        if pk:
            # Either handle the PK case or reject it
            return Response({'error': 'Use PUT for updates'}, status=405)

        user = request.user

        descricao = request.data.get('descricao')
        id_viagem = request.data.get('viagemid_viagem')
        id_tipo_ocorrencia = request.data.get('tipo_ocorrenciaid_tipo_ocorrencia')

        if not (descricao and id_viagem and id_tipo_ocorrencia):
            return Response({'error': 'Campos obrigatórios faltando.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            viagem = Viagem.objects.get(id_viagem=id_viagem)
            tipo_ocorrencia = TipoOcorrencia.objects.get(id_tipo_ocorrencia=id_tipo_ocorrencia)
        except (Viagem.DoesNotExist, TipoOcorrencia.DoesNotExist):
            return Response({'error': 'Viagem ou Tipo de Ocorrência inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)
        except Utilizador.DoesNotExist:
            return Response({'error': 'Utilizador não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            administrador = Administrador.objects.get(id_administrador=1)
        except Administrador.DoesNotExist:
            return Response({'error': 'Administrador padrão não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        ocorrencia = Ocorrencia.objects.create(
            descricao=descricao,
            data_envio=timezone.now().date(),
            data_lida=None,
            viagemid_viagem=viagem,
            utilizadorid_utilizador=utilizador,
            administradorid_administrador=administrador,
            tipo_ocorrenciaid_tipo_ocorrencia=tipo_ocorrencia
        )

        serializer = CreateOcorrenciaSerializer(ocorrencia)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        user = request.user

        ocorrencias = Ocorrencia.objects.filter(utilizadorid_utilizador=user)

        if not ocorrencias.exists():
            return Response({'error': 'Nenhuma ocorrência encontrada para este utilizador.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OcorrenciaSerializer(ocorrencias, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = request.user

        try:
            ocorrencia = Ocorrencia.objects.get(id_ocorrencia=pk)
        except Ocorrencia.DoesNotExist:
            return Response({'error': 'Ocorrência não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        if ocorrencia.utilizadorid_utilizador.id_utilizador != user.id_utilizador:
            return Response({'error': 'Você não tem permissão para editar esta ocorrência.'}, status=status.HTTP_403_FORBIDDEN)

        # Se id_administrador for igual a 1, então nenhum admin leu a ocorrencia
        if ocorrencia.administradorid_administrador.id_administrador == 1:
            return Response({'error': 'Não é permitido editar uma ocorrência com o administrador com ID 1.'}, status=status.HTTP_403_FORBIDDEN)

        descricao = request.data.get('descricao')
        tipo_ocorrenciaid_tipo_ocorrencia = request.data.get('tipo_ocorrenciaid_tipo_ocorrencia')

        if not (descricao or tipo_ocorrenciaid_tipo_ocorrencia):
            return Response({'error': 'Pelo menos um campo (descricao ou tipo_ocorrenciaid_tipo_ocorrencia) deve ser fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

        if descricao:
            ocorrencia.descricao = descricao
        if tipo_ocorrenciaid_tipo_ocorrencia:
            try:
                tipo_ocorrencia = TipoOcorrencia.objects.get(id_tipo_ocorrencia=tipo_ocorrenciaid_tipo_ocorrencia)
                ocorrencia.tipo_ocorrenciaid_tipo_ocorrencia = tipo_ocorrencia
            except TipoOcorrencia.DoesNotExist:
                return Response({'error': 'Tipo de Ocorrência inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        ocorrencia.save()

        serializer = OcorrenciaSerializer(ocorrencia)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user

        try:
            ocorrencia = Ocorrencia.objects.get(id_ocorrencia=pk)
        except Ocorrencia.DoesNotExist:
            return Response({'error': 'Ocorrência não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        if ocorrencia.utilizadorid_utilizador.id_utilizador != user.id_utilizador:
            return Response({'error': 'Você não tem permissão para excluir esta ocorrência.'}, status=status.HTTP_403_FORBIDDEN)

        if ocorrencia.administradorid_administrador.id_administrador != 1:
            return Response({'error': 'Você não tem permissão para excluir esta ocorrência porque o administrador associado não tem o ID igual a 1.'}, status=status.HTTP_403_FORBIDDEN)

        ocorrencia.delete()

        return Response({'message': 'Ocorrência deletada com sucesso.'}, status=status.HTTP_204_NO_CONTENT)


# Validar ocorrência (Para Administradores)
class AdminOcorrenciaView(APIView):
    permission_classes = [IsAuthenticated]


    def get_ocorrencia(self, pk):
        try:
            ocorrencia = Ocorrencia.objects.get(id_ocorrencia=pk)
            return ocorrencia
        except Ocorrencia.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        user = request.user
        if not CheckAdminView.check_admin(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        if pk:
            data = self.get_ocorrencia(pk)
            serializer = OcorrenciaSerializer(data)
        else:
            data = Ocorrencia.objects.all()
            serializer = OcorrenciaSerializer(data, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        user = request.user
        if not CheckAdminView.check_admin(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            ocorrencia = Ocorrencia.objects.get(id_ocorrencia=pk)
        except Ocorrencia.DoesNotExist:
            return Response({'error': 'Ocorrência não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        if ocorrencia.utilizadorid_utilizador.id_utilizador != user.id_utilizador:
            return Response({'error': 'Você não tem permissão para editar esta ocorrência.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            administrador = Administrador.objects.get(utilizadorid_utilizador=user)
        except Administrador.DoesNotExist:
            return Response({'error': 'Administrador associado ao utilizador não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        ocorrencia.data_lida = timezone.now().date()  # Data de hoje
        ocorrencia.administradorid_administrador = administrador

        ocorrencia.save()

        serializer = OcorrenciaSerializer(ocorrencia)
        return Response(serializer.data, status=status.HTTP_200_OK)


"""
TIPO_OCORRENCIA - Listar Tipos de Ocorrencia 
 
    [GET]

"""
class TipoOcorrenciaView(APIView):
    

    def get_tipo_ocorrencia(self, pk):
        try:
            tipo_ocorrencia = TipoOcorrencia.objects.get(id_tipo_ocorrencia=pk)
            return tipo_ocorrencia
        except TipoOcorrencia.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):

        if pk:
            data = self.get_tipo_ocorrencia(pk)
            serializer = TipoOcorrenciaSerializer(data)
        else:
            data = TipoOcorrencia.objects.all()
            serializer = TipoOcorrenciaSerializer(data, many=True)
        return Response(serializer.data)


"""
ALERTA - Funcionalidade de Alerta

    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        descricao (input)
        utilizadorid_utilizador (input)
        tipo_alertaid_tipoalerta (input)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [GET] "Utilizador"
        Headers: 
        Authorization Bearer (access token)

"""

class AlertaView(APIView):
    permission_classes = [IsAuthenticated]

    # Criar alerta, função exclusiva para Admin
    def post(self, request, pk=None):
        user = request.user  
        if not CheckAdminView.check_admin(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            administrador = Administrador.objects.get(utilizadorid_utilizador=user)
        except Administrador.DoesNotExist:
            return Response({'error': 'Erro ao obter dados admin associados.'}, status=status.HTTP_403_FORBIDDEN)

        descricao = request.data.get('descricao')
        id_utilizador_destino = request.data.get('utilizadorid_utilizador')
        id_tipo_alerta = request.data.get('tipo_alertaid_tipoalerta')

        if not (descricao and id_utilizador_destino and id_tipo_alerta):
            return Response({'error': 'Campos obrigatórios faltando.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            utilizador_destino = Utilizador.objects.get(id_utilizador=id_utilizador_destino)
            tipo_alerta = TipoAlerta.objects.get(id_tipo_alerta=id_tipo_alerta)
        except (Utilizador.DoesNotExist, TipoAlerta.DoesNotExist):
            return Response({'error': 'Utilizador destino ou Tipo de Alerta inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        alerta = Alerta.objects.create(
            descricao=descricao,
            utilizadorid_utilizador=utilizador_destino,
            administradorid_administrador=administrador,
            tipo_alertaid_tipo_alerta=tipo_alerta
        )

        serializer = CreateAlertaSerializer(alerta)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def alerta_interno(descricao, id_utilizador_destino, id_tipo_alerta):
        try:
            #Administrador com id=1 corresponde ao SISTEMA
            administrador = Administrador.objects.get(id_administrador=1)
        except Administrador.DoesNotExist:
            raise ValueError("Administrador com id=1 não encontrado.")

        utilizador_destino = get_object_or_404(Utilizador, id_utilizador=id_utilizador_destino)
        tipo_alerta = get_object_or_404(TipoAlerta, id_tipo_alerta=id_tipo_alerta)

        alerta = Alerta.objects.create(
            descricao=descricao,
            utilizadorid_utilizador=utilizador_destino,
            administradorid_administrador=administrador,
            tipo_alertaid_tipo_alerta=tipo_alerta
        )

        return alerta

    def get_alerta(self, pk):
        try:
            alerta = Alerta.objects.get(id_alerta=pk)
            return alerta
        except Alerta.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        user = request.user
        if not CheckAdminView.check_admin(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)
        except Utilizador.DoesNotExist:
            return Response({'error': 'Utilizador não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if pk:
            alerta = Alerta.objects.filter(pk=pk, utilizadorid_utilizador=utilizador).first()
            if not alerta:
                return Response({'error': 'Alerta não encontrado ou não pertence a este utilizador.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = AlertaSerializer(alerta)
        else:
            alertas = Alerta.objects.filter(utilizadorid_utilizador=utilizador)
            serializer = AlertaSerializer(alertas, many=True)

        return Response(serializer.data)


    def get(self, request, pk=None):
        if pk:
            data = self.get_alerta(pk)
            serializer = AlertaSerializer(data)
        else:
            data = Alerta.objects.all()
            serializer = AlertaSerializer(data, many=True)
        return Response(serializer.data)


# Listar alertas do utilizador logado
class UtilizadorAlertaView(APIView):
    permission_classes = [IsAuthenticated]

    def get_alerta(self, pk):
        try:
            alerta = Alerta.objects.get(id_alerta=pk)
            return alerta
        except Alerta.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        user = request.user  # Utilizador logado

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)
        except Utilizador.DoesNotExist:
            return Response({'error': 'Utilizador não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if pk:
            # Buscar um alerta específico, mas somente se for do próprio utilizador
            alerta = Alerta.objects.filter(pk=pk, utilizadorid_utilizador=utilizador).first()
            if not alerta:
                return Response({'error': 'Alerta não encontrado ou não pertence a este utilizador.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = AlertaSerializer(alerta)
        else:
            # Buscar todos os alertas do utilizador
            alertas = Alerta.objects.filter(utilizadorid_utilizador=utilizador)
            serializer = AlertaSerializer(alertas, many=True)

        return Response(serializer.data)

    # Marcar Alertas como Lidos (Utilizador)
    def put(self, request):
        utilizador = request.user

        try:
            alertas_para_atualizar = Alerta.objects.filter(
                utilizadorid_utilizador=utilizador,
                tipo_alertaid_tipo_alerta__id_tipo_alerta=1
            )

            if not alertas_para_atualizar.exists():
                return Response(
                    {"mensagem": "Nenhum alerta com tipo 1 encontrado para este utilizador."},
                    status=status.HTTP_204_NO_CONTENT
                )

            novo_tipo_alerta = TipoAlerta.objects.get(id_tipo_alerta=2)

            alertas_para_atualizar.update(tipo_alertaid_tipo_alerta=novo_tipo_alerta)

            return Response(
                {
                    "mensagem": f"{alertas_para_atualizar.count()} alerta(s) atualizado(s) com sucesso para o tipo 2."
                },
                status=status.HTTP_200_OK
            )

        except TipoAlerta.DoesNotExist:
            return Response({"erro": "Tipo de alerta com ID 2 não existe."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"erro": f"Ocorreu um erro: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Contar o numero de alertas com status 1 do utilizador (alertas nao lidos)
class UtilizadorContarAlertaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        count = Alerta.objects.filter(
            utilizadorid_utilizador=user,
            tipo_alertaid_tipo_alerta__id_tipo_alerta=1
        ).count()

        return Response({count})


"""
TIPO_ALERTA - Listar Tipos de Alerta
 
    [GET]

"""
class TipoAlertaView(APIView):
    

    def get_tipo_alerta(self, pk):
        try:
            tipo_alerta = TipoAlerta.objects.get(id_tipo_alerta=pk)
            return tipo_alerta
        except TipoAlerta.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):

        if pk:
            data = self.get_tipo_alerta(pk)
            serializer = TipoAlertaSerializer(data)
        else:
            data = TipoAlerta.objects.all()
            serializer = TipoAlertaSerializer(data, many=True)
        return Response(serializer.data)


"""
CHAT_VIAGEM - Criar Chat_Viagem

    [POST]

    [GEŦ]

    [DELETE]


"""

# Listar alertas do utilizador logado
class ChatViagemView(APIView):
    permission_classes = [IsAuthenticated]

    # Criar chat_viagem (para sistema)
    def criar_chat_viagem(viagem_id):
        try:
            # Verifica se a viagem existe
            viagem = Viagem.objects.get(id_viagem=viagem_id)

            # Cria o novo chat para a viagem
            novo_chat_viagem = ChatViagem.objects.create(viagemid_viagem=viagem)

            # Retorna o chat criado
            return novo_chat_viagem

        except Viagem.DoesNotExist:
            raise ValueError("Viagem não encontrada.")
        except Exception as e:
            raise ValueError(f"Erro ao criar o ChatViagem: {str(e)}")

    # Deletar chat_viagem (para sistema)
    def deletar_chat_viagem(chat_viagem_id):
        try:
            # Verifica se o ChatViagem existe
            chat_viagem = ChatViagem.objects.get(id_chat_viagem=chat_viagem_id)

            # Deleta o ChatViagem
            chat_viagem.delete()

            return f"ChatViagem com ID {chat_viagem_id} deletado com sucesso."

        except ChatViagem.DoesNotExist:
            raise ValueError("ChatViagem não encontrado.")
        except Exception as e:
            raise ValueError(f"Erro ao deletar o ChatViagem: {str(e)}")


"""
MENSAGEM - Criar Chat_Viagem

    [POST]

    [GEŦ]

    [PUT]

    [DELETE]

    [PUT] "Read"


"""
"""
class MensagemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        valor = request.data.get('valor')
        chat_viagem_id = request.data.get('chat_viagemid_chat_viagem')

        if not valor or not chat_viagem_id:
            return Response({'error': 'Campos obrigatórios faltando.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            chat_viagem = ChatViagem.objects.get(id_chat_viagem=chat_viagem_id)
        except ChatViagem.DoesNotExist:
            return Response({'error': 'Chat de viagem não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)
        except Utilizador.DoesNotExist:
            return Response({'error': 'Utilizador não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        mensagem = Mensagem.objects.create(
            valor=valor,
            data_envio=timezone.now().date(),  # Define o dia de hoje
            lida=0,  # Marca a mensagem como não lida
            chat_viagemid_chat_viagem=chat_viagem,  # Relaciona com o ChatViagem
            utilizadorid_utilizador=utilizador  # Relaciona com o utilizador logado
        )

        serializer = MensagemSerializer(mensagem)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
"""
