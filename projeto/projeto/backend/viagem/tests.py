from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from viagem.views import *
from comunicacao.views import *
from projeto.models import *

User = get_user_model()

class PassageiroViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)
        
        self.user2 = User.objects.create_user(
            id_utilizador=2,
            email="testuser@email2.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)

        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)

        self.url = '/viagem/passageiro/create/'

    def test_get_passageiro_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_passageiro_view(self):
        self.client.force_authenticate(user=self.user2) # autenticar com utilizador sem passageiro associado

        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_passageiro_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReservaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = '/viagem/reserva/'
        self.url2 = f'/viagem/reserva/{self.reserva.pk}/'


    def test_post_reserva_view(self):
        data = {
            "valor": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2,
            "data_viagem": "2025-01-01 00:00:05"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_reserva_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_reserva_view(self):
        response = self.client.delete(self.url2)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CondutorReservaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = '/viagem/reserva_condutor/'
        self.url2 = f'/viagem/reserva_condutor/{self.reserva.pk}/'

    def test_get_condutor_reserva_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_condutor_reserva_view(self):
        response = self.client.put(self.url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CancelarReservaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = f'/viagem/reserva_condutor/cancel/{self.reserva.pk}/'

    def test_put_cancelar_reserva_view(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FinalizarReservaViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade,
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = f'/viagem/reserva/confirm2/{self.reserva.pk}/'

    def test_put_finalizar_reserva_view(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AssociarViagemViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )

        self.user2 = User.objects.create_user(
            id_utilizador=2,
            email="testuser2@email.com", 
            password="password321", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )

        self.user3 = User.objects.create_user(
            id_utilizador=3,
            email="testuser3@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.passageiro2 = Passageiro.objects.create(id_passageiro=2, utilizadorid_utilizador=self.user2)
        self.passageiro3 = Passageiro.objects.create(id_passageiro=3, utilizadorid_utilizador=self.user3)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro3,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )

        self.url = '/viagem/viagem/associate/'

    def test_post_associar_viagem_view(self):
        data = {
            "id_viagem": 1,
            "id_utilizador": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_associar_viagem_view(self):
        data = {
            "id_viagem": 1,
            "id_utilizador": 3
        }
        response = self.client.delete(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AutoDesassociarViagemViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )

        self.user2 = User.objects.create_user(
            id_utilizador=2,
            email="testuser2@email.com", 
            password="password321", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user2)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.passageiro2 = Passageiro.objects.create(id_passageiro=2, utilizadorid_utilizador=self.user2)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro2,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )

        self.url = '/viagem/viagem/desassociate/'

    def test_post_auto_desassociar_viagem_view(self):
        data = {
            "id_viagem": 1,
        }
        response = self.client.delete(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DesvioViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.status_desvio = StatusDesvio.objects.create(id_status_desvio=1, descricao="Inativo")
        self.status_desvio2 = StatusDesvio.objects.create(id_status_desvio=2, descricao="Pendente")
        self.status_desvio3 = StatusDesvio.objects.create(id_status_desvio=3, descricao="Ativo")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = '/viagem/desvio/'
        self.url2 = f'/viagem/desvio/{self.viagem.pk}/'

    def test_post_desvio_view(self):
        data = {
            "id_viagem": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_desvio_view(self):
        response = self.client.delete(self.url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CondutorDesvioViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.status_desvio = StatusDesvio.objects.create(id_status_desvio=1, descricao="Inativo")
        self.status_desvio2 = StatusDesvio.objects.create(id_status_desvio=2, descricao="Pendente")
        self.status_desvio3 = StatusDesvio.objects.create(id_status_desvio=3, descricao="Ativo")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )
        self.desvio = Desvio.objects.create(
                                    id_desvio=1,
                                    data_emissao="2025-01-01",
                                    status_desvioid_status_desvio=self.status_desvio2,
                                    viagemid_viagem=self.viagem
                                )
        self.ponto_desvio = PontoDesvio.objects.create(
                                    id_ponto_desvio=1,
                                    destino=0,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=1
                                )
        self.ponto_desvio2 = PontoDesvio.objects.create(
                                    id_ponto_desvio=2,
                                    destino=1,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=1
                                )
        self.ponto_desvio3 = PontoDesvio.objects.create(
                                    id_ponto_desvio=3,
                                    destino=0,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=0
                                )
        self.ponto_desvio4 = PontoDesvio.objects.create(
                                    id_ponto_desvio=4,
                                    destino=1,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=0
                                )

        self.url = f'/viagem/desvio_condutor/{self.viagem.pk}/'

    def test_put_desvio_condutor_view(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_desvio_condutor_view(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class IniciarViagemViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = f'/viagem/viagem/start/{self.viagem.pk}/'

    def test_put_iniciar_viagem_view(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FinalizarViagemViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem2,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )

        self.url = f'/viagem/viagem/finish/{self.viagem.pk}/'

    def test_put_finalizar_viagem_view(self):
        data = {
            "distancia_percorrida": 10,
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PassageiroAssociarViagemViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.status_desvio = StatusDesvio.objects.create(id_status_desvio=1, descricao="Inativo")
        self.status_desvio2 = StatusDesvio.objects.create(id_status_desvio=2, descricao="Pendente")
        self.status_desvio3 = StatusDesvio.objects.create(id_status_desvio=3, descricao="Ativo")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem2,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )
        self.desvio = Desvio.objects.create(
                                    id_desvio=1,
                                    data_emissao="2025-01-01",
                                    status_desvioid_status_desvio=self.status_desvio2,
                                    viagemid_viagem=self.viagem
                                )
        self.ponto_desvio = PontoDesvio.objects.create(
                                    id_ponto_desvio=1,
                                    destino=0,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=1
                                )
        self.ponto_desvio2 = PontoDesvio.objects.create(
                                    id_ponto_desvio=2,
                                    destino=1,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=1
                                )
        self.ponto_desvio3 = PontoDesvio.objects.create(
                                    id_ponto_desvio=3,
                                    destino=0,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=0
                                )
        self.ponto_desvio4 = PontoDesvio.objects.create(
                                    id_ponto_desvio=4,
                                    destino=1,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=0
                                )

        self.url = '/viagem/viagem/list/'

    def test_get_passageiro_associar_viagem_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CondutorAssociarViagemViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.status_desvio = StatusDesvio.objects.create(id_status_desvio=1, descricao="Inativo")
        self.status_desvio2 = StatusDesvio.objects.create(id_status_desvio=2, descricao="Pendente")
        self.status_desvio3 = StatusDesvio.objects.create(id_status_desvio=3, descricao="Ativo")
        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem2,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )
        self.desvio = Desvio.objects.create(
                                    id_desvio=1,
                                    data_emissao="2025-01-01",
                                    status_desvioid_status_desvio=self.status_desvio2,
                                    viagemid_viagem=self.viagem
                                )
        self.ponto_desvio = PontoDesvio.objects.create(
                                    id_ponto_desvio=1,
                                    destino=0,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=1
                                )
        self.ponto_desvio2 = PontoDesvio.objects.create(
                                    id_ponto_desvio=2,
                                    destino=1,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=1
                                )
        self.ponto_desvio3 = PontoDesvio.objects.create(
                                    id_ponto_desvio=3,
                                    destino=0,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=0
                                )
        self.ponto_desvio4 = PontoDesvio.objects.create(
                                    id_ponto_desvio=4,
                                    destino=1,
                                    desvioid_desvio=self.desvio,
                                    pontoid_ponto=self.ponto,
                                    original=0
                                )

        self.url = '/viagem/viagem/list_condutor/'

    def test_get_condutor_associar_viagem_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# -----------------------------------------
#           Testes de Integracao
# -----------------------------------------

class ReservaViagemTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.user2 = User.objects.create_user(
            id_utilizador=2,
            email="testuser2@email.com", 
            password="password321", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.passageiro2 = Passageiro.objects.create(id_passageiro=2, utilizadorid_utilizador=self.user2)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")

        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )


    # Processo de Reserva
    def test_reserva(self):

        # Solicitar Reserva (Passageiro)
        self.url3 = '/viagem/reserva/'
        data3 = {
            "valor": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2,
            "data_viagem": "2025-01-01 00:00:05"
        }
        response3 = self.client.post(self.url3, data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)


        # Listar Reservas (Passageiro)
        self.url4 = '/viagem/reserva/'
        response4 = self.client.get(self.url4)
        self.assertEqual(response4.status_code, status.HTTP_200_OK)


        # Cancelar Reserva (Passageiro)
        reserva_id = response3.data.get('id') or response3.data.get('pk') or response3.data.get('id_reserva')
        self.assertIsNotNone(reserva_id, "A resposta do POST não contém o ID da reserva.")

        url5 = f'/viagem/reserva/{reserva_id}/'
        response5 = self.client.delete(url5)
        self.assertEqual(response5.status_code, status.HTTP_204_NO_CONTENT)

        # Listar Reservas (Condutor)
        self.url6 = '/viagem/reserva_condutor/'
        response6 = self.client.get(self.url6)
        self.assertEqual(response6.status_code, status.HTTP_200_OK)


        # Aceitar Reserva (Condutor)
        self.url3 = '/viagem/reserva/'
        data3 = {
            "valor": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2,
            "data_viagem": "2025-01-01 00:00:05"
        }
        response3 = self.client.post(self.url3, data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)

        reserva_id = response3.data.get('id') or response3.data.get('pk') or response3.data.get('id_reserva')
        self.assertIsNotNone(reserva_id, "A resposta do PUT não contém o ID da reserva.")

        self.url7 = f'/viagem/reserva_condutor/{reserva_id}/'
        response7 = self.client.put(self.url7)
        self.assertEqual(response7.status_code, status.HTTP_200_OK)


        # Cancelar Reserva (Condutor)
        reserva_id = response3.data.get('id') or response3.data.get('pk') or response3.data.get('id_reserva')
        self.assertIsNotNone(reserva_id, "A resposta do PUT não contém o ID da reserva.")

        self.url8 = f'/viagem/reserva_condutor/cancel/{reserva_id}/'
        response8 = self.client.put(self.url8)
        self.assertEqual(response8.status_code, status.HTTP_200_OK)


        # Confirmar Reserva (Passageiro)
        reserva_id = response3.data.get('id') or response3.data.get('pk') or response3.data.get('id_reserva')
        self.assertIsNotNone(reserva_id, "A resposta do PUT não contém o ID da reserva.")

        self.url7 = f'/viagem/reserva_condutor/{reserva_id}/'
        response7 = self.client.put(self.url7)
        self.assertEqual(response7.status_code, status.HTTP_200_OK)
       
        self.url9 = f'/viagem/reserva/confirm2/{reserva_id}/'
        response9 = self.client.put(self.url9)
        self.assertEqual(response9.status_code, status.HTTP_200_OK)

    
    # Processo de Viagem
    def test_viagem(self):

        # Listar Viagens (Passageiro)
        self.url = '/viagem/viagem/list/'
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


        # Listar Viagens (Condutor)
        self.url2 = '/viagem/viagem/list_condutor/'
        response2 = self.client.get(self.url2)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)


        # Associar Passageiro a Viagem (Passageiro)
        self.url3 = '/viagem/viagem/associate/'
        data3 = {
            "id_viagem": 1,
            "id_utilizador": 2
        }
        response3 = self.client.post(self.url3, data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)


        # Dessasociar Passageiro a Viagem (Passageiro)
        self.url4 = '/viagem/viagem/associate/'
        data4 = {
            "id_viagem": 1,
            "id_utilizador": 2
        }
        response4 = self.client.delete(self.url4, data4, format='json')
        self.assertEqual(response4.status_code, status.HTTP_200_OK)


        # Utilizador associado se dessasocia manualmente (Passageiro)
        self.url3 = '/viagem/viagem/associate/'
        data3 = {
            "id_viagem": 1,
            "id_utilizador": 2
        }
        response3 = self.client.post(self.url3, data3, format='json')
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)
        self.client.force_authenticate(user=self.user2)

        self.url5 = '/viagem/viagem/desassociate/'
        data5 = {
            "id_viagem": 1,
        }
        response5 = self.client.delete(self.url5, data5, format='json')
        self.assertEqual(response5.status_code, status.HTTP_200_OK)


        # Confirmar Viagem (Condutor)
        self.client.force_authenticate(user=self.user)
        self.url6 = f'/viagem/viagem/start/{self.viagem.pk}/'
        response6 = self.client.put(self.url6)
        self.assertEqual(response6.status_code, status.HTTP_200_OK)


        # Finalizar Viagem (Condutor)
        self.url7 = f'/viagem/viagem/finish/{self.viagem.pk}/'
        data7 = {
            "distancia_percorrida": 10,
        }
        response7 = self.client.put(self.url7, data7, format='json')
        self.assertEqual(response7.status_code, status.HTTP_200_OK)


class DesvioViagemTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.grupo = Grupo.objects.create(id_grupo=1, nome="Test", data_criacao="2025-04-01")
        self.estado_civil = EstadoCivil.objects.create(id_estado_civil=1, descricao="Solteiro")
        self.pais = Pais.objects.create(id_pais=1, nome="Portugal")
        self.nacionalidade = Nacionalidade.objects.create(id_nacionalidade=1 ,paisid_pais=self.pais)

        self.user = User.objects.create_user(
            id_utilizador=1,
            email="testuser@email.com", 
            password="password123", 
            grupoid_grupo=self.grupo, 
            estado_civilid_estado_civil=self.estado_civil,
            nacionalidadeid_nacionalidade=self.nacionalidade
        )
        self.client.force_authenticate(user=self.user)

        self.ponto = Ponto.objects.create(id_ponto=1, descricao="Teste")
        self.ponto2 = Ponto.objects.create(id_ponto=2, descricao="Teste2")
        self.passageiro = Passageiro.objects.create(id_passageiro=1, utilizadorid_utilizador=self.user)
        self.condutor = Condutor.objects.create(id_condutor=1, utilizadorid_utilizador=self.user, reputacao=1)
        self.administrador = Administrador.objects.create(id_administrador=1, utilizadorid_utilizador=self.user)
        self.status_reserva = StatusReserva.objects.create(id_status_reserva=1, descricao="Pendente")
        self.status_reserva2 = StatusReserva.objects.create(id_status_reserva=2, descricao="Aceite")
        self.status_reserva3 = StatusReserva.objects.create(id_status_reserva=3, descricao="Finalizada")
        self.status_viagem = StatusViagem.objects.create(id_status_viagem=1, descricao="Pendente")
        self.status_viagem2 = StatusViagem.objects.create(id_status_viagem=2, descricao="Em Andamento")
        self.status_viagem3 = StatusViagem.objects.create(id_status_viagem=3, descricao="Finalizada")
        self.status_desvio = StatusDesvio.objects.create(id_status_desvio=1, descricao="Inativo")
        self.status_desvio2 = StatusDesvio.objects.create(id_status_desvio=2, descricao="Pendente")
        self.status_desvio3 = StatusDesvio.objects.create(id_status_desvio=3, descricao="Ativo")
        self.tipo_alerta = TipoAlerta.objects.create(id_tipo_alerta=1, descricao="Aviso")

        self.reserva = Reserva.objects.create(
                                    id_reserva=1, 
                                    utilizadorid_utilizador=self.user, 
                                    condutorid_condutor=self.condutor, 
                                    passageiroid_passageiro=self.passageiro,
                                    status_reservaid_status_reserva=self.status_reserva2,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=1, 
                                    destino=0, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_reserva = PontoReserva.objects.create(
                                    id_ponto_reserva=2, 
                                    destino=1, 
                                    reservaid_reserva=self.reserva,
                                    pontoid_ponto=self.ponto2
                                )
        self.viagem = Viagem.objects.create(
                                    id_viagem=1,
                                    status_viagemid_status_viagem=self.status_viagem,
                                    condutorid_condutor=self.condutor,
                                    data_viagem="2025-01-01 00:00:00"
                                )
        self.passageiro_viagem = PassageiroViagem.objects.create(
                                    id_passageiro_viagem=1,
                                    passageiroid_passageiro=self.passageiro,
                                    viagemid_viagem=self.viagem,
                                    reservaid_reserva=self.reserva
                                )
        self.ponto_viagem = PontoViagem.objects.create(
                                    id_ponto_viagem=1,
                                    destino=0,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto
                                )
        self.ponto_viagem2 = PontoViagem.objects.create(
                                    id_ponto_viagem=2,
                                    destino=1,
                                    viagemid_viagem=self.viagem,
                                    pontoid_ponto=self.ponto2
                                )


    # Processo de Desvio
    def test_desvio(self):
        
        # Solicitar Desvio (Passageiro)
        self.url = '/viagem/desvio/'
        data = {
            "id_viagem": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


        # Cancelar Solicitacao de Desvio (Passageiro)
        self.url2 = f'/viagem/desvio/{self.viagem.pk}/'
        response2 = self.client.delete(self.url2)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)


        # Aceitar Solicitacao de Desvio (Condutor)
        self.url = '/viagem/desvio/'
        data = {
            "id_viagem": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.url3 = f'/viagem/desvio_condutor/{self.viagem.pk}/'
        response3 = self.client.put(self.url3)
        self.assertEqual(response3.status_code, status.HTTP_200_OK)


        # Rejeitar Solicitacao de Desvio (Condutor)
        self.url = '/viagem/desvio/'
        data = {
            "id_viagem": 1,
            "ponto_inicial_id": 1,
            "ponto_final_id": 2
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.url4 = f'/viagem/desvio_condutor/{self.viagem.pk}/'
        response4 = self.client.put(self.url4)
        self.assertEqual(response4.status_code, status.HTTP_200_OK)
