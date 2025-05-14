from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from .models import *


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
            "senha",
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


class AvaliacaoSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()
    condutorid_condutor = CondutorSerializer()

    class Meta:
        model = Avaliacao
        fields = ["id_avaliacao", "nota", "viagemid_viagem", "condutorid_condutor"]


class BandeiraCartaoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = BandeiraCartao
        fields = ["id_bandeira_cartao", "descricao"]


class TipoCategoriaSerializer(WritableNestedModelSerializer):

    class Meta:
        model = TipoCategoria
        fields = ["id_tipo_categoria", "tipo"]


class CartaConducaoSerializer(WritableNestedModelSerializer):
    condutorid_condutor = CondutorSerializer()
    tipo_categoriaid_tipo_categoria = TipoCategoriaSerializer()

    class Meta:
        model = CartaConducao
        fields = [
            "id_carta_conducao",
            "numero",
            "data_emissao",
            "data_validade",
            "status",
            "foto",
            "condutorid_condutor",
            "tipo_categoriaid_tipo_categoria",
        ]


class CartaoSerializer(WritableNestedModelSerializer):
    bandeira_cartaoid_bandeira_cartao = BandeiraCartaoSerializer()

    class Meta:
        model = Cartao
        fields = [
            "id_cc",
            "digito_seguranca",
            "data_validade",
            "token",
            "bandeira_cartaoid_bandeira_cartao",
        ]


class CartaoUtilizadorSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()
    cartaoid_cc = CartaoSerializer()

    class Meta:
        model = CartaoUtilizador
        fields = ["id", "utilizadorid_utilizador", "cartaoid_cc"]


class ChatViagemSerializer(WritableNestedModelSerializer):
    viagemid_viagem = ViagemSerializer()

    class Meta:
        model = ChatViagem
        fields = ["id_chat_viagem", "viagemid_viagem"]


class TipoVeiculoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = TipoVeiculo
        fields = ["id_tipo_veiculo", "descricao"]


class CorVeiculoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = CorVeiculo
        fields = ["id_cor_veiculo", "descricao"]


class MarcaVeiculoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = MarcaVeiculo
        fields = ["id_marca_veiculo", "descricao"]


class ModeloVeiculoSerializer(WritableNestedModelSerializer):
    marca_veiculoid_marca_veiculo = MarcaVeiculoSerializer()

    class Meta:
        model = ModeloVeiculo
        fields = ["id_modelo_veiculo", "descricao", "marca_veiculoid_marca_veiculo"]


class VeiculoSerializer(WritableNestedModelSerializer):
    tipo_veiculoid_tipo_veiculo = TipoVeiculoSerializer()
    cor_veiculoid_cor_veiculo = CorVeiculoSerializer()
    modelo_veiculoid_modelo_veiculo = ModeloVeiculoSerializer()

    class Meta:
        model = Veiculo
        fields = [
            "id_veiculo",
            "matricula",
            "data_fabricacao",
            "ativo",
            "tipo_veiculoid_tipo_veiculo",
            "cor_veiculoid_cor_veiculo",
            "modelo_veiculoid_modelo_veiculo",
        ]


class CondutorVeiculoSerializer(WritableNestedModelSerializer):
    condutorid_condutor = CondutorSerializer()
    veiculoid_veiculo = VeiculoSerializer()

    class Meta:
        model = CondutorVeiculo
        fields = [
            "id_condutor_veiculo",
            "documento_arquivo",
            "data_emissao",
            "data_validade",
            "condutorid_condutor",
            "veiculoid_veiculo",
        ]


class DistritoSerializer(WritableNestedModelSerializer):
    paisid_pais = PaisSerializer()

    class Meta:
        model = Distrito
        fields = ["id_distrito", "descricao", "paisid_pais"]


class ConselhoSerializer(WritableNestedModelSerializer):
    distritoid_distrito = DistritoSerializer()

    class Meta:
        model = Conselho
        fields = ["id_conselho", "descricao", "distritoid_distrito"]


class TipoContactoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = TipoContacto
        fields = ["id_tipo_contacto", "descricao"]


class ContactoSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()
    tipo_contactoid_tipo_contacto = TipoContactoSerializer()

    class Meta:
        model = Contacto
        fields = [
            "id_contacto",
            "descricao",
            "utilizadorid_utilizador",
            "tipo_contactoid_tipo_contacto",
        ]


class DadosMbSerializer(WritableNestedModelSerializer):

    class Meta:
        model = DadosMb
        fields = ["id_mb", "referencia", "entidade", "data_limite"]


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


class FreguesiaSerializer(WritableNestedModelSerializer):
    conselhoid_conselho = ConselhoSerializer()

    class Meta:
        model = Freguesia
        fields = ["id_freguesia", "descricao", "conselhoid_conselho"]


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


class MoradaSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()
    freguesiaid_freguesia = FreguesiaSerializer()

    class Meta:
        model = Morada
        fields = [
            "id_morada",
            "descricao",
            "utilizadorid_utilizador",
            "freguesiaid_freguesia",
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


class TipoPagamentoSerializer(WritableNestedModelSerializer):
    dados_mbid_mb = DadosMbSerializer()
    cartaoid_cc = CartaoSerializer()

    class Meta:
        model = TipoPagamento
        fields = ["id_tipo_pagamento", "descricao", "dados_mbid_mb", "cartaoid_cc"]


class PassageiroSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorSerializer()

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
        ]


class PagamentoSerializer(WritableNestedModelSerializer):
    tipo_pagamentoid_tipo_pagamento = TipoPagamentoSerializer()
    reservaid_reserva = ReservaSerializer()

    class Meta:
        model = Pagamento
        fields = [
            "id_pagamento",
            "valor",
            "data_pagamento",
            "tipo_pagamentoid_tipo_pagamento",
            "reservaid_reserva",
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


class SuspensaoSerializer(WritableNestedModelSerializer):
    administradorid_administrador = AdministradorSerializer()
    utilizadorid_utilizador = UtilizadorSerializer()

    class Meta:
        model = Suspensao
        fields = [
            "id_suspensao",
            "descricao",
            "data_inicio",
            "data_fim",
            "administradorid_administrador",
            "utilizadorid_utilizador",
        ]


class AuthGroupSerializer(WritableNestedModelSerializer):

    class Meta:
        model = AuthGroup
        fields = ["id", "name"]


class DjangoContentTypeSerializer(WritableNestedModelSerializer):

    class Meta:
        model = DjangoContentType
        fields = ["id", "app_label", "model"]


class AuthPermissionSerializer(WritableNestedModelSerializer):
    content_type = DjangoContentTypeSerializer()

    class Meta:
        model = AuthPermission
        fields = ["id", "name", "content_type", "codename"]


class AuthGroupPermissionsSerializer(WritableNestedModelSerializer):
    group = AuthGroupSerializer()
    permission = AuthPermissionSerializer()

    class Meta:
        model = AuthGroupPermissions
        fields = ["id", "group", "permission"]


class AuthUserSerializer(WritableNestedModelSerializer):

    class Meta:
        model = AuthUser
        fields = [
            "id",
            "password",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        ]


class AuthUserGroupsSerializer(WritableNestedModelSerializer):
    user = AuthUserSerializer()
    group = AuthGroupSerializer()

    class Meta:
        model = AuthUserGroups
        fields = ["id", "user", "group"]


class AuthUserUserPermissionsSerializer(WritableNestedModelSerializer):
    user = AuthUserSerializer()
    permission = AuthPermissionSerializer()

    class Meta:
        model = AuthUserUserPermissions
        fields = ["id", "user", "permission"]


class DjangoAdminLogSerializer(WritableNestedModelSerializer):
    content_type = DjangoContentTypeSerializer()
    user = AuthUserSerializer()

    class Meta:
        model = DjangoAdminLog
        fields = [
            "id",
            "action_time",
            "object_id",
            "object_repr",
            "action_flag",
            "change_message",
            "content_type",
            "user",
        ]


class DjangoMigrationsSerializer(WritableNestedModelSerializer):

    class Meta:
        model = DjangoMigrations
        fields = ["id", "app", "name", "applied"]


class DjangoSessionSerializer(WritableNestedModelSerializer):

    class Meta:
        model = DjangoSession
        fields = ["session_key", "session_data", "expire_date"]
