from django.http.response import Http404, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import get_object_or_404

from projeto.models import *
from .serializers import *
from autenticacao.views import *
from comunicacao.views import AlertaView

"""
PASSAGEIRO - CRUD do Passageiro

    [POST]
        Headers: 
        Authorization Bearer (access token)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

"""
class PassageiroView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        total_passageiros = Passageiro.objects.filter(utilizadorid_utilizador=user).count()

        if total_passageiros == 0:
            passageiro = Passageiro.objects.create(
                utilizadorid_utilizador=user,
                data_criacao=timezone.now().date()
            )
            return JsonResponse("Passageiro adicionado com sucesso.", safe=False)

        serializer = PassageiroSerializer(passageiro)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user

        passageiros = Passageiro.objects.filter(utilizadorid_utilizador=user)
        serializer = PassageiroSerializer(passageiros, many=True, context={"request": request})
        return Response(serializer.data)

    def delete(self, request):
        user = request.user

        try:
            passageiro = Passageiro.objects.get(utilizadorid_utilizador=user.id_utilizador)
        except Passageiro.DoesNotExist:
            return Response({"erro": "Passageiro não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        passageiro.delete()
        return JsonResponse("Passageiro deletado com sucesso.", safe=False)


"""
RESERVA - Funcionalidade de Reserva

    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        valor (input)
        ponto_inicial_id (input)
        ponto_final_id (input)
        data_viagem (input)

    [GET]
        Headers: 
        Authorization Bearer (access token)

    [PUT]
        Headers:
        Authorization Bearer (access token)

        Body:
        valor (input)
        ponto_inicial_id (input)
        ponto_final_id (input)
        data_viagem (input)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

    [GET] "Condutor"
        Headers:
        Authorization Bearer (access token)

    [PUT] "Condutor"
        Headers:
        Authorization Bearer (access token)

    [PUT] "Cancelar"
        Headers:
        Authorization Bearer (access token)

    [PUT] "Finalizar"
        Headers:
        Authorization Bearer (access token)

"""
class ReservaView(APIView):
    permission_classes = [IsAuthenticated]

    # Pedir Reserva
    def post(self, request):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        valor = request.data.get('valor')
        ponto_inicial_id = request.data.get('ponto_inicial_id')
        ponto_final_id = request.data.get('ponto_final_id')
        data_viagem = request.data.get('data_viagem')

        if not valor or not ponto_inicial_id or not ponto_final_id:
            return Response({"erro": "Campos 'valor', 'ponto_inicial_id', 'ponto_final_id' e 'data_viagem' são obrigatórios."}, status=400)

        try:
            ponto_inicial = Ponto.objects.get(id_ponto=ponto_inicial_id)
            ponto_final = Ponto.objects.get(id_ponto=ponto_final_id)
        except Ponto.DoesNotExist:
            return Response({"erro": "Ponto não encontrado."}, status=404)

        try:
            passageiro = Passageiro.objects.get(id_passageiro=1)
            condutor = Condutor.objects.get(id_condutor=1)
            status_reserva = StatusReserva.objects.get(id_status_reserva=1)  # <-- Sempre ID 1
        except (Passageiro.DoesNotExist, Condutor.DoesNotExist, StatusReserva.DoesNotExist):
            return Response({"erro": "Erro ao localizar Passageiro, Condutor ou StatusReserva."}, status=400)

        # Cria a reserva
        reserva = Reserva.objects.create(
            data_emissao=timezone.now().date(),
            valor=valor,
            utilizadorid_utilizador=user,
            condutorid_condutor=condutor,
            passageiroid_passageiro=passageiro,
            status_reservaid_status_reserva=status_reserva,
            data_viagem=data_viagem,
        )

        # Comeco (destino = 0)
        PontoReserva.objects.create(
            destino=0,
            reservaid_reserva=reserva,
            pontoid_ponto=ponto_inicial,
        )

        # Destino (destino = 1)
        PontoReserva.objects.create(
            destino=1,
            reservaid_reserva=reserva,
            pontoid_ponto=ponto_final,
        )

        return Response({"mensagem": "Reserva criada com sucesso!", "id_reserva": reserva.id_reserva}, status=201)

    # Listar minhas Reservas
    def get(self, request):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        reservas = Reserva.objects.filter(utilizadorid_utilizador=user)

        serializer = ReadReservaSerializer(reservas, many=True)

        return Response(serializer.data, status=200) 

    # Mudar Reserva
    def put(self, request, pk):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            reserva = Reserva.objects.get(id_reserva=pk)
        except Reserva.DoesNotExist:
            return Response({"erro": "Reserva não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Verificar se a reserva pertence ao utilizador logado
        if reserva.utilizadorid_utilizador != user:
            return Response({"erro": "Você não tem permissão para alterar esta reserva."}, status=status.HTTP_403_FORBIDDEN)

        # Verificar se o status da reserva é 1 ou 2
        if reserva.status_reservaid_status_reserva.id_status_reserva not in [1, 2]:
            return Response({"erro": "A reserva só pode ser alterada se o status for 1 ou 2."},
                            status=status.HTTP_400_BAD_REQUEST)

        valor = request.data.get('valor')
        ponto_inicial_id = request.data.get('ponto_inicial_id')
        ponto_final_id = request.data.get('ponto_final_id')
        data_viagem = request.data.get('data_viagem')

        if valor is None or ponto_inicial_id is None or ponto_final_id is None:
            return Response({"erro": "Campos 'valor', 'ponto_inicial_id', 'ponto_final_id' e 'data_viagem' são obrigatórios."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            ponto_inicial = PontoReserva.objects.get(reservaid_reserva=reserva, destino=0)
            ponto_final = PontoReserva.objects.get(reservaid_reserva=reserva, destino=1)
        except PontoReserva.DoesNotExist:
            return Response({"erro": "Pontos de reserva (inicial ou final) não encontrados para esta reserva."},
                            status=status.HTTP_404_NOT_FOUND)

        try:
            novo_ponto_inicial = Ponto.objects.get(id_ponto=ponto_inicial_id)
            novo_ponto_final = Ponto.objects.get(id_ponto=ponto_final_id)
        except Ponto.DoesNotExist:
            return Response({"erro": "Ponto inicial ou final não encontrado."},
                            status=status.HTTP_404_NOT_FOUND)

        reserva.valor = valor
        ponto_inicial.pontoid_ponto = novo_ponto_inicial
        ponto_final.pontoid_ponto = novo_ponto_final
        reserva.data_viagem = data_viagem

        # Salvar tudo
        reserva.save()
        ponto_inicial.save()
        ponto_final.save()

        if reserva.status_reservaid_status_reserva.id_status_reserva == 2:
            if reserva.condutorid_condutor:
                condutor_destino = Condutor.objects.get(id_condutor=reserva.condutorid_condutor.id_condutor)
                utilizador_destino = Utilizador.objects.get(id_utilizador=condutor_destino.utilizadorid_utilizador.id_utilizador)
                descricao = f"Dados da Reserva, {reserva.id_reserva} alterados."

                AlertaView.alerta_interno(descricao, utilizador_destino.id_utilizador, 1)

        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Cancelar Reserva
    def delete(self, request, pk):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            reserva = Reserva.objects.get(id_reserva=pk)
        except Reserva.DoesNotExist:
            return Response({"erro": "Reserva não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Verificar se o utilizador da reserva corresponde ao utilizador logado
        if reserva.utilizadorid_utilizador.id_utilizador != user.id_utilizador:
            return Response({"erro": "Você não tem permissão para deletar esta reserva."}, status=status.HTTP_403_FORBIDDEN)

        # Verificar o status da reserva (deve ser 1 ou 2)
        if reserva.status_reservaid_status_reserva.id_status_reserva not in [1, 2]:
            return Response({"erro": "A reserva não pode ser deletada. O status da reserva não é válido."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Comeco (destino = 0) 
            ponto_inicial = PontoReserva.objects.get(reservaid_reserva=reserva, destino=0)
            ponto_inicial.delete()

            # Destino (destino = 1)
            ponto_final = PontoReserva.objects.get(reservaid_reserva=reserva, destino=1)
            ponto_final.delete()
        except PontoReserva.DoesNotExist:
            return Response({"erro": "Ponto de reserva não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Deletar a reserva
        reserva.delete()

        return Response({"mensagem": "Reserva e pontos de reserva associados deletados com sucesso."}, status=status.HTTP_204_NO_CONTENT)


class CondutorReservaView(APIView):
    permission_classes = [IsAuthenticated]

    def get_reserva(self, pk):
        try:
            reserva = Reserva.objects.get(id_reserva=pk)
            return reserva
        except Reserva.DoesNotExist:
            raise Http404

    # Listar todas Reservas (Para Condutores)
    def get(self, request, pk=None):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        if pk:
            data = self.get_reserva(pk)
            serializer = ReadReservaSerializer(data)
        else:
            data = Reserva.objects.all()
            serializer = ReadReservaSerializer(data, many=True)
        return Response(serializer.data)

    # Aceitar a reserva de um Passageiro
    def put(self, request, pk):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            reserva = Reserva.objects.get(id_reserva=pk)
        except Reserva.DoesNotExist:
            return Response({"erro": "Reserva não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Verificar se o status atual da reserva é 1
        if reserva.status_reservaid_status_reserva.id_status_reserva != 1:
            return Response({"erro": "A reserva não está em um status que permite esta alteração."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            passageiro = Passageiro.objects.get(utilizadorid_utilizador=reserva.utilizadorid_utilizador)
        except Passageiro.DoesNotExist:
            return Response({"erro": "Passageiro associado à reserva não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=user)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor associado ao utilizador logado não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            status_reserva = StatusReserva.objects.get(id_status_reserva=2)
        except StatusReserva.DoesNotExist:
            return Response({"erro": "StatusReserva com ID 2 não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        reserva.status_reservaid_status_reserva = status_reserva
        reserva.passageiroid_passageiro = passageiro
        reserva.condutorid_condutor = condutor

        reserva.save()

        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Cancelar reserva aprovada (apenas para Condutores)
class CancelarReservaView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            reserva = Reserva.objects.get(id_reserva=pk)
        except Reserva.DoesNotExist:
            return Response({"erro": "Reserva não encontrada."}, status=status.HTTP_404_NOT_FOUND)

        # Só pode cancelar a reserva se o condutor estiver associado a reserva
        try:
            condutor_logado = Condutor.objects.get(utilizadorid_utilizador=request.user)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor associado ao utilizador logado não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Só pode cancelar a reserva se o status = 2
        if reserva.status_reservaid_status_reserva.id_status_reserva != 2:
            return Response({"erro": "A reserva não está em um status que permite reset."}, status=status.HTTP_400_BAD_REQUEST)

        if reserva.condutorid_condutor != condutor_logado:
            return Response({"erro": "Você não tem permissão para resetar esta reserva."}, status=status.HTTP_403_FORBIDDEN)

        try:
            status_reserva = StatusReserva.objects.get(id_status_reserva=1)
        except StatusReserva.DoesNotExist:
            return Response({"erro": "StatusReserva com ID 1 não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            passageiro = Passageiro.objects.get(id_passageiro=1)
        except Passageiro.DoesNotExist:
            return Response({"erro": "Passageiro com ID 1 não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor_padrao = Condutor.objects.get(id_condutor=1)
        except Condutor.DoesNotExist:
            return Response({"erro": "Condutor com ID 1 não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        reserva.status_reservaid_status_reserva = status_reserva
        reserva.passageiroid_passageiro = passageiro
        reserva.condutorid_condutor = condutor_padrao

        reserva.save()

        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Finalizar reserva aprovada (apenas para Passageiros)
class FinalizarReservaView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            reserva = get_object_or_404(Reserva, id_reserva=pk)

            # Verificar se a reserva pertence ao utilizador logado
            if reserva.utilizadorid_utilizador.id_utilizador != request.user.id_utilizador:
                return Response({'error': 'Não autorizado para alterar esta reserva.'}, status=status.HTTP_403_FORBIDDEN)

            # Verificar se status da reserva é 2
            if reserva.status_reservaid_status_reserva.id_status_reserva != 2:
                return Response({'error': 'Reserva não está em estado válido para conversão (status diferente de 2).'}, status=status.HTTP_400_BAD_REQUEST)

            # Atualizar status da reserva para 3
            reserva.status_reservaid_status_reserva_id = 3  # ID 3 = novo status
            reserva.save()

            viagem = Viagem.objects.create(
                data_viagem=reserva.data_viagem,
                distancia_percorrida=0,
                status_viagemid_status_viagem_id=1, 
                condutorid_condutor=reserva.condutorid_condutor
            )

            PassageiroViagem.objects.create(
                passageiroid_passageiro=reserva.passageiroid_passageiro,
                viagemid_viagem=viagem,
                reservaid_reserva=reserva
            )

            pontos_reserva = PontoReserva.objects.filter(reservaid_reserva=reserva)

            for ponto_reserva in pontos_reserva:
                PontoViagem.objects.create(
                    destino=ponto_reserva.destino,
                    viagemid_viagem=viagem,
                    pontoid_ponto=ponto_reserva.pontoid_ponto
                )

            if reserva.condutorid_condutor:
                condutor_destino = Condutor.objects.get(id_condutor=reserva.condutorid_condutor.id_condutor)
                utilizador_destino = Utilizador.objects.get(id_utilizador=condutor_destino.utilizadorid_utilizador.id_utilizador)
                descricao = f"Viagem confirmada ({reserva.id_reserva})."

                AlertaView.alerta_interno(descricao, utilizador_destino.id_utilizador, 1)

            return Response({'success': 'Reserva convertida em Viagem com sucesso.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Erro ao atualizar reserva: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Finalizar reserva aprovada (apenas para Passageiros) (VERSAO SEM PAGAMENTO)
class FinalizarReserva2View(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            reserva = get_object_or_404(Reserva, id_reserva=pk)

            # Verificar se a reserva pertence ao utilizador logado
            if reserva.utilizadorid_utilizador.id_utilizador != request.user.id_utilizador:
                return Response({'error': 'Não autorizado para alterar esta reserva.'}, status=status.HTTP_403_FORBIDDEN)

            # Verificar se status da reserva é 2
            if reserva.status_reservaid_status_reserva.id_status_reserva != 2:
                return Response({'error': 'Reserva não está em estado válido para conversão (status diferente de 2).'}, status=status.HTTP_400_BAD_REQUEST)

            # Atualizar status da reserva para 3
            reserva.status_reservaid_status_reserva_id = 3  # ID 3 = novo status
            reserva.save()

            viagem = Viagem.objects.create(
                data_viagem=reserva.data_viagem,
                distancia_percorrida=0,
                status_viagemid_status_viagem_id=1, 
                condutorid_condutor=reserva.condutorid_condutor
            )

            PassageiroViagem.objects.create(
                passageiroid_passageiro=reserva.passageiroid_passageiro,
                viagemid_viagem=viagem,
                reservaid_reserva=reserva
            )

            pontos_reserva = PontoReserva.objects.filter(reservaid_reserva=reserva)

            for ponto_reserva in pontos_reserva:
                PontoViagem.objects.create(
                    destino=ponto_reserva.destino,
                    viagemid_viagem=viagem,
                    pontoid_ponto=ponto_reserva.pontoid_ponto
                )

            if reserva.condutorid_condutor:
                condutor_destino = Condutor.objects.get(id_condutor=reserva.condutorid_condutor.id_condutor)
                utilizador_destino = Utilizador.objects.get(id_utilizador=condutor_destino.utilizadorid_utilizador.id_utilizador)
                descricao = f"Viagem confirmada ({reserva.id_reserva})."

                AlertaView.alerta_interno(descricao, utilizador_destino.id_utilizador, 1)

            return Response({'success': 'Reserva convertida em Viagem com sucesso.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Erro ao atualizar reserva: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""
PASSAGEIRO_VIAGEM - Associar/Desasociar Passageiro a Viagem

    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        id_viagem (input)
        id_utilizador (input)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

        Body:
        id_viagem (input)
        id_utilizador (input)

    [GET] "Passageiro"

    [GET] "Condutor"

"""
# Associar Passageiro a Viagem
class AssociarViagemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            id_viagem = request.data.get('id_viagem')
            id_utilizador = request.data.get('id_utilizador')

            if not id_viagem or not id_utilizador:
                return Response({'error': 'id_viagem e id_utilizador são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

            viagem = get_object_or_404(Viagem, id_viagem=id_viagem)

            reserva = get_object_or_404(Reserva, condutorid_condutor=viagem.condutorid_condutor, data_viagem=viagem.data_viagem)

            if reserva.utilizadorid_utilizador.id_utilizador != user.id_utilizador:
                return Response({'error': 'Você não está autorizado a adicionar passageiros nesta viagem.'}, status=status.HTTP_403_FORBIDDEN)

            utilizador_novo = get_object_or_404(Utilizador, id_utilizador=id_utilizador)

            if utilizador_novo.grupoid_grupo_id != request.user.grupoid_grupo_id:
                return Response({'error': 'O utilizador selecionado não pertence ao mesmo grupo que o utilizador logado.'}, status=status.HTTP_403_FORBIDDEN)

            passageiro = get_object_or_404(Passageiro, utilizadorid_utilizador=utilizador_novo)

            PassageiroViagem.objects.create(
                passageiroid_passageiro=passageiro,
                viagemid_viagem=viagem,
                reservaid_reserva=reserva
            )

            return Response({'success': 'Passageiro adicionado com sucesso à viagem.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': f'Ocorreu um erro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            id_viagem = request.data.get('id_viagem')
            id_utilizador = request.data.get('id_utilizador')

            if not id_viagem or not id_utilizador:
                return Response({'error': 'id_viagem e id_utilizador são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

            viagem = get_object_or_404(Viagem, id_viagem=id_viagem)

            reserva = get_object_or_404(Reserva, condutorid_condutor=viagem.condutorid_condutor, data_viagem=viagem.data_viagem)

            if reserva.utilizadorid_utilizador.id_utilizador != user.id_utilizador:
                return Response({'error': 'Você não está autorizado a remover passageiros desta viagem.'}, status=status.HTTP_403_FORBIDDEN)

            utilizador_remover = get_object_or_404(Utilizador, id_utilizador=id_utilizador)

            if utilizador_remover.grupoid_grupo_id != request.user.grupoid_grupo_id:
                return Response({'error': 'O utilizador selecionado não pertence ao mesmo grupo que o utilizador logado.'}, status=status.HTTP_403_FORBIDDEN)

            if utilizador_remover.id_utilizador == reserva.utilizadorid_utilizador.id_utilizador:
                return Response({'error': 'Não é permitido remover o dono da reserva.'}, status=status.HTTP_403_FORBIDDEN)

            passageiro = get_object_or_404(Passageiro, utilizadorid_utilizador=utilizador_remover)

            passageiro_viagem = get_object_or_404(
                PassageiroViagem,
                passageiroid_passageiro=passageiro,
                viagemid_viagem=viagem,
                reservaid_reserva=reserva
            )

            # Deletar
            passageiro_viagem.delete()

            return Response({'success': 'Passageiro removido com sucesso da viagem.'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': f'Ocorreu um erro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Listar viagens (Passageiro)
class PassageiroAssociarViagemView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            passageiro = Passageiro.objects.get(utilizadorid_utilizador=request.user)

            passagens = PassageiroViagem.objects.filter(passageiroid_passageiro=passageiro)

            viagens_ids = passagens.values_list('viagemid_viagem_id', flat=True).distinct()

            viagens = Viagem.objects.filter(id_viagem__in=viagens_ids)

            viagens_data = []

            for viagem in viagens:
                passageiros_viagem = PassageiroViagem.objects.filter(viagemid_viagem=viagem)
                passageiros = [pviagem.passageiroid_passageiro for pviagem in passageiros_viagem]

                viagem_data = ListViagemSerializer(viagem).data

                passageiros_data = PassageiroSerializer(passageiros, many=True).data

                viagem_data['passageiros'] = passageiros_data

                viagens_data.append(viagem_data)

            return Response(viagens_data)

        except Passageiro.DoesNotExist:
            return Response({'error': 'O utilizador logado não está associado a nenhum passageiro.'}, status=404)
        except Exception as e:
            return Response({'error': f'Ocorreu um erro: {str(e)}'}, status=500)


# Listar viagens (Condutor)
class CondutorAssociarViagemView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=request.user)

            viagens = Viagem.objects.filter(condutorid_condutor=condutor)

            viagens_data = []

            for viagem in viagens:
                passageiros_viagem = PassageiroViagem.objects.filter(viagemid_viagem=viagem)
                passageiros = [pviagem.passageiroid_passageiro for pviagem in passageiros_viagem]

                viagem_data = ListViagemSerializer(viagem).data

                passageiros_data = PassageiroSerializer(passageiros, many=True).data

                # Adicionar passageiros e condutor no resultado
                viagem_data['passageiros'] = passageiros_data
                viagem_data['condutor'] = condutor_data

                viagens_data.append(viagem_data)

            return Response(viagens_data)

        except Condutor.DoesNotExist:
            return Response({'error': 'O utilizador logado não está associado a nenhum condutor.'}, status=404)
        except Exception as e:
            return Response({'error': f'Ocorreu um erro: {str(e)}'}, status=500)


"""
DESVIO - Processo de Desvios

    [POST]
        Headers: 
        Authorization Bearer (access token)

        Body:
        id_viagem (input)
        ponto_inicial_id (input)
        ponto_final_id (input)

    [DELETE]
        Headers: 
        Authorization Bearer (access token)

    [PUT] "Condutor"
        Headers: 
        Authorization Bearer (access token)

    [DELETE] "Condutor"
        Headers: 
        Authorization Bearer (access token)

"""
class DesvioView(APIView):
    permission_classes = [IsAuthenticated]

    # Solicitar Desvio (Passageiro)
    def post(self, request):
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        id_viagem = request.data.get('id_viagem')
        ponto_inicial_id = request.data.get('ponto_inicial_id')
        ponto_final_id = request.data.get('ponto_final_id')

        if not id_viagem or not ponto_inicial_id or not ponto_final_id:
            return Response({'error': 'Campos obrigatórios não fornecidos.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            viagem = Viagem.objects.get(pk=id_viagem)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        associado = PassageiroViagem.objects.filter(
            viagemid_viagem=viagem,
            reservaid_reserva__utilizadorid_utilizador=request.user
        ).exists()

        if not associado:
            return Response({'error': 'Você não tem permissão para alterar esta viagem.'}, status=status.HTTP_403_FORBIDDEN)

        Desvio.objects.filter(
            viagemid_viagem=viagem,
            status_desvioid_status_desvio=2
        ).update(status_desvioid_status_desvio=1)

        novo_desvio = Desvio.objects.create(
            data_emissao=timezone.now().date(),
            status_desvioid_status_desvio=StatusDesvio.objects.get(pk=2),
            viagemid_viagem=viagem
        )

        ponto_viagem_origem = PontoViagem.objects.filter(
            viagemid_viagem=viagem, destino=0
        ).first()
        ponto_viagem_destino = PontoViagem.objects.filter(
            viagemid_viagem=viagem, destino=1
        ).first()

        if not ponto_viagem_origem or not ponto_viagem_destino:
            return Response({'error': 'Pontos de origem/destino da viagem não encontrados.'}, status=500)

        # Criar os 4 PontoDesvio
        PontoDesvio.objects.create(
            destino=0,
            original=1,
            desvioid_desvio=novo_desvio,
            pontoid_ponto=ponto_viagem_origem.pontoid_ponto
        )

        PontoDesvio.objects.create(
            destino=1,
            original=1,
            desvioid_desvio=novo_desvio,
            pontoid_ponto=ponto_viagem_destino.pontoid_ponto
        )

        try:
            ponto_inicio_novo = Ponto.objects.get(pk=ponto_inicial_id)
            ponto_final_novo = Ponto.objects.get(pk=ponto_final_id)
        except Ponto.DoesNotExist:
            return Response({'error': 'Um dos novos pontos fornecidos é inválido.'}, status=status.HTTP_400_BAD_REQUEST)

        PontoDesvio.objects.create(
            destino=0,
            original=0,
            desvioid_desvio=novo_desvio,
            pontoid_ponto=ponto_inicio_novo
        )

        PontoDesvio.objects.create(
            destino=1,
            original=0,
            desvioid_desvio=novo_desvio,
            pontoid_ponto=ponto_final_novo
        )

        return Response({'mensagem': 'Desvio criado com sucesso.', 'id_desvio': novo_desvio.id_desvio}, status=201)

    # Listar Desvios de uma Viagem (Passageiro)
    def get(self, request, pk):
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            passageiro = Passageiro.objects.get(utilizadorid_utilizador=request.user)
        except Passageiro.DoesNotExist:
            return Response({'error': 'Utilizador não é um passageiro válido.'}, status=status.HTTP_403_FORBIDDEN)

        associado = PassageiroViagem.objects.filter(
            viagemid_viagem=viagem,
            passageiroid_passageiro=passageiro
        ).exists()

        if not associado:
            return Response({'error': 'Você não está autorizado a visualizar os desvios desta viagem.'},
                            status=status.HTTP_403_FORBIDDEN)

        # Recupera os desvios da viagem
        desvios = Desvio.objects.filter(viagemid_viagem=viagem)

        # Retorna os dados dos desvios
        resultado = [
            {
                'id_desvio': desvio.id_desvio,
                'data_emissao': desvio.data_emissao,
                'status_desvio': desvio.status_desvioid_status_desvio.descricao,
                'viagem_id': desvio.viagemid_viagem.id_viagem
            }
            for desvio in desvios
        ]

        return Response(resultado, status=status.HTTP_200_OK)

    # Cancelar Desvio (Passageiro)
    def delete(self, request, pk):
        if not CheckPassageiroView.check_passageiro(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        # Verificar se o utilizador está associado à viagem via Reserva -> PassageiroViagem
        associado = PassageiroViagem.objects.filter(
            viagemid_viagem=viagem,
            reservaid_reserva__utilizadorid_utilizador=request.user
        ).exists()

        if not associado:
            return Response({'error': 'Você não tem permissão para modificar o desvio desta viagem.'}, status=status.HTTP_403_FORBIDDEN)

        # Buscar desvio ativo
        desvio_ativo = Desvio.objects.filter(
            viagemid_viagem=viagem,
            status_desvioid_status_desvio=2
        ).first()

        if not desvio_ativo:
            return Response({'mensagem': 'Nenhum desvio ativo encontrado para esta viagem.'}, status=status.HTTP_200_OK)

        # Alterar status para inativo (1)
        desvio_ativo.status_desvioid_status_desvio_id = 1
        desvio_ativo.save()

        return Response({'mensagem': 'Desvio desativado com sucesso.', 'id_desvio': desvio_ativo.id_desvio}, status=200)


class CondutorDesvioView(APIView):
    permission_classes = [IsAuthenticated]

    # Listar Desvios (Condutor)
    def get(self, request, pk):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        # Verifica se o utilizador é o condutor da viagem
        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=request.user)
        except Condutor.DoesNotExist:
            return Response({'error': 'Utilizador não é um condutor válido.'}, status=status.HTTP_403_FORBIDDEN)

        if viagem.condutorid_condutor != condutor:
            return Response({'error': 'Você não está autorizado a visualizar os desvios desta viagem.'},
                            status=status.HTTP_403_FORBIDDEN)

        # Recupera os desvios da viagem
        desvios = Desvio.objects.filter(viagemid_viagem=viagem)

        resultado = [
            {
                'id_desvio': desvio.id_desvio,
                'data_emissao': desvio.data_emissao,
                'status_desvio': desvio.status_desvioid_status_desvio.descricao,
                'viagem_id': desvio.viagemid_viagem.id_viagem
            }
            for desvio in desvios
        ]

        return Response(resultado, status=status.HTTP_200_OK)


    # Aceitar Desvio (Condutor)
    def put(self, request, pk):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=request.user)
        except Condutor.DoesNotExist:
            return Response({'error': 'Utilizador não é um condutor válido.'}, status=status.HTTP_403_FORBIDDEN)

        if viagem.condutorid_condutor != condutor:
            return Response({'error': 'Você não tem permissão para modificar esta viagem.'}, status=status.HTTP_403_FORBIDDEN)

        desvio_ativo = Desvio.objects.filter(viagemid_viagem=viagem, status_desvioid_status_desvio=2).first()
        if not desvio_ativo:
            return Response({'error': 'Nenhum desvio ativo encontrado para esta viagem.'}, status=status.HTTP_404_NOT_FOUND)

        desvio_aplicado = Desvio.objects.filter(viagemid_viagem=viagem, status_desvioid_status_desvio=3).first()
        if desvio_aplicado:
            desvio_aplicado.status_desvioid_status_desvio_id = 1
            desvio_aplicado.save()

        desvio_ativo.status_desvioid_status_desvio_id = 3
        desvio_ativo.save()

        for destino_valor in [0, 1]:
            try:
                novo_ponto_desvio = PontoDesvio.objects.get(
                    desvioid_desvio=desvio_ativo,
                    destino=destino_valor,
                    original=0
                )
                ponto_viagem = PontoViagem.objects.get(
                    viagemid_viagem=viagem,
                    destino=destino_valor
                )
                ponto_viagem.pontoid_ponto = novo_ponto_desvio.pontoid_ponto
                ponto_viagem.save()
            except (PontoDesvio.DoesNotExist, PontoViagem.DoesNotExist):
                return Response({'error': f'Erro ao atualizar ponto de destino {destino_valor}.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'mensagem': 'Desvio aplicado com sucesso.', 'id_desvio': desvio_ativo.id_desvio}, status=status.HTTP_200_OK)
    
    # Rejeitar Desvio (Condutor)
    def delete(self, request, pk):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=request.user)
        except Condutor.DoesNotExist:
            return Response({'error': 'Utilizador não é um condutor válido.'}, status=status.HTTP_403_FORBIDDEN)

        if viagem.condutorid_condutor != condutor:
            return Response({'error': 'Você não tem permissão para modificar esta viagem.'}, status=status.HTTP_403_FORBIDDEN)

        desvio = Desvio.objects.filter(viagemid_viagem=viagem, status_desvioid_status_desvio=2).first()
        if not desvio:
            return Response({'error': 'Nenhum desvio pendente encontrado para esta viagem.'}, status=status.HTTP_404_NOT_FOUND)

        desvio.status_desvioid_status_desvio_id = 1
        desvio.save()

        return Response({'mensagem': 'Desvio rejeitado com sucesso.', 'id_desvio': desvio.id_desvio}, status=status.HTTP_200_OK)


"""
DESVIO - Processo de Inicializacao/Finalizacao de Viagens

    [PUT] "Iniciar"
        Headers: 
        Authorization Bearer (access token)

    [PUT] "Finalizar"
        Headers: 
        Authorization Bearer (access token)

        Body:
        distancia_percorrida (input)

"""
# Iniciar Viagem (Condutor)
class IniciarViagemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=request.user)
        except Condutor.DoesNotExist:
            return Response({'error': 'Utilizador não é um condutor válido.'}, status=status.HTTP_403_FORBIDDEN)

        if viagem.condutorid_condutor != condutor:
            return Response({'error': 'Você não está autorizado a iniciar esta viagem.'},
                            status=status.HTTP_403_FORBIDDEN)

        if viagem.status_viagemid_status_viagem.id_status_viagem != 1:
            return Response({'error': 'A viagem não está no estado adequado para ser iniciada (deve estar com status 1).'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            status_viagem_iniciada = StatusViagem.objects.get(id_status_viagem=2)
        except StatusViagem.DoesNotExist:
            return Response({'error': 'Status de viagem "iniciada" (ID=2) não encontrado.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        viagem.status_viagemid_status_viagem = status_viagem_iniciada
        viagem.save()

        return Response({'message': 'Viagem iniciada com sucesso.'}, status=status.HTTP_200_OK)


# Finalizar Viagem (Condutor)
class FinalizarViagemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        if not CheckCondutorView.check_condutor(request.user):
            return Response(
                {"detail": "Permissão Negada."},
                status=status.HTTP_403_FORBIDDEN
            )

        distancia = request.data.get('distancia_percorrida')

        if distancia is None:
            return Response({'error': 'Campo "distancia_percorrida" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            distancia = int(distancia)
        except ValueError:
            return Response({'error': 'O valor de "distancia_percorrida" deve ser um número inteiro.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            viagem = Viagem.objects.get(pk=pk)
        except Viagem.DoesNotExist:
            return Response({'error': 'Viagem não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            condutor = Condutor.objects.get(utilizadorid_utilizador=request.user)
        except Condutor.DoesNotExist:
            return Response({'error': 'Utilizador não é um condutor válido.'}, status=status.HTTP_403_FORBIDDEN)

        if viagem.condutorid_condutor != condutor:
            return Response({'error': 'Você não está autorizado a finalizar esta viagem.'},
                            status=status.HTTP_403_FORBIDDEN)

        if viagem.status_viagemid_status_viagem.id_status_viagem != 2:
            return Response({'error': 'A viagem só pode ser finalizada se estiver com status igual a 2 (em andamento).'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            status_finalizada = StatusViagem.objects.get(id_status_viagem=3)
        except StatusViagem.DoesNotExist:
            return Response({'error': 'Status de viagem "finalizada" (ID=3) não encontrado.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        viagem.status_viagemid_status_viagem = status_finalizada
        viagem.distancia_percorrida = distancia
        viagem.save()

        return Response({'message': 'Viagem finalizada com sucesso.'}, status=status.HTTP_200_OK)


"""
PONTO - Listar Pontos
 
    [GET]

"""
class PontoView(APIView):

    def get_ponto(self, pk):
        try:
            pontos = Ponto.objects.get(id_ponto=pk)
            return pontos
        except Ponto.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_ponto(pk)
            serializer = PontoSerializer(data)
        else:
            data = Ponto.objects.all()
            serializer = PontoSerializer(data, many=True)
        return Response(serializer.data)
