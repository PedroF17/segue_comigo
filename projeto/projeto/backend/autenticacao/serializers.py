from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

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


# Serializer do Utilizador para Registo
class UtilizadorRegistroSerializer(serializers.ModelSerializer):
    grupoid_grupo = serializers.PrimaryKeyRelatedField(queryset=Grupo.objects.all())
    estado_civilid_estado_civil = serializers.PrimaryKeyRelatedField(queryset=EstadoCivil.objects.all())
    nacionalidadeid_nacionalidade = serializers.PrimaryKeyRelatedField(queryset=Nacionalidade.objects.all())

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
            "password",
            "email",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            instance.password = make_password(password)
        return super().update(instance, validated_data)


class PrimeiroUtilizadorRegistroSerializer(serializers.ModelSerializer):
    estado_civilid_estado_civil = serializers.PrimaryKeyRelatedField(
        queryset=EstadoCivil.objects.all()
    )
    nacionalidadeid_nacionalidade = serializers.PrimaryKeyRelatedField(
        queryset=Nacionalidade.objects.all()
    )

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
            "password",
            "email",
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)
        return super().create(validated_data)


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


class FreguesiaSerializer(WritableNestedModelSerializer):
    conselhoid_conselho = ConselhoSerializer()

    class Meta:
        model = Freguesia
        fields = ["id_freguesia", "descricao", "conselhoid_conselho"]


class MoradaShowSerializer(WritableNestedModelSerializer):
    freguesiaid_freguesia = FreguesiaSerializer()

    class Meta:
        model = Morada
        fields = [
            "id_morada",
            "descricao",
            "utilizadorid_utilizador",
            "freguesiaid_freguesia",
        ]


class MoradaSerializer(serializers.ModelSerializer):
    freguesiaid_freguesia = serializers.PrimaryKeyRelatedField(queryset=Freguesia.objects.all())

    class Meta:
        model = Morada
        fields = [
            "id_morada",
            "descricao",
            "freguesiaid_freguesia",
        ]


class TipoContactoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = TipoContacto
        fields = ["id_tipo_contacto", "descricao"]


class ContactoSerializer(serializers.ModelSerializer):
    tipo_contactoid_tipo_contacto = serializers.PrimaryKeyRelatedField(queryset=TipoContacto.objects.all())

    class Meta:
        model = Contacto
        fields = ["id_contacto", "descricao", "tipo_contactoid_tipo_contacto"]


class ContactoShowSerializer(serializers.ModelSerializer):
    tipo_contactoid_tipo_contacto = TipoContactoSerializer()

    class Meta:
        model = Contacto
        fields = ["id_contacto", "descricao", "tipo_contactoid_tipo_contacto"]


class AdministradorSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorRegistroSerializer()

    class Meta:
        model = Administrador
        fields = ["id_administrador", "utilizadorid_utilizador"]


class CondutorSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorRegistroSerializer()
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


class PassageiroSerializer(WritableNestedModelSerializer):
    utilizadorid_utilizador = UtilizadorRegistroSerializer()

    class Meta:
        model = Passageiro
        fields = ["id_passageiro", "data_criacao", "utilizadorid_utilizador"]


# Serializer do Utilizador Tokenizado para Login
class CustomTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        senha = attrs.get("senha")

        try:
            # Busca pelo utilizador utilizando o email fornecido
            user = Utilizador.objects.get(email=email)
        except Utilizador.DoesNotExist:
            raise serializers.ValidationError(_("Email ou senha inválidos"))

        # Verifica a senha fornecida com a senha criptografada
        if not check_password(senha, user.senha):
            raise serializers.ValidationError(_("Email ou senha inválidos"))

        # Gera os tokens de acesso e refresh para o usuário
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

# Serializer do Utilizador Tokenizado para Alterar Senha
class AlterarSenhaSerializer(serializers.Serializer):
    senha_atual = serializers.CharField(write_only=True)  # Para verificar a senha atual
    nova_senha = serializers.CharField(write_only=True)  # Para a nova senha

    def validate_nova_senha(self, value):
        # Validando a nova senha
        validate_password(value)
        return value

    def validate(self, attrs):
        # Recuperar o usuário autenticado
        usuario = self.context['request'].user

        # Verificar se a senha atual está correta
        senha_atual = attrs.get("senha_atual")
        if not check_password(senha_atual, usuario.senha):
            raise serializers.ValidationError("Senha atual incorreta")

        return attrs

    def update(self, instance, validated_data):
        # Criptografar e atualizar a nova senha
        nova_senha = validated_data['nova_senha']
        instance.senha = make_password(nova_senha)
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise ValidationError(_('As senhas novas não coincidem.'))
        return data
    
    def save(self, user):
        user.set_password(self.validated_data['new_password'])
        user.save()
