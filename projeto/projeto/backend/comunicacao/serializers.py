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
            #"senha",
        ]


class AdministradorSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()

    class Meta:
        model = Administrador
        fields = ["id_administrador", "utilizadorid_utilizador"]


class TipoAlertaSerializer(WritableNestedModelSerializer):

    class Meta:
        model = TipoAlerta
        fields = ["id_tipo_alerta", "descricao"]


class CreateAlertaSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Alerta
        fields = [
            "id_alerta",
            "descricao",
            "utilizadorid_utilizador",
            "administradorid_administrador",
            "tipo_alertaid_tipo_alerta",
        ]


class AlertaSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()
    administradorid_administrador = AdministradorSerializer()
    tipo_alertaid_tipo_alerta = TipoAlertaSerializer()

    class Meta:
        model = Alerta
        fields = [
            "id_alerta",
            "descricao",
            "utilizadorid_utilizador",
            "administradorid_administrador",
            "tipo_alertaid_tipo_alerta",
        ]


class CondutorSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()

    class Meta:
        model = Condutor
        fields = [
            "id_condutor",
            "documento_reg_criminal",
            "documento_comprov_residencia",
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

    class Meta:
        model = Viagem
        fields = [
            "id_viagem",
            "data_viagem",
            "distancia_percorrida",
            "status_viagemid_status_viagem",
        ]


class ChatViagemSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()

    class Meta:
        model = ChatViagem
        fields = ["id_chat_viagem", "viagemid_viagem"]


class AvaliacaoSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()
    condutorid_condutor = CondutorSerializer()

    class Meta:
        model = Avaliacao
        fields = ["id_avaliacao", "nota", "viagemid_viagem", "condutorid_condutor"]


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


class TipoOcorrenciaSerializer(WritableNestedModelSerializer):

    class Meta:
        model = TipoOcorrencia
        fields = ["id_tipo_ocorrencia", "descricao"]


class OcorrenciaSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()
    utilizadorid_utilizador = UtilizadorSerializer()
    administradorid_administrador = AdministradorSerializer()
    tipo_ocorrenciaid_tipo_ocorrencia = TipoOcorrenciaSerializer()

    class Meta:
        model = Ocorrencia
        fields = [
            "id_ocorrencia",
            "descricao",
            "data_envio",
            "data_lida",
            "viagemid_viagem",
            "utilizadorid_utilizador",
            "administradorid_administrador",
            "tipo_ocorrenciaid_tipo_ocorrencia",
        ]

class CreateOcorrenciaSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Ocorrencia
        fields = [
            "id_ocorrencia",
            "descricao",
            "data_envio",
            #"data_lida",
            "viagemid_viagem",
            "utilizadorid_utilizador",
            "administradorid_administrador",
            "tipo_ocorrenciaid_tipo_ocorrencia",
        ]
