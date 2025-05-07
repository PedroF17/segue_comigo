from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from views import FirstCreateAccountView, CreateAccountView, ChangePasswordView

# Create your tests here.

User = get_user_model()

class FirstCreateAccountViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = 'utilizador/create_first/'

    def test_post_first_create_account(self):
        data = {
            "group_name": "Test Group",
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
        self.user = User.objects.create_user(
            username="testuser", password="password123"
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
            "grupoid_grupo": 1,
            "estado_civilid_estado_civil": 1,
            "nacionalidadeid_nacionalidade": 1,
            "password": "password123",
            "email": "jane.doe@example.com"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_create_account(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ChangePasswordViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/utilizador/new_password/'
        self.user = User.objects.create_user(
            username="testuser", password="oldpassword123"
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