from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from projeto.models import *


class GrupoSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Grupo
        fields = ["id_grupo", "nome", "data_criacao"]


# Serializer do Utilizador para Registo
class UtilizadorRegistroSerializer(WritableNestedModelSerializer):
    grupoid_grupo = GrupoSerializer()

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
            "password" : {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data["password"] = make_password(password)
        return super().create(validated_data)

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

class CondutorCreateSerializer(WritableNestedModelSerializer):
    #doc_reg_criminal = serializers.FileField(required=False, allow_null=True)
    #doc_comprov_residencia = serializers.FileField(required=False, allow_null=True)

    def validate_doc_reg_criminal(self, file):
        return self._validate_pdf(file, "doc_reg_criminal")

    def validate_doc_comprov_residencia(self, file):
        return self._validate_pdf(file, "doc_comprov_residencia")

    def _validate_pdf(self, file, field_name):
        if not file.name.lower().endswith('.pdf'):
            raise serializers.ValidationError(f"O arquivo '{field_name}' deve estar no formato PDF.")

        if file.size > 300000 * 1024:  # 200 KB
            raise serializers.ValidationError(f"O arquivo '{field_name}' não pode exceder 200KB.")

        return file

    class Meta:
        model = Condutor
        fields = [
            "id_condutor",
            "doc_reg_criminal",
            "doc_comprov_residencia",
            "reputacao",
            "data_criacao",
        ]


class CondutorEditSerializer(WritableNestedModelSerializer):
    #doc_reg_criminal = serializers.FileField(required=False, allow_null=True)
    #doc_comprov_residencia = serializers.FileField(required=False, allow_null=True)

    def validate_doc_reg_criminal(self, file):
        return self._validate_pdf(file, "doc_reg_criminal")

    def validate_doc_comprov_residencia(self, file):
        return self._validate_pdf(file, "doc_comprov_residencia")

    def _validate_pdf(self, file, field_name):
        if not file.name.lower().endswith('.pdf'):
            raise serializers.ValidationError(f"O arquivo '{field_name}' deve estar no formato PDF.")

        if file.size > 300000 * 1024:  # 200 KB
            raise serializers.ValidationError(f"O arquivo '{field_name}' não pode exceder 200KB.")

        return file

    class Meta:
        model = Condutor
        fields = [
            "id_condutor",
            "doc_reg_criminal",
            "doc_comprov_residencia",
        ]


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


class CreateVeiculoSerializer(WritableNestedModelSerializer):

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


class CreateCondutorVeiculoSerializer(WritableNestedModelSerializer):

    def validate_documento_arquivo(self, file):
        return self._validate_pdf(file, "documento_arquivo")

    def _validate_pdf(self, file, field_name):
        if not file.name.lower().endswith('.pdf'):
            raise serializers.ValidationError(f"O arquivo '{field_name}' deve estar no formato PDF.")

        if file.size > 300000 * 1024:  # 200 KB
            raise serializers.ValidationError(f"O arquivo '{field_name}' não pode exceder 200KB.")

        return file

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


class EditCondutorVeiculoSerializer(WritableNestedModelSerializer):

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
