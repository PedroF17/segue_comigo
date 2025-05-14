from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import get_user_model
from django.utils import timezone

import string
import random


from projeto.models import *
from .serializers import *


"""
UTILIZADOR - Criar Utilizador
    
    [POST] "First"
        Body:
        grupo_nome (input)
        nome_primeiro (input)
        nome_ultimo (input)
        data_nasc (input)
        genero (input)
        numero_cc (input)
        estado_civilid_estado_civil (input)
        nacionalidadeid_nacionalidade (input)
        password (input)
        email (input)

    [GET]

    [POST]
        Body:
        nome_primeiro (input)
        nome_ultimo (input)
        data_nasc (input)
        genero (input)
        numero_cc (input)
        grupoid_grupo (input) 
        estado_civilid_estado_civil (input)
        nacionalidadeid_nacionalidade (input) 
        password (input)
        email (input)

    [DELETE]
"""
# Primeira conta criada
class FirstCreateAccountView(APIView):

    def gerar_nome_unico_grupo(self, tamanho=10):
        while True:
            nome_aleatorio = ''.join(random.choices(string.ascii_letters + string.digits, k=tamanho))
            if not Grupo.objects.filter(nome=nome_aleatorio).exists():
                return nome_aleatorio

    def post(self, request):
        nome_unico = self.gerar_nome_unico_grupo()

        novo_grupo = Grupo.objects.create(
            nome=nome_unico,
            data_criacao=timezone.now().date()
        )

        dados_utilizador = request.data.copy()
        dados_utilizador["grupoid_grupo"] = novo_grupo.id_grupo

        serializer = PrimeiroUtilizadorRegistroSerializer(data=dados_utilizador)

        if serializer.is_valid():
            utilizador = serializer.save()
            return Response({
                "mensagem": "Grupo e conta criados com sucesso.",
                "grupo_nome": nome_unico,
                "utilizador": PrimeiroUtilizadorRegistroSerializer(utilizador).data
            }, status=status.HTTP_201_CREATED)

        # Remove grupo se o utilizador não for criado com sucesso
        novo_grupo.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    def post(self, request):
        grupo_nome = request.data.get("grupo_nome")

        if not grupo_nome:
            return Response(
                {"erro": "O campo 'grupo_nome' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        novo_grupo = Grupo.objects.create(
            nome=grupo_nome,
            data_criacao=timezone.now().date()
        )

        dados_utilizador = request.data.copy()
        dados_utilizador["grupoid_grupo"] = novo_grupo.id_grupo

        serializer = PrimeiroUtilizadorRegistroSerializer(data=dados_utilizador)

        if serializer.is_valid():
            utilizador = serializer.save()
            return Response({
                "mensagem": "Grupo e conta criados com sucesso.",
                "utilizador": PrimeiroUtilizadorRegistroSerializer(utilizador).data
            }, status=status.HTTP_201_CREATED)

        novo_grupo.delete()
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """


class CreateAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        grupo = request.user.grupoid_grupo
        utilizadores = Utilizador.objects.filter(grupoid_grupo=grupo)

        resultado = [
            {
                "nome_primeiro": u.nome_primeiro,
                "nome_ultimo": u.nome_ultimo,
                "email": u.email
            }
            for u in utilizadores
        ]

        return Response(resultado, status=status.HTTP_200_OK)

    def post(self, request):
        grupo = request.user.grupoid_grupo

        dados_utilizador = request.data.copy()
        dados_utilizador["grupoid_grupo"] = grupo.id_grupo

        serializer = PrimeiroUtilizadorRegistroSerializer(data=dados_utilizador)

        if serializer.is_valid():
            utilizador = serializer.save()
            return Response({
                "mensagem": "Utilizador criado com sucesso no grupo do utilizador autenticado.",
                "utilizador": PrimeiroUtilizadorRegistroSerializer(utilizador).data
            }, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        utilizador = request.user
        grupo = request.user.grupoid_grupo

        # Verifica quantos utilizadores estão no grupo
        total_utilizadores = Utilizador.objects.filter(grupoid_grupo=grupo).count()

        # Deleta o utilizador
        utilizador.delete()

        # Se era o único, deleta também o grupo
        if total_utilizadores == 1:
            grupo.delete()
            return Response({"mensagem": "Utilizador e grupo associados foram removidos."}, status=status.HTTP_200_OK)

        return Response({"mensagem": "Utilizador removido com sucesso."}, status=status.HTTP_200_OK)


"""
class CreateAccountView(APIView):

    def post(self, request):
        serializer = UtilizadorRegistroSerializer(data=request.data)

        if serializer.is_valid():
            utilizador = serializer.save()

            # Re-serializa para esconder senha e mostrar dados limpos
            response_data = UtilizadorRegistroSerializer(utilizador).data

            return Response({
                "mensagem": "Conta criada com sucesso.",
                "utilizador": response_data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
UTILIZADOR - Alterar Senha

    [POST]
        Headers:
        Authorization Bearer (access token)

        Body:
        old_password (input)
        new_password (input)
        confirm_new_password (input)
"""
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_new_password = request.data.get("confirm_new_password")
        
        if not old_password:
            return Response({"erro": "Senha antiga não fornecida."}, status=status.HTTP_400_BAD_REQUEST)
        if not new_password:
            return Response({"erro": "Nova senha não fornecida."}, status=status.HTTP_400_BAD_REQUEST)
        if new_password != confirm_new_password:
            return Response({"erro": "A nova senha e a confirmação não coincidem."}, status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(old_password):
            return Response({"erro": "Senha antiga incorreta."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({"mensagem": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)


"""
UTILIZADOR - Dados de um Utilizador

    [GET]
        Headers:
        Authorization Bearer (access token) 

    [PUT]
        Headers:
        Authorization Bearer (access token) 

        Body:
        id_utilizador (input)
        nome_primeiro (input)
        nome_ultimo (input)
        data_nasc (input)
        genero (input)
        numero_cc (input)
        data_criacao (input)
        grupoid_grupo (input) (grupo)
        estado_civilid_estado_civil (input)
        nacionalidadeid_nacionalidade (input)
        password (input)
        email (input)
"""
class AccountView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        user = request.user

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)
        except Utilizador.DoesNotExist:
            return Response({"erro": "Utilizador não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UtilizadorRegistroSerializer(utilizador)
        
        return Response({
            "mensagem": "Dados do utilizador recuperados com sucesso.",
            "utilizador": serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)
        except Utilizador.DoesNotExist:
            return Response({"erro": "Utilizador não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UtilizadorRegistroSerializer(utilizador, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "mensagem": "Dados atualizados com sucesso.",
                "utilizador": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
GRUPO - Alterar Dados do Grupo
 
    [PUT]
        Headers: 
        Authorization Bearer (access token) 

        Body:
        id_utilizador (input)
        nome_primeiro (input)
        nome_ultimo (input)
        data_nasc (input)
        genero (input)
        numero_cc (input)
        data_criacao (input)
        grupoid_grupo (input) (grupo)
        estado_civilid_estado_civil (input)
        nacionalidadeid_nacionalidade (input)
        password (input)
        email (input)

"""
class GrupoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        utilizador_autenticado = request.user
        grupo = utilizador_autenticado.grupoid_grupo

        # Filtra apenas os utilizadores que pertencem ao grupo e possuem registro como Passageiro
        utilizadores = Utilizador.objects.filter(
            grupoid_grupo=grupo,
            passageiro__isnull=False
        ).distinct()

        serializer = UtilizadorRegistroSerializer(utilizadores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = [IsAuthenticated]

    def put(self, request):
        utilizador = request.user

        try:
            grupo = Grupo.objects.get(utilizadorid_utilizador=utilizador.id_utilizador)
        except Grupo.DoesNotExist:
            return Response({"erro": "Grupo não encontrado para este utilizador."}, status=status.HTTP_404_NOT_FOUND)

        # Gerar nome aleatório único
        def gerar_nome_unico():
            while True:
                nome = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
                if not Grupo.objects.filter(nome=nome).exists():
                    return nome

        novo_nome = gerar_nome_unico()
        grupo.nome = novo_nome
        grupo.save()

        return Response({"novo_nome_grupo": novo_nome}, status=status.HTTP_200_OK)

    """
    def put(self, request):
        user = request.user

        try:
            utilizador = Utilizador.objects.get(id_utilizador=user.id_utilizador)

            grupo = utilizador.grupoid_grupo
        except Utilizador.DoesNotExist:
            return Response({"erro": "Utilizador não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Grupo.DoesNotExist:
            return Response({"erro": "Grupo associado não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        novo_nome = request.data.get("nome")

        if not novo_nome:
            return Response({"erro": "O campo 'nome' é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        grupo.nome = novo_nome
        grupo.save()

        serializer = GrupoSerializer(grupo)
        return Response({
            "mensagem": "Nome do grupo atualizado com sucesso.",
            "grupo": serializer.data
        }, status=status.HTTP_200_OK)
    """

class CodigoGrupoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        utilizador = request.user

        try:
            grupo = Grupo.objects.get(utilizadorid_utilizador=utilizador.id_utilizador)
        except Grupo.DoesNotExist:
            return Response(
                {"erro": "Grupo associado ao utilizador não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(grupo.nome)

    def put(self, request):
        utilizador = request.user
        grupo_id = request.data.get("grupo_id")

        if not grupo_id:
            return Response(
                {"erro": "O campo 'grupo_id' é obrigatório."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            grupo = Grupo.objects.get(id_grupo=grupo_id)
        except Grupo.DoesNotExist:
            return Response(
                {"erro": "Grupo com o ID fornecido não existe."},
                status=status.HTTP_404_NOT_FOUND
            )

        utilizador.grupoid_grupo = grupo
        utilizador.save()

        return Response(
            {"mensagem": "Grupo atualizado com sucesso."},
            status=status.HTTP_200_OK
        )


"""
CONTACTO - CRUD do Contacto
 
    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        descricao (input)
        tipocontactoid_tipo_contacto (input)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [PUT]
        Headers: 
        Authorization Bearer (access token) 

        Body:
        descricao (input)
        tipocontactoid_tipo_contacto (input)

"""
class ContactoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ContactoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(utilizadorid_utilizador=user)
            return JsonResponse("Contacto adicionado com sucesso.", safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)

    def get_contact(self, user, pk):
        try:
            return Contacto.objects.get(id_contacto=pk, utilizadorid_utilizador=user)
        except Contacto.DoesNotExist:
            raise Http404("Contacto não encontrado.")

    def get(self, request, pk=None):
        user = request.user
        if pk:
            contacto = self.get_contact(user, pk)
            serializer = ContactoShowSerializer(contacto)
        else:
            contactos = Contacto.objects.filter(utilizadorid_utilizador=user)
            serializer = ContactoShowSerializer(contactos, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        user = request.user
        contacto = self.get_contact(user, pk)
        serializer = ContactoSerializer(contacto, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Contacto atualizado com sucesso.", safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)

    def delete(self, request, pk):
        user = request.user
        contacto = self.get_contact(user, pk)
        contacto.delete()
        return JsonResponse("Contacto deletado com sucesso.", safe=False)

"""
MORADA - CRUD da Morada
 
    [DELETE]
        Headers: 
        Authorization Bearer (access token)

    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        descricao (input)
        utilizadorid_utilizador (input)
        freguesiaid_freguesia (input)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [PUT]
        Headers: 
        Authorization Bearer (access token) 

        Body:
        descricao (input)
        utilizadorid_utilizador (input)
        freguesiaid_freguesia (input)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

"""
class MoradaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = MoradaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(utilizadorid_utilizador=user)
            return JsonResponse("Morada adicionada com sucesso.", safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)

    def get_morada(self, user, pk):
        try:
            return Morada.objects.get(id_morada=pk, utilizadorid_utilizador=user)
        except Morada.DoesNotExist:
            raise Http404("Morada não encontrada.")

    def get(self, request, pk=None):
        user = request.user
        if pk:
            morada = self.get_morada(user, pk)
            serializer = MoradaShowSerializer(morada)
        else:
            moradas = Morada.objects.filter(utilizadorid_utilizador=user)
            serializer = MoradaShowSerializer(moradas, many=True)
        return Response(serializer.data)

    def put(self, request, pk=None):
        user = request.user
        morada = self.get_morada(user, pk)
        serializer = MoradaSerializer(morada, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Morada atualizada com sucesso.", safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)

    def delete(self, request, pk):
        user = request.user
        morada = self.get_morada(user, pk)
        morada.delete()
        return JsonResponse("Morada deletada com sucesso.", safe=False)


"""
TIPO_CONTACTO - Listar Tipos de Contactos
 
    [GET]

"""
class TipoContactoView(APIView):

    def get_tipo_contacto(self, pk):
        try:
            tipo_contacto = TipoContacto.objects.get(id_tipo_contacto=pk)
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


"""
ESTADO_CIVIL - Listar Tipos de Estados Civis
 
    [GET]

"""
class EstadoCivilView(APIView):

    def get_estado_civil(self, pk):
        try:
            estado_civil = EstadoCivil.objects.get(id_estado_civil=pk)
            return estado_civil
        except EstadoCivil.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_estado_civil(pk)
            serializer = EstadoCivilSerializer(data)
        else:
            data = EstadoCivil.objects.all()
            serializer = EstadoCivilSerializer(data, many=True)
        return Response(serializer.data)


"""
NACIONALIDADE - Listar Nacionalidades
 
    [GET]

"""
class NacionalidadeView(APIView):

    def get_nacionalidade(self, pk):
        try:
            pais = Nacionalidade.objects.get(id_nacionalidade=pk)
            return pais
        except Nacionalidade.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_pais(pk)
            serializer = NacionalidadeSerializer(data)
        else:
            data = Nacionalidade.objects.all()
            serializer = NacionalidadeSerializer(data, many=True)
        return Response(serializer.data)


"""
PAIS - Listar Paises
 
    [GET]

"""
class PaisView(APIView):

    def get_pais(self, pk):
        try:
            pais = Pais.objects.get(id_pais=pk)
            return pais
        except Pais.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_pais(pk)
            serializer = PaisSerializer(data)
        else:
            data = Pais.objects.all()
            serializer = PaisSerializer(data, many=True)
        return Response(serializer.data)


"""
DISTRITO - Listar Distritos
 
    [GET]

"""
class DistritoView(APIView):

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


"""
CONSELHO - Listar Conselhos
 
    [GET]

"""
class ConselhoView(APIView):

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


"""
FREGUESIA - Listar Freguesias
 
    [GET]

"""
class FreguesiaView(APIView):

    def get_freguesia(self, pk):
        try:
            freguesia = Freguesia.objects.get(id_freguesia=pk)
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


"""
ADMINISTRADOR - Verificar se é Admin
 
    [GET]
        Headers: 
        Authorization Bearer (access token) 

"""
class CheckAdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        utilizador = request.user

        eh_admin = Administrador.objects.filter(utilizadorid_utilizador=utilizador).exists()

        return Response({'is_admin': eh_admin}, status=status.HTTP_200_OK)

    def check_admin(user):
        return Administrador.objects.filter(utilizadorid_utilizador=user).exists()


"""
CONDUTOR - Verificar se é Condutor
 
    [GET]
        Headers: 
        Authorization Bearer (access token) 

"""
class CheckCondutorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        utilizador = request.user

        eh_condutor = Condutor.objects.filter(utilizadorid_utilizador=utilizador).exists()

        return Response({'is_condutor': eh_condutor}, status=status.HTTP_200_OK)

    def check_condutor(user):
        return Condutor.objects.filter(utilizadorid_utilizador=user).exists()


"""
PASSAGEIRO - Verificar se é Passageiro
 
    [GET]
        Headers: 
        Authorization Bearer (access token) 

"""
class CheckPassageiroView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        utilizador = request.user

        eh_passageiro = Passageiro.objects.filter(utilizadorid_utilizador=utilizador).exists()

        return Response({'is_passageiro': eh_passageiro}, status=status.HTTP_200_OK)

    def check_passageiro(user):
        return Passageiro.objects.filter(utilizadorid_utilizador=user).exists()
