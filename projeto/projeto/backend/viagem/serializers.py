from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from projeto.models import *


class PaisSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Pais
        fields = ["id_pais", "nome"]


class NacionalidadeSerializer(WritableNestedModelSerializer):
    paisid_pais = PaisSerializer()

    class Meta:
        model = Nacionalidade
        fields = ["id_nacionalidade", "paisid_pais"]


class EstadoCivilSerializer(WritableNestedModelSerializer):

    class Meta:
        model = EstadoCivil
        fields = ["id_estado_civil", "descricao"]


class GrupoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Grupo
        fields = ["id_grupo", "nome", "data_criacao"]


class UtilizadorSerializer(WritableNestedModelSerializer):
    grupoid_grupo = GrupoSerializer()
    estado_civilid_estado_civil = EstadoCivilSerializer()
    nacionalidadeid_nacionalidade = NacionalidadeSerializer()

    class Meta:
        model = Utilizador
        fields = [
            "id_utilizador",
            "nome_primeiro",
            "nome_ultimo",
            "data_nasc",
            "genero",
            "numero_cc",
            "data_criacao",
            "grupoid_grupo",
            "estado_civilid_estado_civil",
            "nacionalidadeid_nacionalidade",
        ]


class AdministradorSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()

    class Meta:
        model = Administrador
        fields = ["id_administrador", "utilizadorid_utilizador"]


class CondutorSerializer(WritableNestedModelSerializer):
    #utilizadorid_utilizador = UtilizadorSerializer()
    doc_reg_criminal = serializers.FileField(required=False, allow_null=True)
    doc_comprov_residencia = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Condutor
        fields = [
            "id_condutor",
            "doc_reg_criminal",
            "doc_comprov_residencia",
            "reputacao",
            "data_criacao",
            "utilizadorid_utilizador",
        ]


class StatusViagemSerializer(WritableNestedModelSerializer):

    class Meta:
        model = StatusViagem
        fields = ["id_status_viagem", "descricao"]


class ViagemSerializer(WritableNestedModelSerializer):
    status_viagemid_status_viagem = StatusViagemSerializer()
    condutorid_condutor = CondutorSerializer()

    class Meta:
        model = Viagem
        fields = [
            "id_viagem",
            "data_viagem",
            "distancia_percorrida",
            "status_viagemid_status_viagem",
            "condutorid_condutor"
        ]


class ListViagemSerializer(WritableNestedModelSerializer):
    status_viagemid_status_viagem = StatusViagemSerializer()

    class Meta:
        model = Viagem
        fields = [
            "id_viagem",
            "data_viagem",
            "distancia_percorrida",
            "status_viagemid_status_viagem",
            "condutorid_condutor"
        ]


class AvaliacaoSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()
    condutorid_condutor = CondutorSerializer()

    class Meta:
        model = Avaliacao
        fields = ["id_avaliacao", "nota", "viagemid_viagem", "condutorid_condutor"]


class ChatViagemSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()

    class Meta:
        model = ChatViagem
        fields = ["id_chat_viagem", "viagemid_viagem"]


class StatusDesvioSerializer(WritableNestedModelSerializer):

    class Meta:
        model = StatusDesvio
        fields = ["id_status_desvio", "descricao"]


class DesvioSerializer(WritableNestedModelSerializer):
    status_desvioid_status_desvio = StatusDesvioSerializer()
    viagemid_viagem = ViagemSerializer()

    class Meta:
        model = Desvio
        fields = [
            "id_desvio",
            "data_emissao",
            "status_desvioid_status_desvio",
            "viagemid_viagem",
        ]


class MensagemSerializer(WritableNestedModelSerializer):
    chat_viagemid_chat_viagem = ChatViagemSerializer()
    utilizadorid_utilizador = UtilizadorSerializer()

    class Meta:
        model = Mensagem
        fields = [
            "id_mensagem",
            "valor",
            "data_envio",
            "lida",
            "chat_viagemid_chat_viagem",
            "utilizadorid_utilizador",
        ]


class PassageiroSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()

    class Meta:
        model = Passageiro
        fields = ["id_passageiro", "data_criacao", "utilizadorid_utilizador"]


class ReadPassageiroSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Passageiro
        fields = ["id_passageiro", "data_criacao", "utilizadorid_utilizador"]


class ReservaSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()
    condutorid_condutor = CondutorSerializer()
    passageiroid_passageiro = PassageiroSerializer()

    class Meta:
        model = Reserva
        fields = [
            "id_reserva",
            "data_emissao",
            "valor",
            "utilizadorid_utilizador",
            "condutorid_condutor",
            "passageiroid_passageiro",
            "data_viagem",
        ]


class ReadReservaSerializer(WritableNestedModelSerializer):
    condutorid_condutor = CondutorSerializer()
    passageiroid_passageiro = ReadPassageiroSerializer()

    class Meta:
        model = Reserva
        fields = [
            "id_reserva",
            "data_emissao",
            "valor",
            "utilizadorid_utilizador",
            "condutorid_condutor",
            "passageiroid_passageiro",
            "data_viagem",
        ]


class PassageiroViagemSerializer(WritableNestedModelSerializer):
    passageiroid_passageiro = PassageiroSerializer()
    viagemid_viagem = ViagemSerializer()
    reservaid_reserva = ReservaSerializer()

    class Meta:
        model = PassageiroViagem
        fields = [
            "id_passageiro_viagem",
            "passageiroid_passageiro",
            "viagemid_viagem",
            "reservaid_reserva",
        ]


class PontoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Ponto
        fields = ["id_ponto", "descricao"]


class PontoViagemSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()
    pontoid_ponto = PontoSerializer()

    class Meta:
        model = PontoViagem
        fields = ["id_ponto_viagem", "destino", "viagemid_viagem", "pontoid_ponto"]
