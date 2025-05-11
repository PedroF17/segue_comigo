from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from autenticacao.views import *
from projeto.models import *

User = get_user_model()

class FirstCreateAccountViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/create_first/'
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1, paisid_pais=self.pais)

    def test_post_first_create_account(self):
        data = {
            "grupo_nome": "Test Group",
            "nome_primeiro": "John",
            "nome_ultimo": "Doe",
            "data_nasc": "1990-01-01",
            "genero": "M",
            "numero_cc": "123456789",
            "estado_civilid_estado_civil": 1,
            "nacionalidadeid_nacionalidade": 1,
            "password": "password123",
            "email": "john.doe@example.com"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class CreateAccountViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/create/'
        
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

    def test_get_create_account(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_post_create_account(self):
        data = {
            "nome_primeiro": "Jane",
            "nome_ultimo": "Doe",
            "data_nasc": "1995-05-05",
            "genero": "F",
            "numero_cc": "987654321",
            "estado_civilid_estado_civil": 1,
            "nacionalidadeid_nacionalidade": 1,
            "password": "password123",
            "email": "jane.doe@example.com",
            "data_criacao": "1995-05-05",
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_delete_create_account(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

"""
class ChangePasswordViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/new_password/'
        
        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="oldpassword123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)

    def test_post_change_password(self):
        data = {
            "old_password": "oldpassword123",
            "new_password": "newpassword123",
            "confirm_new_password": "newpassword123"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""


class AccountViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/view/'

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

    def test_get_account_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_account_view(self):
        data = {
            "nome_primeiro": "Jane",
            "nome_ultimo": "Doe",
            "data_nasc": "1995-05-05",
            "genero": "F",
            "numero_cc": "987654321",
            "estado_civilid_estado_civil": 1,
            "nacionalidadeid_nacionalidade": 1,
            "password": "password123",
            "email": "jane.doe@example.com",
            "data_criacao": "1995-05-05"
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GrupoViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/grupo/view/'

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

    def test_put_grupo_view(self):
        data = {
            "nome": "Grupo da Jane"
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ContactoViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/contacto/'

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
        
        self.tipo_contacto = TipoContacto.objects.create(id_tipo_contacto=1, descricao="Email")
        self.contacto = Contacto.objects.create(
            id_contacto=1,
            descricao="teste@email.com",
            tipo_contactoid_tipo_contacto=self.tipo_contacto,
            utilizadorid_utilizador=self.user
        )

        self.client.force_authenticate(user=self.user)
        self.url2 = f'/utilizador/contacto/{self.contacto.pk}/'

    def test_get_contacto_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_contacto_view(self):
        data = {
            "descricao": "1@1.com",
            "tipo_contactoid_tipo_contacto": 1
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_contacto_view(self):
        data = {
            "descricao": "2@2.com",
            "tipo_contactoid_tipo_contacto": 1
        }
        response = self.client.put(self.url2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_contacto_view(self):
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MoradaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/morada/'

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

        self.distrito = Distrito.objects.create(id_distrito=1, descricao="Lisboa", paisid_pais=self.pais)
        self.conselho = Conselho.objects.create(id_conselho=1, descricao="Cascais", distritoid_distrito=self.distrito)
        self.freguesia = Freguesia.objects.create(id_freguesia=1, descricao="Carcavelos", conselhoid_conselho=self.conselho)
        self.morada = Morada.objects.create(id_morada=1, 
                                            descricao="R. Dr Manuel", 
                                            utilizadorid_utilizador=self.user, 
                                            freguesiaid_freguesia=self.freguesia)
        
        

        self.client.force_authenticate(user=self.user)
        self.url2 = f'/utilizador/morada/{self.morada.pk}/'

    def test_get_morada_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_morada_view(self):
        data = {
            "descricao": "R. D Joao",
            "freguesiaid_freguesia": 1
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_morada_view(self):
        data = {
            "descricao": "R. D Joao",
            "freguesiaid_freguesia": 1
        }
        response = self.client.put(self.url2, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_morada_view(self):
        response = self.client.get(self.url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TipoContactoViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/tipo_contacto/'

        self.tipo_contacto = TipoContacto.objects.create(id_tipo_contacto=1, descricao="Email")

    def test_get_tipo_contacto_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EstadoCivilViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/estado_civil/'

        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")

    def test_get_estado_civil_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NacionalidadeViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/nacionalidade/'

        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1, paisid_pais=self.pais)

    def test_get_nacionalidade_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PaisViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/pais/'

        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")

    def test_get_pais_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DistritoViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/distrito/'

        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.distrito = Distrito.objects.create(id_distrito=1, descricao="Lisboa", paisid_pais=self.pais)

    def test_get_distrito_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ConselhoViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/conselho/'

        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.distrito = Distrito.objects.create(id_distrito=1, descricao="Lisboa", paisid_pais=self.pais)
        self.conselho = Conselho.objects.create(id_conselho=1, descricao="Cascais", distritoid_distrito=self.distrito)

    def test_get_conselho_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FreguesiaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/freguesia/'

        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.distrito = Distrito.objects.create(id_distrito=1, descricao="Lisboa", paisid_pais=self.pais)
        self.conselho = Conselho.objects.create(id_conselho=1, descricao="Cascais", distritoid_distrito=self.distrito)
        self.freguesia = Freguesia.objects.create(id_freguesia=1, descricao="Carcavelos", conselhoid_conselho=self.conselho)

    def test_get_freguesia_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
