from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Administrador(models.Model):
    id_administrador = models.AutoField(db_column='ID_administrador', primary_key=True)  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.

    class Meta:
        managed = True 
        db_table = 'Administrador'


class Alerta(models.Model):
    id_alerta = models.AutoField(db_column='ID_alerta', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.
    administradorid_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='AdministradorID_administrador')  # Field name made lowercase.
    tipo_alertaid_tipo_alerta = models.ForeignKey('TipoAlerta', models.DO_NOTHING, db_column='Tipo_AlertaID_tipo_alerta')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Alerta'


class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(db_column='ID_avaliacao', primary_key=True)  # Field name made lowercase.
    nota = models.IntegerField(db_column='Nota', blank=True, null=True)  # Field name made lowercase.
    viagemid_viagem = models.ForeignKey('Viagem', models.DO_NOTHING, db_column='ViagemID_viagem')  # Field name made lowercase.
    condutorid_condutor = models.ForeignKey('Condutor', models.DO_NOTHING, db_column='CondutorID_condutor')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Avaliacao'


class BandeiraCartao(models.Model):
    id_bandeira_cartao = models.AutoField(db_column='ID_bandeira_cartao', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Bandeira_Cartao'


class CartaConducao(models.Model):
    id_carta_conducao = models.AutoField(db_column='ID_carta_conducao', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', unique=True, blank=True, null=True)  # Field name made lowercase.
    data_emissao = models.DateField(db_column='Data_emissao', blank=True, null=True)  # Field name made lowercase.
    data_validade = models.DateField(db_column='Data_validade', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    condutorid_condutor = models.ForeignKey('Condutor', models.DO_NOTHING, db_column='CondutorID_condutor')  # Field name made lowercase.
    tipo_categoriaid_tipo_categoria = models.ForeignKey('TipoCategoria', models.DO_NOTHING, db_column='Tipo_CategoriaID_tipo_categoria')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Carta_Conducao'


class Cartao(models.Model):
    id_cc = models.AutoField(db_column='ID_cc', primary_key=True)  # Field name made lowercase.
    digito_seguranca = models.IntegerField(db_column='Digito_seguranca', blank=True, null=True)  # Field name made lowercase.
    data_validade = models.DateField(db_column='Data_validade', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', unique=True, max_length=200, blank=True, null=True)  # Field name made lowercase.
    bandeira_cartaoid_bandeira_cartao = models.ForeignKey(BandeiraCartao, models.DO_NOTHING, db_column='Bandeira_CartaoID_bandeira_cartao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cartao'


class CartaoUtilizador(models.Model):
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.
    cartaoid_cc = models.ForeignKey(Cartao, models.DO_NOTHING, db_column='CartaoID_cc')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cartao_Utilizador'


class ChatViagem(models.Model):
    id_chat_viagem = models.AutoField(db_column='ID_chat_viagem', primary_key=True)  # Field name made lowercase.
    viagemid_viagem = models.ForeignKey('Viagem', models.DO_NOTHING, db_column='ViagemID_viagem')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Chat_Viagem'


class Condutor(models.Model):
    id_condutor = models.AutoField(db_column='ID_condutor', primary_key=True)
    doc_reg_criminal = models.FileField(upload_to='docs/condutores/', db_column='Doc_reg_criminal', blank=True, null=True)
    doc_comprov_residencia = models.FileField(upload_to='docs/condutores/', db_column='Doc_comprov_residencia', blank=True, null=True)
    reputacao = models.IntegerField(db_column='Reputacao', blank=True, null=True)
    data_criacao = models.DateField(db_column='Data_criacao', blank=True, null=True)
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')

    class Meta:
        managed = True
        db_table = 'Condutor'

class CondutorVeiculo(models.Model):
    id_condutor_veiculo = models.AutoField(db_column='ID_condutor_veiculo', primary_key=True)  # Field name made lowercase.
    #documento_arquivo = models.CharField(db_column='Documento_arquivo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    documento_arquivo = models.FileField(upload_to='docs/condutores/', db_column='Documento_arquivo', blank=True, null=True)
    data_emissao = models.DateField(db_column='Data_emissao', blank=True, null=True)  # Field name made lowercase.
    data_validade = models.DateField(db_column='Data_validade', blank=True, null=True)  # Field name made lowercase.
    condutorid_condutor = models.ForeignKey(Condutor, models.DO_NOTHING, db_column='CondutorID_condutor')  # Field name made lowercase.
    veiculoid_veiculo = models.ForeignKey('Veiculo', models.DO_NOTHING, db_column='VeiculoID_veiculo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Condutor_Veiculo'


class Conselho(models.Model):
    id_conselho = models.AutoField(db_column='ID_conselho', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    distritoid_distrito = models.ForeignKey('Distrito', models.DO_NOTHING, db_column='DistritoID_distrito')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Conselho'


class Contacto(models.Model):
    id_contacto = models.AutoField(db_column='ID_contacto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.
    tipo_contactoid_tipo_contacto = models.ForeignKey('TipoContacto', models.DO_NOTHING, db_column='Tipo_ContactoID_tipo_contacto')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Contacto'


class CorVeiculo(models.Model):
    id_cor_veiculo = models.AutoField(db_column='ID_cor_veiculo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Cor_Veiculo'


class DadosMb(models.Model):
    id_mb = models.AutoField(db_column='ID_mb', primary_key=True)  # Field name made lowercase.
    referencia = models.IntegerField(db_column='Referencia', blank=True, null=True)  # Field name made lowercase.
    entidade = models.IntegerField(db_column='Entidade', blank=True, null=True)  # Field name made lowercase.
    data_limite = models.DateField(db_column='Data_limite', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Dados_MB'


class Desvio(models.Model):
    id_desvio = models.AutoField(db_column='ID_desvio', primary_key=True)  # Field name made lowercase.
    data_emissao = models.DateField(db_column='Data_emissao', blank=True, null=True)  # Field name made lowercase.
    status_desvioid_status_desvio = models.ForeignKey('StatusDesvio', models.DO_NOTHING, db_column='Status_DesvioID_status_desvio')  # Field name made lowercase.
    viagemid_viagem = models.ForeignKey('Viagem', models.DO_NOTHING, db_column='ViagemID_viagem')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Desvio'


class Distrito(models.Model):
    id_distrito = models.AutoField(db_column='ID_distrito', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    paisid_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaisID_pais')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Distrito'


class EstadoCivil(models.Model):
    id_estado_civil = models.AutoField(db_column='ID_estado_civil', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Estado_Civil'


class Freguesia(models.Model):
    id_freguesia = models.AutoField(db_column='ID_freguesia', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    conselhoid_conselho = models.ForeignKey(Conselho, models.DO_NOTHING, db_column='ConselhoID_conselho')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Freguesia'


class Grupo(models.Model):
    id_grupo = models.AutoField(db_column='ID_grupo', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_criacao = models.DateField(db_column='Data_criacao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Grupo'


class MarcaVeiculo(models.Model):
    id_marca_veiculo = models.AutoField(db_column='ID_marca_veiculo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Marca_Veiculo'


class Mensagem(models.Model):
    id_mensagem = models.AutoField(db_column='ID_mensagem', primary_key=True)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    data_envio = models.DateField(db_column='Data_envio', blank=True, null=True)  # Field name made lowercase.
    lida = models.IntegerField(db_column='Lida', blank=True, null=True)  # Field name made lowercase.
    chat_viagemid_chat_viagem = models.ForeignKey(ChatViagem, models.DO_NOTHING, db_column='Chat_ViagemID_chat_viagem')  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Mensagem'


class ModeloVeiculo(models.Model):
    id_modelo_veiculo = models.AutoField(db_column='ID_modelo_veiculo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marca_veiculoid_marca_veiculo = models.ForeignKey(MarcaVeiculo, models.DO_NOTHING, db_column='Marca_VeiculoID_marca_veiculo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Modelo_Veiculo'


class Morada(models.Model):
    id_morada = models.AutoField(db_column='ID_morada', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.
    freguesiaid_freguesia = models.ForeignKey(Freguesia, models.DO_NOTHING, db_column='FreguesiaID_freguesia')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Morada'


class Nacionalidade(models.Model):
    id_nacionalidade = models.AutoField(db_column='ID_nacionalidade', primary_key=True)  # Field name made lowercase.
    paisid_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaisID_pais')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Nacionalidade'


class Ocorrencia(models.Model):
    id_ocorrencia = models.AutoField(db_column='ID_ocorrencia', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    data_envio = models.DateField(db_column='Data_envio', blank=True, null=True)  # Field name made lowercase.
    data_lida = models.DateField(db_column='Data_lida', blank=True, null=True)  # Field name made lowercase.
    viagemid_viagem = models.ForeignKey('Viagem', models.DO_NOTHING, db_column='ViagemID_viagem')  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.
    administradorid_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='AdministradorID_administrador')  # Field name made lowercase.
    tipo_ocorrenciaid_tipo_ocorrencia = models.ForeignKey('TipoOcorrencia', models.DO_NOTHING, db_column='Tipo_OcorrenciaID_tipo_ocorrencia')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ocorrencia'


class Pagamento(models.Model):
    id_pagamento = models.AutoField(db_column='ID_pagamento', primary_key=True)  # Field name made lowercase.
    valor = models.IntegerField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    data_pagamento = models.DateField(db_column='Data_pagamento', blank=True, null=True)  # Field name made lowercase.
    tipo_pagamentoid_tipo_pagamento = models.ForeignKey('TipoPagamento', models.DO_NOTHING, db_column='Tipo_PagamentoID_tipo_pagamento')  # Field name made lowercase.
    reservaid_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='ReservaID_reserva')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pagamento'


class Pais(models.Model):
    id_pais = models.AutoField(db_column='ID_pais', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Pais'


class Passageiro(models.Model):
    id_passageiro = models.AutoField(db_column='ID_passageiro', primary_key=True)  # Field name made lowercase.
    data_criacao = models.DateField(db_column='Data_criacao', blank=True, null=True)  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Passageiro'


class PassageiroViagem(models.Model):
    id_passageiro_viagem = models.AutoField(db_column='ID_passageiro_viagem', primary_key=True)  # Field name made lowercase.
    passageiroid_passageiro = models.ForeignKey(Passageiro, models.DO_NOTHING, db_column='PassageiroID_passageiro')  # Field name made lowercase.
    viagemid_viagem = models.ForeignKey('Viagem', models.DO_NOTHING, db_column='ViagemID_viagem')  # Field name made lowercase.
    reservaid_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='ReservaID_reserva')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Passageiro_Viagem'


class Ponto(models.Model):
    id_ponto = models.AutoField(db_column='ID_ponto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ponto'


class PontoViagem(models.Model):
    id_ponto_viagem = models.AutoField(db_column='ID_ponto_viagem', primary_key=True)  # Field name made lowercase.
    destino = models.IntegerField(db_column='Destino', blank=True, null=True)  # Field name made lowercase.
    viagemid_viagem = models.ForeignKey('Viagem', models.DO_NOTHING, db_column='ViagemID_viagem')  # Field name made lowercase.
    pontoid_ponto = models.ForeignKey(Ponto, models.DO_NOTHING, db_column='PontoID_ponto')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ponto_Viagem'


class PontoReserva(models.Model):
    id_ponto_reserva = models.AutoField(db_column='ID_ponto_reserva', primary_key=True)  # Field name made lowercase.
    destino = models.IntegerField(db_column='destino', blank=True, null=True)  # Field name made lowercase.
    reservaid_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='ReservaID_reserva')  # Field name made lowercase.
    pontoid_ponto = models.ForeignKey(Ponto, models.DO_NOTHING, db_column='PontoID_ponto')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Ponto_Reserva'


class PontoDesvio(models.Model):
    id_ponto_desvio = models.AutoField(db_column='ID_ponto_desvio', primary_key=True)  # Field name made lowercase.
    destino = models.IntegerField(db_column='destino', blank=True, null=True)  # Field name made lowercase.
    desvioid_desvio = models.ForeignKey('Desvio', models.DO_NOTHING, db_column='desvioid_desvio')  # Field name made lowercase.
    pontoid_ponto = models.ForeignKey(Ponto, models.DO_NOTHING, db_column='pontoid_ponto')  # Field name made lowercase.
    original = models.IntegerField(db_column='original', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Ponto_Desvio'


class StatusReserva(models.Model):
    id_status_reserva = models.AutoField(db_column='ID_status_reserva', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Status_Reserva'


class Reserva(models.Model):
    id_reserva = models.AutoField(db_column='ID_reserva', primary_key=True)  # Field name made lowercase.
    data_emissao = models.DateField(db_column='Data_emissao', blank=True, null=True)  # Field name made lowercase.
    valor = models.IntegerField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.
    condutorid_condutor = models.ForeignKey(Condutor, models.DO_NOTHING, db_column='CondutorID_condutor')  # Field name made lowercase.
    passageiroid_passageiro = models.ForeignKey(Passageiro, models.DO_NOTHING, db_column='PassageiroID_passageiro')  # Field name made lowercase.
    status_reservaid_status_reserva = models.ForeignKey(StatusReserva, models.DO_NOTHING, db_column='Status_reservaID_status_reserva')
    # data_viagem = models.DateField(db_column='Data_viagem', blank=True, null=True)  # Field name made lowercase.
    data_viagem = models.DateTimeField(db_column='Data_viagem', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Reserva'


class StatusDesvio(models.Model):
    id_status_desvio = models.AutoField(db_column='ID_status_desvio', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Status_Desvio'


class StatusViagem(models.Model):
    id_status_viagem = models.AutoField(db_column='ID_status_viagem', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Status_Viagem'


class Suspensao(models.Model):
    id_suspensao = models.AutoField(db_column='ID_suspensao', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    data_inicio = models.DateField(db_column='Data_inicio', blank=True, null=True)  # Field name made lowercase.
    data_fim = models.DateField(db_column='Data_fim', blank=True, null=True)  # Field name made lowercase.
    administradorid_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='AdministradorID_administrador')  # Field name made lowercase.
    utilizadorid_utilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='UtilizadorID_utilizador')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Suspensao'


class TipoAlerta(models.Model):
    id_tipo_alerta = models.AutoField(db_column='ID_tipo_alerta', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_Alerta'


class TipoCategoria(models.Model):
    id_tipo_categoria = models.AutoField(db_column='ID_tipo_categoria', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_Categoria'


class TipoContacto(models.Model):
    id_tipo_contacto = models.AutoField(db_column='ID_tipo_contacto', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_Contacto'


class TipoOcorrencia(models.Model):
    id_tipo_ocorrencia = models.AutoField(db_column='ID_tipo_ocorrencia', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_Ocorrencia'


class TipoPagamento(models.Model):
    id_tipo_pagamento = models.AutoField(db_column='ID_tipo_pagamento', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dados_mbid_mb = models.ForeignKey(DadosMb, models.DO_NOTHING, db_column='Dados_MBID_mb')  # Field name made lowercase.
    cartaoid_cc = models.ForeignKey(Cartao, models.DO_NOTHING, db_column='CartaoID_cc')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_Pagamento'


class TipoVeiculo(models.Model):
    id_tipo_veiculo = models.AutoField(db_column='ID_tipo_veiculo', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Tipo_Veiculo'


class UtilizadorManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError("O utilizador deve ter um email.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, senha, **extra_fields)


class Utilizador(AbstractBaseUser):
    id_utilizador = models.AutoField(primary_key=True)
    nome_primeiro = models.CharField(max_length=30, blank=True, null=True)
    nome_ultimo = models.CharField(max_length=30, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    numero_cc = models.IntegerField(blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True, blank=True, null=True)

    # Associações externas
    grupoid_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='GrupoID_grupo')  # Field name made lowercase.
    estado_civilid_estado_civil = models.ForeignKey(EstadoCivil, models.DO_NOTHING, db_column='Estado_CivilID_estado_civil')  # Field name made lowercase.
    nacionalidadeid_nacionalidade = models.ForeignKey(Nacionalidade, models.DO_NOTHING, db_column='NacionalidadeID_nacionalidade') 

    # Dados do Utilizador Padrão do Django
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, db_column='Senha')  
    last_login = models.DateTimeField(blank=True, null=True)   
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilizadorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_primeiro', 'nome_ultimo']

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Utilizador'


class Veiculo(models.Model):
    id_veiculo = models.AutoField(db_column='ID_veiculo', primary_key=True)  # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', unique=True, max_length=7, blank=True, null=True)  # Field name made lowercase.
    data_fabricacao = models.DateField(db_column='Data_fabricacao', blank=True, null=True)  # Field name made lowercase.
    ativo = models.IntegerField(db_column='Ativo', blank=True, null=True)  # Field name made lowercase.
    tipo_veiculoid_tipo_veiculo = models.ForeignKey(TipoVeiculo, models.DO_NOTHING, db_column='Tipo_VeiculoID_tipo_veiculo')  # Field name made lowercase.
    cor_veiculoid_cor_veiculo = models.ForeignKey(CorVeiculo, models.DO_NOTHING, db_column='Cor_VeiculoID_cor_veiculo')  # Field name made lowercase.
    modelo_veiculoid_modelo_veiculo = models.ForeignKey(ModeloVeiculo, models.DO_NOTHING, db_column='Modelo_VeiculoID_modelo_veiculo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Veiculo'


class Viagem(models.Model):
    id_viagem = models.AutoField(db_column='ID_viagem', primary_key=True)  # Field name made lowercase.
    # data_viagem = models.DateField(db_column='Data_viagem', blank=True, null=True)  # Field name made lowercase.
    data_viagem = models.DateTimeField(db_column='Data_viagem', blank=True, null=True)
    distancia_percorrida = models.IntegerField(db_column='Distancia_percorrida', blank=True, null=True)  # Field name made lowercase.
    status_viagemid_status_viagem = models.ForeignKey(StatusViagem, models.DO_NOTHING, db_column='Status_ViagemID_status_viagem')  # Field name made lowercase.
    condutorid_condutor = models.ForeignKey(Condutor, models.DO_NOTHING, db_column='CondutorID_condutor')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Viagem'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
