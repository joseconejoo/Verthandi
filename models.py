# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

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


class SoporteDatos(models.Model):
    usuario = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.CharField(max_length=254, blank=True, null=True)
    fedicion = models.DateTimeField(blank=True, null=True)
    cod_area = models.IntegerField(blank=True, null=True)
    cod_nivel = models.IntegerField(blank=True, null=True)
    cedula = models.PositiveIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'soporte_datos'


class SoporteNiveles(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    nivel = models.IntegerField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'soporte_niveles'


class SoportePDetal(models.Model):
    nombre = models.CharField(max_length=30)
    p_opci = models.ForeignKey('SoportePOpci', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'soporte_p_detal'


class SoportePOpci(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'soporte_p_opci'


class SoporteSopNotif(models.Model):
    cod_usu = models.ForeignKey(AuthUser, models.DO_NOTHING)
    descrip1 = models.ForeignKey(SoportePDetal, models.DO_NOTHING, blank=True, null=True)
    tipo_sop = models.ForeignKey(SoportePOpci, models.DO_NOTHING)
    usu_tec = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=200)
    num_pc = models.IntegerField()
    problemaad = models.CharField(db_column='problemaAd', max_length=500)  # Field name made lowercase.
    estado_sop = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'soporte_sop_notif'
