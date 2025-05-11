from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from comunicacao.views import *
from projeto.models import *

User = get_user_model()

class OcorrenciaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)


        self.tipo_ocorrencia = TipoOcorrencia.objects.create(id_tipo_ocorrencia=1, descricao="Avaliacao")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Teste")
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.administrador2 = Administrador.objects.create(id_administrador=2, utilizadorid_utilizador=self.user) # put n aceita id_administrador=1
        self.viagem = Viagem.objects.create(
                                id_viagem=1,
                                status_viagemid_status_viagem=self.status_viagem,
                                condutorid_condutor=self.condutor
                            )
        self.ocorrencia = Ocorrencia.objects.create(
                                id_ocorrencia=1,
                                descricao="teste",
                                data_envio="2025-01-01",
                                data_lida="2025-01-01",
                                viagemid_viagem=self.viagem,
                                utilizadorid_utilizador=self.user,
                                administradorid_administrador=self.administrador2,
                                tipo_ocorrenciaid_tipo_ocorrencia=self.tipo_ocorrencia
                            )

        self.ocorrencia2 = Ocorrencia.objects.create(
                                id_ocorrencia=2,
                                descricao="teste",
                                data_envio="2025-01-01",
                                data_lida="2025-01-01",
                                viagemid_viagem=self.viagem,
                                utilizadorid_utilizador=self.user,
                                administradorid_administrador=self.administrador,
                                tipo_ocorrenciaid_tipo_ocorrencia=self.tipo_ocorrencia
                            )

        self.url = '/comunicacao/ocorrencia/'
        self.url2 = f'/comunicacao/ocorrencia/{self.ocorrencia.pk}/'
        self.url3 = f'/comunicacao/ocorrencia/{self.ocorrencia2.pk}/'

    def test_get_ocorrencia_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_ocorrencia_view(self):
        data = {
            "descricao": "teste",
            "viagemid_viagem": 1,
            "tipo_ocorrenciaid_tipo_ocorrencia": 1
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_ocorrencia_view(self):
        data = {
            "descricao": "teste",
            "viagemid_viagem": 1,
            "tipo_ocorrenciaid_tipo_ocorrencia": 1
        }
        response = self.client.put(self.url2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ocorrencia_view(self):
        response = self.client.delete(self.url3)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TipoOcorrenciaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/comunicacao/tipo_ocorrencia/'

        self.tipo_ocorrencia = TipoOcorrencia.objects.create(id_tipo_ocorrencia=1, descricao="Avaliacao")
        
    def test_get_tipo_ocorrencia_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

